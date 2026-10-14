---
name: equinet-layout
description: Plan and build visually rich Equinet pages from content — turns copy, research or a topic into a section-by-section layout brief, then a finished page built from the Equinet design system's full asset kit — illustrations (whole, or recomposed into bespoke infographics), icons including Lucide, module comps as layout patterns, marketing infographics as style reference, stat blocks, charts, flowcharts, comparisons and HubSpot elements. Use this whenever the user wants an Equinet page, pillar page, landing page, infographic or layout; asks what visuals or modules suit some content; or asks how to present stats, steps, comparisons or data for Equinet — even if they don't say "layout" or "brief".
---

# Equinet layout

Turns content into a **visually rich** Equinet page, in two phases: a brief
that decides what every section becomes, then — once approved — a build that
uses the design system's assets to the full.

The standard to aim for: a page that looks designed, not assembled. Every
section carries a visual element unless it is genuinely an argument best told
in prose — and even then, an icon, a pull-quote or a spot graphic usually
earns its place. A page of headings and paragraphs is a failed build.

## Before starting

This sits on the Equinet design system (`equinetmedia/equinet-design-system`).
Choose assets from `assets/manifest.json` (every asset's background, roles,
palette and subject) and rework them per `assets/REWORKING.md`, targeting
elements by `data-role`.
Its `README.md` opens with a rules digest of binding token, type and
accessibility rules. If the repo isn't in this session, ask for `README.md`
and `assets/illustrations/INDEX.md`.

## The asset kit — four ways to use it

Every asset folder is usable. Work down this list for each section; **the
answer is never "nothing"** — if a whole illustration doesn't match, you build
one from parts.

**1. Place a whole illustration** when its subject matches the section.
Find it in `assets/illustrations/INDEX.md`. Crop, scale and reposition it
freely — illustrations are reference, not sealed artwork.

**Rework to fit the data.** A placed or composed graphic should match the
content's shape exactly — five steps means five cards, not four. Add or
remove `card`/`node`/`connector` elements by `data-role`, move the single
`accent` to the element that is the point, and put every label in HTML
around the graphic, since illustrations carry no live text.

**2. Compose a bespoke graphic** when nothing matches the subject. This is
the normal case for most topics, not a fallback. Pull primitives out of the
illustration files and assemble a new infographic for this content — see
`references/visual-kit.md` for the parts and how to rebuild them as live,
tokened elements. A topic the illustrations never covered still gets a
proper Equinet infographic, built from Equinet parts.

