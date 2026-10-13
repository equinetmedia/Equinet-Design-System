---
id: chart-assets
status: current
read_when: >-
  Putting a statistic on a page. Records which figures are verified against
  their source and which must not be quoted. Read with
  assets/charts/data.json.
verified: 2026-10-13
---

# Charts

Seven data charts on AI adoption in manufacturing, added 2026-10-02. A new
category: unlike illustrations, these carry **real statistics with cited
sources**, so they're governed by the system's one hard limit — never invent
data — rather than by the recomposition freedom illustrations get.

| File | Title | Form | Source |
| --- | --- | --- | --- |
| `chart-ai-results-not-universal` | But AI is not delivering spectacular results for everyone | 3 donuts | MIT NANDA; Makerverse; Make UK |
| `chart-ai-adoption-manufacturing-2025` | Global Manufacturing Organisations — 2025 — State of AI Adoption | Horizontal grouped bars | MIT |
| `chart-ai-leaders-widening-gap` | Leading companies are widening the gap in AI | Dumbbell | MIT MIMO; McKinsey |
| `chart-ai-targets-achieved` | Successful AI-related targets achieved | Gauge | BCG |
| `chart-robotic-arms-roi` | ROI from intelligent AI-powered robotic arms | 3 gauges | WEF |
| `chart-ai-industry-output` | The impact of AI on industry output | Stacked bars | Accenture and Frontier Economics |
| `chart-ai-adoption-barriers` | Most significant barriers to the adoption of AI | Grouped bars, 2023 vs 2024 | Rootstock Software |

All 1200px wide; six on a white ground, one transparent.

## The figures are in `data.json`, not in the artwork

**Every chart has zero live text.** All numbers, labels, axis values and
source lines are outlined to paths, so no model can read or edit them — and
retyping figures by hand is exactly where numbers get mistyped or invented.

`data.json` holds every figure as data, with its source and a status:

- **verified** — checked against the source's own published statement and
  found to match.
- **transcribed** — read from the artwork; the source is cited but the figure
  hasn't been independently checked. Usable, but verify before building a new
  claim on it.
- **not-quotable** — the chart plots positions without printing values. Don't
  quote numbers read off the geometry; they're estimates, not data.

**To use a chart's data in a new design, rebuild the chart live from
`data.json`** — real `<text>`, real values, sources shown. Don't reuse the SVG
and edit it, and don't retype from the picture.

## What the review found

Each chart was rendered and read, its geometry measured against its labels,
and where possible its figures and sources checked against the publisher.

**The barriers chart is labelled "% illustrative" — but its data is real.**
The 2023 figures (49, 43, 37) and the 2024 figures (45, 44) match Rootstock's
published survey releases exactly. The label wrongly tells readers genuine
survey data is made up. It should be removed.

**The adoption chart's bars are not drawn to scale.** Measured against their
labels, 12 of 15 bars deviate by more than 1.5 points — 62% is drawn as
69.2%, 77% as 82.4%, 37% as 41.5% — in both directions, so the bars were sized
by eye. Ordering is preserved, but gaps are distorted. The smallest bars
(2–4%) are drawn near 5%, probably a deliberate minimum to fit the label;
that's defensible and should be stated, but it doesn't explain the large
errors. Rebuild from `data.json`.

**The two other bar charts are accurate.** Industry output is within 0.1 of
every value; barriers within 0.4 points. Donuts, gauges and the dumbbell were
not measured — their arcs and plotted positions need different geometry — so
they carry no accuracy claim either way.

**Source names misspelled on the artwork:**
- "MIT NANDO" → **MIT NANDA** (MIT Media Lab's Project NANDA)
- "Rootsock Software" → **Rootstock Software**

**The 95% statistic is broader on the chart than in the source.** The chart
says organisations report zero measurable ROI from "AI pilots"; the MIT NANDA
study covers *generative* AI pilots specifically, and is a preliminary report
with a limited, self-reported sample. Say "generative AI" when using it.

**Smaller details:**
- The dumbbell's subtitle says "HPI impact multiple"; both its footnotes say
  KPI. Almost certainly a typo.
- "20/30%" reads as a ratio or "20 or 30"; a range is written "20–30%".
- In the adoption chart, two labels (52%, 4%) set the % sign smaller and
  raised; the other thirteen don't.
- In industry output, only the Manufacturing bar has rounded top corners.
- `#FEE8D6`, the light range segment in the robotic-arms gauge, isn't a token —
  another pale-orange near-miss; nearest token `--equinet-color-orange--pale`.

None of this is corrected in the SVGs: changing delivered artwork is the
designer's decision. It's recorded here and in `data.json` so the fixes can be
made at source, and so any rebuild starts from the right figures.

## Palette — an open question

These charts use **navy, orange and teal** (`--equinet-color-navy`,
`--equinet-color-amber-400`, `--equinet-color-teal-default`) for their series.
The system's sanctioned data-visualisation palette is the three
`--equinet-color-chart-blue-*` tokens — sanctioned from a single infographic.
None of the seven charts uses them. Seven real charts are stronger evidence of
how Equinet draws data than the one file the current rule rests on, so this
needs a decision rather than either rule being assumed.

## Not annotated with `data-role`, deliberately

The role classifier built for illustrations would mislabel these: every orange
bar would become the single `accent`, every navy bar a `glyph`. And the motion
layer's generic `data` animation grows elements upward, which is wrong for
horizontal bars and meaningless for arcs. Charts need chart-aware roles and
orientation-aware motion; until then they're left unannotated, and motion.js
leaves them alone.
