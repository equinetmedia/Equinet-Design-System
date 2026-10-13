#!/usr/bin/env python3
"""
Equinet design system — tokens.json generator.

    python tools/build-tokens-json.py            # rewrite tokens.json
    python tools/build-tokens-json.py --check    # fail if it would change
    python tools/build-tokens-json.py --report   # print the coverage report only

WHY THIS EXISTS
    tokens.css and tokens.json were both hand-kept, and only one of them was
    true: on 2026-10-13 the JSON carried 60 of the CSS's 215 tokens. Every
    token added to the CSS since 2026-09-23 was invisible to anything reading
    the JSON. Transcribing once would have fixed that day and nothing after
    it, so the JSON is now generated.

WHAT IS AUTHORITATIVE
    tokens.css owns every NAME and every VALUE. This script never invents
    either. If a value is wrong, fix the CSS.

    tokens.json owns the hand-written `usage` prose — the contrast
    measurements, the provenance notes, the "this module has drifted"
    warnings. None of that is derivable from the CSS, and it is the most
    valuable content in the file. The generator MERGES: it carries every
    existing `usage` string forward by token name, and only falls back to the
    CSS inline comment for a token that has none yet.

    The `type` block is likewise preserved. Claude Design's type styles are a
    curated structure (groups of named styles), not a flat list of tokens, so
    there is no 1:1 mapping from the CSS's fontsize/fontweight/lineheight
    variables. The generator validates the block against the CSS instead of
    regenerating it — see check_type_block().

SCHEMA LIMITS, ALL LEARNED THE HARD WAY (see CHANGELOG 2026-09-23)
    - There is no `motion` family. Duration tokens live under `duration`;
      under `motion` they were silently dropped.
    - `textTransform` and `textShadow` are not valid fields on a type style.
      They were added once and silently ignored. The h2 uppercase + drop
      shadow requirement lives in README.md and tokens.css only.
    - Duplicate token names are silently dropped, so the generator refuses to
      emit one.
    Because the failure mode is SILENT, anything this script cannot represent
    is written to tools/tokens-unrepresentable.md rather than quietly omitted.
"""

import argparse
import json
import os
import re
import sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(ROOT, "tokens.css")
JSON_OUT = os.path.join(ROOT, "tokens.json")
REPORT = os.path.join(ROOT, "tools", "tokens-unrepresentable.md")

SCHEMA_FAMILIES = ["color", "type", "spacing", "duration", "radius", "size", "shadow"]


# ---------------------------------------------------------------------------
# Routing. First matching rule wins, so order matters: the specific patterns
# sit above the general prefixes they would otherwise be swallowed by.
# ---------------------------------------------------------------------------
ROUTES = [
    # --- not representable in the schema, each with the reason ----------------
    (r"^--equinet-(font|fontsize|fontweight|lineheight|letterspacing|fontstyle)\b",
     None, "typography — carried by the `type` block's named styles, which have no token-array equivalent"),
    (r"^--equinet-paraspacing-",
     None, "paragraph spacing — no field for it on a type style; applied directly in module CSS"),
    (r"^--equinet-text-transform-",
     None, "textTransform is not a valid field on a type style (confirmed against the grammar 2026-09-23); the h2 uppercase requirement lives in README.md and tokens.css"),
    (r"^--equinet-motion-ease",
     None, "easing curve — no family reads a timing function; consumed directly from tokens.css"),
    (r"^--equinet-(btn-scale|icon-stroke)",
     None, "unitless number (a scale factor / stroke width) — no numeric family in the schema"),

    # --- specific before general ---------------------------------------------
    (r"^--equinet-motion-duration", "duration", None),
    (r"^--equinet-motion-stagger", "duration", None),
    (r"^--equinet-motion-travel", "size", None),
    (r"^--equinet-btn-(fill|label|icon)", "color", None),
    (r"^--equinet-btn-radius", "radius", None),
    (r"^--equinet-btn-height", "size", None),
    (r"^--equinet-border-radius-", "radius", None),
    (r"^--equinet-border-width-", "size", None),
    (r"^--equinet-icon-size", "size", None),

    # --- general prefixes -----------------------------------------------------
    (r"^--equinet-color-", "color", None),
    (r"^--equinet-(cta|neutral|surface-page)", "color", None),
    # semantic colour aliases whose names don't start with `color-`
    (r"^--equinet-(text-action|icon-primary)", "color", None),
    (r"^--equinet-shadow-", "shadow", None),
    (r"^--equinet-space-", "spacing", None),
    (r"^--equinet-scale-", "spacing", None),
    (r"^--equinet-radius-", "radius", None),
]

