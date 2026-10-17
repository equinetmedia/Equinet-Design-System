#!/usr/bin/env python3
"""
Equinet design system — documentation consistency checker.

Run from the repo root:  python tools/check-docs.py

Companion to tools/build-manifest.py. That script makes the asset inventory
machine-readable; this one makes sure the prose never contradicts it.

Every check below corresponds to a class of error already found in this repo
by hand. The point is that an agent reading the docs is reading something
true, because a human can no longer silently let a count, a token name or a
cross-reference go stale.

Exit code 0 = clean, 1 = problems found. Safe to wire into CI or a
pre-commit hook.
"""

import json
import os
import re
import sys
from collections import Counter
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems = []
notes = []


def fail(check, detail):
    problems.append((check, detail))


def note(detail):
    notes.append(detail)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def md_files(skip=("CHANGELOG.md",)):
    """Every tracked markdown file. CHANGELOG is historical by design, so
    stale statements inside it are expected and are not errors."""
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "__MACOSX", "node_modules"}]
        for fn in filenames:
            if fn.endswith(".md"):
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                if rel not in skip:
                    out.append(rel)
    return sorted(out)


# --------------------------------------------------------------------------
# 1. Counts in prose must match the files on disk
#    Written counts go stale on every asset drop. Rather than ban them, the
#    rule is: any count in prose must be inside a generated block (see
#    check 7) or must match reality right now.
# --------------------------------------------------------------------------
WORD_NUMBERS = {
    "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
    "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20,
}


def actual_counts():
    manifest = json.loads(read("assets/manifest.json"))
    assets = manifest["assets"]
    by_cat = Counter(a["category"] for a in assets)
    by_group = Counter(a["group"] for a in assets)
    return {
        "assets": len(assets),
        "illustration": by_cat["illustration"],
        "icon": by_cat["icon"],
        "layout-blueprint": by_cat["layout-blueprint"],
        "style-reference": by_cat["style-reference"],
        "chart": by_cat["chart"],
        "brand": by_cat["brand"],
        "button-source": by_cat["button-source"],
        "reworkable": sum(1 for a in assets if a.get("reworkable")),
        "illustration_groups": len({a["group"] for a in assets if a["category"] == "illustration"}),
        "icon_groups": len({a["group"] for a in assets if a["category"] == "icon"}),
        "by_group": dict(by_group),
    }


# Phrase → the count key it must agree with. Extend as the docs grow.
COUNT_CLAIMS = [
    (r"(\d+|\w+) standalone graphics", "illustration"),
    (r"(\d+|\w+) files? in (?:three|four|five|\d+) groups", "icon"),
    (r"all (\d+) assets", "assets"),
    (r"one entry per asset \((\d+)\)", "assets"),
    (r"(?:the )?(\d+|\w+) reworkable assets", "reworkable"),
    (r"(\d+|\w+) (?:Figma )?(?:module )?comps\b", "layout-blueprint"),
    (r"(\d+|\w+) (?:Figma )?exports of complete modules", "layout-blueprint"),
    (r"(\d+|\w+) infographics", "style-reference"),
    (r"(\d+|\w+) sourced data charts", "chart"),
]


def check_counts(counts):
    for rel in md_files():
        text = read(rel)
        for line_no, line in enumerate(text.split("\n"), 1):
            for pattern, key in COUNT_CLAIMS:
                for m in re.finditer(pattern, line, re.I):
                    raw = m.group(1).lower()
                    claimed = WORD_NUMBERS.get(raw)
                    if claimed is None:
                        if not raw.isdigit():
                            continue
                        claimed = int(raw)
                    if claimed != counts[key]:
                        fail(
                            "stale count",
                            f"{rel}:{line_no} claims {claimed} for '{key}' "
                            f"(actual {counts[key]}): {m.group(0)!r}",
                        )


# --------------------------------------------------------------------------
# 2. Every --equinet-* token named in prose or code must exist in tokens.css
#    tokens.css is the only source of truth; a cited token that does not
#    resolve is an invitation for a model to invent a value.
# --------------------------------------------------------------------------
def defined_tokens():
    return set(re.findall(r"(--equinet-[a-z0-9\-]+)\s*:", read("tokens.css")))


def check_token_citations(defined):
    bare = {t[2:] for t in defined}
    targets = md_files() + ["components/bundle.css", "components/motion.js"]
    for rel in targets:
        text = read(rel)
        cited = set(re.findall(r"--equinet-[a-z0-9\-]+", text))
        cited |= {"--" + n for n in re.findall(r"`(equinet-[a-z0-9\-]+)`", text)}
        for token in sorted(cited):
            if token.endswith("-"):      # deliberate wildcard, e.g. --equinet-space-*
                continue
            if token not in defined and token[2:] not in bare:
                fail("undefined token", f"{rel} cites {token}, not in tokens.css")


