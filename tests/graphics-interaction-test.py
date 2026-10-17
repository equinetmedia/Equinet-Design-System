#!/usr/bin/env python3
"""Interactive-graphics test — verifies the INTERACTIVE GRAPHICS section of
components/bundle.css and the HOTSPOT ACTIVATION block of components/motion.js
in a real headless browser.

Run from the repo root:
    pip install playwright && python -m playwright install chromium
    python tests/graphics-interaction-test.py

Checks, each one a thing that would ship silently broken:
  linked graphic   — lifts on hover AND on keyboard focus, not on either alone
  hotspot hover    — highlights via stroke/fill only, never transform/opacity,
                     because motion.js animates both of those on [data-role]
  hotspot focus    — visible navy ring, reachable by Tab, survives hover
  roving tabindex  — the whole graphic is ONE tab stop, not one per hotspot
  keyboard         — arrows move and select, Home/End jump, Space never
                     scrolls the page
  aria             — tablist/tab/tabpanel wired up, panels labelled by their
                     tab, and an unnamed hotspot warns
  no-JS            — panels stay in the document (answer engines read them)
  reduced motion   — the lift is withdrawn, the colour feedback is kept
"""
import os
import sys
import tempfile

from playwright.sync_api import sync_playwright

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = tempfile.mkdtemp(prefix="eq-graphics-")

FIXTURE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://{repo}/tokens.css">
<link rel="stylesheet" href="file://{repo}/components/bundle.css">
<style>body{{margin:0;padding:40px;font-family:sans-serif}} .eq-graphic{{width:320px}}</style>
</head><body>

<a class="eq-graphic" id="linked" href="#somewhere">
  <svg data-asset="linked-demo" viewBox="0 0 200 100">
    <rect data-role="card" x="10" y="10" width="180" height="80" fill="#eeeeee"></rect>
  </svg>
  <span class="eq-graphic__link"></span>
</a>

<div class="eq-graphic eq-graphic--tabs" id="hotspots">
  <svg data-asset="hotspot-demo" viewBox="0 0 300 100" role="tablist" aria-label="Three stages">
    <g class="eq-graphic__hotspot" id="h1" role="tab" aria-controls="p1">
      <title>Step one</title>
      <rect data-role="hit" x="10" y="10" width="60" height="60"></rect>
      <circle data-role="node" cx="40" cy="40" r="18" fill="#00426C"></circle>
    </g>
    <g class="eq-graphic__hotspot" id="h2" role="tab" aria-controls="p2">
      <title>Step two</title>
      <rect data-role="hit" x="110" y="10" width="60" height="60"></rect>
      <circle data-role="node" cx="140" cy="40" r="18" fill="#E06730"></circle>
    </g>
    <g class="eq-graphic__hotspot" id="h3" role="tab" aria-controls="p3">
      <rect data-role="hit" x="210" y="10" width="60" height="60"></rect>
      <circle data-role="node" cx="240" cy="40" r="18" fill="#6BBFC6"></circle>
    </g>
  </svg>
  <div class="eq-graphic__panel" id="p1"><p>Panel one</p></div>
  <div class="eq-graphic__panel" id="p2"><p>Panel two</p></div>
  <div class="eq-graphic__panel" id="p3"><p>Panel three</p></div>
</div>