HEX = re.compile(r"^#[0-9A-Fa-f]{3,8}$")
VAR_ONLY = re.compile(r"^var\(\s*(--equinet-[A-Za-z0-9\-]+)\s*(?:,[^)]*)?\)$")
ANY_VAR = re.compile(r"var\(\s*(--[A-Za-z0-9\-]+)")


def route(name):
    """-> (family | None, reason | None). Unrouted names are an error, not a skip."""
    for pattern, family, reason in ROUTES:
        if re.match(pattern, name):
            return family, reason
    return "UNROUTED", "no routing rule matches this name — add one to ROUTES in this script"


# ---------------------------------------------------------------------------
# Parse tokens.css
# ---------------------------------------------------------------------------
def parse_css(text):
    """Return an ordered list of {name, value, comment} in declaration order.

    Only declarations inside the single :root block are read — tokens.css owns
    the only :root in the system, so anything outside it is not a token.
    """
    start = text.index(":root")
    body = text[start:]

    # Strip block comments but keep a map from declaration name to the comment
    # that trails it on the same line (or the lines immediately after, for the
    # wrapped ones), since that prose is the fallback `usage`.
    out = OrderedDict()
    duplicates = []
    pending_comment = []
    in_comment = False

    for raw in body.split("\n"):
        line = raw

        if in_comment:
            end = line.find("*/")
            if end == -1:
                pending_comment.append(line.strip())
                continue
            pending_comment.append(line[:end].strip())
            line, in_comment = line[end + 2:], False

        decl = re.match(r"\s*(--equinet-[a-z0-9\-]+)\s*:\s*(.+?)\s*;", line)
        if not decl:
            # a comment line with no declaration resets the trailing-comment buffer
            if "/*" in line and "*/" not in line:
                in_comment = True
                pending_comment = [line[line.index("/*") + 2:].strip()]
            continue

        name, value = decl.group(1), decl.group(2)
        if name in out:
            # The schema silently drops a duplicate name, so the CSS must not
            # declare one. Recorded here rather than overwritten.
            duplicates.append(name)
        rest = line[decl.end():]
        comment_bits = []

        if "/*" in rest:
            frag = rest[rest.index("/*") + 2:]
            if "*/" in frag:
                comment_bits.append(frag[: frag.index("*/")].strip())
            else:
                comment_bits.append(frag.strip())
                in_comment = True
                pending_comment = comment_bits
                out[name] = {"name": name, "value": value, "comment": None, "_pending": True}
                continue

        out[name] = {
            "name": name,
            "value": value,
            "comment": clean_comment(" ".join(comment_bits)) or None,
        }
        pending_comment = []

        # attach a multi-line trailing comment to the declaration that opened it
        for prev in reversed(list(out.values())):
            if prev.get("_pending"):
                prev["comment"] = clean_comment(" ".join(pending_comment)) or None
                prev.pop("_pending", None)
                break

    for entry in out.values():
        if entry.pop("_pending", None):
            entry["comment"] = clean_comment(" ".join(pending_comment)) or None

    return list(out.values()), duplicates


# A comment that only restates the resolved value ("#F5844D", "4px", "0.45s")
# carries no information the token itself doesn't — drop it rather than emit a
# `usage` string that tells a reader nothing.
VALUE_ECHO = re.compile(r"^(#[0-9A-Fa-f]{3,8}|[\d.]+(px|rem|em|ms|s|%)?)$")


def clean_comment(text):
    text = re.sub(r"\s+", " ", (text or "")).strip(" ·-")
    if not text or VALUE_ECHO.match(text):
        return ""
    return text.strip()