# --------------------------------------------------------------------------
# 3. tokens.css -> tokens.json parity
#    tokens.json is GENERATED from tokens.css by tools/build-tokens-json.py.
#    This check does not re-derive the mapping — it just asks the generator
#    whether the committed file is what it would produce. Anything the schema
#    cannot represent is listed in tools/tokens-unrepresentable.md and is a
#    legitimate absence, not drift.
# --------------------------------------------------------------------------
def check_token_parity(defined):
    import subprocess

    gen = os.path.join(ROOT, "tools", "build-tokens-json.py")
    if not os.path.exists(gen):
        fail("token parity", "tools/build-tokens-json.py is missing — tokens.json has no generator")
        return
    result = subprocess.run(
        [sys.executable, gen, "--check"], cwd=ROOT, capture_output=True, text=True
    )
    if result.returncode == 2:
        for line in result.stdout.strip().split("\n"):
            if line.strip().startswith("- "):
                fail("tokens.css invalid", line.strip()[2:])
    elif result.returncode != 0:
        fail(
            "token parity",
            "tokens.json does not match what tools/build-tokens-json.py produces "
            "from tokens.css — run `python tools/build-tokens-json.py`",
        )
    report = os.path.join(ROOT, "tools", "tokens-unrepresentable.md")
    if not os.path.exists(report):
        fail(
            "token parity",
            "tools/tokens-unrepresentable.md is missing — without it, a token absent "
            "from tokens.json looks like an oversight rather than a schema limit",
        )


# --------------------------------------------------------------------------
# 4. Internal section cross-references must resolve
#    'see **Module anatomy**' pointing at a section that was never written
#    sends a reader looking for rules that do not exist.
# --------------------------------------------------------------------------
def check_section_refs():
    for rel in md_files():
        text = read(rel)
        headings = {h.strip().lower() for h in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.M)}
        headings |= {h.split("—")[0].strip().strip("`").lower() for h in headings}
        for m in re.finditer(r"see \*\*([^*]+)\*\*", text):
            target = m.group(1).strip().lower()
            if not any(target in h for h in headings):
                fail("dangling reference", f"{rel} says 'see **{m.group(1)}**' — no such section")