{script}
</body></html>"""

SCRIPT = '<script src="file://{repo}/components/motion.js"></script>'

passed, failed = [], []


def check(name, condition, detail=""):
    (passed if condition else failed).append(name + (f" — {detail}" if detail and not condition else ""))


def write(path, script=True):
    html = FIXTURE.format(repo=REPO, script=SCRIPT.format(repo=REPO) if script else "")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return "file://" + path


def main():
    with_js = write(os.path.join(TMP, "with-js.html"))
    no_js = write(os.path.join(TMP, "no-js.html"), script=False)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()

        # ---------------------------------------------------------- no JS --
        page = browser.new_page(java_script_enabled=False)
        page.goto(no_js)
        check("no-JS: panels remain in the document",
              page.locator("#p1").count() == 1)
        check("no-JS: panel text is readable by a crawler",
              "Panel one" in page.content())
        page.close()

        # --------------------------------------------------------- with JS --
        page = browser.new_page()
        warnings = []
        page.on("console", lambda m: warnings.append(m.text) if m.type == "warning" else None)
        page.goto(with_js)
        page.wait_for_timeout(200)

        check("unnamed tab warns in the console",
              any("accessible name" in w for w in warnings),
              f"warnings seen: {warnings}")

        # tab defaults
        check("first tab is selected on load",
              page.get_attribute("#h1", "aria-selected") == "true")
        check("its panel is showing",
              page.get_attribute("#p1", "hidden") is None)
        check("the other panels are hidden",
              page.get_attribute("#p2", "hidden") is not None
              and page.get_attribute("#p3", "hidden") is not None)
        check("svg is announced as a tablist",
              page.get_attribute("#hotspots svg", "role") == "tablist")
        check("panels get role=tabpanel",
              page.get_attribute("#p2", "role") == "tabpanel")
        check("panels are labelled by their tab",
              page.get_attribute("#p1", "aria-labelledby") == "h1")

        # ------------------------------------------------- linked graphic --
        def transform_of(sel):
            return page.eval_on_selector(sel, "e => getComputedStyle(e).transform")

        rest = transform_of("#linked")
        page.hover("#linked")
        page.wait_for_timeout(450)
        hovered = transform_of("#linked")
        check("linked graphic lifts on hover", hovered != rest, f"{rest} -> {hovered}")
        check("lift is a 6px rise", "-6" in hovered.replace(" ", ""), hovered)

        page.mouse.move(0, 0)
        page.wait_for_timeout(800)
        page.keyboard.press("Tab")
        page.wait_for_timeout(450)
        check("linked graphic lifts on keyboard focus too",
              transform_of("#linked") != rest)

        # ------------------------------------------------------- hotspots --
        page.goto(with_js)
        page.wait_for_timeout(150)

        def hit_style(hotspot, prop):
            return page.eval_on_selector(
                f'{hotspot} [data-role="hit"]', f"e => getComputedStyle(e).{prop}"
            )

        # #h1 is the selected tab on load, so rest and hover feedback are
        # measured on an UNSELECTED hotspot. Selection outranks hover.
        check("unselected hit rect is invisible at rest",
              hit_style("#h3", "stroke") in ("rgba(0, 0, 0, 0)", "transparent"))
        check("the selected one is marked navy",
              "0, 66, 108" in hit_style("#h1", "stroke"))

        page.hover("#h3")
        page.wait_for_timeout(300)
        stroke = hit_style("#h3", "stroke")
        check("hover strokes an unselected hit rect orange",
              "224, 103, 48" in stroke, stroke)
        check("hover does not transform the hotspot",
              hit_style("#h3", "transform") in ("none", "matrix(1, 0, 0, 1, 0, 0)"))
        check("hover does not change opacity",
              hit_style("#h3", "opacity") == "1")

        page.hover("#h1")
        page.wait_for_timeout(300)
        check("selection outranks hover on the selected tab",
              "0, 66, 108" in hit_style("#h1", "stroke"))

        # ------------------------------------------- roving tabindex / keys --
        page.goto(with_js)
        page.wait_for_timeout(150)

        check("roving tabindex: only the selected tab is in the tab order",
              page.get_attribute("#h1", "tabindex") == "0"
              and page.get_attribute("#h2", "tabindex") == "-1"
              and page.get_attribute("#h3", "tabindex") == "-1")

        page.keyboard.press("Tab")          # #linked
        page.keyboard.press("Tab")          # into the graphic — ONE stop
        focused = page.evaluate("document.activeElement.id")
        check("the whole graphic is one tab stop", focused == "h1",
              f"focus landed on {focused!r}")

        ring = hit_style("#h1", "stroke")
        check("focus ring is navy", "0, 66, 108" in ring, ring)
        check("focus ring is thicker than hover",
              hit_style("#h1", "strokeWidth").startswith("4"))

        page.keyboard.press("ArrowRight")
        page.wait_for_timeout(100)
        check("ArrowRight moves to the next hotspot",
              page.evaluate("document.activeElement.id") == "h2")
        check("automatic activation: moving selects it",
              page.get_attribute("#h2", "aria-selected") == "true")
        check("its panel is revealed",
              page.get_attribute("#p2", "hidden") is None)
        check("the previous panel is hidden again",
              page.get_attribute("#p1", "hidden") is not None)

        page.keyboard.press("ArrowLeft")
        page.wait_for_timeout(100)
        check("ArrowLeft moves back",
              page.evaluate("document.activeElement.id") == "h1")

        page.keyboard.press("ArrowLeft")
        page.wait_for_timeout(100)
        check("ArrowLeft wraps to the last hotspot",
              page.evaluate("document.activeElement.id") == "h3")

        page.keyboard.press("Home")
        page.wait_for_timeout(100)
        check("Home jumps to the first",
              page.evaluate("document.activeElement.id") == "h1")

        page.keyboard.press("End")
        page.wait_for_timeout(100)
        check("End jumps to the last",
              page.evaluate("document.activeElement.id") == "h3")

        check("selected hotspot stays marked",
              "0, 66, 108" in hit_style("#h3", "stroke"))

        page.keyboard.press("Space")
        page.wait_for_timeout(100)
        scrolled = page.evaluate("window.scrollY")
        check("Space does not scroll the page", scrolled == 0, f"scrollY={scrolled}")

        page.click("#h2")
        page.wait_for_timeout(100)
        check("clicking a hotspot selects it",
              page.get_attribute("#h2", "aria-selected") == "true")

        check("panel is focusable, so its content is reachable",
              page.get_attribute("#p2", "tabindex") == "0")
        page.close()

        # ------------------------------------------------- reduced motion --
        page = browser.new_page(reduced_motion="reduce")
        page.goto(with_js)
        page.wait_for_timeout(150)
        before = page.eval_on_selector("#linked", "e => getComputedStyle(e).transform")
        page.hover("#linked")
        page.wait_for_timeout(400)
        check("reduced motion: no lift",
              page.eval_on_selector("#linked", "e => getComputedStyle(e).transform") == before)

        page.hover("#h3")
        page.wait_for_timeout(300)
        check("reduced motion: colour feedback kept",
              "224, 103, 48" in page.eval_on_selector(
                  '#h3 [data-role="hit"]', "e => getComputedStyle(e).stroke"))

        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("ArrowRight")
        page.wait_for_timeout(100)
        check("reduced motion: hotspots still function",
              page.get_attribute("#h2", "aria-selected") == "true")
        page.close()
        browser.close()

    for name in passed:
        print(f"  pass  {name}")
    for name in failed:
        print(f"  FAIL  {name}")
    print(f"\n{len(passed)} passed, {len(failed)} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
