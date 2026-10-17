#!/usr/bin/env python3
"""Reading-progress test — [data-progress] / [data-step] in a real browser.

    python tests/progress-test.py

The distinction being protected: progress emphasis is a REPORT, not a
promise. It must never behave like an affordance, must never hide content
behind scrolling, and must never flicker on an upward scroll.
"""
import os, sys, tempfile
from playwright.sync_api import sync_playwright

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = tempfile.mkdtemp(prefix="eq-progress-")

HTML = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://{r}/tokens.css">
<link rel="stylesheet" href="file://{r}/components/bundle.css">
<style>body{{margin:0}}.sp{{height:120vh}}.step{{height:70vh;padding:40px}}</style>
</head><body>
<div class="sp"></div>
<div data-progress id="flow">
  <div class="step eq-card" data-step id="s1"><h3>One</h3><p>Readable always.</p></div>
  <div class="step eq-card" data-step id="s2"><h3>Two</h3></div>
  <div class="step eq-card" data-step id="s3"><h3>Three</h3></div>
</div>
<div class="sp"></div>
<script src="file://{r}/components/motion.js"></script>
</body></html>"""

passed, failed = [], []
def ok(n, c, d=""):
    (passed if c else failed).append(n + (f"  — {d}" if d else ""))

def css(pg, sel, prop):
    return pg.evaluate("([s,p])=>getComputedStyle(document.querySelector(s))[p]", [sel, prop])

def reached(pg, sel):
    return pg.evaluate("s=>document.querySelector(s).classList.contains('is-reached')", sel)

def main():
    path = os.path.join(TMP, "p.html"); open(path, "w").write(HTML.format(r=REPO))
    url = "file://" + path
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 800})
        pg.goto(url); pg.wait_for_timeout(300)

        ok("G1 nothing is reached before scrolling", not reached(pg, "#s1"))
        ok("G2 an unreached step stays readable — never below 0.6",
           float(css(pg, "#s1", "opacity")) >= 0.6, css(pg, "#s1", "opacity"))
        ok("G3 an unreached step is not displaced",
           css(pg, "#s1", "transform") in ("none", "matrix(1, 0, 0, 1, 0, 0)"))

        pg.locator("#s1").scroll_into_view_if_needed(); pg.wait_for_timeout(700)
        ok("G4 reaching a step lights it", reached(pg, "#s1"))
        ok("G5 the reached step is at full strength", css(pg, "#s1", "opacity") == "1")
        ok("G6 and lifted 4px — a report, not an invitation",
           "-4" in css(pg, "#s1", "transform").replace(" ", ""), css(pg, "#s1", "transform"))
        ok("G7 a later step is not yet reached", not reached(pg, "#s3"))

        pg.locator("#s3").scroll_into_view_if_needed(); pg.wait_for_timeout(700)
        ok("G8 scrolling on reaches the later step", reached(pg, "#s3"))

        pg.mouse.wheel(0, -4000); pg.wait_for_timeout(700)
        ok("G9 reached is permanent — no flicker scrolling back up",
           reached(pg, "#s1") and reached(pg, "#s3"))

        # it must never behave like an affordance
        pg.hover("#s2"); pg.wait_for_timeout(500)
        ok("G10 hovering an unlinked step does nothing — no false promise",
           css(pg, "#s2", "cursor") != "pointer")
        pg.close()

        # no JS at all
        pg = b.new_page(viewport={"width": 1200, "height": 800}, java_script_enabled=False)
        pg.goto(url); pg.wait_for_timeout(300)
        ok("G11 no JS: every step readable, nothing hidden behind scrolling",
           float(css(pg, "#s3", "opacity")) >= 0.6, css(pg, "#s3", "opacity"))
        pg.close()

        # reduced motion
        pg = b.new_page(viewport={"width": 1200, "height": 800}, reduced_motion="reduce")
        pg.goto(url); pg.wait_for_timeout(300)
        ok("G12 reduced motion: every step at full strength immediately",
           css(pg, "#s3", "opacity") == "1" and not reached(pg, "#s3"),
           css(pg, "#s3", "opacity"))
        ok("G13 reduced motion: nothing travels",
           css(pg, "#s1", "transform") in ("none", "matrix(1, 0, 0, 1, 0, 0)"))
        pg.close(); b.close()

    for n in passed: print(f"  pass  {n}")
    for n in failed: print(f"  FAIL  {n}")
    print(f"\n{len(passed)} passed, {len(failed)} failed")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
