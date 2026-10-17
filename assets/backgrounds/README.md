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

# `backgrounds/`

Two different things live here, used two different ways.

**The draughtsman's line work** (`draftmans-background-*`) is artwork, placed
as a CSS `background-image`.

**The radial gradients** (`radial-background-*`) are *reference geometry*.
They are never placed — the surface is built in CSS as `.eq-surface`. See
"Radial surfaces" at the end.

## `draftmans-background-*` — 1619 wide, transparent

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


## Radial surfaces — `radial-background-01` / `-02`, 1920 × 805

A module surface that isn't flat: a soft off-centre pool of white falling
away to `--equinet-color-surface--alt`. Depth without adding anything a
reader has to look at. Built as `.eq-surface` in `components/bundle.css`.

Each file is one rect filled with a two-stop radial gradient. That is the
whole asset — 449 and 439 bytes.

### Why these are built in CSS and the line work isn't

Rendered side by side at 1920 × 805, the CSS version differs from the SVG by
**a maximum of 5/255 on any channel and 1.07/255 on average** — below the
threshold `tests/motion-test.py` already treats as identical. CSS costs no
asset, re-proportions to any module height, and leaves the surface tokens
swappable. There is nothing to gain from shipping the file.

### The signature, from decoding both `gradientTransform` matrices

| | `-01` | `-02` |
| --- | --- | --- |
| Centre | 73.2% across, 22.4% down | 33.4% across, 41.1% down |
| Semi-axis 1 | 845.8px (44.1% of width) | 592.6px (30.9%) |
| Semi-axis 2 | 1710.9px (212.5% of height) | 1198.6px (148.9%) |
| **Axis ratio** | **2.02 : 1** | **2.02 : 1** |
| Skew off perpendicular | ~10.9° | ~10.9° |

**Both stops are already tokens** — white is `--equinet-color-surface` and
`#F6F5F5` is `--equinet-color-surface--alt`, which `tokens.css` has called
the "module gradient start/end stop" since 2026-08-07. These exports are the
geometry for stops the system already had.

**The 2.02:1 ratio appears in both files.** That is not a coincidence; it is
what makes the pool read as a soft wash rather than a spotlight. Hold it when
inventing a variation.

**Neither centre is at 50% 50%.** `-01` pools upper-right and `-02`
upper-left, so alternating them down a page stops consecutive sections
matching.

**The ~11° skew can't be expressed in CSS** — `radial-gradient` has no
rotation — and at a 4% luminance delta between the stops it makes no visible
difference, which is what the pixel comparison above measures.

### Making a variation

Override the four custom properties:

```css
.my-module { --eq-surface-x: 20%; --eq-surface-y: 60%;
             --eq-surface-w: 35%; --eq-surface-h: 165%; }
```

Keep `--eq-surface-h` about twice `--eq-surface-w` once both are resolved
against the module's own box, keep the centre off 50% 50%, and it will still
look like Equinet.

The flat colour sits underneath as `background-color` and the pool on top as
`background-image`, so an editor's background choice still shows through
wherever the pool has fallen away — see the digest rule *"Padding and
background are the editor's"*.


## `radial-background-dark` — 1920 × 805

A deep navy surface, darkest at the bottom-left and lifting to
`--equinet-color-navy` across the frame. Built as `.eq-surface--dark`.

**Use it sparingly** — a section or a card meant to stand apart, never a
second default. It is deliberately excluded from the sibling rotation, so a
dark surface is only ever something someone chose.

### A different signature from the light pair

