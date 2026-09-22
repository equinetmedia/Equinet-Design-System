# Equinet

A design system for HubSpot CMS modules, rebuilt in full on 2026-09-22 from
everything gathered across the Equinet Module Development project: six
standing directive documents, `/modules/tokens.css`, the CSS of three delivered
modules (`cim-methodology`, `plain_hero_banner`, `cagr-four-column`), and the
build history of fourteen shipped modules. Every value is traced to a Figma
export, a directive, or a shipped module — nothing here is approximated.

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

Two durations are the whole system: **0.3s ease-in-out** for anything that
scales, **200ms ease** for colour, shadow and small icon shifts. Do not introduce
a third.

| Effect | Value |
| --- | --- |
| Primary button grow | `scale(1.03)`, origin centre |
| Primary button press | `scale(0.99)` |
| Button radius on hover | 7px → 8px |
| Textual button arrow | `translateX(8px)` |
| Card emphasis grow | `scale(1.04)` |

The button grow is capped at 1.03 so it cannot reflow neighbours or overflow a
grid cell. The radius grows with it — both Figma hover exports show this.

Every shipped module declares its motion unconditionally and withdraws it inside
`@media (prefers-reduced-motion: reduce)`. The reduced-motion rendering is a
complete design, not a degraded one.

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

Two hover treatments are currently shipping — a `translateY(-6px)` lift in one
module family and a border-and-shadow elevate in another. This is unresolved.
Match whichever pattern the module's own family already uses, and say which you
matched.

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

## Open decisions

- Whether the primary button's universal-inclusion rule should stay absolute
  or narrow to modules whose design includes a CTA.
- Which card hover is the system behaviour: lift or elevate.
- Whether reduced motion is gated with a `no-preference` wrapper or a `reduce`
  override. Every module does the latter; the written doctrine says the former.
- Card shadow blur: 5px or 10px.
- Whether the two primary-button shadow tokens are transposed.
- Whether Playfair Display is a system face or a per-module accent.
- Line heights below `lead`, which are currently untokenised.
- Whether `equinet-color-heading` and `equinet-color-text` should merge.
