# Content shape → format

Find the shape first, then read across. If content fits no row, it's prose —
which is a correct outcome, not a failure.

## The matrix

| Content shape | How to recognise it | Format | Equinet reference |
| --- | --- | --- | --- |
| **One striking number** | A single figure that carries the point on its own | Stat callout — large number, short label, source line | New component; stat styling from `cagr-four-column` |
| **2–4 comparable numbers** | Several figures measured the same way | Stat row | `cagr-four-column` stat rows (`--equinet-fontsize-stat`, 18px value / 16px label, `--equinet-color-border` rule between) |
| **Change over time** | Values across dates or periods | Line chart | New — build from `chart-blue-*` tokens |
| **Comparison across categories** | Same measure, several named items | Bar chart, sorted by value | New — build from `chart-blue-*` tokens |
| **Parts of a whole** | Shares that sum to 100% | Stacked bar, or a single bar split into segments | New. Avoid pies — see below |
| **Ordered steps** | "First… then… finally", a numbered method | Process sequence | `5_column_block_process`; `flows/` illustrations; `2_column_intelligence_engine_steps` |
| **Branching process** | Steps with decisions or alternative paths | Flowchart | New. `systems/` illustrations as style reference |
| **Cycle or feedback loop** | Output feeds back into input | Loop diagram | `systems/commercial-insight-and-feedback-loops`; `pictonodes/pictonode-review` |
| **Two options side by side** | "X versus Y", before/after, with/without | Two-column comparison | `2-column-comparison` |
| **Items with several attributes** | Rows of things, each with the same properties | Table | New. Only when genuinely tabular |
| **3–5 parallel ideas** | Equal-weight points, no order | Card row | `growth_cards`; `cagr-four-column`; `sector-three-column-case-study` |
| **Service or capability** | What Equinet does, as an offer | Service tile + short copy | `assets/icons/service-tiles/` |
| **A quote or endorsement** | Attributed words from a real person | Testimonial | `pencil_testimonial` |
| **Proof from a real client** | Named customer, outcome, context | Case study | `sector-three-column-case-study` |
| **Definitions / common questions** | "What is…", "How does…" | FAQ / accordion | New as a component — also the strongest AEO format |
| **Several parallel views of one topic** | Content that splits into peer tabs | Tabs | `tabbed_navigation`, `tabbed_navigation_v2` |
| **An argument or explanation** | Reasoning, nuance, a case being made | Prose | — |

## Choosing between close calls

**Stat callout vs stat row.** One number that is the headline gets a callout.
Several numbers that support one point get a row. Two callouts on one screen
compete; merge them into a row.

**Bar vs line.** Line only when the x-axis is time and the reader should see
the trajectory. Anything categorical is a bar, even if the categories happen
to be ordered.

**Why not pies.** People compare lengths far more accurately than angles or
areas, so a pie makes the reader work harder to see the same thing a bar
shows at once, and it breaks down past three or four segments. A single
horizontal bar split into segments carries the same parts-of-a-whole idea
legibly. Use a pie only if the user asks for one.

**Process sequence vs flowchart.** If every reader takes the same path, it's a
sequence — a flowchart's boxes-and-arrows add nothing. Use a flowchart only
when the path genuinely branches.

**Cards vs table.** Cards when each item needs a sentence of explanation. A
table when items share several short, comparable attributes. A table with one
attribute column is a list.

**Illustration vs data visual.** An illustration conveys a concept; a chart
conveys a measurement. Don't use an illustration where the content has real
numbers, and don't build a chart to decorate a concept.

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
