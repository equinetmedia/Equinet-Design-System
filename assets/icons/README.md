---
id: icon-assets
status: current
read_when: >-
  Inlining an icon. Says which groups take currentColor, which hardcode their
  ink, and which are brand marks that must not be recoloured.
depends_on: assets/icons/ICON-REFERENCE.md
verified: 2026-10-13
---

# Icons

Small glyphs that sit inside or beside a control, as opposed to the standalone
graphics in `assets/illustrations/`. The quick test: if flattening a graphic to
a single ink would ruin it, it's an illustration, not an icon.

Four groups, 21 files:

| Group | Count | Size | Ink | Recolours with `currentColor`? |
| --- | --- | --- | --- | --- |
| (root) | 3 | 24 × 24, 15.6 × 13.1, 26 × 26 | `currentColor` | Yes |
| `nodes/` | 5 | 43 × 43 | White glyph on a `#242630` dark tile | Tile no; **glyph yes — substitutable** |
| `service-marks/` | 5 | 69 × 69 | White glyph on a `#242630` dark tile | Tile no; **glyph yes — substitutable** |
| `service-tiles/` | 8 | 65 × 65 | White glyph on a navy gradient tile | **No** — by design |

---

## Root — control icons

Extracted from the Figma button exports on 2026-09-23: verbatim path data,
viewBoxes computed from true bounding boxes with a path parser, not retyped.

| File | Size | Used by | Source export |
| --- | --- | --- | --- |
| `arrow-chevron.svg` | 24 × 24 | Textual button, navigation button | `button_textual_default.svg` |
| `arrow-solid.svg` | 15.627 × 13.129 | Primary button | `button_primary_large_default.svg` |
| `play-circle.svg` | 26 × 26 | Primary button, video variant | `button_primary_video_default.svg` |

The two arrows are genuinely different shapes, not one icon at two sizes: the
chevron is a 2px round-capped stroke pair, the solid arrow a filled path. Sizes
match comments in two shipped modules' CSS independently.

These take `currentColor`, so a button's hover state recolours label and glyph
in one declaration. Inline them in `module.html` rather than linking —
`currentColor` only inherits from an inline element.

## `nodes/` — 43 × 43 concept marks

Added 2026-09-23. Five single-ink marks: attract, connect, growth, hubspot,
verified. Mostly one path each; `growth` has seven.

**Their ink is `#242630`** — `--equinet-color-heading`, the same near-black
used for headings, not true black (`--equinet-color-black` / `#000000` is a
separate token). The files were delivered as `node-black-*`; "black" was
dropped from the names on 2026-09-26 because it misdescribed the colour.

**Structure: a white glyph on a dark tile.** Each node is a full-size
43 × 43 rounded rect (`rx 5.01`, `#242630`) with a white glyph on top — the
same container-plus-glyph construction as the service tiles. An earlier audit
misread the `#242630` tile as the glyph's own ink and recorded these as
single-ink marks; corrected 2026-09-26. As with the tiles, **the tile is the
brand asset and the white glyph is substitutable** with a context-appropriate
Lucide icon (`stroke-width="1"`, white). Replace all five or none.

A sixth file, `node-black-hubspot-1.svg` (its original export name), was **dropped as a true duplicate**:
identical geometry to `node-hubspot.svg`, differing only by sub-0.001px
floating-point rounding in the exported path. Unlike the animated sector
pictograph, there was no second behaviour to preserve.

## `service-marks/` — 69 × 69 service-line marks

Added 2026-10-02. Four marks named for service lines — commercial data,
commercial diagnostic, commercial positioning, market amplification. Same
construction as `nodes/` — a dark `#242630` rounded tile (`rx 7.55`) carrying
a white glyph — at a larger size, so they're a set of their own rather than
mixed into the 43px nodes.

Same rule as nodes and tiles: **the tile is fixed, the white glyph is
substitutable** for a context-appropriate Lucide icon (`stroke-width="1"`,
white). Replace all four or none.

Delivered as `commercial-*-icon` and `market-amplification-icon`; renamed to
`mark-*` on filing.

**The set now has five — the fifth is derived, not delivered.** The engine
hero (`illustrations/heroes/hero-commercial-intelligence-engine`) shows five
pillars, and its card icons are these marks: every glyph matches at identical
geometry *and* identical absolute placement in its 68.12px tile, measured to
within 0.01. Card 03, **Commercial Systems**, carries a fifth glyph the set
didn't have. `mark-commercial-systems.svg` was built from it by the same
transform: its path copied verbatim, moved from the hero tile into a standard
mark tile (68.12px, `#242630`, `rx 7.55404`). Its placement matches the
siblings' within 0.06px. In the hero that card's tile is orange — a
highlighted state — but the mark uses the dark tile like the other four.

