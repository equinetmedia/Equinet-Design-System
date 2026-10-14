#!/usr/bin/env python3
"""
Equinet — built-page auditor.

    python tools/check-built-page.py path/to/page.html

Reads a finished page and reports the things that look completely normal in a
screenshot and are wrong in the file. Companion to check-docs.py: that one
audits the repo, this one audits what the repo produced.

WHY IT EXISTS
    A GEO landing page shipped on 2026-10-13 with tokens.css fully inlined —
    215 tokens available, zero undefined — and then wrote 80 hardcoded font
    sizes, 155 hardcoded spacings, and a box-shadow that was the card and
    hover shadows pasted together, so six cards sat permanently in their
    hover state. The same page inlined the whole of bundle.css and none of
    motion.js, which is invisible because the no-JS fallback is clean.
    Nothing about that page looked broken. All of it was measurable.

WHAT IT CHECKS
    tokens      hardcoded px / shadow values where a token holds that value
    motion      is motion.js actually in the file, and is anything annotated
    graphics    inline SVG vs <img>, data-asset coverage, hotspots
    portable    real viewBox, template bindings left in the markup
    faq         FAQPage JSON-LD matching the visible questions

Exit code 0 clean, 1 problems found. Accepts a Claude Design self-extracting
bundle and unpacks it first — the wrapper is a loader, not the page.
"""

import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

problems, notes, facts = [], [], []


def fail(check, detail):
    problems.append((check, detail))


def note(detail):
    notes.append(detail)


def fact(label, value):
    facts.append((label, value))


# ---------------------------------------------------------------------------
# Load the page. A Claude Design export is a loader wrapping the real page in
# a __bundler/template script; auditing the wrapper tells you nothing.
# ---------------------------------------------------------------------------
def load(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r'<script type="__bundler/template"[^>]*>(.*?)</script>', raw, re.S)
    if not m:
        return raw, False
    try:
        return json.loads(m.group(1)), True
    except json.JSONDecodeError:
        return raw, False


def system_css():
    """The repo's own CSS, so inlined copies of it aren't counted as the
    page's hardcoded values — tokens.css legitimately contains literals."""
    out = ""
    for rel in ("tokens.css", "components/bundle.css", "components/motion.js"):
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            out += open(p, encoding="utf-8").read()
    return out


def markup_only(page):
    """Element counts must ignore <style> and <script> bodies — bundle.css's
    own comments mention `<img>`, which counted as two images on every page
    that inlined it. JSON-LD is kept, since the FAQ check reads it."""
    out = re.sub(r"<style[^>]*>.*?</style>", "", page, flags=re.S | re.I)
    out = re.sub(
        r'<script(?![^>]*application/ld\+json)[^>]*>.*?</script>', "", out, flags=re.S | re.I
    )
    return out


def strip_system(page, system):
    """Remove any run of system CSS/JS that was inlined verbatim. Done line by
    line: a line present in the system files is not the page's own code."""
    system_lines = {ln.strip() for ln in system.split("\n") if len(ln.strip()) > 12}
    kept = [ln for ln in page.split("\n") if ln.strip() not in system_lines]
    return "\n".join(kept)


# ---------------------------------------------------------------------------
# tokens — the check this tool was built for
# ---------------------------------------------------------------------------
def token_values():
    """value -> [token names]. Only tokens whose value is a literal worth
    matching: px sizes, shadows, radii. Aliases resolve to their target."""
    css = open(os.path.join(ROOT, "tokens.css"), encoding="utf-8").read()
    raw = dict(re.findall(r"(--equinet-[a-z0-9\-]+)\s*:\s*([^;]+);", css))

    def resolve(v, depth=0):
        if depth > 10:
            return v
        m = re.match(r"^var\(\s*(--equinet-[a-z0-9\-]+)", v.strip())
        return resolve(raw[m.group(1)], depth + 1) if m and m.group(1) in raw else v.strip()

    by_value = {}
    for name, value in raw.items():
        lit = resolve(value)
        by_value.setdefault(norm(lit), []).append(name)
    # Prefer the semantic token over the primitive it points at: a reader
    # should be told to write --equinet-space-md, not --equinet-scale-600.
    for key in by_value:
        by_value[key].sort(key=lambda n: (n.startswith("--equinet-scale-"), len(n)))
    return by_value


