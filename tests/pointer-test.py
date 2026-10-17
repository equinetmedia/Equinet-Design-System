#!/usr/bin/env python3
"""Pointer-response test — .eq-card--spotlight / .eq-card--edge in a real
headless browser.

    python tests/pointer-test.py

Checks the things that would ship silently wrong: tracking that doesn't
follow, a hover state that latches on touch, information living only in
hover, and reduced motion losing the feedback along with the movement.
"""
import os, sys, tempfile
from playwright.sync_api import sync_playwright

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = tempfile.mkdtemp(prefix="eq-pointer-")

HTML = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://{r}/tokens.css">
<link rel="stylesheet" href="file://{r}/components/bundle.css">
<style>body{{margin:0;padding:40px;display:flex;gap:24px}}.eq-card{{width:280px;height:200px}}</style>
</head><body>
<article class="eq-card eq-card--spotlight" id="spot">
  <h3 class="eq-card__title"><a class="eq-card__link" href="#a" id="spotlink">Recommended</a></h3>
  <p class="eq-card__text">Readable without any hover state.</p>
</article>
<article class="eq-card eq-card--edge" id="edge">
  <h3 class="eq-card__title"><a class="eq-card__link" href="#b">Case study</a></h3>
</article>
<article class="eq-card" id="plain"><h3 class="eq-card__title">Plain</h3></article>
<script src="file://{r}/components/motion.js"></script>
</body></html>"""

passed, failed = [], []
def ok(name, cond, detail=""):
    (passed if cond else failed).append(name + (f"  — {detail}" if detail else ""))

def prop(pg, sel, name):
    return pg.evaluate("([s,n])=>getComputedStyle(document.querySelector(s)).getPropertyValue(n).trim()", [sel, name])

def opacity(pg, sel, pseudo):
    return pg.evaluate("([s,p])=>getComputedStyle(document.querySelector(s),p).opacity", [sel, pseudo])

def main():
    path = os.path.join(TMP, "p.html")
    open(path, "w").write(HTML.format(r=REPO))
    url = "file://" + path

    with sync_playwright() as pw:
        b = pw.chromium.launch()

        # ---------------------------------------------------- fine pointer --
        pg = b.new_page(viewport={"width": 1200, "height": 500})
        pg.goto(url); pg.wait_for_timeout(300)

        ok("P1 at rest the spotlight is invisible", opacity(pg, "#spot", "::before") == "0")
        ok("P2 content is readable with no hover — nothing lives in the effect",
           pg.evaluate("()=>document.querySelector('#spot .eq-card__text').textContent.length>10"))

        box = pg.locator("#spot").bounding_box()
        pg.mouse.move(box["x"] + 60, box["y"] + 50); pg.wait_for_timeout(250)
        x1, y1 = prop(pg, "#spot", "--eq-pointer-x"), prop(pg, "#spot", "--eq-pointer-y")
        ok("P3 entering writes the pointer position", x1.endswith("px") and y1.endswith("px"), f"{x1} {y1}")

        pg.mouse.move(box["x"] + 220, box["y"] + 160); pg.wait_for_timeout(250)
        x2, y2 = prop(pg, "#spot", "--eq-pointer-x"), prop(pg, "#spot", "--eq-pointer-y")
        ok("P4 the effect tracks — moving changes both axes",
           x2 != x1 and y2 != y1, f"{x1},{y1} -> {x2},{y2}")
        ok("P5 coordinates are card-relative, not page-relative",
           0 <= float(x2[:-2]) <= box["width"] and 0 <= float(y2[:-2]) <= box["height"],
           f"{x2},{y2} in a {box['width']:.0f}x{box['height']:.0f} card")
        ok("P6 hovering fades it in", opacity(pg, "#spot", "::before") == "1")

        pg.mouse.move(5, 5); pg.wait_for_timeout(900)
        ok("P7 leaving fades it out", opacity(pg, "#spot", "::before") == "0")
        ok("P8 leaving resets the position to centre",
           prop(pg, "#spot", "--eq-pointer-x") == "50%",
           prop(pg, "#spot", "--eq-pointer-x"))

        ok("P9 a plain card gets no treatment at all",
           opacity(pg, "#plain", "::before") in ("0", "1") and
           pg.evaluate("()=>!document.querySelector('#plain').hasAttribute('data-pointer-ready')"))

        pg.keyboard.press("Tab"); pg.wait_for_timeout(250)
        ok("P10 keyboard focus gets the same emphasis, centred",
           opacity(pg, "#spot", "::before") == "1" and prop(pg, "#spot", "--eq-pointer-x") == "50%")

        box = pg.locator("#edge").bounding_box()
        pg.mouse.move(box["x"] + 40, box["y"] + 40); pg.wait_for_timeout(250)
        ok("P11 the edge variant tracks too", prop(pg, "#edge", "--eq-pointer-x").endswith("px"))
        ok("P12 edge lights its border, not a wash", opacity(pg, "#edge", "::after") == "1")
        pg.close()

        # --------------------------------------------------- coarse pointer --
        pg = b.new_page(viewport={"width": 390, "height": 700},
                        has_touch=True, is_mobile=True)
        pg.goto(url); pg.wait_for_timeout(300)
        ok("P13 touch: the script does not attach",
           pg.evaluate("()=>!document.querySelector('#spot').hasAttribute('data-pointer-ready')"))
        pg.close()

        # --------------------------------------------------- reduced motion --
        pg = b.new_page(viewport={"width": 1200, "height": 500}, reduced_motion="reduce")
        pg.goto(url); pg.wait_for_timeout(300)
        ok("P14 reduced motion: no tracking attached",
           pg.evaluate("()=>!document.querySelector('#spot').hasAttribute('data-pointer-ready')"))
        box = pg.locator("#spot").bounding_box()
        pg.mouse.move(box["x"] + 200, box["y"] + 150); pg.wait_for_timeout(250)
        ok("P15 reduced motion: feedback kept, centred and still",
           opacity(pg, "#spot", "::before") == "1" and prop(pg, "#spot", "--eq-pointer-x") == "50%")
        pg.close()
        b.close()

    for n in passed: print(f"  pass  {n}")
    for n in failed: print(f"  FAIL  {n}")
    print(f"\n{len(passed)} passed, {len(failed)} failed")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
