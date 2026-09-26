# Equinet

## Rules at a glance

The binding rules, in one place. Each links to the section that explains it.
If you read nothing else here, read this. Full detail in **Instructions for
AI-generated design**.

| # | Rule |
| --- | --- |
| 1 | **Tokens only.** Every colour, size, weight, tracking, spacing, radius and shadow comes from `tokens.css`. A value not in there is a defect, not a choice. |
| 2 | **No invented hues.** The palette is complete for UI. Distinguish items by position, weight, icon or an existing tint pairing — never a new colour. Two named exceptions: the chart and diagram categories, for marketing artwork only. |
| 3 | **Three typefaces, no fourth.** Open Sans headings, Source Sans 3 body, Playfair Display as an optional accent. |
| 4 | **Section headings**: `--equinet-fontsize-section-heading` (36px), uppercase, with `--equinet-shadow-heading`. Weight follows family — 800 Open Sans, 900 body family. Not `--equinet-fontsize-h2` (48px, canonical but applied nowhere). |
| 5 | **Padding and background are the editor's.** Never hardcoded past override. Exposed in Module Style settings, injected at render. |
| 6 | **Full-bleed background image ⇒ parallax**, via `IntersectionObserver` + `requestAnimationFrame`. Never `background-attachment: fixed`. |
| 7 | **Motion needs both halves**: declared inside `prefers-reduced-motion: no-preference`, withdrawn inside `reduce`. |
| 8 | **Icons**: inline SVG only. Equinet's own are 2px stroke; a Lucide substitute declares **1px** and is marked as a placeholder. Nothing over **48px**. Never fabricate a glyph. |
| 9 | **Illustrations are reference, not sealed artwork.** Recompose freely — crop, scale, overlap, extract, rearrange. Colour, typography and iconography still follow the system. |
| 10 | **Choose illustrations on subject** via `assets/illustrations/INDEX.md`. **If nothing matches, use none.** A near-miss reads as filler. |
| 11 | **`scenes/` are opaque**; `sectors/`, `systems/`, `flows/` are transparent and need a surface; `pictonodes/` are square and never sit in a 16:9 row. |
| 12 | **WCAG 2.1 AA**, measured not estimated. One signed-off exception: the primary button's white label. |
| 13 | **Say so rather than approximate.** If a rule can't be met — no matching illustration, no icon geometry, no token for a value — state it plainly instead of filling the gap with something plausible. |

> **Do not add a `---` horizontal rule to this file.** The design-system
> format treats the first `---` as the boundary between author text and
> generated sections, and rewrites everything below it on save. A stray rule
> would mark the whole brand book as regenerable. Use a heading to separate
> sections instead.

## About this system

A design system for HubSpot CMS modules, first built on 2026-09-22 from six
standing directive documents, `/modules/tokens.css`, and the CSS of
`cim-methodology` and `plain_hero_banner` (the only two modules with real CSS
available at that point). It was extended the same day once `cagr-four-column`,
`sector-three-column-case-study`, `pencil_testimonial` and `workshop_one_column`
were read in full — see **Component inventory** for exactly which of the
fourteen shipped modules are verified against real CSS versus named from
build history only. Every value here is traced to a Figma export, a
directive, or a shipped module — nothing is approximated.

The system serves one thing: drag-and-drop modules an editor can place, restyle
and reorder without breaking the design. That constraint — and the fact that
the "user" of most of these rules is a content editor, not a developer — shapes
almost everything below.

## How it is consumed

Modules load `/modules/tokens.css` on line 1 of `module.html` and read every
value through a custom property:

```html
{{ require_css(get_asset_url('/modules/tokens.css')) }}
```

```css
background: var(--equinet-btn-fill--primary, #E06730);
```

The fallback is not decoration. If the token file is ever unreachable the module
still renders at its exact intended value.

Three rules hold this together:

- `tokens.css` owns the only `:root` block in the system. A module never
  declares one.
- Names are `--equinet-<category>-<role>`, with modifiers after a double
  hyphen — `--equinet-color-orange--dark`. Lowercase throughout.
- Semantic roles alias the palette rather than repeating a hex, so each literal
  is defined in exactly one place.

## Colour

Navy and orange carry the brand. Navy is structural — navigation buttons, card
borders, focus rings. Orange is the accent that marks anything the reader is
meant to act on: the primary button, the eyebrow, the arrow on a textual link.

The greys are near-black rather than true grey: headings at `#242630`, body at
`#3B3F51`. Surfaces are white, with `equinet-color-surface--alt` as the second
stop of a subtle module gradient.

Choose by role, never by appearance. A card background takes the surface token
even where it happens to match the page.

**This is the complete palette for UI. Nothing outside it — ever.** Where
content needs several items visually told apart — categories in a card grid,
states in a comparison, anything editors will place and restyle — the
distinction comes from position, iconography, typographic weight, or a tint
pairing already in the system (navy fill against orange fill, or a pale/surface
tint against a full-strength one), never from an invented hue. A generated
module using a UI colour not listed above is a defect, not a stylistic
choice, however well it reads.

**One narrow, named exception: data visualization.** See below. It exists
because real marketing content already used it, not because the rule above
loosened — the exception is scoped to charts specifically and does not
license a designer or an AI reaching for a new hue anywhere else.

**Anchor colours need pinning.** A theme-level anchor rule will win on at least
one state unless the override is applied with `!important` across base, `:hover`,
`:focus-visible`, `:active` and `:visited`. Half-pinned links flicker colour
between states.

