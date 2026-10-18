---
id: component-sources
status: current
read_when: >-
  Building or checking the eyebrow or the stacked card. Holds the Figma
  exports these components were measured from, the measurements, when the
  solid eyebrow is allowed, and the contrast limits on both.
depends_on: components/bundle.css
verified: 2026-10-16
---

# `components/` — Figma exports of components, not artwork

These are the design source of record for a component, the same role
`assets/buttons/` plays for the buttons. **Never place one on a page.** They
carry live `<text>`, so the type renders from whatever font the viewer has;
the component is built in CSS and the export is what you measure against.

Added 2026-10-16.

## `eyebrow-plain` / `eyebrow-solid` — 115 × 32

The small uppercase label above a heading. Built as `.eq-eyebrow` and
`.eq-eyebrow--solid` in `components/bundle.css`.

| Measured | Value | Token |
| --- | --- | --- |
| Size | 12px | `--equinet-fontsize-kicker` |
| Weight | bold / 700 | `--equinet-fontweight-kicker` |
| Tracking | 0.2em | `--equinet-letterspacing-kicker` |
| Label | `#E06730` | `--equinet-color-orange` |
| Pill fill | `#FCE9E0` | `--equinet-color-orange--pale` |
| Pill radius | `rx="8"` | `--equinet-radius-pill` |
| Side inset | text at `x="24"` | `--equinet-space-md` |
| Frame | 115 × 32 | 10px + 12px line + 10px |

Everything resolves to an existing token. Nothing new was needed.

One thing not to copy from the export: it names the family **Source Sans
Pro**, which is the old name for what this system calls
`--equinet-font-body`. Use the token.

The pill height is built from padding rather than a fixed `32px`, so a long
label wraps instead of overflowing. The 0.2em of tracking hangs off the last
letter, so the CSS indents by the same amount to put it back on the left —
without that the label sits 2.4px right of centre in the pill, which is
visible at this size.

### `--solid` takes no icon

Plain text, ruled 2026-10-17. The pill is already the emphasis — it is
rationed precisely because it shouts — and a glyph inside it is emphasis
decorating emphasis. In Gestalt terms the pill is a common region doing the
grouping on its own; a second focal point inside a shape whose purpose is to
have one works against it.

`bundle.css` hides an icon placed there, so a page renders correctly either
way, and `check-built-page.py` reports it so the mistake is visible rather
than silently absorbed. Icons belong on the plain eyebrow, where
`.eq-eyebrow__icon` is built for them.

### When `--solid` is allowed

**Hero banners, CTA banners, and modules carrying exceptional value. Nothing
else.** The plain eyebrow is the default and is almost always the right one.

The pill is emphasis, and emphasis that appears on every section stops being
emphasis. If a page has more than one or two, they are decoration and the
plain variant was the right call.

## `card-stacked-layout-01` — 391 × 528 frame, 323 × 459.377 card

The `.eq-card` variant for a card carrying more than a title and a line of
text: a full-bleed image, a stats table, source links out, and a read-more.
Built as `.eq-card--stacked` in `components/bundle.css`.

| Measured | Value | Token |
| --- | --- | --- |
| Card | 323 × 459.377, `rx="7"` | `--equinet-radius-card` |
| Image | 323 × 181.377 full-bleed | ratio 1.781 — effectively 16:9 |
| Side padding | content x 62→337 in a card x 38→361 | `--equinet-space-md` (24px) |
| Heading | 24px / 600, `#242630` | `fontsize-card-heading`, `fontweight-semibold`, `color-heading` |
| Stat label | 16px, `#3B3F51` | `fontsize-body`, `color-body` |
| Stat value | 18px / 600, `#E06730` | `fontsize-stat`, `color-orange` |
| Stat rule | 1px, `#B1B7C8` | `border-width-sm`, `color-border` |
| Stat row | 34px tall, 10px to the next | |
| Sources | 11px, baselines 24px apart | `fontsize-caption` |
| Read more | 16px / 600, `#E06730` | `fontsize-body`, `color-orange` |

Every value resolves to an existing token. The icons are Lucide
`external-link` and `book-open`, which take the house substitute weight — see
`assets/icons/ICON-REFERENCE.md`.

**The read-more is the card's `.eq-card__link`**, so the whole card is the
target and lifts with it. Nothing else inside may be a second link to the
same place.

### Two things in the export not to inherit

1. **The card's drop shadow is `dx-4 dy34 std17 alpha .07`** — that is
   `--equinet-shadow-card--hover`, not `--equinet-shadow-card`. Either the
   comp was exported in its hover state or it drifted. The component uses the
   resting token and lifts to the hover one through `.eq-card`.
2. **"CO-PACKER" is clipped mid-word in the export.** Figma gave the
   heading's drop-shadow filter a 120.426px region and the text is wider. A
   bounding-box artifact, not a design decision.

