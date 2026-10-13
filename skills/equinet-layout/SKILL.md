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

**The brief is the default. Always offer it; never skip it unasked.** Where
the prompt hasn't ruled, write the brief and stop — a page is cheaper to
redirect as a plan than as a build.

**`build direct` is the opt-in exception.** When the prompt says `build
direct` (or plainly asks to skip the brief), still do steps 1–4 — they decide
what every section becomes — and skip only step 5's approval stop. Open the
build with the section plan as a short list, so the thinking is visible and
correctable even though you didn't wait. "Skip the brief" never means skip the
planning; a build that goes straight to markup is the one that arrives as
headings and paragraphs.

## Phase 2 — Build

1. Build from the approved brief, section by section.
2. Reuse first: `.eq-stagger`, `.eq-lead` (with `--accent` and `--on-dark`), the button classes, the shipped modules, the
   comp layouts. Build new only where nothing exists — and say so.
3. Compose graphics from the visual kit in the brand palette. Make them
   substantial: an infographic is several related elements with a clear
   visual relationship, not one icon in a box.
4. Apply AEO structure (below) and the design-system digest throughout.
5. **Count, then report.** Before finishing, count and state these five
   numbers in the reply:

   - SVG roots on the page, and how many carry `data-asset`
   - drawn elements inside them, and how many carry `data-role`
   - blocks carrying `data-reveal`
   - whether `motion.js` is inlined (yes/no) and its byte count
   - FAQ items, and whether the `FAQPage` JSON-LD matches them word for word
   - SVGs carrying a real `viewBox` attribute, out of the total
   - template loops or `{{ }}` bindings left in the markup (must be 0)

   Any count that reads 0 of N, or a `motion.js` answer of "no", means the
   page is dead on arrival — fix it before replying, don't report it as a
   caveat. Counting is the only way to catch this, because a page missing all
   of its motion looks completely normal in a screenshot.
6. Finish with three short lists, every build, asked for or not:
   - **New components built** — anything that didn't already exist, so it can
     be promoted into `bundle.css` rather than rebuilt next time.
   - **Data gaps** — figures a section would have carried if the content had
     them, and any `data.json` value left unused because it is `transcribed`
     or `not-quotable` rather than `verified`.
   - **Needs confirmation** — placeholder links, invented service wording,
     claims about the client, and anything else written to fill a hole rather
     than supplied. A `#` href and a paragraph describing a service the user
     never described both belong here. Silence on these reads as "checked",
     which is the one thing it never means.

## Built into every page — no prompt needed

Every build ships these three, whether or not the prompt mentions them.
They're the difference between a page that looks designed and one that feels
designed.

**Do this first, before any of the three: inline the CSS and the JS.** Paste
the needed rules from `bundle.css` and the *whole* of `motion.js` into the
page. Do not reference them with a `<link>` or a `<script src>` unless the
page provably resolves repository paths — a standalone HTML file, a Claude
Design page, an artifact and an emailed deliverable all do not. **This is the
normal case, not the exception.**

A reference that doesn't resolve **fails silently**: no console error, no
broken layout, nothing missing on screen. Every rule below can be followed
perfectly and the page still arrives dead, which is exactly how this went
wrong twice — see CHANGELOG, 2026-10-02 and 2026-10-13. If you are unsure
whether the page can reach the repo, inline it. Inlining costs a few
kilobytes; the alternative costs the whole feature with no symptom.

**Literal HTML, not a template.** Write the page as real markup: real
`<details>` elements, real cards, real `viewBox` attributes on every SVG. Do
not express repeated content as a template loop over a data array, and do not
leave runtime-only attribute spellings in the file. The page must read
correctly as plain HTML with no runtime, for three reasons that all bite
later:

- **It's the whole AEO argument.** Content that exists only after JavaScript
  runs is content an answer engine may never see. A page about being cited,
  whose source carries no text, fails at the thing it describes.
- **It's what ports.** A module build lifts this markup into HubSpot. A loop
  over `{{ items }}` and a non-standard `viewBox` spelling both arrive broken.
- **It's what the JSON-LD has to match.** Questions bound to a data array
  can't be diffed against the `FAQPage` block by reading the file.

If the surface you're building on rewrites the markup on export, say so in
the reply and tell the user the rendered DOM is the deliverable, not the
saved file.

**1. Interaction states on everything interactive.** Use the components in
`components/bundle.css`, which already carry hover, focus-visible and active
states: `.btn-primary`, `.btn-navigation` and `.btn-textual` for actions, and
`.eq-card` for content cards. A card that links somewhere gets
`.eq-card__link` inside it — that stretches the link over the whole card and
makes it lift 6px on hover *and* on keyboard focus. A card that doesn't link
anywhere gets no link and doesn't lift: rising on hover promises a click.

**2. Entrance motion.** `components/motion.js`, inlined per the rule above.
It animates two things:
- **Graphics** — inline every SVG (never `<img>`), put `data-asset="name"` on
  its root, and a `data-role` (card, node, connector, glyph, accent, panel) on
  every drawn element, *including in graphics you compose from scratch*.
  Without `data-asset` and roles, the script has nothing to animate.
- **Blocks** — add `data-reveal` to cards, stat panels and section blocks.
  Siblings arrive in sequence.

**3. An FAQ as an accordion.** Every page gets an FAQ section built with
`.eq-faq` on native `<details>`/`<summary>`, plus `FAQPage` JSON-LD whose
questions and answers match the visible text word for word. It's the
strongest answer-engine format on the page, and the native element keeps
every answer in the document even when collapsed.

```html
<div class="eq-faq">
  <details class="eq-faq__item">
    <summary class="eq-faq__question">What is GEO?
      <span class="eq-faq__icon" aria-hidden="true"><!-- assets/icons/arrow-chevron.svg, inline --></span>
    </summary>
    <div class="eq-faq__answer"><p>…</p></div>
  </details>
</div>
```

The chevron is Equinet's own `arrow-chevron` — the CSS rotates it to point
down, and up when open.

**What all three already handle, so don't re-implement it:** reduced motion
(everything static, feedback kept), no-JS fallback (nothing hidden, FAQ still
works), keyboard access, and visible focus. Verified in a real browser by
`tests/components-test.py` and `tests/motion-test.py`.

**Don't add:** looping or ambient animation, or hover motion on a graphic that
isn't inside a link. Motion should answer an action or mark an arrival, not
decorate.

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