**3. Borrow a layout from `assets/comps/`.** The comps are real,
shipped Equinet module compositions — hero, two-column comparison, five-column
methodology, three-column case study. Use them as blueprints: reproduce their
structure, spacing and hierarchy with live components and this page's
content. (Don't embed a comp as a flat image — rebuild what it shows.)

**4. Match the style of `assets/marketing/`.** Seventeen published Equinet
infographics show how the brand builds diagrams: grey line-work, pale panels,
an orange accent used once or twice, blue for data. When composing a graphic
in step 2, make it look like it belongs in that folder.

**Icons — use Lucide freely.** Any section, list item, card, stat or step can
carry an icon. Where Equinet has no geometry of its own, use Lucide as the
primary iconography source, not a reluctant stand-in: `stroke-width="1"`,
24×24 canvas, round caps and joins, never over 48px, fetched from the library
rather than drawn from memory. Add a one-line comment naming the icon
(`<!-- lucide/target -->`) so its source is traceable. Equinet's own icons
(`assets/icons/`) take priority where one fits.

## Phase 1 — Brief

1. **Find the content's shapes** — numbers, ordered steps, comparisons,
   categories, loops, definitions, quotes, claims. See
   `references/content-to-format.md`.
2. **Give every section a format and a visual.** Format from the content
   shape; visual from the four-way kit above; icons wherever they help
   scanning.
3. **Choose the HubSpot element** that carries the reader's next step — see
   `references/hubspot-elements.md`.
4. **Write the brief** using `references/brief-template.md`.
5. **Stop and ask for approval** before building.

**The brief is the default** — never skipped unasked. `build direct` is the
opt-in exception: still do steps 1–4, skip only step 5's approval stop, and
open the build with the section plan as a short list. Skipping the brief never
means skipping the planning.

## Phase 2 — Build

1. Build from the approved brief, section by section.
2. Reuse first: `.eq-stagger`, `.eq-lead` (with `--accent` and `--on-dark`), the button classes, the shipped modules, the
   comp layouts. Build new only where nothing exists — and say so.
3. Compose graphics from the visual kit in the brand palette. Make them
   substantial: an infographic is several related elements with a clear
   visual relationship, not one icon in a box.
4. Apply AEO structure (below) and the design-system digest throughout.
5. **Count, then report.** State these in the reply before finishing. Any
   "0 of N" means the page is dead on arrival — fix it, don't caveat it.

   - SVG roots, and how many carry `data-asset`
   - drawn elements, and how many carry `data-role`
   - blocks carrying `data-reveal`
   - is `motion.js` inlined? bytes?
   - SVGs with a real `viewBox`, out of the total
   - template loops or `{{ }}` left in the markup (must be 0)
   - hardcoded px font-sizes, spacings and shadows where a token exists
     (must be 0 — run `tools/check-built-page.py`)
   - FAQ items, and does the JSON-LD match them word for word?
   - multi-part graphics, and how many are tab sets

6. **Close with three lists:** new components built; data gaps (including any
   `data.json` value left unused as `transcribed` or `not-quotable`); and
   needs confirmation — placeholder links, invented wording, claims about the
   client. Silence on these reads as "checked".

## Built into every page — no prompt needed

Every build ships these, whether or not the prompt mentions them.

**0. Inline the CSS and the JS — do this first.** The *whole* of
`bundle.css`, the *whole* of `motion.js`, and the `:root` block from
`tokens.css`, pasted into the page. Never a `<link>` or `<script src>`: a
standalone file, a Claude Design page, an artifact and an emailed deliverable
all fail to resolve repo paths, and they fail **silently** — no error, nothing
missing on screen, just a dead page. If unsure, inline it.

**Use the tokens.** Once `tokens.css` is in the page, every font size,
spacing value, radius and shadow comes from `var(--equinet-…, fallback)`.
Writing `font-size: 36px` or `padding: 24px` or a pasted `box-shadow` when a
token holds that value is the most common way a page drifts off-system while
looking roughly right. `tools/check-built-page.py` counts these.

**1. Literal HTML, not a template.** Real `<details>`, real cards, real
`viewBox` on every SVG. No loops over data arrays, no `{{ }}` bindings, no
runtime-only attribute spellings. The page must read correctly with no
JavaScript — it is the AEO argument, it is what ports into HubSpot, and it is
what lets the JSON-LD be checked against the visible text. If your surface
rewrites markup on export, say so and name the rendered DOM as the
deliverable.

**2. Interaction states on everything interactive.** `.btn-primary`,
`.btn-navigation`, `.btn-textual` for actions; `.eq-card` for content cards.
A card that links somewhere gets `.eq-card__link` inside it and lifts 6px on
hover and keyboard focus. A card that links nowhere gets neither: rising on
hover promises a click.

**3. Entrance motion.** `motion.js` animates two things:
- **Graphics** — inline every SVG (never `<img>`), `data-asset="name"` on the
  root, and a `data-role` (card, node, connector, glyph, accent, panel) on
  every drawn element, *including graphics you compose from scratch*. Without
  these the script has nothing to animate.
- **Blocks** — `data-reveal` on cards, stat panels and section blocks.

**4. Navigable graphics.** Any multi-part graphic — a flow, a system diagram,
a set of stages — is a tab set: each part a hotspot revealing a detail panel,
one showing at a time.

```html
<div class="eq-graphic eq-graphic--tabs">
  <svg data-asset="flow-name" viewBox="…" role="tablist" aria-label="The four stages">
    <g class="eq-graphic__hotspot" role="tab" id="t1" aria-controls="p1">
      <title>Audit</title>                     <!-- the accessible name -->
      <rect data-role="hit" x="…" y="…" width="…" height="…"></rect>
      …the artwork for this stage…
    </g>
  </svg>
  <div class="eq-graphic__panel" id="p1"><p>The detail for that stage.</p></div>
</div>
```

`motion.js` wires the ARIA, the roving tabindex (one tab stop for the whole
graphic), arrow keys, Home/End, and selection. **Write the panels visible** —
only the script sets `hidden`, so with no script every panel still reads.
Every hotspot needs a transparent `<rect data-role="hit">` of at least
24 × 24 units and an accessible name from `<title>` or `aria-label`.

A panel carries the context the graphic can't draw, not a caption restating
the label. A part with nothing worth revealing isn't a hotspot.

`role="button"` on a lone hotspot is the disclosure variant.
`.eq-graphic__link` makes the whole graphic a link — rare.

**5. An FAQ as an accordion.** `.eq-faq` on native `<details>`/`<summary>`,
plus `FAQPage` JSON-LD matching the visible text word for word.

```html
<div class="eq-faq">
  <details class="eq-faq__item">
    <summary class="eq-faq__question">What is GEO?
      <span class="eq-faq__icon" aria-hidden="true"><!-- arrow-chevron.svg, inline --></span>
    </summary>
    <div class="eq-faq__answer"><p>…</p></div>
  </details>
</div>
```

**Don't add:** looping or ambient animation, or any response on a graphic
that does nothing. Don't highlight with `transform` or `opacity` — `motion.js`
animates both on `[data-role]` during entrance. Stroke and fill only.

**Already handled, so don't re-implement:** reduced motion, no-JS fallback,
keyboard access, visible focus. Covered by `tests/components-test.py`,
`tests/motion-test.py` and `tests/graphics-interaction-test.py`.

## The one hard limit: never invent data

Visual richness comes from design, never from made-up facts. A stat block
needs a real figure from the supplied content — or from
`assets/charts/data.json`, which holds sourced figures on AI adoption in
manufacturing, each marked verified, transcribed or not-quotable. Show the
source with the figure. Never quote a `not-quotable` value, and treat
`transcribed` figures as needing a check before a new claim is built on them. If a section
would suit data the content lacks, the brief lists it as a gap for the user —
and the section gets a composed graphic or icon treatment instead of a fake
number. This is the only place to hold back; everywhere else, use the kit.

## Charts

No chart component exists yet. Build charts live — real `<text>`, real values
from the content or `data.json`, the source shown beneath — and note them as
new so they can be promoted. Draw bars to scale: one of the seven existing
charts sizes bars by eye, off by up to 7 points, and a chart that misstates
its own data undoes the credibility the source lends it. Prefer bars to pies.

Palette: **navy, orange and teal** — `--equinet-color-navy`,
`--equinet-color-amber-400`, `--equinet-color-teal-default`. Ruled 2026-10-13
in favour of the seven shipped charts over the `--equinet-color-chart-blue-*`
tokens, which were sanctioned from a single infographic and which no real
chart uses. Don't ask which palette; this one.

## AEO structure

- H2s phrased the way someone would ask.
- Each section opens with a direct, self-contained answer, then expands.
- Terms defined on first use; entities named explicitly.
- Tables and lists where content is genuinely enumerable.
- One idea per section, so any chunk stands alone as an answer.
- Every page ends with an FAQ (see "Built into every page") — it's the
  strongest AEO format, because it's literally question and answer.