## Data visualization

A separate, small palette for charts and data graphics only — never for UI,
buttons, text, or anything a content editor places in a module. Sanctioned
2026-09-23, sourced from a published marketing infographic
("Equinet-Media-ABM-underpinned-by-Loop-Marketing-in-HubSpot"), not from a
shipped module — the first token category in this system to come from
marketing collateral rather than product code.

| Token | Value | Role |
| --- | --- | --- |
| `equinet-color-chart-blue-light` | `#81ACD7` | Gradient, lightest stop |
| `equinet-color-chart-blue-mid` | `#5688BA` | Gradient, middle stop |
| `equinet-color-chart-blue-dark` | `#3D71A5` | Gradient, darkest stop |

This is a genuinely different blue family from `equinet-color-navy` — lighter,
more muted, not a tint or shade of it. Deliberately so: navy is a UI colour
with jobs (navigation, borders, focus rings), and mixing the two families in
the same element would blur what's chart versus what's interface.

**Unresolved discrepancy, logged not fixed:** the same infographic uses
`#ECEAEA` for a panel background — close to but not identical to
`equinet-color-surface--alt` (`#F6F5F5`). Not promoted as its own token.
Could be a deliberate second, more muted grey for data-viz contexts
specifically, or could just be drift that should use the existing surface
token instead. Needs a decision, not an assumption either way.

**Source: `assets/marketing/`.** Reference material — infographics and
marketing graphics, not reusable module assets — kept for exactly this kind
of audit trail. Every file in it is checked for real colour/font values
against this file before anything from it is trusted; see that folder's own
`README.md` for the process and its index of what's contributed what.

## Diagram illustration

A second, small marketing-only palette — illustration line colours and
background tints used across diagram-style infographics. Sanctioned
2026-09-23 from an initial batch of seven marketing graphics, then extended
the same day once a second batch of nine brought the total to seventeen
files audited.

| Token | Value | Role | Evidence |
| --- | --- | --- | --- |
| `equinet-color-diagram-line` | `#68728F` | Illustration line and icon colour, blue-tinted — used as both `fill` and `stroke` | 7 of 7 files (first batch) |
| `equinet-color-diagram-line--neutral` | `#6C7074` | Same role, neutral-grey variant with no blue cast | 5 of 17 files, fill and stroke both |
| `equinet-color-diagram-tint` | `#D6D8E1` | Light panel/shape tint | 3 of 7 files |
| `equinet-color-diagram-tint--pale` | `#ECEDF2` | Palest background tint | 7 of 7 files |

Same boundary as data-viz: marketing illustration only, never UI, never a
module. Neither `diagram-line` variant is a tint of `equinet-color-body` or
`equinet-color-border` — they're distinct mid-tones that exist to be a
diagram's default ink colour, one with a blue cast and one without.