# Which token families may legitimately answer which property. Without this,
# `font-size: 12px` matches --equinet-scale-300 and the tool teaches nonsense.
TOKEN_FAMILIES = {
    "type": ("--equinet-fontsize-", "--equinet-lineheight-", "--equinet-letterspacing-"),
    "space": ("--equinet-space-", "--equinet-scale-"),
    "radius": ("--equinet-radius-", "--equinet-border-radius-", "--equinet-btn-radius"),
    "shadow": ("--equinet-shadow-",),
}


def candidates(by_value, key, group):
    """Tokens of the right family holding exactly this value."""
    allowed = TOKEN_FAMILIES.get(group, ())
    return [n for n in by_value.get(key, []) if n.startswith(allowed)]


def norm(value):
    """Compare values ignoring whitespace, zero-unit and case noise, so
    `1px 1px 5px 0 rgba(0,0,0,0.13)` matches `1px 1px 5px 0px rgba(0, 0, 0, 0.13)`."""
    v = re.sub(r"\s+", "", value.strip().lower().rstrip(";"))
    # Only a standalone zero loses its unit. `(?<!\d)` matters: without it
    # this turned "20px" into "20" and the unit filter then skipped it.
    v = re.sub(r"(?<![\d.])0px(?![\d.])", "0", v)
    return v


PROPERTY_GROUPS = {
    "font-size": "type",
    "line-height": "type",
    "letter-spacing": "type",
    "padding": "space", "padding-top": "space", "padding-bottom": "space",
    "padding-left": "space", "padding-right": "space",
    "margin": "space", "margin-top": "space", "margin-bottom": "space",
    "margin-left": "space", "margin-right": "space",
    "gap": "space", "row-gap": "space", "column-gap": "space",
    "border-radius": "radius",
    "box-shadow": "shadow",
}


def check_tokens(own, by_value):
    """A literal that equals a token's value is a token that wasn't used."""
    hits = Counter()
    examples = {}
    total_props = Counter()
    pasted = Counter()

    for prop, group in PROPERTY_GROUPS.items():
        for m in re.finditer(rf"(?<![\w-]){re.escape(prop)}\s*:\s*([^;{{}}]+)[;}}]", own, re.I):
            value = m.group(1).strip()
            total_props[group] += 1
            if "var(" in value:
                continue
            if not re.search(r"\d\s*(px|rem|em)\b", value) and group != "shadow":
                continue   # unitless numbers are SVG attributes, not CSS lengths
            key = norm(value)
            found = candidates(by_value, key, group)
            if found:
                hits[(group, prop, key)] += 1
                examples.setdefault((group, prop, key), found[0])
            # a multi-value shadow built from two tokens pasted together
            elif group == "shadow" and "," in value:
                parts = [norm(x) for x in re.split(r",(?![^(]*\))", value)]
                named = [candidates(by_value, x, "shadow")[0]
                         for x in parts if candidates(by_value, x, "shadow")]
                if len(named) > 1:
                    pasted[(norm(value), " + ".join(named), value[:58])] += 1

    for (_, named, shown), count in pasted.items():
        fail("shadow", f"{count} rule(s) set `box-shadow: {shown}…` — that is "
                       f"{named} pasted together. Two shadow tokens in one rule "
                       "means the element sits permanently in its hover state")

    for group in ("type", "space", "radius", "shadow"):
        n = sum(c for (g, _, _), c in hits.items() if g == group)
        if n:
            which = sorted({(p, k, examples[(g, p, k)])
                            for (g, p, k) in hits if g == group})[:4]
            shown = ", ".join(f"`{p}: {k}` → `var({t})`" for p, k, t in which)
            fail("hardcoded " + group,
                 f"{n} literal value{'s' if n != 1 else ''} where a token holds "
                 f"that exact value. e.g. {shown}")
        fact(f"{group} declarations", f"{total_props[group]} ({n} hardcoded to a token value)")


# ---------------------------------------------------------------------------
# motion, graphics, portability, faq
# ---------------------------------------------------------------------------
def check_motion(page):
    inlined = "IntersectionObserver" in page
    fact("motion.js inlined", "yes" if inlined else "NO")
    if not inlined:
        fail("motion", "motion.js is not in the page — no IntersectionObserver anywhere. "
                       "The CSS half can be fully inlined and nothing moves; the no-JS "
                       "fallback is clean, so this looks completely normal")
    if ".eq-card" in page and "box-shadow" in page and "bundle.css" not in page:
        note("bundle.css appears inlined without its source comment")