## `tag` / `tag-grey-outline` / `tag-grey-solid` / `tag-blue-solid` — 162 × 32

A small label carrying a fact about an item. Built as `.eq-tag` in
`components/bundle.css`.

### A tag is not an eyebrow

Both are 12px pills and they do opposite jobs:

| | `.eq-eyebrow` | `.eq-tag` |
| --- | --- | --- |
| Case | UPPERCASE | Sentence |
| Tracking | 0.2em | 0.02em |
| Colour | orange | grey, or navy/amber |
| Radius | 8px | 4px |
| Names | what a **section** is | a fact about an **item** |
| How many | one, above the heading | zero or several, with the item |

"Scoped before set-up" is a tag. "PRICING" is an eyebrow. If the words would
read oddly in capitals, it is a tag.

### Four variants, ascending weight

| Class | Ground | Border | Label | For |
| --- | --- | --- | --- | --- |
| `.eq-tag` | `charade-50` | `charade-300` | `charade-500` | the default, a neutral fact |
| `.eq-tag--outline` | none | `charade-300` | `charade-500` | several together, where filled pills become a block of colour |
| `.eq-tag--solid` | `charade-500` | same | `charade-50` | the one tag that matters among several |
| `.eq-tag--blue` | `blue-default` | same | `amber-400` | a commercial claim. Rare. |

**At most one emphasised tag in a group** — the same discretion rule as the
spotlight. Four blue tags in a row have emphasised nothing.

**A tag states a fact; it is not a control.** No hover, no cursor change, no
lift. A tag that genuinely filters something is a `<button>` and takes button
styling instead.

### Measured

162 × 32, text inset 24, `rx="3.5"` on a rect inset 0.5 — a 4px outer radius
with a crisp 1px stroke. 12px / 600 / +0.02em, Source Sans. One new token:
`--equinet-letterspacing-tag`.

The export's 32px frame **includes** its 1px stroke, so the CSS subtracts the
border from the vertical padding. Without that the tag renders 34px and sits
a shade taller than the eyebrow it so often stands beside.

### Contrast — three of the four sit just under the line

| | | |
| --- | --- | --- |
| `.eq-tag` | 4.46:1 | short by 0.04 |
| `.eq-tag--outline` **on white** | 4.78:1 | passes |
| `.eq-tag--outline` **on `surface--alt`** | 4.39:1 | short by 0.11 |
| `.eq-tag--solid` | 4.46:1 | short by 0.04 |
| `.eq-tag--blue` | 4.15:1 | short by 0.35 |

12px at 600 is not large text, so the threshold is 4.5:1.

**Note the ground matters.** The outline variant passes on white and fails on
`surface--alt`. A tag is not independent of what it sits on, and a page that
moves one onto a tinted surface has changed its compliance without changing
the tag.

A 0.04 miss is a rounding artifact; a 0.35 one is not. But all four are
misses, and **the fix here is close to free**: `--equinet-color-muted`
(#5D6375) clears 5.59:1 and 5.50:1 on both pale grounds, is visually a
half-step darker, and already exists in this system described as "secondary
text" — which is exactly what a tag label is. `.eq-tag--aa` applies it,
opt-in. The comp values ship as drawn.

## Contrast — three components now carry the same failure

The eyebrow, 12px / 700:

| Label on | Ratio | |
| --- | --- | --- |
| `orange--pale` (the pill) | 2.90:1 | fails |
| white | 3.41:1 | fails |
| `surface--alt` | 3.14:1 | fails |
| navy | 3.08:1 | fails |

The stacked card, on white:

| | Ratio | |
| --- | --- | --- |
| Heading 24/600 | 15.05:1 | passes |
| Stat label 16 | 10.42:1 | passes |
| Source 11px | 10.42:1 | passes |
| **Stat value 18/600** | **3.41:1** | **fails** |
| **Read more 16/600** | **3.41:1** | **fails** |

Neither 12px/700 nor 18px/600 is large text — that needs 18.66px bold or 24px
regular — so all of these want 4.5:1.

The compliant forms in `bundle.css`:

- `.eq-eyebrow--solid-safe` — the pill with the label in
  `--equinet-color-text`: 12.93:1.
- `.eq-eyebrow--on-dark` — `--equinet-color-orange--pale` on a dark module
  ground, where orange fails against both navy and night.
- `.eq-card__stat--aa` and `.eq-card__action--aa` — these **drop the orange**,
  because no orange in this system reaches 4.5:1 on white.
  `--equinet-color-orange--dark` is the closest at 4.37:1 and still short, so
  a class called "safe" could not honestly use it.

This is the same open question as `README.md`'s "One unresolved", and it now
has three components attached: the primary button, the eyebrow and the stacked
card. There is precedent for accepting it — the white button label was
accepted by the client at 3.4:1 on 2026-09-21 — but that exception was
explicitly scoped so it "does not extend to any other component", so these
need their own ruling rather than inheriting it.
