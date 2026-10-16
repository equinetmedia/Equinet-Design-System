---
id: background-assets
status: current
read_when: >-
  Putting a draughtsman's line-work background behind a module. Covers the
  three files, how to place them, why they go in CSS rather than inline, and
  where text must not sit.
depends_on: assets/manifest.json
verified: 2026-10-16
---

# `backgrounds/` — 1619 wide, transparent

Draughtsman's line work: construction circles, arcs, dashed centre lines and
crosshairs, the way a technical drawing looks before anything is dimensioned.
They sit *behind* a module as texture. They are not illustrations, they carry
no meaning, and nothing in them should ever be read.

Added 2026-10-16. The first asset group in this system whose job is to be
ignored.

| File | viewBox | Aspect | Ink | Open area |
| --- | --- | --- | --- | --- |
| `draftmans-background-hero-banner` | 1619 × 820 | 1.97 | `--equinet-color-charade-400` (#8790A9) | Upper left; density sits centre-right |
| `draftmans-background-process-flow` | 1619 × 784 | 2.07 | `--equinet-color-charade-500` (#68728F) | Upper right and lower left; three node clusters along the centre line |
| `draftmans-background-market-amplification` | 1619 × 735 | 2.20 | `--equinet-color-charade-500` (#68728F) | Left two-thirds nearly empty; weight in the upper right |

Both colours are existing tokens. Nothing in these files is unsanctioned.

## Put them in CSS, not in the markup

```css
.eq-module--drafting {
  background-image: url("…/draftmans-background-process-flow.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
```

Three reasons this is not a preference:

1. **`motion.js` would animate them.** Each file is 15–21 paths wide, well
   over the 64px graphic gate, and most of those paths are dashed strokes —
   exactly what the connector draw-on targets. Inlined and annotated, a
   background would draw itself on every scroll. It is texture; it should
   never move.
2. **They are decorative, and CSS backgrounds are invisible to assistive
   technology for free.** Inline SVG needs `aria-hidden="true"` and a
   `role="presentation"` that someone has to remember.
3. **Never annotate them.** No `data-asset`, no `data-role`, under any
   circumstances — not even inline. They are not graphics.

In a HubSpot module the file is a hosted asset and the path is a HubL
`{{ get_asset_url(...) }}`; the background colour and gradient underneath
stay editor-controlled as usual — see the digest rule *"Padding and
background are the editor's"*.

## Where text must not sit

Measured, body text `#242530` over the line work on white:

| Ink | At full opacity | Under the 0.7 group |
| --- | --- | --- |
| charade-400 (hero) | 4.77:1 — passes | 7.10:1 |
| charade-500 (other two) | **3.18:1 — fails AA** | 5.55:1 |

Each file has one group at `opacity="0.7"`; the rest of the strokes are at
full strength. So body text crossing a full-opacity charade-500 line is below
the 4.5:1 threshold.

In practice the strokes are hairlines — 0.5 units on a 1619 viewBox, under a
pixel at any normal render width — so the area of text actually touching a
line is tiny. WCAG has no exemption for that, and the fix is free: all three
files were drawn with large open areas, so **set the copy in the open side
and let the density fall on the other**. The table above says where that is
for each one.

Never put the line work behind a stat figure, a chart, or anything a reader
has to decode. Headings and short copy only.

## How they are drawn

Worth matching if another one is ever needed:

- **One ink per file**, no fills, no gradients, no text.
- **Hairline strokes** — mostly `0.5`, with `0.3`, `0.37621`, `0.526694`,
  `1.15893` and `2` for emphasis. Deliberately inconsistent, the way a real
  construction drawing is.
- **A repeating dash family** — `7.52`, `9.03`, `12.16`, `13`, `14.06`, `52`
  and one `293.57`. The same numbers recur across all three files; they are
  the signature.
- **Clipped to the frame** with two `<clipPath>` per file, so arcs run off the
  edge rather than resolving inside it. That is what makes them read as a
  detail of something larger.
- **One group at `opacity="0.7"`** for the second plane, giving depth without
  a second colour.

## Scaling

The strokes scale with the viewBox, so they stay proportional but not
constant: at 1440px wide a `0.5` stroke renders about 0.44px — a faint
antialiased line, which is the intent — while a 2560px hero thickens it to
0.79px and the drawing reads more strongly. Below about 900px the finest
strokes start to disappear. On mobile, drop the background or switch to a
cropped region rather than scaling the whole 1619 frame down.
