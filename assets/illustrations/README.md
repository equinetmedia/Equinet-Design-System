# Illustrations

Standalone graphics — **not icons**. Anything multi-colour, detailed, or meant
to stand on its own belongs here. The quick test: if flattening a graphic to a
single ink would ruin it, it's an illustration. Icons inherit `currentColor`
from the control around them; none of these can.

Three subgroups, 24 files:

| Group | Count | Artboard | Palette | Role |
| --- | --- | --- | --- | --- |
| `pictonodes/` | 8 | 118 × 118 (square) | Night, chart-blue, amber | Spot graphics beside a heading or list item |
| `scenes/` | 12 | 641 × 360 (16:9) | Blue-900, blue-400, amber | Service and process illustrations |
| `sectors/` | 4 | 641 × 361 (16:9) | Blue-default, charade-500, amber | Sector/vertical pictographs |

---

## `scenes/` — service and process illustrations

Twelve 641 × 360 illustrations, added 2026-09-23, in three naming families
that map to service lines:

- **`brand-development-*`** (3): brand consistency, ideal customer profile,
  market clarity
- **`create-*`** (3): a clear positioning strategy, a unified messaging
  framework, your own brand AI agent
- **`website-design-*`** (6): building, journey mapping, monitoring &
  improving, prototyping, smart goal setting, wireframing

4–10 paths each — simpler than the pictonodes despite the larger artboard, so
they carry a lighter, more diagrammatic look.

Palette: `#002E4A` (`--equinet-color-blue-900`), `#81ACD7`
(`--equinet-color-blue-400`), `#F5844D` (`--equinet-color-amber-400`), and in
four files `#F6F5F5` (`--equinet-color-surface-200`). All resolve to existing
tokens; nothing new.

## `sectors/` — vertical pictographs

Four 641 × 361 illustrations covering B2B software, built environment (two
variants) and networked infrastructure.

**A different palette from `scenes/`, deliberately.** These use `#00426C`
(`--equinet-color-blue-default`) and `#68728F`
(`--equinet-color-charade-500`) where the scenes use `#002E4A` and `#81ACD7`.
Both families share `#F5844D`. Whether the two palettes are meant to stay
distinct — sector work reading differently from service work — or whether one
has drifted is **an open question**, not something to normalize by assumption.
Note that `#68728F` is `equinet-color-diagram-line`, sanctioned for marketing
illustration, which suggests the sectors family is the more conventional one.

The 1px artboard difference (361 vs. 360) is almost certainly an export
rounding artefact rather than intent.

### One file is animated, and it has an accessibility problem

`equinet-sector-build-environment-pictograph-1.svg` is **not** a duplicate of
`equinet-sector-build-environment-pictograph.svg` — it's the animated variant,
carrying an embedded `<style>` block with `@keyframes` and:

```css
animation: kf_Vector_transform_0 2s linear infinite;
```

**It has no `prefers-reduced-motion` guard.** An indefinitely looping
animation with no way to stop it is exactly what this system's motion rule
exists to prevent — see `README.md`, "Motion", which requires both a
`no-preference` wrapper and a `reduce` fallback. It is the only animated file
in the whole asset set.

Until it's fixed, use the static `equinet-sector-build-environment-pictograph.svg`
by default. If the animation is wanted, the embedded style block needs a guard
added:

```css
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; }
}
```

Flagged rather than edited: changing delivered artwork is the designer's call,
not something to do silently.

## `pictonodes/` — square spot graphics

Eight 118 × 118 illustrations: line graph, multitask, paper review, pie chart,
review, stack, the CDE, website. 9–24 paths, the densest of the three groups.

Palette: `#242630` (`--equinet-color-night-default`), `#81ACD7` and `#5688BA`
(the chart-blues), `#F5844D`. All existing tokens.

Six are exactly 118 × 118; `pictonode-thecde` is 119 × 117 and
`pictonode-website` 121 × 116. Worth normalizing if they ever share a grid —
the 1–3px difference shows as misalignment.

They won't survive scaling down: at 16px the 1.84px strokes collapse into
noise. Render at or near 118px.

---

## Usage, all groups

Place via `<img>`, not inlined. There's no `currentColor` to inherit, so
inlining buys nothing, and at 1–6 KB each, repeating the markup across modules
is wasteful.

An illustration carrying meaning needs an accessible name. One that's purely
decorative, beside text that already says the same thing, takes `alt=""`.

`scenes/` and `sectors/` are 16:9 — they fit a standard media frame without
cropping. `pictonodes/` are square and don't; don't mix the two in one row.

## Naming

Kept as delivered. Both conventions are descriptive and internally consistent
(`pictonode-<subject>`, `<service-line>-<topic>-v1`,
`equinet-sector-<vertical>-pictograph`), which is what matters here — these
are referenced by what they depict, unlike icons, which are named for the slot
they fill.
