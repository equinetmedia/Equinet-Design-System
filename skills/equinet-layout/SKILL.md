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

## Before any of this: why the rules are the rules

`METHODOLOGY.md` holds the reasoning behind everything below — how a page is
read (NN/g), what a component looks like it does (IxDF), and how the offer
earns the next step (Baymard). **Read it when a rule has to be applied to a
case it does not cover, or when a rule looks wrong.** Where a rule covers the
case, follow the rule: it is more specific and already measured.

The short version, because it decides most calls:

- Readers scan headings and the left edge. Headings carry the argument.
- Group by proximity and shared surface. A border is the last resort.
- Make depth reachable, not present — tabs, accordions, panels.
- Every visual promise must be keepable. A hover state is a promise.
- Respond within 120ms; release over 600ms.
- One primary action, repeated, never competing.
- Nothing may exist only in motion or hover.

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
   - sections opening with an eyebrow, out of the total (every one)
   - icons placed: Equinet's own, vendored Lucide, and any you could not
     find (that last number should be 0 — name them if not)
   - sections carrying a draughtsman's background (2–3 expected; 0 is a fix)
   - does a reader of only the headings get the whole argument? yes/no
   - primary CTAs (one action, repeated) and whether the offer's shape —
     duration, what you leave with, what it costs — is stated before it
   - multi-part graphics, and how many are tab sets — **every one of them
     should be**, so anything short of all is a fix, not a statistic

6. **Close with three lists:** new components built; data gaps (including any
   `data.json` value left unused as `transcribed` or `not-quotable`); and
   needs confirmation — placeholder links, invented wording, claims about the
   client. Silence on these reads as "checked".

## Phase 3 — Review before you hand it back

Phase 2's count catches what is missing. This catches what is wrong. Answer
each line yes or no **about the page you just built**, and fix anything that
answers no before replying. A no you report instead of fixing is a defect you
noticed and shipped.

Fifteen questions, grouped by where the reasoning comes from. The long form
is `METHODOLOGY.md`.

**How it is read — NN/g**

1. Does a reader of only the headings get the whole argument? If the headings
   are labels rather than claims, rewrite them.
2. Does every section open with its answer, before any throat-clearing?
3. Does the first screenful carry the claim *and* a reason to believe it —
   not the whole argument, but enough to earn the scroll?
4. Is anything that looks like decoration actually decoration? A real offer
   styled like a banner gets skipped.
5. Is the detail reachable rather than present — tabs, accordions, panels —
   so the reader wanting the summary is not taxed by the one wanting depth?

**What things look like they do — IxDF**

6. Does every hover state, cursor change and lift belong to something that
   actually does something? Count the inert ones; the answer should be zero.
7. Is grouping done by proximity and shared surface before borders? A box
   around things already close is noise.
8. Is every target at least 24 x 24, and is the whole card the target rather
   than just its title?
9. Does every control have a visible hover, focus-visible and active state?
10. Can a keyboard reach everything a pointer can, with focus as visible as
    hover?

**Whether it earns the next step — Baymard**

11. Is there exactly one primary action, repeated, with nothing competing for
    the same styling?
12. Does the CTA say where it goes? "Submit" and "Learn more" carry no scent.
13. Is the shape of the offer — how long, what you leave with, what it costs —
    stated *before* the button, not after?
14. Does every figure carry its source beside it?
15. Does the page still work with no JavaScript, no pointer and no motion?

Report the numbers you answered no to and what you changed. If all fifteen
are yes, say so in one line.

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

**Decide what a card does before you build it.** A page of seventeen cards
that all link nowhere is a page where nothing responds to the cursor, and it
reads as broken even though every rule was followed. Either give a card a
destination — the section it summarises, the FAQ answer it previews, the
anchor it belongs to — or make the content a panel rather than a card. If
most cards on the page end up inert, that is a layout problem, not a styling
one.

**3. Entrance motion.** `motion.js` animates two things:
- **Graphics** — inline every SVG (never `<img>`), and on graphics **larger
  than 64px**, `data-asset="name"` on the root plus a `data-role` (card,
  node, connector, glyph, accent, panel) on every drawn element, *including
  graphics you compose from scratch*. Without these the script has nothing to
  animate.
- **Blocks** — `data-reveal` on cards, stat panels and section blocks.

**Don't annotate icons.** A 24px tick or chevron gets inlined like everything
else, but no `data-asset` and no `data-role`. A page carries dozens of them,
and animating each one's paths adds hundreds of elements to the entrance for
line art a few pixels across — it buys nothing a reader sees and makes
scrolling stutter. `motion.js` enforces the same 64px gate itself.

