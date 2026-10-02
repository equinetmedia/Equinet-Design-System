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

**3. Borrow a layout from `assets/comps/`.** The four comps are real,
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

## Phase 2 — Build

1. Build from the approved brief, section by section.
2. Reuse first: `.eq-stagger`, `.eq-lead` (with `--accent` and `--on-dark`), the button classes, the shipped modules, the
   comp layouts. Build new only where nothing exists — and say so.
3. Compose graphics from the visual kit in the brand palette. Make them
   substantial: an infographic is several related elements with a clear
   visual relationship, not one icon in a box.
4. Apply AEO structure (below) and the design-system digest throughout.
5. Finish with a short list of any new components built.

## Motion

Inline graphics and load `components/motion.js` — every annotated graphic then
gets a once-only entrance (ground, cards, lines drawing on, nodes, glyphs,
accent last), with no per-graphic code. Elements you add while reworking must
keep a `data-role` or they won't join the sequence. Don't add looping or
hover animation to graphics: a graphic isn't a control, and motion on hover
implies it can be clicked.

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

Palette: the documented data palette is `--equinet-color-chart-blue-*`, but
all seven real charts in `assets/charts/` use navy, orange and teal. That's an
open decision — see `assets/charts/README.md` — so match whichever the user
confirms, and say which you used.

## AEO structure

- H2s phrased the way someone would ask.
- Each section opens with a direct, self-contained answer, then expands.
- Terms defined on first use; entities named explicitly.
- Tables and lists where content is genuinely enumerable.
- One idea per section, so any chunk stands alone as an answer.
- An FAQ section is the strongest AEO format — include one where the content
  answers common questions.