| | Light (`-01`, `-02`) | Dark |
| --- | --- | --- |
| Stops | `surface` → `surface--alt` | `blue-950` (#011420) → `blue-default` (#00426C) |
| Polarity | light at the centre | **dark at the centre**, lifting outward |
| Centre | upper, off to one side | 4.3% / 93.2% — bottom-left, almost off-frame |
| Axis ratio | 2.023 : 1 | **2.385 : 1** |
| Extent | 44% / 31% of width | 77.8% × 442.5% — runs well past the edges |

Both stops are already tokens. The extent is the interesting part: the pool
is so much larger than the frame that only part of its range is ever visible,
which is what makes it a slow wash rather than a pool you can see the edge
of.

**Don't carry the light pair's rules over.** The 2:1 ratio and the
white-at-centre polarity are theirs, not this one's.

### Closeness

CSS reproduces this to within **7/255 on any channel, 1.11/255 on average** —
close, but not the 5/255 the light pair manage. The −20° rotation does more
work here because the two stops genuinely differ in luminance. The values in
`bundle.css` are a fitted approximation rather than a transcription, found by
searching centre and extent against the rendered SVG. The file stays here if
a build ever needs it exactly.

### What can sit on it

Measured against **both** stops; the worst case is shown, because a surface
that passes at one end and fails at the other has failed.

| | Worst case | |
| --- | --- | --- |
| white | 10.52:1 | body text anywhere |
| `surface--alt` | 9.67:1 | fine |
| `orange--pale` | 8.95:1 | fine — what `.eq-eyebrow--on-dark` uses |
| `teal-default` | 4.96:1 | **passes AA for body — the one accent that does** |
| `orange--light` | 4.15:1 | large text and graphics only |
| **`orange`** | **3.08:1** | **fails at any size. Not an accent here.** |

`.eq-surface--dark` sets `color` to `--equinet-color-surface` so content
inherits something readable instead of each module remembering, and gives a
nested `.eq-eyebrow` its on-dark colour without the modifier. Anything
wanting the accent sets it explicitly — and on this ground that means teal or
`orange--pale`, not orange.

## Varying it automatically

The goal is not randomness. It is that **two surfaces a reader sees together
should not match** — and that whatever a module renders today it renders
again tomorrow. A background that changes between page loads breaks caching,
breaks screenshot diffs, and makes a client think something is wrong. Never
reach for a random value here.

There are four light positions: `--01` and `--02` as measured, `--03` and
`--04` mirrored from them. `--dark` is not one of them and never enters the
rotation. Three ways to choose between the four, in the order to try.

### 1. Siblings — free, no configuration

Where the surfaces are actual siblings, `.eq-surface` with no variant class
rotates through all four by position and repeats on the fifth. Nothing to
set. An explicit `--01`…`--04` always beats position, so an editor's choice
is never overridden.

This is the common case inside one module with several stacked sections. It
is **not** the case across a HubSpot drag-and-drop area, where each module
renders inside its own wrapper and the surfaces are not siblings.

### 2. In a module — the editor chooses, with an automatic default

```json
{
  "name": "surface_style",
  "label": "Section surface",
  "type": "choice",
  "display": "select",
  "default": "auto",
  "help_text": "Auto varies the gradient so stacked modules don't repeat. Pick a position to pin it.",
  "choices": [
    ["auto", "Auto — vary by position"],
    ["01", "Pool upper right"],
    ["02", "Pool upper left"],
    ["03", "Pool upper left, wide"],
    ["04", "Pool upper right, narrow"],
    ["flat", "Flat — no gradient"]
  ]
}
```

```html
{% set surface = module.surface_style %}
<section class="eq-section
  {%- if surface != 'flat' %} eq-surface{% endif %}
  {%- if surface not in ['auto', 'flat'] %} eq-surface--{{ surface }}{% endif %}">
```

`flat` matters: this is a surface treatment, and an editor who wants a plain
background must be able to say so — the digest rule that padding and
background are the editor's applies here too.

### 3. `auto` across modules — derive it from the module instance

Siblings don't work across a dnd area, so `auto` needs something that is
unique per module and stable forever. The module's own `name` is both:

```html
{% set positions = ['01', '02', '03', '04'] %}
{% set pick = positions[name|md5|truncate(6, true, '')|int(0, 16) % 4] %}
```

**Verify `md5` and the base-16 `int` against your HubL version before
shipping this** — if either is unavailable, the same idea works off any
stable numeric in `name`, and the fallback when the derivation yields nothing
is `--01`, never a random pick.

What this does NOT guarantee is that two adjacent modules differ: four
positions means roughly a one-in-four chance any given pair matches. If a
page must alternate strictly, the editor sets the position by hand on each
module — which is what the choice field is for, and why `auto` is a default
rather than the only option.
