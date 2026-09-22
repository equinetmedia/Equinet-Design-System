# Equinet

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

**This is the complete palette. Nothing outside it — ever.** Where content
needs several items visually told apart — categories in an infographic, series
in a chart, states in a comparison — the distinction comes from position,
iconography, typographic weight, or a tint pairing already in the system
(navy fill against orange fill, or a pale/surface tint against a full-strength
one), never from an invented hue. A generated layout using a colour not listed
above is a defect, not a stylistic choice, however well it reads.

**Anchor colours need pinning.** A theme-level anchor rule will win on at least
one state unless the override is applied with `!important` across base, `:hover`,
`:focus-visible`, `:active` and `:visited`. Half-pinned links flicker colour
between states.

## Type

Three families, each with a fixed job. Open Sans sets headings. Source Sans 3
sets body, UI text and button labels — it stands in for Myriad Pro, which is an
Adobe face and will not render in a browser. Myriad Pro stays first in the stack
so a licensed embed added to the theme later is picked up automatically. Playfair
Display is an optional italic accent line, used to offset a heavy Open Sans
heading beneath it.

All three load from Google Fonts. There are no font files in this system.

Display headings run at `line-height: 1` with `letter-spacing: -0.05em`. The
eyebrow runs the other way, at `0.1em` to `0.2em` tracking, uppercase, with a
matching `text-indent` so the trailing letter-space does not push the label off
centre inside its pill.

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
| Textual button arrow | `translateX(8px)` in most modules; `translateX(16px)` in `sector-three-column-case-study` — **unreconciled**, pick one |
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
- **New: arrow travel distance disagrees.** `translateX(8px)` in most modules,
  `translateX(16px)` in `sector-three-column-case-study`, on the same pattern.
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
