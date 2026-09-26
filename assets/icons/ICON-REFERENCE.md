# Icon reference — matching Lucide or Phosphor to the house style

For choosing a third-party icon where Equinet has no real geometry. The three
control icons in this folder define the style; this file states it explicitly
so a substitute can be matched rather than guessed at.

## The house style, measured

Taken from `arrow-chevron.svg`, extracted verbatim from
`button_textual_default.svg`:

| Property | Value |
| --- | --- |
| Canvas | 24 × 24 |
| Stroke width | 2 |
| Line caps | round |
| Line joins | round |
| Fill | `none` |
| Stroke | `currentColor` |

## Use Lucide. Its geometry matches exactly; its stroke is set finer on purpose.

Lucide's own design rules specify a 24 × 24 canvas, 2px stroke, round joins,
round caps and centred strokes, with `fill="none"` and
`stroke="currentColor"` on the root element. Canvas, caps, joins and colour
handling all match the house style exactly.

**Stroke is the one deliberate exception.** Equinet overrides Lucide's native
2 down to 1 — see the next section. Everything else about a Lucide icon is
used as shipped.

The match is literal, not stylistic. Lucide's `arrow-right` is stored as:

```
M5 12h14m-7-7l7 7l-7 7
```

Equinet's chevron, extracted from the Figma button export, is:

```
M5 12H19        M12 5L19 12L12 19
```

Same path, different notation — `5 + 14 = 19`, and the three chevron points
are identical. The house arrow **is** Lucide's arrow-right. A designer drew
to that grid, or the icon came from that lineage; either way, a Lucide
substitute will sit beside the real icons without a visible seam.

**Phosphor is the fallback, and needs work to fit.** It's a 256 × 256 canvas
with filled paths and six weights (Thin, Light, Regular, Bold, Fill,
Duotone). None of those is a 2px stroke on a 24 grid, so a Phosphor icon
placed next to `arrow-chevron` will read heavier or lighter. If a needed icon
exists only in Phosphor, use the **Regular** weight, rescale to a 24 × 24
viewBox, and expect to check it optically against a real icon rather than
trusting the numbers.

## Substituted icons are 1px, and never exceed 48px

**Rule set 2026-09-24.** Every Lucide (or other substituted) icon declares
`stroke-width="1"`, not Lucide's native 2, and renders at 48px or smaller.

This is a deliberate divergence from the house style, not a match to it.
Equinet's own icons are 2px on a 24 canvas; a substitute at 1px renders half
that weight at the same size. Two consequences, both intended:

- Lucide icons read as a finer, lighter layer than Equinet's own 2px marks —
  a deliberate visual distinction between the brand's signature icons and
  general-purpose iconography.
- **Never scale the declared stroke up to "correct" the difference.** At 48px
  a 1px declaration happens to render 2px, matching the house weight exactly —
  that's arithmetic, not the goal. Keep the declaration at 1 at every size.

| | Equinet's own | Substituted |
| --- | --- | --- |
| Declared stroke | `2` | `1` |
| Canvas | 24 × 24 | 24 × 24 |
| Caps / joins | round | round |
| Max display size | 48px | 48px |

The 48px ceiling applies to both. Above it an icon stops reading as an icon
and starts reading as an illustration — at which point use
`assets/illustrations/`, which is built for that job.

Tokens: `--equinet-icon-stroke` (2), `--equinet-icon-stroke--substitute` (1),
`--equinet-icon-size-max` (48px).

## Picking a substitute

1. Search Lucide first, by what the icon *does*, not by name.
2. Keep Lucide's own root attributes — don't restate `fill` or `stroke` on
   inner paths; the wrapper applies them, and duplicating them breaks colour
   inheritance in a dark context.
3. Size it to the slot the real icons use: 24 × 24 for a chevron-class glyph,
   26 × 26 where a play-circle sits.
4. Name its source in a one-line comment (`<!-- lucide/x -->`), so anyone
   reading the markup can tell a Lucide icon from Equinet's own geometry.
   That's provenance, not a warning label — use Lucide freely.

```html
<!-- lucide/x -->
<span class="eq-icon" aria-hidden="true">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
       stroke="currentColor" stroke-width="1"
       stroke-linecap="round" stroke-linejoin="round">
    <path d="M18 6 6 18M6 6l12 12"/>
  </svg>
</span>
```