**A card that carries more than a title and a line of text** —
an image, figures, links out, a read-more — is `.eq-card--stacked`. Full-bleed
16:9 media at the top, padding on the body rather than the card, stat rows
ruled at 1px, and the read-more as the card's single `.eq-card__link` so the
whole card is the target. Measurements in `assets/components/README.md`.

**Heading level and type size are two different decisions.** The element
(`<h1>`–`<h6>`) comes from document structure: descending, never skipping,
one `<h1>` per page. The size comes from a **role** token — card heading,
eyebrow, price. They rarely agree, and that is correct: one `<h3>` can
legitimately render at four different sizes on one page. Never size text by
reaching for `--equinet-fontsize-h3` because the element is an `<h3>`.
Getting this backwards ships one of two failures: a broken heading order to
get the right size, or the wrong size to keep the order. Roles are tabled in
`TYPE-ROLES.md`.

**Two things that ruling settles.** A heading that *opens* a section is 40px
(`--equinet-fontsize-h2`); one *inside* a section is 36px
(`--equinet-fontsize-section-heading`). And 48px is no longer a heading size
at all — it survives only as `--equinet-fontsize-price`, which is a `<p>`,
never an `<hN>`. Comps that shipped 36px section headings predate this; treat
that as drift to correct, not intent to reproduce. It is the one place a comp
is not ground truth.

**Typography is `.eq-h1` … `.eq-body`**, not hand-set sizes. Open Sans 800
at -0.07em, uppercase, for h1/h2/h3-section; Source Sans for the card
heading, h4, lead and body. Where two display headings would stack, make one
`--light` (weight 300) — and leave its shadow off, which is the variant
rather than an omission. Full scale in `assets/type/README.md`.

**A fact about an item is a `.eq-tag`, not an eyebrow.** Sentence case,
grey, 4px radius — "Scoped before set-up". An eyebrow is UPPERCASE and names
what a *section* is — "PRICING". If the words would read oddly in capitals,
it is a tag. Four variants in ascending weight (`--outline`, `--solid`,
`--blue`), and **at most one emphasised tag in a group**. A tag is not a
control: no hover, no cursor change. One that genuinely filters is a
`<button>`.

**The eyebrow is orange, `#E06730`.** Ruled 2026-10-17. One Figma export
(`assets/type/eyebrow-fontstyle.svg`) shows it in the heading colour; that
export is superseded on colour. Orange measures 3.41:1 on white, below AA,
and that is a known accepted cost — **do not substitute a darker colour to
satisfy contrast**. `--solid-safe` exists for a build explicitly told to be
compliant, and for nothing else.

**The eyebrow above a heading is `.eq-eyebrow`.** The plain orange one is
the default. `.eq-eyebrow--solid` — the same label in a pale pill — is
rationed to hero banners, CTA banners and modules carrying exceptional value.
More than one or two on a page means it is decoration and the plain variant
was right. Orange at 12px/700 fails AA on every ground this system has, so
where a build can't carry that, `--solid-safe` and `--on-dark` are the
compliant forms; see `assets/components/README.md`.

**A section that needs depth gets `.eq-surface`**, not a flat fill — an
off-centre pool of white falling away to `surface--alt`, built in CSS. There
are four positions. Stacked siblings rotate through them on their own, so
plain `.eq-surface` on each is usually all you need; name `--01`…`--04` to
pin one, or override the four custom properties for a bespoke pool. Keep the
2:1 axis ratio and the centre off 50% 50%, and never choose a position at
random — the same page must render the same way tomorrow.

`.eq-surface--dark` is the deep navy version, for a section or card meant to
stand apart. **Sparingly** — it never joins the rotation. Content on it
inherits white; the one accent that passes AA there is `teal-default`, and
orange does not (3.08:1).

**Every section opens with an eyebrow.** `.eq-eyebrow`, plain and orange. It
names what the section *is* before the heading claims anything — the pattern
across every shipped pencilBar module. A section that opens straight into a
heading reads as a wall; the eyebrow is what lets a scanning reader place it.
The `--solid` pill stays rationed to hero and CTA banners, **and takes no
icon — plain text only.** The pill is already the emphasis; a glyph inside it
is emphasis decorating emphasis, and the two compete rather than compound.
Icons belong on the plain eyebrow.

**Pair the eyebrow with an icon wherever the section has a subject an icon
can carry.** `.eq-eyebrow__icon` before the label, taking `currentColor` so
it follows the eyebrow onto a dark surface without a second rule. Reach into
`assets/icons/` first — the service marks and concept nodes are Equinet's
own — and otherwise take one of the **2159 Lucide glyphs
vendored in `assets/icons/lucide/`** — the whole library is there. Its
`INDEX.md` opens with a 76-glyph shortlist covering most pages; search the
full list only if none of those fit. Inline the file. Never reproduce an icon's path
data from memory, even one you think you know: that is why pages were coming
back with no substituted icons at all. If the glyph you need is not in the
folder, say so in the close-out instead of inventing it
(`assets/icons/ICON-REFERENCE.md`).

