# Equinet assets for layout decisions

A pointer file. The authoritative detail lives in the design system repo;
this summarises what a layout decision needs and says where to look.

## Illustrations — `assets/illustrations/`

Always choose via `assets/illustrations/INDEX.md`, which lists every file's
subject and topics. **If nothing matches the section's subject, use none.**
The set covers Equinet's service lines, sectors and business-process
concepts; it does not cover consumer tech, AI ethics, psychology, wellbeing,
news or third-party products.

| Group | Shape | Best for | Placement |
| --- | --- | --- | --- |
| `scenes/` (12) | 16:9, **opaque** navy gradient | Service and process concepts | Media panel, card header. Never on a white surface |
| `sectors/` (4) | 16:9, transparent | Industry verticals | Needs a surface behind it |
| `systems/` (5) | 16:9, transparent | Commercial-systems diagrams | Needs a surface; dense, suits explanation sections |
| `flows/` (3) | 16:9, transparent | Ordered four-step sequences | Needs a surface; implies order — don't use for unordered items |
| `pictonodes/` (8) | Square 118px | Spot graphic beside a heading or list item | Inline; never in a 16:9 row |

**Illustrations are reference, not sealed artwork.** Crop, scale, overlap,
extract elements and recombine them. What stays fixed: colour (tokens only),
typography and iconography. When extracting, re-check contrast — an element
loses the ground it was drawn against — and sample colour from `tokens.css`,
not the artwork, since several values in those files are unsanctioned.

**`flows/` cards are the real card pattern** — their shadow is
`--equinet-shadow-card--hover` scaled 1.154×. A card lifted from one can be
rebuilt as live components rather than pasted as artwork.

## Icons — `assets/icons/`

| Group | Use |
| --- | --- |
| Root (3): `arrow-chevron`, `arrow-solid`, `play-circle` | Inside buttons; take `currentColor` |
| `service-tiles/` (8) | One per service. The tile is fixed; the white glyph may be swapped for a Lucide icon |
| `nodes/` (5) | Concept marks. Brand assets — place, don't alter |

Missing an icon? Lucide, `stroke-width="1"`, marked `PLACEHOLDER:` in a
comment, never over 48px. Never draw one. See
`assets/icons/ICON-REFERENCE.md`.

## Components — `components/bundle.css`

| Exists | Doesn't exist yet |
| --- | --- |
| `.btn-primary` (+ `--video`, `--hover-light`, `--hover-dark`) | Charts of any kind |
| `.btn-navigation` | Stat callout / stat row as a standalone component |
| `.btn-textual` | Tables |
| `.eq-stagger` (+ `--scene`, `--transparent`, `__row--compact`) | Flowcharts |
| | FAQ / accordion |

Anything in the right-hand column gets built from tokens and **flagged as new
in the output**, so it can be promoted into the design system instead of
living as a one-off.

## Data visualisation tokens

`--equinet-color-chart-blue-light` (`#81ACD7`), `-mid` (`#5688BA`), `-dark`
(`#3D71A5`). Charts and data graphics only — never UI, buttons or text.
Distinct from `--equinet-color-navy` by design. For chart structure (axes,
gridlines, labels) use the diagram greys: `--equinet-color-diagram-line`,
`--equinet-color-diagram-tint`, `--equinet-color-border`.

Three blues is a small palette. A chart needing more than three series is
usually a chart with too many series — consider splitting it before reaching
for a colour that isn't a token.