## The three icons still missing geometry

Known from their modules' CSS — size and colour behaviour — but never
supplied as markup. Each has an obvious Lucide equivalent:

| Needed | Slot | Size | Lucide substitute |
| --- | --- | --- | --- |
| `close` | `cim-methodology` video modal, 20 × 20 glyph in a 44 × 44 circle | 20 × 20 | `x` |
| `checkmark` | `workshop_one_column` bullet list | 26 × 26 | `circle-check` |
| `external-link` | `cagr-four-column` pill link | 16 × 16 | `external-link` |

Use these. If Equinet's own Figma geometry for any of them turns up later,
it takes priority — the same way `arrow-chevron`, `arrow-solid` and
`play-circle` came from the button exports — but until then Lucide is the
right answer, not a stopgap.

## Service tiles: glyphs ARE substitutable — rule set 2026-09-24

**This reverses an earlier rule in this file.** The tiles were previously
listed as un-substitutable brand marks. They aren't: the *tile* is the brand
asset — the 65 × 65 rounded rect, its `#265D94` → `#002E4A` gradient, the
`rx 10.3409` corner — and the white glyph inside it is iconography, which
follows the same rules as any other icon here.

Substitution is clean because the geometry already matches. Measured across
all eight tiles: **2px stroke, round caps, round joins**, white, with the
glyph occupying roughly a 27px box inside the 65px tile. Lucide is 2px on a
24 canvas with the same caps and joins — so a Lucide icon scaled into that
box needs no restyling, the same way the house chevron turned out to *be*
Lucide's `arrow-right`.

### Contract for a replaced glyph

| Property | Value |
| --- | --- |
| Source | Lucide, current version |
| Canvas | 24 × 24, placed in a ~27px box centred in the 65px tile |
| Stroke | `1`, `white` — the substitute weight, not the tile's original 2 |
| Caps / joins | `round` / `round` |
| Fill | `none` |
| Tile | Untouched — same rect, gradient, radius |

**A replaced tile glyph will be finer than an unreplaced one.** The delivered
tiles carry 2px glyphs; a Lucide substitute declares 1. That's the
substitution rule applying consistently, and it means a part-replaced set
will look mixed. Replace the whole set or none of it.

(The delivered tiles also aren't internally consistent:
`services-positioning-strategy` has a `1.15385` stroke on one path and
`services-value-architecture` uses `1.92308`, where the rest are 2. That
inconsistency disappears if the set is replaced wholesale.)

### Mapping, by service context

| Tile | Lucide icon | Why |
| --- | --- | --- |
| `services-positioning-audit` | `search-check` | An audit is an inspection that reaches a verdict |
| `services-positioning-strategy` | `target` | A chosen position to aim at |
| `services-competitor-analysis` | `chart-no-axes-column` | Comparing performance across players |
| `services-ideal-customer-profile` | `user-round-search` | Identifying a specific customer type |
| `services-commercial-narritive` | `message-square-quote` | A told story, not a document |
| `services-value-architecture` | `layers` | Structure built up in layers |
| `services-sales-enablement-alignment` | `handshake` | Two functions brought into agreement |
| `services-digital-experience-alignment` | `monitor-check` | A digital surface, verified |

These are proposals based on what each service means, not decisions — a
designer may well prefer a different glyph, and the mapping should be edited
rather than treated as fixed. What is fixed is the contract above.

### Path data comes from Lucide, never from memory

Do not transcribe a Lucide path from recall when building a replacement.
Fetch it from the library — `lucide.dev`, the npm package, or a
`lucide-react` import — and keep its root attributes rather than restating
`fill` or `stroke` on inner paths. A remembered path is a fabricated path,
which is the failure this whole file exists to prevent. The three root icons
here were extracted from real exports with a parser precisely because
estimates weren't good enough.

## `nodes/` — still not substitutable

The five 43 × 43 concept marks are a different case. They have no enclosing
brand container to preserve; the mark *is* the whole asset, and there's no
Lucide equivalent for an Equinet concept node. Replacing one wouldn't be
substituting a glyph inside a brand asset, it would be replacing the brand
asset. If a new node is needed, that's a request for the designer.
