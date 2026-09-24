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

## Use Lucide. It is an exact match, not an approximation.

Lucide's own design rules specify a 24 × 24 canvas, 2px stroke, round joins,
round caps and centred strokes, with `fill="none"` and
`stroke="currentColor"` on the root element. Every property above matches.

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

## Picking a substitute

1. Search Lucide first, by what the icon *does*, not by name.
2. Keep Lucide's own root attributes — don't restate `fill` or `stroke` on
   inner paths; the wrapper applies them, and duplicating them breaks colour
   inheritance in a dark context.
3. Size it to the slot the real icons use: 24 × 24 for a chevron-class glyph,
   26 × 26 where a play-circle sits.
4. Mark it as a placeholder in the module comment. The placeholder policy
   allows a substitute; it doesn't allow presenting one as Equinet artwork.

```html
<!-- PLACEHOLDER: lucide/x — no Equinet geometry for `close` yet -->
<span class="eq-icon" aria-hidden="true">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
       stroke="currentColor" stroke-width="2"
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

These are suggestions for a placeholder, not a decision to adopt Lucide's
artwork permanently. If the real Figma geometry turns up, it replaces the
substitute — the same way `arrow-chevron`, `arrow-solid` and `play-circle`
replaced guesswork once the button exports arrived.

## What not to substitute

`nodes/` and `service-tiles/` are Equinet-specific marks — concept nodes and
branded service tiles. There is no Lucide or Phosphor equivalent, and a
generic icon in their place would misrepresent a brand asset rather than
stand in for a missing utility glyph. If one is needed and doesn't exist,
that's a request for the designer.
