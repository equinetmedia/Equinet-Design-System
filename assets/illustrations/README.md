# Illustrations

Standalone graphics — **not icons**. Anything multi-colour, detailed, or meant
to stand on its own belongs here. The quick test: if flattening a graphic to a
single ink would ruin it, it's an illustration. Icons inherit `currentColor`
from the control around them; none of these can.

Four subgroups, 29 files:

**Choosing one? Read `INDEX.md` first** — it lists every file's subject and
topics, and carries the selection rules, including the one that matters most:
if nothing matches the page's subject, use no illustration rather than the
nearest-looking file.

**`scenes/` are opaque.** All 12 have a navy-to-blue gradient covering the
full artboard. They work as media panels and card headers, not as transparent
spot art. Every other group is transparent.

| Group | Count | Artboard | Palette | Role |
| --- | --- | --- | --- | --- |
| `pictonodes/` | 8 | 118 × 118 (1.000) | Night, chart-blue, amber | Spot graphics beside a heading or list item |
| `scenes/` | 12 | 641 × 360 (1.781) | Blue-900, blue-400, amber | Service and process illustrations |
| `sectors/` | 4 | 641 × 361 (1.776) | Blue-default, charade-500, amber | Sector/vertical pictographs |
| `systems/` | 5 | 460 × 259 (1.776) | Night, charade, blue-400, amber | Commercial-systems process diagrams |

The three 16:9 groups are interchangeable in one frame — 1.776 and 1.781 are
the same ratio within rounding, despite the different pixel dimensions.
`pictonodes/` is square and is not.

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

## `systems/` — commercial-systems process diagrams

Five 460 × 259 diagrams, added 2026-09-23: account management & expansion
enablement, commercial data health & enrichment, commercial insight and
feedback loops, CRM/ERP integration, sales enablement & execution support.

22–36 paths each — the densest group in the set, and unlike the others they
lean on grey structure rather than colour, with `#8790A9`
(`--equinet-color-charade-400`) carrying most of the line work and orange
appearing once or twice per file as an accent.

Palette, all resolving to tokens:

| Value | Token |
| --- | --- |
| `#242630` | `--equinet-color-night-default` |
| `#8790A9` | `--equinet-color-charade-400` |
| `#81ACD7` | `--equinet-color-blue-400` |
| `#D6D8E1` | `--equinet-color-charade-200` |
| `#3B3F51` | `--equinet-color-night-700` (CRM/ERP only) |
| `#F5844D` | `--equinet-color-amber-400` |
| `#F1F1F1` | `--equinet-color-diagram-surface` — **new, sanctioned from this batch** |

Two escalations came out of this group. `#8790A9` had been logged as
"single-file, too weak to sanction" in an earlier marketing batch; it appears
in all five of these plus two marketing files, and was already a real token
from the Figma import, so that question is closed. `#F1F1F1` was genuinely
new — in all five files, in no token — and earned its own token on that
cross-file evidence.

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

**These are reference, not sealed artwork.** A file can be placed whole,
cropped into, scaled, overlapped or rearranged, and its elements can be pulled
out and recombined into new compositions. Arrangement carries no authority.

What does carry authority, and survives any recomposition unchanged: **colour**
(every value a token from `tokens.css`), **typography** (the type scale and
families there — never the comp's own text treatment), and **iconography**
(`assets/icons/`, with `ICON-REFERENCE.md` for a substitute). A shape lifted
out of an illustration is not a licence to invent an icon.

`INDEX.md` carries the full rules, including the two that bite in practice:
extracted elements lose the ground they were drawn against, and several
colours in these files are logged-but-unsanctioned values that shouldn't be
propagated forward.

**Placing a whole file:** use `<img>`. There's no `currentColor` to inherit, so
inlining buys nothing, and at 1–6 KB each, repeating markup across modules is
wasteful. **Extracting elements:** inline the SVG, so the parts are addressable.

An illustration carrying meaning needs an accessible name. One that's purely
decorative, beside text that already says the same thing, takes `alt=""`.

`scenes/`, `sectors/` and `systems/` are 16:9 and interchangeable in a standard
media frame. `pictonodes/` are square; don't mix them into a 16:9 row. A
recomposed graphic sets its own frame and isn't bound by either.

## Naming

Kept as delivered. Both conventions are descriptive and internally consistent
(`pictonode-<subject>`, `<service-line>-<topic>-v1`,
`equinet-sector-<vertical>-pictograph`), which is what matters here — these
are referenced by what they depict, unlike icons, which are named for the slot
they fill.