It's marked DERIVED in a comment inside the file. Confirm with the designer
before treating it as final.

In engine order: 01 diagnostic · 02 positioning · 03 systems · 04 data ·
05 amplification.

## `service-tiles/` — 65 × 65 tiles

Added 2026-09-23. Eight rounded tiles (`rx 10.34`), each a white line glyph on
a navy gradient, one per service:

`tile-commercial-narrative` · `tile-competitor-analysis` ·
`tile-digital-experience-alignment` · `tile-ideal-customer-profile` ·
`tile-positioning-audit` · `tile-positioning-strategy` ·
`tile-sales-enablement-alignment` · `tile-value-architecture`

(`commercial-narrative` was delivered misspelled as `narritive`; corrected in
the 2026-09-26 rename.)

Gradient: `#265D94` (`--equinet-color-blue-700`) to `#002E4A`
(`--equinet-color-blue-900`), top-right to bottom-left. Both are existing
tokens; nothing new.

These are **self-contained tiles, not glyphs**. The background is part of the
artwork, the glyph is hardcoded white, and neither responds to
`currentColor` — correctly so, since a white-on-navy tile only works on its own
ground. Place them as `<img>` when using one as delivered.

**The glyph inside a tile is substitutable; the tile is not** — rule set
2026-09-24, reversing an earlier note here. The brand asset is the 65 × 65
rounded rect with its navy gradient; the white glyph inside it is
iconography and follows the same rules as any other icon. Swapping one for a
context-appropriate Lucide icon is sanctioned, and the geometry already
matches: the tile glyphs are 2px stroke with round caps and joins, the same
grid Lucide draws on. `ICON-REFERENCE.md` carries the contract and a
per-service mapping. Inline the SVG when replacing, so the glyph paths are
addressable; keep the rect, gradient and radius untouched.

Recolouring a tile is still out — the white-on-navy pairing is the asset.

Three of the eight overlap in subject with `illustrations/scenes/`
(`ideal-customer-profile`, `positioning-strategy`, and
`sales-enablement-alignment` against the scenes' `sales-enablement` material).
Same topics, different scale and treatment: use a tile in a list or a service
card, a scene as a media panel. See `assets/illustrations/INDEX.md`.

---

## Still missing

`close` (from `cim-methodology`'s video modal, 20 × 20 in a 44 × 44 circle),
`checkmark` / check-circle (`workshop_one_column`'s bullets, 26 × 26) and
`external-link` (`cagr-four-column`'s pill, 16 × 16). Known from their modules'
CSS — size and colour behaviour — but no geometry, because no `module.html`
carrying them has been shared.

## Substituted icons: 1px, max 48px

Rule set 2026-09-24. A Lucide or other substituted icon declares
`stroke-width="1"` — half the weight of Equinet's own 2px icons, on purpose,
so a substitute is identifiable on sight. No icon exceeds 48px, substituted
or not; past that it reads as an illustration. Full rationale and the
per-size arithmetic in `ICON-REFERENCE.md`.

## Using Lucide

**Matching a substitute: see `ICON-REFERENCE.md`.** It records the measured
house style (24 × 24, 2px stroke, round caps and joins, `currentColor`),
names Lucide as an exact match rather than an approximation — the house
chevron is literally Lucide's `arrow-right`, same path in different notation
— explains what has to change to make a Phosphor icon fit, and lists a
suggested substitute for each of the three icons still missing geometry.



**Lucide is the iconography source for anything Equinet doesn't have its own
geometry for — use it generously.** Cards, list items, stats, steps and
service rows all benefit from an icon. Rules: `stroke-width="1"`, 24 × 24
canvas, round caps and joins, never over 48px, a one-line source comment
(`<!-- lucide/name -->`), and path data fetched from the library rather than
drawn from memory. The one thing to avoid is drawing a custom glyph by hand —
Lucide covers almost everything, so there's rarely a reason to.

## `status/` — the check

Four exports of a check in a circle, 32 × 32, the reference geometry for
`.eq-check`. They carry a signal rather than depict a subject, and their
colours are hard-coded, so they are not inlined directly — the component reads
the same geometry with its colours from custom properties so it can follow the
ground. See `assets/icons/status/README.md`.