def check_graphics(page):
    svgs = re.findall(r"<svg\b[^>]*>", page, re.I)
    imgs = re.findall(r"<img\b[^>]*>", page, re.I)
    annotated = [s for s in svgs if "data-asset" in s]
    fact("inline SVGs", len(svgs))
    fact("SVGs with data-asset", f"{len(annotated)} of {len(svgs)}")
    fact("<img> elements", len(imgs))
    fact("data-role attributes", len(re.findall(r"data-role=", page)))
    fact("data-reveal blocks", len(re.findall(r"data-reveal", page)))

    if svgs and not annotated:
        fail("graphics", f"0 of {len(svgs)} SVG roots carry data-asset — nothing to animate")
    elif len(annotated) < len(svgs):
        fail("graphics", f"only {len(annotated)} of {len(svgs)} SVG roots carry data-asset; "
                         f"{len(svgs) - len(annotated)} graphics are inert")
    if imgs:
        fail("graphics", f"{len(imgs)} <img> element(s) — every graphic must be inline SVG "
                         "or it cannot be animated or recoloured")
    if not re.search(r"data-reveal", page):
        fail("graphics", "no data-reveal blocks — cards and panels won't stagger in")

    tabs = len(re.findall(r'role="tab"', page))
    hits = len(re.findall(r'data-role="hit"', page))
    fact("hotspots (role=tab)", tabs)
    if tabs and not hits:
        fail("graphics", f"{tabs} tab hotspot(s) with no data-role=\"hit\" rect — "
                         "no target, no highlight, no focus ring")


def check_portable(page):
    real = len(re.findall(r"\bviewBox=", page))
    runtime = len(re.findall(r"sc-camel-view-box", page))
    loops = len(re.findall(r"<sc-for\b", page)) + len(re.findall(r"\{\{", page))
    fact("SVGs with a real viewBox", f"{real} (runtime-spelled: {runtime})")
    fact("template bindings", loops)
    if runtime:
        fail("portable", f"{runtime} SVG(s) use a runtime viewBox spelling instead of "
                         "viewBox — every one loses its scaling when the markup is "
                         "lifted into HubSpot")
    if loops:
        fail("portable", f"{loops} template binding(s) left in the markup — the content "
                         "only exists after JavaScript runs, which is the opposite of "
                         "what an AEO page needs")


def check_faq(page):
    ld = re.search(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', page, re.S)
    visible = re.findall(r"<summary[^>]*>(.*?)</summary>", page, re.S)
    fact("FAQ items (<summary>)", len(visible))
    if not visible:
        fail("faq", "no <details>/<summary> FAQ — the strongest answer-engine format "
                    "on the page is missing")
        return
    if not ld:
        fail("faq", "FAQ present but no FAQPage JSON-LD")
        return
    try:
        data = json.loads(ld.group(1))
    except json.JSONDecodeError:
        fail("faq", "FAQPage JSON-LD does not parse")
        return
    questions = [e.get("name", "") for e in data.get("mainEntity", [])]
    fact("JSON-LD questions", len(questions))
    if len(questions) != len(visible):
        fail("faq", f"{len(visible)} visible question(s) but {len(questions)} in the "
                    "JSON-LD — they must match one for one")


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip().split("\n\n")[1].strip())
        return 2
    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"no such file: {path}")
        return 2

    page, unwrapped = load(path)
    if unwrapped:
        print("(unwrapped a Claude Design bundle — auditing the real page inside)\n")
    own = strip_system(page, system_css())

    check_tokens(own, token_values())
    check_motion(page)
    markup = markup_only(page)
    check_graphics(markup)
    check_portable(markup)
    check_faq(markup)

    width = max(len(k) for k, _ in facts)
    print(f"{os.path.basename(path)} — {len(page):,} bytes\n")
    for label, value in facts:
        print(f"  {label:<{width}}  {value}")

    if problems:
        grouped = {}
        for check, detail in problems:
            grouped.setdefault(check, []).append(detail)
        for check in sorted(grouped):
            print(f"\n{check.upper()}")
            for detail in grouped[check]:
                print(f"  - {detail}")
    if notes:
        print("\nNOTES")
        for d in notes:
            print(f"  - {d}")

    print(f"\n{len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
