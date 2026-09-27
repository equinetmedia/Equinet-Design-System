# Illustrations

Standalone graphics — **not icons**. Anything multi-colour, detailed, or meant
to stand on its own belongs here. The quick test: if flattening a graphic to a
single ink would ruin it, it's an illustration. Icons inherit `currentColor`
from the control around them; none of these can.

Five subgroups, 32 files:

**Choosing one? Read `INDEX.md` first** — it lists every file's subject and
topics. Place a whole illustration when its subject matches; when none does,
compose a bespoke graphic from the set's structural primitives (cards,
connectors, nodes, panels) rather than forcing a near-miss or leaving the
section bare.

**`scenes/` are opaque.** All 12 have a navy-to-blue gradient covering the
full artboard. They work as media panels and card headers, not as transparent
spot art. Every other group is transparent.

| Group | Count | Artboard | Palette | Role |
| --- | --- | --- | --- | --- |
| `pictonodes/` | 8 | 118 × 118 (1.000) | Night, chart-blue, amber | Spot graphics beside a heading or list item |
| `scenes/` | 12 | 641 × 360 (1.781) | Blue-900, blue-400, amber | Service and process illustrations |
| `sectors/` | 4 | 641 × 361 (1.776) | Blue-default, charade-500, amber | Sector/vertical pictographs |
| `systems/` | 5 | 460 × 259 (1.776) | Night, charade, blue-400, amber | Commercial-systems process diagrams |
| `flows/` | 3 | 1209 × 675 (1.791) | Night, charade-500, border, orange | Horizontal step-flow diagrams |

The four 16:9 groups are interchangeable in one frame — 1.776 to 1.791, the
same ratio within rounding, despite four different pixel sizes.
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

`sector-built-environment-animated.svg` is **not** a duplicate of
`sector-built-environment.svg` — it's the animated variant,
carrying an embedded `<style>` block with `@keyframes` and:

```css
animation: kf_Vector_transform_0 2s linear infinite;
```

**It has no `prefers-reduced-motion` guard.** An indefinitely looping
animation with no way to stop it is exactly what this system's motion rule
exists to prevent — see `README.md`, "Motion", which requires both a
`no-preference` wrapper and a `reduce` fallback. It is the only animated file
in the whole asset set.

Until it's fixed, use the static `sector-built-environment.svg`
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

## `flows/` — horizontal step-flow diagrams

Three 1209 × 675 diagrams, added 2026-09-24: turning commercial data into an
uncorrupted source of truth, making technical expertise machine-readable, and
smarter content operations for manufacturing growth.

All three share one composition exactly — a left-to-right sequence of four
170.389 × 170.389 cards joined by arrows, each card holding a single dark
glyph, the row terminating in an orange-accented box. 15–16 paths each.
They are the most templated group in the set: same geometry, same palette,
same counts, differing only in the glyphs and the final accent.

**They're built from UI primitives, not free-drawn.** The cards carry
`rx 18.0784` corners, a 4px `#B1B7C8` border, and a vertical
`#F6F5F5` → `white` gradient — the module background gradient, reversed. Their
drop shadow is `-4.616px 39.236px 39.236px rgba(0,0,0,0.07)`, which is
`--equinet-shadow-card--hover` (`-4px 34px 34px rgba(0,0,0,0.07)`) scaled by
exactly 1.154 on every component, alpha unchanged. That's the real card token
enlarged for the artboard, not a lookalike.

Useful consequence for recomposition: a card lifted out of one of these can
be rebuilt as an actual `.eq-card` with real tokens rather than pasted as
artwork, because it already *is* the card pattern.

Palette, all existing tokens:

| Value | Token | Role here |
| --- | --- | --- |
| `#242630` | `--equinet-color-heading` | The glyph inside each card |
| `#68728F` | `--equinet-color-diagram-line` | Connector nodes and stubs |
| `#B1B7C8` | `--equinet-color-border` | Card borders and the flow arrows |
| `#F6F5F5` | `--equinet-color-surface--alt` | Card gradient start |
| `#E06730` | `--equinet-color-orange` | The terminal accent box |

One palette distinction worth noting: these use `#E06730`, the primary
orange, where every other illustration group reaches for `#F5844D`
(`amber-400`). And `#B1B7C8` is a UI border token doing illustration line
work — the only group where that happens.

## `pictonodes/` — square spot graphics

Eight 118 × 118 illustrations: line graph, multitask, paper review, pie chart,
review, stack, the CDE, website. 9–24 paths, the densest of the three groups.

Palette: `#242630` (`--equinet-color-night-default`), `#81ACD7` and `#5688BA`
(the chart-blues), `#F5844D`. All existing tokens.

Six are exactly 118 × 118; `pictonode-the-cde` is 119 × 117 and
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