# ---------------------------------------------------------------------------
# Value shaping
# ---------------------------------------------------------------------------
def shape_value(entry, family, defined):
    """Aliases stay aliases. Colours get the theme map. Everything else is literal."""
    raw = entry["value"]
    alias = VAR_ONLY.match(raw)
    if alias:
        target = alias.group(1)
        if target not in defined:
            raise ValueError(f"{entry['name']} aliases {target}, which tokens.css does not define")
        return "{%s}" % target[2:]
    if family == "color":
        if not HEX.match(raw) and not raw.startswith("rgb"):
            raise ValueError(f"{entry['name']} routed to `color` but its value is {raw!r}")
        return {"light": raw}
    return raw


def resolve(name, by_name, seen=None):
    """Follow var() aliases down to a literal, for validating the type block."""
    seen = seen or set()
    if name in seen or name not in by_name:
        return None
    seen.add(name)
    raw = by_name[name]["value"]
    alias = VAR_ONLY.match(raw)
    return resolve(alias.group(1), by_name, seen) if alias else raw


# ---------------------------------------------------------------------------
# The type block: preserved, then validated against the CSS
# ---------------------------------------------------------------------------
def check_type_block(existing, by_name):
    """Every declared size/weight/tracking should exist somewhere in tokens.css.

    A style is free to combine values that no single CSS variable names, but a
    value appearing in NO variable is almost always a typo or drift — the
    48px/36px section-heading bug was exactly that shape.
    """
    problems = []
    literals = {resolve(n, by_name) for n in by_name}
    literals.discard(None)

    for group in existing.get("type", {}).get("groups", []):
        for style in group.get("styles", []):
            label = f"type.{group.get('name')}.{style.get('name')}"
            for field in ("fontSize", "letterSpacing"):
                val = style.get(field)
                if val and str(val) not in literals and not str(val).endswith("em"):
                    problems.append(f"{label}.{field} = {val} — no tokens.css variable holds that value")
            weight = style.get("fontWeight")
            if weight and str(weight) not in literals:
                problems.append(f"{label}.fontWeight = {weight} — no tokens.css variable holds that value")
            for banned in ("textTransform", "textShadow"):
                if banned in style:
                    problems.append(
                        f"{label} declares {banned}, which the schema silently ignores — "
                        "remove it and keep the requirement in README.md"
                    )
    return problems


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build():
    css_text = open(CSS, encoding="utf-8").read()
    entries, duplicates = parse_css(css_text)
    by_name = {e["name"]: e for e in entries}
    defined = set(by_name)

    existing = json.load(open(JSON_OUT, encoding="utf-8"))

    # Carry forward every hand-written usage string, keyed by token name.
    prior_usage = {}

    def harvest(node):
        # VALUE_ECHO guard: an earlier run of this script could have written a
        # useless usage string ("4px") before that filter existed. Without the
        # guard such a string would be harvested back in on every run and
        # become permanent. Real hand-written prose never looks like a value.
        if isinstance(node, dict):
            if "name" in node and "usage" in node:
                if not VALUE_ECHO.match(str(node["usage"]).strip()):
                    prior_usage[node["name"]] = node["usage"]
            for v in node.values():
                harvest(v)
        elif isinstance(node, list):
            for v in node:
                harvest(v)

    harvest(existing)

    families = {f: [] for f in SCHEMA_FAMILIES if f != "type"}
    unrepresentable, errors, seen_names = [], [], set()
    for dup in duplicates:
        errors.append(f"{dup} is declared more than once in tokens.css — "
                      "the schema silently drops a duplicate name")

    for entry in entries:
        family, reason = route(entry["name"])

        if family == "UNROUTED":
            errors.append(f"{entry['name']}: {reason}")
            continue
        if family is None:
            unrepresentable.append((entry["name"], entry["value"], reason))
            continue

        token_name = entry["name"][2:]
        if token_name in seen_names:
            errors.append(f"{token_name} declared twice — the schema silently drops duplicates")
            continue
        seen_names.add(token_name)

        for ref in ANY_VAR.findall(entry["value"]):
            if ref not in defined:
                errors.append(f"{entry['name']} references {ref}, which tokens.css does not define")
        try:
            value = shape_value(entry, family, defined)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        token = {"name": token_name, "value": value}
        usage = prior_usage.get(token_name) or entry["comment"]
        if usage:
            token["usage"] = usage
        families[family].append(token)

    errors += check_type_block(existing, by_name)

    doc = OrderedDict()
    doc["name"] = existing.get("name", "Equinet")
    doc["version"] = existing.get("version", 1)
    doc["color"] = {
        "themes": existing.get("color", {}).get("themes", [{"id": "light", "name": "Light"}]),
        "tokens": families["color"],
    }
    doc["type"] = existing["type"]
    for family in ("spacing", "duration", "radius", "size", "shadow"):
        block = OrderedDict()
        if family == "duration":
            block["note"] = existing.get("duration", {}).get(
                "note",
                "Named 'duration', not 'motion' — the schema does not read a family "
                "literally called 'motion'; tokens under that name were silently dropped.",
            )
        block["tokens"] = families[family]
        doc[family] = block

    return doc, entries, unrepresentable, errors