# --------------------------------------------------------------------------
# 5. Relative file references must exist
# --------------------------------------------------------------------------
def check_file_refs():
    on_disk = set()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "__MACOSX", "node_modules"}]
        for fn in filenames:
            on_disk.add(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    dirs_on_disk = {os.path.dirname(p) for p in on_disk}
    pattern = re.compile(r"`((?:assets|skills|components|tools|tests)/[A-Za-z0-9_./\-]*)`")
    for rel in md_files():
        for line_no, line in enumerate(read(rel).split("\n"), 1):
            for ref in pattern.findall(line):
                clean = ref.rstrip("/")
                if clean in on_disk or clean in dirs_on_disk:
                    continue
                if ref.endswith("/") or "." not in os.path.basename(clean):
                    fail("missing path", f"{rel}:{line_no} references directory {ref!r}")
                else:
                    fail("missing path", f"{rel}:{line_no} references file {ref!r}")


# --------------------------------------------------------------------------
# 6. Markdown tables must have a consistent cell count
#    A short row silently drops a field for anything parsing the table.
# --------------------------------------------------------------------------
def check_tables():
    for rel in md_files():
        width = None
        for line_no, line in enumerate(read(rel).split("\n"), 1):
            stripped = line.strip()
            if not stripped.startswith("|"):
                width = None
                continue
            cells = stripped.count("|") - 1
            if set(stripped) <= set("| -:"):
                width = cells
                continue
            if width is None:
                continue
            if cells != width:
                fail("malformed table", f"{rel}:{line_no} has {cells} cells, table is {width} wide")


# --------------------------------------------------------------------------
# 7. The rules digest must not be referenced by number
#    Rule numbers shift every time a rule is inserted. Already broke once
#    ('13-rule digest' when it was 14). Reference rules by name instead.
# --------------------------------------------------------------------------
def check_digest_refs():
    for rel in md_files():
        for line_no, line in enumerate(read(rel).split("\n"), 1):
            m = re.search(r"\b(?:digest )?rules? (\d+)(?:[–-]\d+)?\b(?! of this)", line, re.I)
            if m and "digest" in line.lower():
                fail(
                    "brittle reference",
                    f"{rel}:{line_no} cites a digest rule by number ({m.group(0)!r}); "
                    "numbers shift when a rule is inserted — cite it by name",
                )


# --------------------------------------------------------------------------
# 8. CHANGELOG must be newest-first and carry its historical-record warning
# --------------------------------------------------------------------------
def check_changelog():
    text = read("CHANGELOG.md")
    head = text[: text.find("\n## ")]
    if "superseded" not in head.lower() and "historical" not in head.lower():
        fail(
            "changelog framing",
            "CHANGELOG.md has no header telling a reader its entries are historical "
            "and may describe rules since reversed — a model will read them as current",
        )
    dates = re.findall(r"^## (\d{4}-\d{2}-\d{2})", text, re.M)
    if dates != sorted(dates, reverse=True):
        first_wrong = next(
            (d for a, d in zip(sorted(dates, reverse=True), dates) if a != d), dates[0]
        )
        fail(
            "changelog order",
            f"entries are not newest-first (top entry is {dates[0]}, newest is "
            f"{max(dates)}); first out-of-order entry: {first_wrong}",
        )


# --------------------------------------------------------------------------
# 9. Every markdown file should carry routing frontmatter
#    So an agent can decide whether to open a file without reading it.
#
#    Two deliberate exemptions, both of which would BREAK something:
#
#    README.md — the design-system format treats the first `---` in this file
#      as the boundary between author text and generated sections, and
#      rewrites everything below it on save. YAML frontmatter opens with
#      `---`, so adding it would mark the entire brand book as regenerable.
#      This already happened once (CHANGELOG, 2026-09-24). README.md is read
#      first by convention, so it needs no routing hint anyway. Check 11
#      enforces the zero-horizontal-rules rule instead.
#
#    SKILL.md — its frontmatter is validated against the Agent Skills schema.
#      A YAML error there stops the skill loading entirely (CHANGELOG,
#      2026-09-26), and unknown top-level keys are not worth that risk. Its
#      `description` already states when to read it, which is what read_when
#      exists for.
# --------------------------------------------------------------------------
REQUIRED_FRONTMATTER = {"id", "status", "read_when", "verified"}
FRONTMATTER_EXEMPT = {
    "README.md": "first `---` would mark the brand book regenerable",
    "skills/equinet-layout/SKILL.md": "Agent Skills schema owns this frontmatter",
}


def check_frontmatter():
    for rel in md_files(skip=()):
        if rel in FRONTMATTER_EXEMPT:
            continue
        text = read(rel)
        if not text.startswith("---\n"):
            fail("no frontmatter", f"{rel} has no YAML frontmatter block")
            continue
        block = text.split("---\n", 2)[1]
        keys = set(re.findall(r"^([a-z_]+):", block, re.M))
        required = set(REQUIRED_FRONTMATTER)
        if re.search(r"^status:\s*generated\s*$", block, re.M):
            # A generated file has no human-verified date — its freshness is
            # whatever its generator last produced, which check 3 enforces.
            required.discard("verified")
        missing = required - keys
        if missing:
            fail("frontmatter", f"{rel} frontmatter missing: {', '.join(sorted(missing))}")
        for line in block.split("\n"):
            if re.match(r"^[a-z_]+ [>|]", line):
                fail(
                    "frontmatter",
                    f"{rel} has '{line.strip()}' — a folded scalar needs a colon "
                    "('key: >-'), or the whole block fails to parse",
                )
        m = re.search(r"^verified:\s*(\d{4}-\d{2}-\d{2})", block, re.M)
        if m:
            age = (date.today() - date.fromisoformat(m.group(1))).days
            if age > 60:
                note(f"{rel} last verified {age} days ago ({m.group(1)})")


# --------------------------------------------------------------------------
# 11. README.md must contain zero horizontal rules
#     The design-system format rewrites everything after the first `---`.
#     A stray rule silently marks the brand book as generated content.
# --------------------------------------------------------------------------
def check_readme_no_rules():
    for line_no, line in enumerate(read("README.md").split("\n"), 1):
        if re.match(r"^\s{0,3}(-{3,}|\*{3,}|_{3,})\s*$", line):
            fail(
                "README horizontal rule",
                f"README.md:{line_no} is a horizontal rule. The design-system format "
                "treats the first one as the author/generated boundary and rewrites "
                "everything below it. Use a heading to separate sections.",
            )


# --------------------------------------------------------------------------
# 10. Every asset must be reachable by subject, not just by filename
# --------------------------------------------------------------------------
def check_asset_discoverability():
    assets = json.loads(read("assets/manifest.json"))["assets"]
    index = read("assets/illustrations/INDEX.md")
    for a in assets:
        if a["category"] == "illustration" and a["name"] not in index:
            fail(
                "undiscoverable asset",
                f"{a['path']} is not named in assets/illustrations/INDEX.md — "
                "it can only be found by guessing its filename",
            )
        # Lucide icons are named by what they do — `calendar-clock` needs no
        # subject line. The check exists for Equinet's own artwork, where the
        # filename and the subject are not the same thing.
        if (a["category"] in {"illustration", "icon"}
                and a["group"] not in {"root", "lucide"}):
            if not (a.get("subject") or a.get("topics")):
                note(f"{a['path']} has no subject/topics in the manifest")


def main():
    counts = actual_counts()
    defined = defined_tokens()

    check_counts(counts)
    check_token_citations(defined)
    check_token_parity(defined)
    check_section_refs()
    check_file_refs()
    check_tables()
    check_digest_refs()
    check_changelog()
    check_frontmatter()
    check_asset_discoverability()
    check_readme_no_rules()

    if problems:
        grouped = {}
        for check, detail in problems:
            grouped.setdefault(check, []).append(detail)
        for check in sorted(grouped):
            print(f"\n{check.upper()}  ({len(grouped[check])})")
            for detail in grouped[check]:
                print(f"  - {detail}")

    if notes:
        print(f"\nNOTES  ({len(notes)})")
        for detail in notes[:20]:
            print(f"  - {detail}")
        if len(notes) > 20:
            print(f"  … and {len(notes) - 20} more")

    print(f"\n{len(problems)} problem(s), {len(notes)} note(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
