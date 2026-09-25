# Icons

Small glyphs that sit inside or beside a control, as opposed to the standalone
graphics in `assets/illustrations/`. The quick test: if flattening a graphic to
a single ink would ruin it, it's an illustration, not an icon.

Three groups, 16 files:

| Group | Count | Size | Ink | Recolours with `currentColor`? |
| --- | --- | --- | --- | --- |
| (root) | 3 | 24 × 24, 15.6 × 13.1, 26 × 26 | `currentColor` | Yes |
| `nodes/` | 5 | 43 × 43 | `#242630` | **No** — hardcoded, see below |
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

**The filenames say "black" but the ink is `#242630`** —
`--equinet-color-heading`, the same near-black used for headings, not true
black (`--equinet-color-black` / `#000000`, which does exist as a separate
token). The names are kept as delivered, but don't read them as a colour
specification.

**They hardcode that fill rather than using `currentColor`**, unlike the root
icons. As delivered they can't follow a control's colour. If they're meant to
sit inside anything with a hover or a dark variant, the fill wants swapping for
`currentColor` — a one-line change per file, but a change to delivered artwork,
so it's flagged rather than made.

A sixth file, `node-black-hubspot-1.svg`, was **dropped as a true duplicate**:
identical geometry to `node-black-hubspot.svg`, differing only by sub-0.001px
floating-point rounding in the exported path. Unlike the animated sector
pictograph, there was no second behaviour to preserve.

## `service-tiles/` — 65 × 65 tiles

Added 2026-09-23. Eight rounded tiles (`rx 10.34`), each a white line glyph on
a navy gradient, one per service:

`commercial-narritive` *(sic — delivered spelling)* · `competitor-analysis` ·
`digital-experience-alignment` · `ideal-customer-profile` ·
`positioning-audit` · `positioning-strategy` · `sales-enablement-alignment` ·
`value-architecture`

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

## Placeholder policy

**Matching a substitute: see `ICON-REFERENCE.md`.** It records the measured
house style (24 × 24, 2px stroke, round caps and joins, `currentColor`),
names Lucide as an exact match rather than an approximation — the house
chevron is literally Lucide's `arrow-right`, same path in different notation
— explains what has to change to make a Phosphor icon fit, and lists a
suggested substitute for each of the three icons still missing geometry.



Decided 2026-09-23. A neutral icon set (Lucide or similar) is an acceptable
stand-in where a design calls for an icon not held here — but it must read as a
placeholder, not be presented as a real Equinet icon. Don't fabricate a
plausible-looking custom shape; the icons above exist because real geometry was
measured rather than guessed.
