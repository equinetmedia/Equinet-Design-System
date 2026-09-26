# Brief template

Use this structure. The brief is what the user approves, so it must be
scannable and specific enough to build from without re-reading the content.
**Every section has a Visual entry** — "none" is not a valid answer.

```markdown
# Layout brief — {page title}

**Goal:** {the one thing the page should make the reader do}
**Primary CTA:** {action} → {HubSpot element or `.btn-primary` destination}
**Layout basis:** {which comp(s) the page structure borrows from}

## Sections

### 1. {Section name}
- **Content shape:** {what the content is — e.g. "four ordered steps"}
- **Format:** {e.g. horizontal step flow}
- **Visual:** {one of —
    placed: `{file}` from INDEX.md (subject match), cropped/scaled as needed
    composed: {recipe from visual-kit.md} built from {primitives}, icons: lucide/{…}
    comp layout: `{comp}` structure rebuilt with this content}
- **Icons:** {Equinet icon or lucide/{name} per item, where they aid scanning}
- **Built with:** {existing module/component, or NEW — {what}}
- **Reader's next step:** {or "continues"}
- **AEO:** {the question this section answers}

## New components this page needs
{Charts, stat rows, tables, flowcharts, FAQs, composed graphics — listed so
the best can be promoted into the design system.}

## Data gaps
{Figures a section would benefit from but the content doesn't supply. These
sections still get a visual — a composed graphic or icon treatment — just not
a stat block with an invented number.}
```

## A good section entry

```markdown
### 3. How the process works
- **Content shape:** four ordered steps, same path for every reader
- **Format:** horizontal step flow
- **Visual:** composed — step flow (from `flows/`): four cards, connectors
  with chevrons, nodes holding lucide/search, lucide/layers, lucide/pen-line,
  lucide/rocket; orange accent on the final card
- **Icons:** as above
- **Built with:** NEW composed graphic on `.eq-stagger` full-width row
- **Reader's next step:** continues to proof
- **AEO:** "How does the process work?"
```

## When the subject matches no illustration

This is common, and the answer is to compose — not to skip:

```markdown
### 4. Why engagement algorithms hold attention
- **Content shape:** a cycle — prompt → reward → return → prompt
- **Format:** feedback loop
- **Visual:** composed — feedback loop (from
  `systems/commercial-insight-and-feedback-loops`): four nodes on a circle,
  directional connectors, lucide/bell, lucide/sparkles, lucide/repeat,
  lucide/hourglass; pale panel ground
- **Icons:** as above
- **Built with:** NEW composed graphic
- **AEO:** "How do recommendation engines keep people engaged?"
```

No illustration covers that subject, and the section still gets a full
Equinet infographic, built from Equinet parts.

## A real data gap

```markdown
## Data gaps
- Section 2 would suit a stat row, but the content gives no figures. It gets
  an icon grid of the three claims instead. Supply three comparable figures
  with sources to upgrade it to stats.
```
