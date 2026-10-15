---
id: content-to-format
status: current
read_when: >-
  Deciding what format a piece of content becomes — bar vs line, sequence vs
  flowchart, cards vs table.
depends_on: skills/equinet-layout/SKILL.md
verified: 2026-10-13
---

# Content shape → format

Find the shape first, then read across. Every section ends up with a visual:
where the content is argument rather than structure, the format is prose, but
it still carries a spot graphic, a pull-quote or an icon — see
`visual-kit.md`.

## The matrix

| Content shape | How to recognise it | Format | Equinet reference |
| --- | --- | --- | --- |
| **One striking number** | A single figure that carries the point on its own | Stat callout — large number, short label, source line | New component; stat styling from `cagr-four-column` |
| **2–4 comparable numbers** | Several figures measured the same way | Stat row | `cagr-four-column` stat rows (`--equinet-fontsize-stat`, 18px value / 16px label, `--equinet-color-border` rule between) |
| **Change over time** | Values across dates or periods | Line chart | New — navy, orange and teal (ruled 2026-10-13) |
| **Comparison across categories** | Same measure, several named items | Bar chart, sorted by value | New — navy, orange and teal (ruled 2026-10-13) |
| **A single share** | One percentage of a whole — "95% of…" | Donut | `chart-ai-results-not-universal` (three donuts) — see below |
| **Parts of a whole** | Several shares that sum to 100% | Stacked bar, or a single bar split into segments | New. Not a pie — see below |
| **Ordered steps** | "First… then… finally", a numbered method | Process sequence | `5_column_block_process`; `flows/` illustrations; `2_column_intelligence_engine_steps` |
| **Branching process** | Steps with decisions or alternative paths | Flowchart | New. `systems/` illustrations as style reference |
| **Cycle or feedback loop** | Output feeds back into input | Loop diagram | `systems/system-insight-feedback-loops`; `pictonodes/pictonode-review` |
| **Two options side by side** | "X versus Y", before/after, with/without | Two-column comparison | `2-column-comparison` |
| **Items with several attributes** | Rows of things, each with the same properties | Table | New. Only when genuinely tabular |
| **3–5 parallel ideas** | Equal-weight points, no order | Card row | `growth_cards`; `cagr-four-column`; `sector-three-column-case-study` |
| **Service or capability** | What Equinet does, as an offer | Service tile + short copy | `assets/icons/service-tiles/` |
| **A quote or endorsement** | Attributed words from a real person | Testimonial | `pencil_testimonial` |
| **Proof from a real client** | Named customer, outcome, context | Case study | `sector-three-column-case-study` |
| **Definitions / common questions** | "What is…", "How does…" | FAQ / accordion | New as a component — also the strongest AEO format |
| **Several parallel views of one topic** | Content that splits into peer tabs | Tabs | `tabbed_navigation`, `tabbed_navigation_v2` |
| **An argument or explanation** | Reasoning, nuance, a case being made | Prose with a visual anchor | A pictonode, a pull-quote on a pale panel, or an icon-led summary list |

## Choosing between close calls

**Stat callout vs stat row.** One number that is the headline gets a callout.
Several numbers that support one point get a row. Two callouts on one screen
compete; merge them into a row.

**Bar vs line.** Line only when the x-axis is time and the reader should see
the trajectory. Anything categorical is a bar, even if the categories happen
to be ordered.

**Donuts, yes — pies, no.** The objection to pies is comparison: people read
lengths far more accurately than angles or areas, so a multi-segment pie makes
the reader work harder to see what a bar shows at once, and it falls apart
past three or four segments. None of that applies to a **single share**, where
there is nothing to compare — the ring is a gauge, and the number in the
middle does the reading. Equinet already draws them: three of them, in
`chart-ai-results-not-universal`.

Use a donut for one figure. Use a stacked bar for several shares that sum to
100%. Never a multi-segment pie.

**House style, measured from `chart-ai-results-not-universal`:**

- **Filled arc paths, not a stroked circle.** 17 paths, no `<circle>`, no
  `stroke-dasharray` anywhere in that file. Draw the ring as two arcs.
- **Track first, then value.** A full-circle track in
  `--equinet-color-night-100` (#F6F7F9), then the value arc over it in
  `--equinet-color-blue-default` (#00426C). That paint order is what the real
  file uses.
- **Starts at twelve o'clock, runs clockwise.** Square-cut ends, no rounded
  caps.
- **Band about one seventh of the diameter** — a generous ring, not a thin
  line.
- **The number sits in the middle**, large, in `--equinet-color-text`
  (#242530). It is the thing being read; the ring is context.
- **Caption below in sentence case**, three or four short lines, then the
  source smaller again in `--equinet-color-night-700` (#3B3F51).
- **In a row of three**, separated by thin vertical rules.

A donut with no number in it is a decoration. If the figure isn't worth
setting large, it doesn't need a chart.

**Process sequence vs flowchart.** If every reader takes the same path, it's a
sequence — a flowchart's boxes-and-arrows add nothing. Use a flowchart only
when the path genuinely branches.

**Cards vs table.** Cards when each item needs a sentence of explanation. A
table when items share several short, comparable attributes. A table with one
attribute column is a list.

**Illustration vs data visual.** An illustration conveys a concept; a chart
conveys a measurement. Where content has real numbers, chart them; where it
has a concept, compose or place an illustration. Many sections want both — a
stat row beside a composed graphic.

## Sequencing a page

- Open with the answer: hero, then the most important point stated plainly.
- Alternate density. A data-heavy section followed by another reads as a
  report; follow it with prose or an illustration.
- `.eq-stagger` alternation suits a run of 3+ explained points with media.
  Break it for a full-width moment — a stat row, a chart — then resume.
- Put proof (case study, testimonial) after the claim it supports, not before.
- End with one clear next step, not three competing CTAs.

## Data rules

- Every number traces to the supplied content, with its source shown.
- Label axes and units. A chart without units is decoration.
- Start bar-chart axes at zero; a truncated axis exaggerates differences.
- Round to the precision the source supports — don't add false decimals.
- If a section would be stronger with data the content lacks, say so in the
  brief. Don't supply it.
