# Marketing reference

Infographics and marketing graphics — not icons, not the brand mark, and not
reusable by any module. This folder exists for one reason: real published
content occasionally uses a colour or pattern that isn't in `tokens.css` yet,
and when that happens it needs a decision, the way
`equinet-color-chart-blue-*` did.

## What goes here vs. what doesn't

- **Here**: finished marketing SVGs, kept as reference for the audit trail —
  why a token exists, what it was sourced from, when.
- **`assets/icons/`**: small, reusable glyphs a module actually embeds.
- **`assets/brand/`**: the wordmark, and anything else that's the literal
  brand mark rather than illustrative content.

A file landing in the wrong one of these three doesn't break anything
mechanically, but it misleads whoever reads the folder structure looking for
"what can I embed in a module" versus "what's this token's provenance."

## The rule: nothing gets trusted on arrival

Adding a file here is not the same as adding it to the design system. Every
file added is audited the same way, before anything from it is treated as
fact:

1. Extract the actual fill colours and any font info directly from the file
   — `grep`, not eyeballing a rendered preview, the same way the ABM
   infographic was checked.
2. Check each value against `tokens.css`. A match needs nothing. A near-miss
   (close but not identical, like `#ECEAEA`, `#F3F2F2` and `#F3F3F4` all
   sitting near `equinet-color-surface--alt` without matching it or each
   other) gets logged as a discrepancy, not silently reconciled either
   direction. A genuinely new value gets flagged as a decision, not added on
   assumption.
3. A batch of files doesn't get assumed consistent with each other. Two
   infographics from different periods can carry two different "one-off"
   palettes; each is checked on its own, not averaged or reconciled against
   its neighbours without evidence.

Nothing here is a component. Nothing here is a token until a decision says
so and `tokens.css` / `README.md` are updated to match, with the same
provenance discipline as everything else in this system.

## Index

| File | Added | What it contributed |
| --- | --- | --- |
| `equinet-media-abm-loop-marketing-hubspot.svg` | 2026-09-23 | `equinet-color-chart-blue-*` (sanctioned); `#ECEAEA` and `#F3F2F2` vs. `equinet-color-surface--alt` (both logged, unresolved — `#F3F2F2` missed in this file's first audit pass, caught 2026-09-23 during the second batch's cross-check) |
| `how-equinet-media-enables-ai-augmented-sales.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-line--neutral` (stroke), `-tint--pale`; `#444A60` logged, single-file, not promoted |
| `commercial-systems-aeo-rewards-structure-and-accuracye-blue.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-tint--pale`; `#E3EFFC`, `#CFE0F4` logged, single-file, not promoted |
| `commercial-systems-construction-and-deployment.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-tint`, `-tint--pale` |
| `commercial-systems-hubspot-as-your-operational-core.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-tint`, `-tint--pale` |
| `commercial-systems-the-knowledge-base_091526.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-tint--pale` |
| `equinet-media-the-infinity-loop.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-line--neutral`, `-tint`, `-tint--pale`; `#FFE6DB` **resolved** — folded into `equinet-color-orange--pale`; `#F49E78` logged, still weak |
| `putting-your-market-map-to-work.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-line--neutral` (stroke), `-tint--pale` |
| `HubSpot_Agents.svg` | 2026-09-23 | Real `font-family="Myriad Pro"` confirmed (first file in this folder with recoverable font info — text not outlined); confirmed diagram tokens; `#343330`, `#A4A4A4` logged, single-file; gradient stops `#FF4800`, `#FBDDD2` logged, single-file |
| `TAMbot.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-tint`, border, orange-family tokens; Myriad Pro `<text>` confirmed |
| `GEO-Ops.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-tint--pale`; Myriad Pro `<text>` confirmed |
| `Custom-GTPs-and-GEMs.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-line--neutral` (stroke), `-tint--pale`; Myriad Pro `<text>` confirmed |
| `The-Brand-Ops-Agent.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, border; `#F3F3F4` logged as part of the near-white cluster (see `README.md`) |
| `Using-AI-to-rack-ABM-engagement-across-buying-groups-and-channels.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`, `-tint--pale`; Myriad Pro `<text>` confirmed |
| `Using-AI-t0-Trigger-workflows-from-account-activity.svg` | 2026-09-23 | Confirmed `equinet-color-diagram-line`; Myriad Pro `<text>` confirmed |
| `Deploy-AI-to-generate-and-schedule-personalised-sequences.svg` | 2026-09-23 | `#FFE6DB` contributed to the orange-pale fold decision; `#F6F7F9`, `#8790A9` logged, single-file; Myriad Pro `<text>` confirmed |
| `Use-AI-driven-scoring-to-focus-on-leads-most-likely-to-convert.svg` | 2026-09-23 | `#FFE6DB` contributed to the orange-pale fold decision; confirmed `equinet-color-diagram-line--neutral`; `#F49E78` (2nd file); Myriad Pro `<text>` confirmed |

`equinet-color-diagram-*` (now five tokens, after `-line--neutral` was added
following this second batch) and the `#FFE6DB` → `orange--pale` fold are
covered in full in `README.md`, "Diagram illustration." The near-white
cluster (`#ECEAEA`, `#F3F2F2`, `#F3F3F4`) remains an open decision.
