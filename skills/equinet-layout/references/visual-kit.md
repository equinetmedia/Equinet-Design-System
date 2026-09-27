# Visual kit — building Equinet graphics from parts

The illustration files are a parts bin. Every graphic below is built from
primitives that already exist in `assets/illustrations/`, rebuilt as live HTML
and CSS with tokens — so a bespoke infographic for any topic still looks
unmistakably Equinet.

## Primitives

Measured from the illustration files; the right-hand column is what to use
when rebuilding at page scale.

| Primitive | Where it comes from | Rebuild with |
| --- | --- | --- |
| **Card** | `flows/` — 170px, 4px border, gradient fill | `background: linear-gradient(var(--equinet-color-surface--alt), var(--equinet-color-surface))`, `border: 2px solid var(--equinet-color-border)`, `border-radius: var(--equinet-radius-card)`, `box-shadow: var(--equinet-shadow-card--hover)` |
| **Connector** | `flows/`, `systems/` — `#B1B7C8` strokes between elements | A 2px line in `--equinet-color-border`; the `arrow-chevron` icon at the head for direction |
| **Node** | `flows/` — circles, `#68728F` | A 24–28px circle in `--equinet-color-diagram-line`; holds a Lucide icon or a step number in white |
| **Accent / outcome** | `flows/` — the orange-bordered terminal box | `--equinet-color-orange` border on the final element. **Once per graphic** — it marks where the process arrives |
| **Panel** | `systems/` — pale `#F1F1F1` grounds | `background: var(--equinet-color-diagram-surface)` behind a group of related elements |
| **Line-work** | `systems/`, `marketing/` — grey structural lines | `--equinet-color-diagram-line` or `--equinet-color-charade-400` |
| **Data fill** | `marketing/` ABM infographic — three-step blues | `--equinet-color-chart-blue-light`, `-mid`, `-dark` — data only |
| **Spot graphic** | `pictonodes/` — 118px | Place whole beside a heading or in a list |
| **Icon** | `assets/icons/`, then Lucide | Lucide at `stroke-width="1"`, ≤48px, `currentColor` |

## Compositions

Each recipe names the illustration it's derived from, so you can open that
file for reference.

**Horizontal step flow** — *from `flows/`*
Three to five cards in a row, joined by connectors with chevrons, each card
holding a node (icon or number) above a short label. The last card carries
the orange accent. Stacks vertically below 768px, connectors turning
downward. Use for any ordered process.

**Hub and spoke** — *from `systems/`*
A central node or card, with connectors radiating to three to six satellite
cards on a pale panel. Use for a core idea with dependent parts — a platform
and its integrations, a strategy and its pillars.

**Feedback loop** — *from `systems/system-insight-feedback-loops`*
Nodes placed around a circle, connectors running in one direction between
them, a label at each node. Use for cycles — insight → action → measure →
insight.

**Layer stack** — *from `pictonodes/pictonode-stack`*
Horizontal bands stacked vertically, narrowing or widening, each labelled.
Use for architecture, maturity levels, or anything built in layers.

**Stat panel** — *from `cagr-four-column`*
A card holding a large figure (`--equinet-fontsize-stat` or larger for a
callout), a Lucide icon, a short label and a source line; a
`--equinet-color-border` rule between stats in a row. Real figures only.

**Comparison split** — *from the `2-column-comparison` comp*
Two panels side by side with a divider, matched rows so the eye compares
across. The preferred side can carry the orange accent.

**Icon grid** — *from `service-tiles/`*
Three to six cards each led by an icon, for parallel capabilities or
benefits. Use the service tiles where the subject is an Equinet service;
compose with Lucide icons otherwise.

## Style — how Equinet infographics look

Drawn from the seventeen files in `assets/marketing/`:

- **Grey dominant.** Structure in diagram greys and borders, on white or a
  pale panel. The graphic reads as calm and technical.
- **One accent.** Orange appears once or twice, marking the outcome or the key
  element — never as decoration.
- **Blue for data.** The chart blues carry quantities; they don't decorate.
- **Consistent weight.** Connectors and borders at one weight throughout a
  graphic; Lucide icons at `stroke-width="1"`.
- **Generous space.** Elements breathe; a crowded diagram reads as a
  diagram of the crowd.

## Whole illustrations — placement

When an illustration's subject matches, place it whole (see `INDEX.md`):

| Group | Notes |
| --- | --- |
| `scenes/` | Opaque navy gradient — use as a full media panel or card header, on its own ground |
| `sectors/` | Opaque **light** gradient (`#F6F5F5` → white) — fill the frame edge to edge; keep off dark sections |
| `systems/`, `flows/` | Transparent — sit them on a pale panel or white |
| `pictonodes/` | Square spot graphics — beside headings and list items |

Crop and scale freely. Colour, type and iconography stay per the system; when
you extract an element, sample its colour from `tokens.css` rather than the
artwork.

## Layouts from `assets/comps/`

| Comp | Blueprint for |
| --- | --- |
| `module__2-column-hero-banner` | Opening a page — proposition left, visual right |
| `module__2-column-comparison` | Any side-by-side argument |
| `module__5_column_block_methodology` | A named method in steps, with an orange eyebrow and 56px Open Sans heading |
| `module__sector-three-column-case-study` | Grouped proof — three columns of sector cards, 36px/900 section heading |

Reproduce the structure with live components. Open the comp to read its
spacing and hierarchy; its live `<text>` elements give real type sizes.