def write_report(entries, unrepresentable, doc):
    emitted = sum(
        len(doc[f]["tokens"]) for f in SCHEMA_FAMILIES if f != "type"
    )
    lines = [
        "---",
        "id: tokens-unrepresentable",
        "status: generated",
        "read_when: >-",
        "  Working out why a token in tokens.css does not appear in tokens.json.",
        "  Generated by tools/build-tokens-json.py — do not hand-edit.",
        "depends_on: tokens.css",
        "---",
        "",
        "# Tokens that cannot be expressed in tokens.json",
        "",
        f"`tokens.css` declares **{len(entries)}** variables. **{emitted}** are emitted as",
        f"tokens; **{len(unrepresentable)}** have no representation in Claude Design's schema",
        "and are listed below with the reason.",
        "",
        "This file exists because the schema fails *silently*: an unsupported family or",
        "field is dropped without an error, which is how the `motion` family and the h2",
        "`textTransform` were both lost in 2026-09-23. A token absent from `tokens.json`",
        "is therefore not evidence that it is unimportant — read `tokens.css`.",
        "",
        "| Token | Value | Why it isn't in tokens.json |",
        "| --- | --- | --- |",
    ]
    for name, value, reason in unrepresentable:
        value = value if len(value) < 48 else value[:45] + "…"
        lines.append(f"| `{name}` | `{value}` | {reason} |")
    lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if tokens.json is out of date")
    ap.add_argument("--report", action="store_true", help="print the coverage report, write nothing")
    args = ap.parse_args()

    doc, entries, unrepresentable, errors = build()

    if errors:
        print("REFUSING TO WRITE — fix tokens.css first:\n")
        for e in dict.fromkeys(errors):   # dedupe, keep order
            print("  -", e)
        return 2

    rendered = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    report = write_report(entries, unrepresentable, doc)
    emitted = sum(len(doc[f]["tokens"]) for f in SCHEMA_FAMILIES if f != "type")

    print(f"tokens.css declares {len(entries)} variables")
    print(f"  emitted as tokens : {emitted}")
    print(f"  unrepresentable   : {len(unrepresentable)}  (see tools/tokens-unrepresentable.md)")
    for family in SCHEMA_FAMILIES:
        if family != "type":
            print(f"    {family:9s} {len(doc[family]['tokens'])}")

    if args.report:
        return 0

    current = open(JSON_OUT, encoding="utf-8").read() if os.path.exists(JSON_OUT) else ""
    current_report = open(REPORT, encoding="utf-8").read() if os.path.exists(REPORT) else ""

    if args.check:
        stale = (rendered != current) or (report + "\n" != current_report)
        print("\ntokens.json is " + ("STALE — run tools/build-tokens-json.py" if stale else "up to date"))
        return 1 if stale else 0

    open(JSON_OUT, "w", encoding="utf-8").write(rendered)
    open(REPORT, "w", encoding="utf-8").write(report + "\n")
    print("\nwrote tokens.json and tools/tokens-unrepresentable.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
