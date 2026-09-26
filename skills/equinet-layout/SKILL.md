---
name: equinet-layout
description: Plan and build Equinet pages from content — decides which visual formats (stat blocks, charts, flowcharts, comparisons, infographics, illustrations) and which HubSpot elements (modules, forms, meetings, video, CTAs) best carry a piece of content, produces a section-by-section layout brief for approval, then builds it against the Equinet design system. Use this whenever the user wants to turn content, copy, research, a topic or a brief into an Equinet page, pillar page, landing page or infographic layout; asks what layout, visual or module would suit some content; or asks how to present stats, steps, comparisons or data for Equinet — even if they don't say "layout" or "brief".
---

# Equinet layout

Turns content into an Equinet page in two deliberate phases: a **brief** that
decides what each section becomes, then — only after the user approves it — a
**build** against the design system. The brief exists so layout decisions are
reviewed while they're still cheap to change.

The core idea: **the shape of the content decides the format**, never the
other way round. A number wants a stat block because it is a number, not
because stat blocks look good. Choosing a format first and fitting content to
it is how pages end up with invented statistics and illustrations that don't
match their subject.

## Before starting

This skill sits on top of the Equinet design system
(`equinetmedia/equinet-design-system`, private). Its `README.md` opens with a
13-rule digest; those rules are binding and this skill does not restate them.
If the repo files aren't available in this session, ask for `README.md` and
`assets/illustrations/INDEX.md` before building — the brief can proceed
without them, but flag that asset choices are unverified.

## Phase 1 — Brief

1. **Read the content and find its shapes.** Before thinking about visuals,
   list what the content actually contains: numbers, ordered steps, two-way
   comparisons, categories with attributes, cause-and-effect loops,
   definitions, quotes, claims. Read `references/content-to-format.md` for
   how each shape maps to a format.
2. **Map shapes to formats**, one section at a time.
3. **Choose supporting HubSpot elements** — what each section asks the reader
   to *do* next, and which module or native feature carries it. Read
   `references/hubspot-elements.md`.
4. **Choose assets** — illustration, icon, or none — per
   `references/equinet-assets.md`. The illustration rule is strict: match on
   subject via `INDEX.md`, and if nothing matches, use none.
5. **Write the brief** in the format in `references/brief-template.md`.
6. **Stop and ask for approval.** Do not build until the user approves or
   amends the brief. If they amend, revise the brief and confirm again.

## Phase 2 — Build

Once approved:

1. Build section by section from the brief, not from a fresh reading of the
   content — the brief is the agreed spec.
2. Use existing components first: `.eq-stagger` for alternating media/text,
   the button classes in `components/bundle.css`, and the shipped modules
   named in the brief.
3. Where the brief calls for something with no component yet — a chart, a
   stat row, a table, a flowchart — build it from tokens, and **say in the
   output that it's new**, so it can be promoted into the design system
   rather than living as a one-off.
4. Follow AEO structure throughout (see below).
5. End with a short list of anything that couldn't be satisfied.

## Rules that are easy to break here

**Never invent data to fill a format.** If the content has no number, there is
no stat block. If it has no sequence, there is no flowchart. A layout skill is
exactly where a plausible-looking "73% of buyers…" gets fabricated to fill a
slot that looked good in the plan. Every figure on the page must trace to the
content supplied; if a section would benefit from data the content lacks,
say so in the brief as a gap for the user to fill.

**Don't format everything.** Prose is a legitimate format. A page where every
section is a visual reads as noise, and a claim forced into a chart becomes
less clear, not more. Aim for rhythm — visuals where the content has shape,
prose where it's argument.

**Charts: build from the chart tokens, and flag them.** There is no chart
component. `--equinet-color-chart-blue-light`, `-mid` and `-dark` are the
sanctioned palette, for charts only, never UI. Prefer bars over pies — see
`references/content-to-format.md`.

**Say so rather than approximate.** A near-miss illustration, an invented
number or a fabricated icon is worse than an honest gap, because it looks
finished and hides the problem.

## AEO structure

Pages are built to be extracted and cited by answer engines as well as read:

- H2s phrased the way someone would actually ask the question.
- Each section opens with a direct, self-contained answer in one or two
  sentences, then expands.
- Terms defined on first use — not three sections earlier.
- Tables and lists only where content is genuinely enumerable; they extract
  cleanly, but a forced table is worse than prose.
- Entities named explicitly rather than "it" or "this approach".
- One idea per section, so any chunk can stand alone as an answer.

An FAQ section serves AEO directly — it's the one format that is literally
question-and-answer. See `references/hubspot-elements.md`.
