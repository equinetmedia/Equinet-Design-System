---
id: reworking
status: current
read_when: >-
  Adapting an existing SVG asset to the shape of the content — adding or
  removing cards, nodes or connectors, or moving the accent. Targets elements
  by data-role.
depends_on: assets/manifest.json
verified: 2026-10-13
---

# Reworking assets to fit the data

How a model adapts Equinet graphics to the content being presented — adding a
step, relabelling a node, recolouring an emphasis, fitting a chart to real
figures. Written for an agent working directly on the SVG files.

## Start here

1. **Choose from `assets/manifest.json`**, not by browsing filenames. It lists
   every asset's category, dimensions, background, which roles it contains,
   its palette mapped to tokens, and — for illustrations and tiles — what it
   depicts and which topics it suits.
2. **Check `category`.** Only `illustration` and `icon` assets are reworked.
   `layout-blueprint` (comps) are rebuilt as live components, never edited or
   embedded. `style-reference` (marketing) are looked at, not edited.
   `button-source` are Figma exports kept as the measurement record — don't
   touch them. `brand` is the wordmark; never alter it.
3. **Target elements by `data-role`**, never by guessing at path coordinates.

## Roles

Every reworkable SVG has a `data-asset` and `data-group` on its root, and a
`data-role` on each drawn element. Roles were assigned from colour tokens and
verified non-destructive — stripping them reproduces each original
byte-for-byte.

| Role | What it is | Typical rework |
| --- | --- | --- |
| `background` | Full-artboard fill on opaque artwork | Leave it. Scenes are dark, sectors light |
| `tile` | Dark container behind an icon glyph | Leave it — the tile is the brand asset |
| `card` | A content card | Add, remove, reposition to match item count |
| `panel` | Pale surface grouping related elements | Resize to enclose what it groups |
| `connector` | Line or arrow between elements | Add or remove with the elements it joins |
| `node` | Circular point on a flow or loop | One per step or stage; match the data's count |
| `glyph` | Icon or pictographic line-work | Swap for a Lucide icon that fits the content |
| `accent` | Orange emphasis — the outcome | Move to whichever element is the point. **Once per graphic** |
| `data` | Chart-blue data element | Resize to real values; never invented ones |
| `shape` | Unclassified, usually invisible bounds | Leave it |

Select with, for example, `[data-role="node"]` or
`svg[data-asset="flow-content-operations"] [data-role="accent"]`.

## The rule that shapes everything: labels live outside the SVG

**No illustration contains live text** — every group audited at zero `<text>`
elements. Illustrations are pure structure. So data labels, step names,
figures and captions go in **HTML**, positioned over or beside the graphic —
never typed into the SVG. That keeps text real, selectable, translatable,
accessible and extractable for AEO, and keeps type on the `tokens.css` scale.

The two groups that do carry live text — `comps/` (60 runs) and `marketing/`
(39) — are reference, not rework targets.

## Constraints on any rework

- **Colour: tokens only.** Every palette entry in `manifest.json` names its
  token. An entry marked `unsanctioned` is a colour in the artwork that isn't
  a token — replace it with the listed `nearest_token` rather than carrying
  the raw hex into new work.
- **One accent.** Move it to the element that is the point; don't add a
  second.
- **Glyphs:** Equinet's own icons first, otherwise Lucide at
  `stroke-width="1"`, never over 48px, path fetched from the library with a
  `<!-- lucide/name -->` comment. Never draw a glyph by hand. Inside a `tile`,
  keep the glyph white.
- **Never invent data.** A `data` element is sized to a real figure from the
  supplied content. No figure, no data element.
- **Backgrounds travel with opaque artwork only.** Extract an element from a
  scene and it loses the navy ground it was drawn against — re-check contrast.

## Per-group recipes

**`flows/` — ordered steps.** Four `card`s at a constant 271.508 pitch,
each 170.389 wide, a `node` on each card's right edge, `connector`s between,
the `accent` on the last. To change the step count, see the worked example —
appending at the same pitch overflows.

**`systems/` — hub, spoke, loop.** `card`s and `node`s linked by
`connector`s on a `panel`. Match `node` count to the number of parts or
stages; move `connector`s with them; resize the `panel` to enclose the group.

**`sectors/` — vertical pictographs.** Opaque light background. Rework is
mostly `glyph` substitution and `accent` placement; the composition is the
sector's identity.

**`scenes/` — service concepts.** Opaque dark background. Rework is `glyph`
and `accent` changes; don't lift elements onto light grounds without
re-checking contrast.

**`pictonodes/` — square spot graphics.** Small and dense. Swap the `glyph`,
move the `accent`. Keep at native size.

**`service-tiles/`, `nodes/` — icon tiles.** Keep the `tile`. Swap the white
`glyph` for a Lucide icon; replace a whole set or none, so 1px substitutes
don't sit beside delivered 2px glyphs. `node-hubspot` is the HubSpot logo —
never substitute it.

## Worked example — a flow with five steps instead of four

The content lists five ordered steps; the best match is
`flow-content-operations`, which has four.

1. **Don't append.** A fifth card at the existing 271.508 pitch starts at
   x = 1136.7 and ends at 1307.0 — past the 1209 artboard.
2. **Choose:** widen the artboard by one pitch (`viewBox` width
   1209 → 1480.5), or keep 1209 and recompute the pitch across the same span.
   Keeping the artboard preserves the 16:9 frame the page layout expects;
   prefer that.
3. **Rebuild the row:** duplicate one `card` + its `node` + the following
   `connector` as a unit, then set all five x positions to the new pitch.
4. **Move the `accent`** to the fifth card — the outcome is now there.
5. **Swap each card's `glyph`** for a Lucide icon matching its step.
6. **Put the five step labels in HTML** under the graphic, aligned to the
   card centres — not in the SVG.
7. **Check:** one accent; every colour a token; no connector left dangling.

## Motion survives a rework — if roles do

Graphic motion keys off `data-role`, so a reworked graphic animates with no
extra work **provided every element you add carries a role**. A duplicated
card should keep `data-role="card"`; a new connector needs
`data-role="connector"`. An element without a role isn't animated and arrives
with the ground, which reads as a mistake mid-entrance. Keep the single
`accent` single — it's choreographed to arrive last.

## After editing

Regenerate `assets/manifest.json` so it reflects the change — it's built from
the files and should never be hand-edited.