**Icons are not confined to eyebrows.** A card with a subject takes one, a
stat panel takes one, a list of steps takes one per step. The system ships
21 icons across four groups and they are the cheapest way to give a section
a face. The limit is meaning, not quantity: an icon that illustrates nothing
is noise, and the same icon used twice on a page for two different things is
worse than none.

**Every page uses the draughtsman's line work — on two or three sections,
not one and not every one.** It was going unused because nothing here said to
reach for it; placement was documented and selection was not. A page without
it is a page of flat panels.

Match the file to what the section is about:

| File | The section it belongs behind |
| --- | --- |
| `draftmans-background-hero-banner` | the hero, almost always |
| `draftmans-background-process-flow` | a method, a sequence, a how-it-works |
| `draftmans-background-market-amplification` | reach, growth, distribution, results |

Two or three across a page. More and it stops being texture. Set the copy in
the open side of the frame — `assets/backgrounds/README.md` names which side
that is for each — and never put it behind a stat, a chart, or anything a
reader has to decode. It pairs with `.eq-surface`: the surface gives the
section its depth, the line work gives it a subject.

**Module backgrounds are a separate thing from graphics.**
`assets/backgrounds/` holds draughtsman's line work — construction circles,
arcs, dashed centre lines — meant to sit behind a section as texture. Place
one as a CSS `background-image`, never inline, and never give it `data-asset`
or `data-role`: inlined and annotated it would draw itself on every scroll,
and it is texture, not a graphic. Set the copy in the open side of the frame
and keep it away from stats and charts. `assets/backgrounds/README.md` says
which side is open for each of the three.

**A composed graphic has to hold its own next to the real ones.** Measured
across the 36 illustration assets: median **16 drawn elements**, 2 filters,
1 gradient, 2 clip paths. A graphic you compose should land in that range.
Three lines and two circles is not an infographic — it is a diagram of one,
and on a page beside real Equinet artwork it reads as a placeholder.

What the real assets do that a thin composition doesn't:

- **Arrowheads on connectors.** Equinet draws them as filled paths at the end
  of the line, not with `marker-end`. A bare `<line>` between two nodes is an
  unfinished connector — this is the single most visible tell.
- **Depth.** Soft shadows via `<filter>`, subtle gradients on panels, and
  elements that overlap and layer rather than sitting in a flat row. Pull the
  `<defs>` from a real asset and reuse them.
- **Caps and joins.** Small rects where a line meets a card, rounded corners,
  dots at junctions — the details that make a flow look drawn rather than
  plotted.
- **Labels inside the artwork**, as outlined paths, positioned with the
  geometry.

**Never crop a whole asset's `viewBox` to fit a slot.** Narrowing
`0 0 1209 675` to `20 200 1180 300` cuts off whatever sits outside the band —
on 2026-10-14 that silently removed all four labels from a flow and nobody
saw it until the page was reviewed. Scale the asset, give it a different
slot, or recompose it properly. Changing the viewBox is not resizing.

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

**Unlinked content still moves — just never in answer to a pointer.** The
distinction is the whole rule:

- **Pointer-responsive motion is a promise.** A lift, a spotlight, a cursor
  change each say *act on me*. They belong only to things that do something.
- **Progress-responsive motion is a report.** It answers *where am I*,
  invites nothing, and carries no affordance.

So a card, stat panel, graphic or infographic that links nowhere gets:
entrance once on arrival (`data-reveal`), **progress emphasis as it is read**
(`data-progress` on the group, `data-step` on each part), and transitions when
its own content changes (the tab set). It never gets a hover lift, a
spotlight, a pointer-tracked anything or a cursor change.

Progress emphasis is what makes a long graphic worth scrolling — in a
five-step flow the step you have reached is the one that is lit. Reached is
permanent: scrolling back up must not unlight what a reader has passed, which
is the commonest way this effect turns nauseating. An unreached step never
drops below 0.6 opacity, because a step a reader cannot read is information
hidden behind scrolling. Under `reduce` every step sits reached at once.

**At most one card per group tracks the pointer.** `.eq-card--spotlight` (a
warm pool under the cursor) and `.eq-card--edge` (the border lighting where
the cursor is nearest) are for the card carrying the decision — the
recommended option, the live case study, the figure that matters. A row where
all four glow has emphasised nothing. Everything else keeps the plain lift,
and a card linking nowhere still responds to nothing: a tracked spotlight is
a far louder promise than a 6px rise.

Nothing may live only in a hover state. Whatever a spotlight emphasises has
to read without it.

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