**Resolved 2026-09-23: `#FFE6DB` is `equinet-color-orange--pale`, not a
separate colour.** It showed up in 3 files (7 occurrences total — matching
`orange--pale`'s own usage count exactly), which moved it from "near-miss
worth logging" to "used as deliberately as an actual token." Folded in
rather than kept as a parallel value; any future sighting of `#FFE6DB` should
be treated as this token.

**Still unresolved — a cluster, not a one-off:** `#ECEAEA` and `#F3F2F2`
(both in the ABM infographic — the latter missed in that file's first audit
pass) and `#F3F3F4` (`The-Brand-Ops-Agent.svg`) are three near-identical,
very pale, cool-toned near-whites. None matches `equinet-color-surface--alt`
or `equinet-color-diagram-tint--pale` exactly, and none matches each other
exactly either. Reads less like three isolated choices and more like nobody
has one settled near-white to reach for. Not promoted; needs a decision
rather than a guess at which (if any) should become the real value.

**Still logged, not promoted — too weak a signal so far:** `#444A60`,
`#E3EFFC`, `#CFE0F4` (single file each, first batch); `#FF4800`, `#FBDDD2`,
`#A4A4A4`, `#343330`, `#F6F7F9`, `#8790A9` (single file each, second batch);
`#F49E78` (now 2 of 17 files — climbing, still not strong enough to sanction
on its own).

## Type

Three families, each with a fixed job. Open Sans sets headings. Source Sans 3
sets body, UI text and button labels. Playfair Display is an optional italic
accent line, used to offset a heavy Open Sans heading beneath it.

**Myriad Pro is gone from the stack as of 2026-09-23**, not just deprioritized.
It was originally kept first as a placeholder for a licensed embed that never
arrived — Myriad Pro is an Adobe face and never rendered in a browser. Claude
Design hit this same wall independently while building from this system,
asked for a font file, got none, and fell back to Source Sans 3 permanently.
`tokens.css` now matches that: `'Source Sans 3', sans-serif`, no Myriad Pro
reference at all. If a licensed embed ever does arrive, it goes back in as a
deliberate re-addition, not a silent restoration of dead weight.

This is a web-rendering fact, not a claim about brand intent — the second
marketing batch (nine files, same day) has real `<text>` elements explicitly
declaring `font-family="Myriad Pro"`, unlike every other marketing SVG
audited, where text is outlined to paths with nothing recoverable. Myriad Pro
is genuinely the brand's intended typeface at the design level; it just can't
ship in a browser without a licence the system doesn't have.

All three load from Google Fonts. There are no font files in this system.

Display headings run at `line-height: 1` with negative tracking —
`-0.05em` at 56px, `-0.07em` at 60px, both now tokens. The eyebrow runs the
other way: `0.2em` at 12px, `0.1em` at 16px, uppercase, with a matching
`text-indent` so the trailing letter-space does not push the label off centre
inside its pill. All four values were read from live-text comps on
2026-09-24; before that the category had no tokens at all and every module
hardcoded its own.

**h2 is a firm requirement, confirmed 2026-09-23: uppercase, with the heading
drop shadow.** `text-transform: uppercase` (`--equinet-text-transform-h2`)
and `text-shadow: -2px 2px 4px rgba(0, 0, 0, 0.15)` (`--equinet-shadow-heading`
— the same token display headings already use) apply to every h2, no
exceptions. Both tokens existed already from the Figma import; this makes
them mandatory rather than descriptive metadata sitting unused. Note the
separate, still-open discrepancy: canonical Figma specifies h2 at 48px, but
`cagr-four-column` ships it at 36px — the uppercase/shadow requirement holds
regardless of which size wins that argument.

**Size resolved 2026-09-24: use `--equinet-fontsize-section-heading` (36px),
not `--equinet-fontsize-h2` (48px).** The live-text comps settled it — both
comps carrying a section heading set 36px at weight 900, matching what
`cagr-four-column` ships. The 48px Figma variable is kept as the canonical
definition but is applied nowhere, so it's the exception, not the default.

**Weight is family-dependent, and always was.** Open Sans headings take 800
(`--equinet-fontweight-display`), Myriad Pro / Source Sans 3 headings take 900
(`--equinet-fontweight-black`). The long-standing "cagr uses 800 but sector
hardcodes 900" open item was comparing two different families, not catching
drift.

**This requirement can't be fully expressed in `tokens.json`.** Claude
Design's actual token schema has no `textTransform` or `textShadow` field on
a type style — checked directly against its documented grammar, 2026-09-23.
An earlier attempt to add both to the h2 entry was silently ignored; removed,
and the h2 sample text is now written in caps as the closest structural hint
the schema allows. The requirement itself still lives here and in
`tokens.css` (`--equinet-text-transform-h2`, applied directly in module CSS);
anything reading only `tokens.json` for type styles won't see it.

**Lead text has a real gap, found 2026-09-23: no colour token at all.**
The shipped module (`plain_hero_banner`) sets colour via an editor-controlled
inline field with no CSS fallback whatsoever — unlike padding, which always
carries a `var(--token, fallback)` even while being editor-controllable. If
that field is ever unset, lead text renders with no colour applied, which on
a navy background is functionally invisible. `equinet-color-lead` (aliasing
`equinet-color-body`) now exists as that missing fallback. Also caught in the
same pass: `font-style: italic` was hardcoded in the module but absent from
`tokens.json` entirely — `equinet-fontstyle-lead` now covers it — and the
`equinet-fontsize-lead` token (20px) doesn't match what `plain_hero_banner`
actually ships (22px desktop) — sourced from a different module, not
reconciled.

`text-wrap` is split by role: `pretty` on body copy and card descriptions to pull
down single-word orphans, `balance` on display headings and short accent lines
where an even two-line wrap matters more than the exact break.

Sizes and line heights are computed, never eyeballed — sizes from SVG coordinate
arithmetic, vertical metrics from the TTF binary.

## Spacing

Two kinds of value, and only one of them is a token.

**Rhythm** repeats across modules and sits on a 4px grid: `equinet-space-md`
(24px) is the workhorse — gutter, grid gap, card interior, modal padding.
`equinet-space-4xl` (96px) is the section rhythm top and bottom, clamped to
`equinet-space-3xl` (56px) on mobile.

**Measured** values are component internals derived from SVG coordinates and
deliberately off-grid: 9, 15, 22, 26, 27, 30, 44, 68, 94. They stay literal, each
annotated with the arithmetic that produced it. Rounding them onto the grid would
falsify the comp.

Container widths are per-module, set by the comp — 1716px for a five-card row,
1120px for a hero. They are not a shared scale.

**Padding belongs to the editor.** No module hardcodes it. It is exposed in the
Module Style settings and injected through a module-scoped custom property, so a
mobile clamp can still apply over the editor's value:

```css
padding-top: min(var(--cim-pad-top, 96px), 56px);
```

Background colour and background gradient are editor-controlled on the same
principle.

## Breakpoints

| Band | Query |
| --- | --- |
| Mobile | `max-width: 767px` |
| Tablet | `min-width: 768px` and `max-width: 1023px` |
| Laptop | `min-width: 1024px` and `max-width: 1439px` |
| Desktop | `min-width: 1440px` |

Mobile and tablet appear in every module. Laptop and desktop only where a
multi-column grid needs an intermediate step.

Mobile overrides are resolved by matching selector weight, not `!important`.
Media queries add no specificity, so a mobile rule at `(0,1,0)` loses to a
desktop rule at `(0,2,0)` regardless of source order.

## Motion

Two durations anchor the system: **0.3s ease-in-out** for anything that
scales or moves, **200ms ease** for colour, shadow and small icon shifts.
Two more exist for specific effects: **0.6s** for a card or image settling
back after a hover ends, and **0.45s** for the one reveal-wipe transition in
`sector-three-column-case-study`. Don't introduce a fifth without promoting
it to a token.

| Effect | Value |
| --- | --- |
| Primary button grow | `scale(1.03)`, origin centre |
| Primary button press | `scale(0.99)` |
| Button radius on hover | 7px → 8px |
| Card hover lift | `translateY(-6px)` — **canonical**, per `cagr-four-column`'s own code comment, attributed to `growth_cards` |
| Card image zoom + desaturate | `scale(1.06)`, `grayscale(0%)` |
| Textual button arrow | `translateX(16px)` — **resolved 2026-09-23** from the Figma exports |
| Card emphasis grow | `scale(1.04)` — `cim-methodology` only, a pinned "elevated" state, not a hover default |

The button grow is capped at 1.03 so it cannot reflow neighbours or overflow a
grid cell. The radius grows with it — both Figma hover exports show this.

**Reduced motion: do both halves.** The correct pattern, confirmed by the two
most disciplined modules read so far (`cagr-four-column`,
`sector-three-column-case-study`), is to declare entrance motion inside
`@media (prefers-reduced-motion: no-preference)` *and* back it with an
unconditional `@media (prefers-reduced-motion: reduce)` block that force-kills
any transition or transform left running. `cim-methodology` and
`plain_hero_banner` only carry the second half — that's a gap in those two
modules, not a second valid pattern to choose between.

```css
@media (prefers-reduced-motion: no-preference) {
  .eq-card:hover { transform: translateY(-6px); transition: transform 0.3s ease-in-out; }
}
@media (prefers-reduced-motion: reduce) {
  .eq-card { transition: none !important; }
  .eq-card:hover { transform: none; }
}
```

Motion values are not tokenised. The durations and the button scale are; the
arrow travel, press and card grow are not yet.

## Buttons

Three variants of one component, separated only by tokens. The primary variant
is governed by three standing directives, folded in here in full because they
constrain every future button build, not just the ones already shipped.

**Figma mapping.** A layer whose `id` is formatted `primary_button_(name)` maps
to the `.btn-primary` class or component. The `(name)` segment identifies the
instance — a second checkout button, a hero CTA — and does not earn its own
styling; it is still `.btn-primary`.

**Universal inclusion.** The primary button ships in every module without
exception, even where the current design does not place one. This is an
absolute rule as written, though it is also an open question in this system —
see **Open decisions** — because it means a purely informational module still
carries a button nobody asked for.

**State styling and fallback.** All four states — `.btn-primary`,
`.btn-primary:hover`, `.btn-primary:active`, `.btn-primary:focus-visible` — are
coded exactly as `tokens.css` defines them. If `tokens.css` is not reachable in
the target environment, the exact standard token values are hardcoded directly
into the module rather than improvised. 56px tall as `min-height`, not `height`,
so an editor-entered label can wrap without clipping.

**Interactive animation.** Hover applies a subtle grow via `transform: scale()`
— capped at 1.03 so it cannot reflow neighbours or overflow a grid cell — eased
with `transition: transform 0.3s ease-in-out`. This is the only animation the
directive specifies for the button; the radius growing alongside it (7px → 8px)
and the 0.99 press scale are both observed in shipped modules but are not yet
promoted to a written rule.

**SVG hover theming.** Where a module's Figma export supplies both a light and
a dark SVG for the hover state, `fields.json` gains a *Toggle Dark or Light*
field, and the template selects the asset from it — light SVG on dark
backgrounds, dark SVG on light backgrounds — so contrast holds after an editor
changes the module background. Where only one SVG state exists, the toggle is
omitted rather than offering a choice with no second asset behind it. Two hover
*fills* exist for the same reason: `--hover-light` on dark module backgrounds,
`--hover-dark` on light ones, each with its own shadow token tinted to its fill.
The toggle must be set whenever the background changes.

**Navigation** swaps to the navy fill and switches its label to
`equinet-btn-label--navigation--hover` on hover.

**Textual** drops the fill entirely, takes the text-colour label, and slides its
arrow 8px on hover.

The focus ring is never removed. `:focus-visible` is styled separately from
`:hover` so keyboard users get an indicator pointer users do not see, and it is
drawn in navy — an orange ring on an orange fill is invisible.

**The "transposed shadow tokens" question is resolved, and it wasn't a token
problem.** `cagr-four-column` correctly references
`var(--equinet-shadow-btn--primary, …)`. `cim-methodology` and
`plain_hero_banner` hardcode a literal `box-shadow` value instead of using the
variable at all, and that literal doesn't match what's in `tokens.css`. Fix
those two modules to reference the token; the token itself is correct as
written.

## Cards

Cards clip with `overflow: clip`, never `overflow: hidden`: `clip` does not
create a scroll container, so it will not swallow a focus ring or trap a sticky
child.

A clickable card is a link or a button in the markup, not a `div` with a handler.
The reference approach is a stretched overlay anchor at `inset: 0` with
`border-radius: inherit`, so the whole card is the target and the focus ring
follows the card's corners.

Where cards sit in a row and must share baselines, the gap is held by a
`min-height` zone on the element above, not by a margin — each zone sized to
absorb one wrapped line. At mobile the zones collapse to `0` and an explicit
margin takes over; a fixed zone in a single-column stack just leaves a hole.

**Hover is a lift.** `translateY(-6px)` is canonical — `cagr-four-column`
names it as such in its own code comment, tracing it back to `growth_cards`.
`cim-methodology`'s border-and-shadow "elevate," with no movement, is the
outlier: it's how one module happens to work, not an equally valid second
pattern to choose between.

**Card shadow blur is 5px, not 10px.** `tokens.css` and `cagr-four-column`
both use `1px 1px 5px 0px rgba(0,0,0,.13)`, correctly bound through
`var(--equinet-shadow-card, …)`. `cim-methodology`'s `10px` blur is a
hardcoded literal, not a token reference — it drifted, rather than
representing a second correct value. Fix it to reference the token.

**Where a card carries a photo, the image does the moving, not always the
card.** `cagr-four-column`: the image zooms and desaturates-to-colour on
hover, layered on top of the card's own lift. `sector-three-column-case-study`
takes this further: two accent-bar pseudo-elements cross-fade colour (navy at
rest, orange on hover) with **no transform at all** — deliberately, per its
own comment, because lateral movement over a photo pulls the eye away from
the content, and three of these firing in a grid reads as restless. Whether
this card's root also lifts alongside the crossfade is still open — worth
checking against the module directly rather than assuming either way.

**Zero-specificity reset, declared first.** Both of the properly-tokenized
modules read so far open with a `:where()` block resetting margins, list
styles and media sizing at zero specificity, before anything else:

```css
:where(.your-module) :where(p, h1, h2, h3, h4, h5, h6, ul, ol, dl, dt, dd, figure, blockquote) { margin: 0; }
:where(.your-module) :where(ul, ol) { padding: 0; list-style: none; }
:where(.your-module) :where(img, picture, svg) { max-width: 100%; }
```

This lets every subsequent measured value win outright, with no specificity
arithmetic against a theme's element rules. `cim-methodology` and
`plain_hero_banner` predate this pattern and don't have it — worth retrofitting
rather than treating as optional going forward.

## Backgrounds and parallax

Any module whose background image is configured to cover the entire module or
container gets a dynamic parallax effect — this is a standing requirement, not
a per-design decision. The background image moves at a distinct, offset speed
relative to the page scroll and the foreground content.

`background-attachment: fixed` is not used to achieve this: it does not
function on iOS Safari. The implementation is an `IntersectionObserver` that
starts and stops the effect as the module enters and leaves the viewport,
driving a `requestAnimationFrame` loop, the whole thing gated behind
`prefers-reduced-motion`. No scroll listener runs while the module is
off-screen, and none attaches at all when reduced motion is requested.

## Editor-controlled styling

Two properties are never hardcoded in a way that overrides the person placing
the module, on the same principle in both cases: the value is exposed in the
Module Style settings, and the module's code reads it dynamically at render so
an editor's change is reflected immediately.

**Padding.** No module fixes top, right, bottom or left padding in its core CSS
or inline styles in a way that overrides editor preference. It is exposed and
fully editable in the Style settings, and injected at render — see **Spacing**
for the mobile-clamp pattern this implies.

**Background.** Background colour and background gradient are both directly
linked and fully editable in the Style settings or configuration file, on the
same terms. A module that also offers a background image still offers the
colour and gradient fields, because the image may be removed.

## Icons

Inline SVG only. No icon fonts, no `{% icon %}` tags, no `{% cta %}` tags.

An SVG lifted from a Figma export is re-based to a local `viewBox` before
embedding so it scales from its own coordinate space. Decorative icons take
`aria-hidden="true"` and `focusable="false"`; an icon carrying meaning alone gets
an accessible name. Icons inherit colour through `currentColor` wherever the
design allows, so one state change recolours text and icon together.

Nothing is invented. If an element is not in the source comp, it does not appear
in the build.

**Shared assets: `assets/icons/`.** Every module currently carries its own
copy of the icons it uses — the arrow, the checkmark, the close glyph — inline
in its own `module.html`. That folder is the intended shared home for them
instead, so a module references one canonical file rather than repeating
markup. It's empty of real SVGs as of 2026-09-22: see its own `README.md` for
the inventory of what's known and why the arrow specifically needs a decision
before it can be centralized — it isn't one shape today.

## Component CSS

`components/bundle.css` is the pure-CSS component layer — no build step, no
preprocessor, no JavaScript. It loads after `tokens.css`, and every value
resolves to a token with its SVG-measured literal as the fallback, so a module
renders correctly even if the token file is unreachable.

It covers all three button variants in every state, measured from the Figma
exports on 2026-09-23:

| Variant | Geometry | Radius on hover | Icon |
| --- | --- | --- | --- |
| `.btn-primary` | 232 × 56, `rx 7` | 7 → 8 | `arrow-solid` (15.63 × 13.13) |
| `.btn-primary--video` | 235 × 56, `rx 7` | 7 → 8 | `play-circle` (26 × 26) |
| `.btn-navigation` | 243 × **54**, `rx 7` | **stays 7** | `arrow-chevron` (24 × 24) |
| `.btn-textual` | 24 tall, no fill | — | `arrow-chevron` (24 × 24) |

Two things the exports corrected. The navigation button is **54px tall, not
56** — it does not share `--equinet-btn-height` — and its radius does **not**
grow on hover, unlike the primary's 7 → 8. Both were assumed uniform before
the real exports existed.

The classes there are unscoped, for Claude Design previews and reference.
Inside a HubSpot module every selector is namespaced under that module's root
class — see **Module anatomy**.

## Illustrations

`assets/illustrations/` holds 32 standalone graphics in five subgroups:
`pictonodes/` (8, square 118 × 118), `scenes/` (12, 16:9 service and process
illustrations), `sectors/` (4, 16:9 vertical pictographs), `systems/`
(5, 16:9 commercial-systems process diagrams) and `flows/` (3, 16:9
horizontal four-step sequences). All are
multi-colour and stand alone, distinct from the single-ink glyphs in
`assets/icons/`. Every colour across all 24 resolves to an existing token —
but to the marketing and chart palettes, not the UI one, which is itself the
clue that they're collateral rather than interface. Full per-group breakdown,
palette mapping and usage rules in that folder's own `README.md`.

**One file there has an accessibility defect:**
`sectors/equinet-sector-build-environment-pictograph-1.svg` carries an
embedded `2s linear infinite` CSS animation with no `prefers-reduced-motion`
guard — the one thing the motion rule above exists to prevent. Use its static
twin until that's fixed.

The dividing line, since it will come up again: if flattening a graphic to one
ink would ruin it, it's an illustration, not an icon. Icons inherit
`currentColor` from the control around them; illustrations can't.

## Staggered content blocks

`components/bundle.css` carries `.eq-stagger`, an alternating media/text row
pattern built to the real illustration ratios. Media leads on odd rows, text
on even ones, driven by `:nth-child` rather than a modifier class — an editor
adding a row can't break the rhythm, and the DOM order stays the reading order
for screen readers and keyboard focus.

```html
<div class="eq-stagger">
  <div class="eq-stagger__row">
    <div class="eq-stagger__media eq-stagger__media--scene">
      <img src="assets/illustrations/scenes/…-wireframing-v1.svg" alt="">
    </div>
    <div class="eq-stagger__body">
      <p class="eq-stagger__eyebrow">Website design</p>
      <h2 class="eq-stagger__heading">Wireframing</h2>
      <p class="eq-stagger__text">…</p>
    </div>
  </div>
</div>
```

**Pick the media modifier by folder — this is the part that goes wrong
silently:**

| Folder | Modifier | Why |
| --- | --- | --- |
| `scenes/` | `--scene` | Opaque navy gradient, full artboard. Fills the frame edge to edge; adding padding would expose page colour around a hard dark rectangle |
| `sectors/`, `systems/` | `--transparent` | Line work with no background — needs a surface behind it or it floats on the page |
| `pictonodes/` | use `__row--compact` | 118 × 118 is too small to hold half a row; it sits inline beside the text at native size |

The three 16:9 groups are interchangeable in one row (1.776–1.781, the same
ratio within rounding). `pictonodes/` are square and are not — don't mix them.

Below 768px every row stacks media-first, including the even ones: alternation
in a single column reads as a mistake rather than rhythm.

Choosing *which* illustration is a separate question — see
`assets/illustrations/INDEX.md`, and its rule that if nothing matches the
subject, the right output is a layout with no illustration.

## Module comps

`assets/comps/` holds three Figma exports of complete modules —
`2-column-hero-banner`, `5_column_block_methodology` and
`sector-three-column-case-study`, all 1920px wide. They are the design source
of record those modules were built from.

**Never place one in a layout.** Each is a picture of a whole rendered module,
its own headings and buttons included; using one as page artwork would embed a
fake module as a flat image. They exist to be compared against — parity QA,
token provenance, and settling disputes between a shipped module and a token,
the way the button exports settled the arrow-travel distance.

Re-exported 2026-09-24 with live `<text>` elements rather than outlined paths,
and a fourth comp added. Between them they declare 60 text runs with real
family, size, weight and tracking — which settled the h2 size, the heading
weight question, and the whole letter-spacing token category that had been
flagged missing since the first reconciliation.

## Layout skill — `skills/equinet-layout/`

A skill that turns content into an Equinet page in two phases: a
section-by-section **layout brief** (which format each piece of content
becomes, which asset, which HubSpot element carries the reader's next step),
then — only after approval — the **build** against this design system.

Its core rule: the shape of the content decides the format. A number becomes
a stat block because it's a number; content with no numbers gets no stat
block. It never invents data to fill a format, and it flags any component it
has to build new — charts, stat rows, tables, flowcharts and FAQs have no
component here yet.

It lives in this repo so Claude Design reads it with the rest of the system.
For Claude chat, the same folder is packaged as `equinet-layout.skill` and
installed from the file card. **This repo copy is canonical:** after editing
the folder, re-package and reinstall, or the chat copy drifts behind.

## Brand mark

`assets/brand/` holds the Equinet Media wordmark, two ready-made variants —
`wordmark-light.svg` (white fill, for navy or dark grounds) and
`wordmark-dark.svg` (`equinet-color-text` fill, for light grounds). Same
artwork, same light/dark toggle logic already used for button hover states,
picked by background contrast rather than habit. Full usage rules in that
folder's own `README.md`.

## Instructions for AI-generated design

For Claude Design, or any other tool generating a mockup, page, or component
from this system. Every rule below is a requirement, not a preference — the
same standard the colour rule already holds generated output to. Each links
back to the section that defines the actual values, so this isn't a restatement
of them, just the mandate to use them.

**Assets — use what's real, never invent what isn't, and leave it out if
nothing fits.**
- Illustrations: read `assets/illustrations/INDEX.md` before choosing one. It
  lists every file's subject and topics, and says which are opaque. Match on
  subject, not on how a filename sounds. **If no illustration matches the
  page's subject, use none** — the set covers Equinet's own service lines and
  sectors, so a page about anything outside that has no fit here, and the
  nearest-looking file is still the wrong file. A mismatched graphic reads as
  filler.
- The 12 files in `scenes/` have an opaque navy gradient baked into the full
  artboard. They are media panels and card headers, not transparent spot art;
  dropping one on a white surface leaves a hard dark rectangle.
- **Illustrations are artistic and styling reference, not sealed artwork.**
  Place a file whole, crop into a detail, scale it, overlap it, or pull
  elements out and recombine them into a new composition — arrangement and
  formation are free. Three things are not, and must survive any
  recomposition: **colour** (token values only, and the illustration-side
  categories at that), **typography** (the `tokens.css` scale and families),
  and **iconography** (`assets/icons/`, with `ICON-REFERENCE.md` for a
  substitute). Rearranging is licence to compose, never licence to invent a
  hue, a typeface or a glyph. Two traps when extracting: an element loses the
  ground it was drawn against, so re-check contrast; and several colours in
  these files are logged-but-unsanctioned, so sample from `tokens.css` rather
  than from the artwork. Full rules in `assets/illustrations/INDEX.md`.
- Wordmark: `assets/brand/wordmark-light.svg` or `wordmark-dark.svg`, picked
  by background contrast (see **Brand mark**). Never render the name as
  styled text standing in for the logo.
- Icons: `assets/icons/` holds 16 files in three groups — three control icons
  that take `currentColor`, five 43 × 43 concept marks (`nodes/`) and eight
  65 × 65 service tiles (`service-tiles/`). Read that folder's `README.md`
  first: only the three root icons recolour with their control; the nodes
  hardcode their ink; and the tiles are white-on-navy artwork that must not be
  recoloured — though the **glyph inside a tile is substitutable**, and may be
  swapped for a context-appropriate Lucide icon keeping the rect, gradient and
  radius untouched (rule set 2026-09-24; `ICON-REFERENCE.md` has the contract
  and a per-service mapping). Three icons are still missing
  geometry (`close`, `checkmark`, `external-link`); for those, **a neutral
  icon set (Lucide or similar) is an acceptable placeholder** — decided
  2026-09-23 — but it must read as a placeholder, not be presented as a real
  Equinet icon — and match it to the house style using
  `assets/icons/ICON-REFERENCE.md`. Note the substitution rule set
  2026-09-24: a Lucide icon declares `stroke-width="1"`, not Lucide's native
  2, and no icon — substituted or Equinet's own — exceeds 48px. Substitutes
  are deliberately finer than real Equinet artwork, which makes a placeholder
  visible on sight; don't scale the stroke up to match. Don't fabricate a plausible-looking custom shape; that's
  exactly the kind of invented geometry the no-hallucination principle exists
  to prevent.

**Spacing and frame — token values only, nothing arbitrary.**
- Padding and gaps: the `equinet-space-*` scale (see **Spacing**). A raw
  pixel value not on that scale is a promotion candidate, not a free choice.
- Corners: `equinet-radius-card` or `equinet-btn-radius` (see **Surface**).
- Elevation: `equinet-shadow-*`, matched to the resolved card-lift pattern
  (see **Cards**) — not a new shadow invented to taste.
- Borders and dividers: `equinet-color-border` for UI; the `diagram-line`
  tokens only for marketing/illustration content, never for UI (see
  **Diagram illustration**).

**Typography — the two families, the real scale, nothing else.**
Open Sans for headings, Source Sans 3 for body, Playfair Display only as the
already-established optional accent (see **Type**). No third typeface. No
size outside `equinet-fontsize-*`. Section headings are
`--equinet-fontsize-section-heading` (36px), not `--equinet-fontsize-h2`
(48px, the canonical Figma variable, applied in no comp). Weight follows the
family: 800 for Open Sans, 900 for the body family. Every h2 is uppercase with
the heading drop shadow, no exceptions — see **Type** for the exact values.

**Where tokens don't dictate an answer, general UI practice fills the gap —
it doesn't license invention:**
- Contrast: WCAG 2.1 AA, measured rather than eyeballed (see
  **Accessibility**) — except the one signed-off exception already on
  record for the primary button.
- Alignment: repeated elements — cards in a row, icons in a list — share a
  baseline or edge, not independently placed.
- Hierarchy: one clear focal point per section; heading level follows
  document order, never chosen for its visual size (see **Type**).
- Density: the button's 56px height and the spacing scale's rhythm exist so
  interactive targets and gaps don't need re-deriving per design — use them
  rather than judging by eye whether something looks crowded.

**Layout — start from the pattern, then vary it.**
`.eq-stagger` in `components/bundle.css` handles alternating media/text rows,
sized to the real illustration ratios and already carrying the right media
modifier per folder. Vary the rhythm where the content earns it — regroup,
break the alternation for a full-width moment — but keep spacing on the
`--equinet-space-*` scale, and don't put square `pictonodes/` in a 16:9 row.

**Say so rather than approximate.**
If something here can't be satisfied — no illustration matches the subject, a
needed icon has no geometry, a token doesn't exist for a value the design
wants — state that plainly in the output instead of filling the gap with
something plausible. A near-miss illustration, an invented hue or a fabricated
glyph is worse than an honest omission, because it looks finished and hides
the problem. This applies to every rule above.

## Accessibility

WCAG 2.1 AA is the floor, and conformance is measured rather than assumed.
Contrast is calculated from the token values or sampled from rendered pixels —
gradients and text over images at their worst point, not their average.

Native elements first: `<button>` for actions, `<a>` for navigation, real heading
levels in document order. ARIA only where no native element carries the
semantics.

**One accepted exception.** The white primary-button label measures 3.4:1 at
rest, 2.5:1 on the light hover and 4.4:1 on the dark hover — below the 4.5:1
minimum for 16px text. The client accepted this on 2026-09-21. It is not to be
compensated for with a text shadow or stroke, and it does not extend to any other
component. Raising the label to 18.66px at weight 700 would bring the default and
dark-hover fills into the large-text threshold; the light hover would still fail.

**One unresolved.** Orange eyebrow text on the pale orange pill measures 2.9:1.
This has not been raised with the client.

## Engineering contract

This system is consumed as HubSpot CMS modules, not as a component bundle, so
the constraints that keep an implementation on-system live here as prose
rather than as code. A build is not finished until it passes:

- **Fields.json.** Padding, background colour and background gradient are
  style-group fields with `module.styles.*` accessors — a bare `module.*`
  path silently resolves to empty. `controlling_field_path`, not
  `controlling_field`, drives visibility. Repeaters set
  `occurrence.sorting_label_field: null`. Field names are unique across the
  whole file, including inside groups and repeaters.
- **HubL.** Link fields are read as `field.url.href`, guarded before
  `escape_url` is applied to avoid breaking the anchor on an empty value. Only
  `\"` and `\\` are valid escapes in a HubL string — `\s` fails the upload
  lexer where `\\s` succeeds.
- **Forbidden strings.** No FontAwesome, `{% icon %}` or `{% cta %}` — icons
  are inline SVG, links are native anchors and buttons.
- **CSS scoping.** No `:root` block outside `tokens.css`. `overflow: clip`,
  not `overflow: hidden`, so a clipped container cannot swallow a focus ring.
  A `transition` list lives on the component that animates, never in a shared
  hover block a later rule can silently override.
- **Measurement, not estimation.** Font metrics come from the TTF binary
  (`sTypoAscender`, `sTypoDescender`, `USE_TYPO_METRICS`), not an approximation.
  Contrast is computed from sampled pixels (sRGB-linearised, Pillow), not
  judged by eye.
- **Debugging order.** A hover effect that does not fire is, more often than
  not, a missing or misnamed class in the rendered DOM — checked before the
  CSS rule is suspected.

## Component inventory

Fourteen modules have shipped on this system. New work is checked against this
list before a new pattern is proposed, so the system does not accumulate two
components that do the same job:

`sector-three-column-case-study` · `cagr-four-column` · `pencil_testimonial` ·
`EQNewsletterSubscription` · `2-column-comparison` · `plain_hero_banner` ·
`workshop_one_column` · `2_column_intelligence_engine_steps` ·
`2_column_commercial_diagnostics` · `tabbed_navigation` / `tabbed_navigation_v2`
· `5_column_block_process` · `growth_cards` · `EQ Workshop Hero Banner` ·
`cim-methodology` (Commercial Intelligence Methodology)

**Verified against actual CSS, as of 2026-09-22:** `cim-methodology`,
`plain_hero_banner`, `sector-three-column-case-study`, `cagr-four-column`,
`pencil_testimonial`, `workshop_one_column`, `2_column_intelligence_engine_steps`
(confirmed intentionally empty). The remaining seven are named from build
history only — nobody has read their CSS. `growth_cards` in particular is
cited by name as the origin of the card-lift pattern without its file ever
having been seen directly.

**Two integrity problems, not new modules:**
- A file uploaded as `5-column-block-process.css` is a byte-for-byte
  duplicate of `cim-methodology`'s CSS. The actual five-column module's
  styling has never been provided under any filename.
- `new_header_module_2026_v3.css` doesn't conform to this system at all — an
  off-brand green palette, its own `:root` block, FontAwesome glyphs, no
  `--equinet-*` token usage anywhere. Excluded from this compilation rather
  than treated as a fifteenth module; worth confirming whether it's meant to
  be on-brand before it ships.

**Also surfaced, out of scope for this system:** `single_narrow_text_column`
is an ESCATEC module (`--escatec-*` prefix), structurally near-identical to
`plain_hero_banner`'s button pattern with the client swapped. Good sign the
patterns generalize past Equinet; its tokens don't belong in this file.

## Open decisions

- Whether the primary button's universal-inclusion rule should stay absolute
  or narrow to modules whose design includes a CTA. `cagr-four-column` ships
  `.btn-primary` styling with **no button layer anywhere in its Figma comp**,
  specifically so a future rich-text-inserted button inherits the component —
  a deliberate case for keeping the rule absolute, not just an oversight.
- **Resolved 2026-09-23: arrow travel is 16px.** The Figma exports settle it —
  `button_textual_default.svg` places the chevron at x190,
  `button_textual-Hover.svg` at x206, and the artboard widens by exactly 16.
  `sector-three-column-case-study` was right; `plain_hero_banner` and
  `cim-methodology` ship 8px and have drifted. Token:
  `--equinet-motion-travel--arrow`.
- **New: two button class families coexist.** `.btn-primary` throughout, but
  `sector-three-column-case-study` also carries `.button_primary_large` and
  `.button_textual` as parallel selectors on the same rules. Worth deciding
  whether these are sanctioned aliases or naming drift to retire.
- **New: heading weight and family are inconsistent.** `cagr-four-column` uses
  `--equinet-fontweight-display` (800) via `--equinet-font-heading`.
  `sector-three-column-case-study` hardcodes `font-weight: 900 !important`
  and `font-family: "Open Sans" !important` directly, bypassing both tokens.
- Whether Playfair Display is a system face or a per-module accent.
- Line heights below `lead`, which are currently untokenised.
- Whether `equinet-color-heading` and `equinet-color-text` should merge.
