# Brief template

Use this structure exactly. The brief is what the user approves, so it must be
readable at a glance and specific enough to build from without re-reading the
content.

```markdown
# Layout brief — {page title}

**Goal:** {the one thing the page should make the reader do}
**Primary CTA:** {action} → {HubSpot element or `.btn-primary` destination}
**Design system:** {README supplied: yes / no — if no, asset choices unverified}

## Sections

### 1. {Section name}
- **Content shape:** {what the content actually is — e.g. "three comparable figures"}
- **Format:** {e.g. stat row}
- **Built with:** {existing module / component, or "NEW — {what}"}
- **Asset:** {file from INDEX.md, icon, or "none — no subject match"}
- **Reader's next step:** {or "none — continues to next section"}
- **AEO:** {question-shaped heading this section answers}

### 2. …

## New components this page needs
{Anything with no existing component — chart, stat row, table, flowchart,
FAQ. Listed so they can be promoted into the design system.}

## Gaps
{Anything the content doesn't supply that a section would need — data,
a quote, a client name. Never filled in by assumption.}

## Rhythm check
{One line: does density alternate, or is it visual after visual?}
```

## Example of a good section entry

```markdown
### 3. How the process works
- **Content shape:** four ordered steps, same path for every reader
- **Format:** process sequence (not a flowchart — no branching)
- **Built with:** `5_column_block_process`, reduced to four columns
- **Asset:** `flows/smarter-content-operations-for-manufacturing-growth` —
  subject match on content operations
- **Reader's next step:** none — continues to proof
- **AEO:** "How does content operations work for manufacturers?"
```

## Example of an honest gap

```markdown
## Gaps
- Section 2 would be stronger as a stat row, but the content gives no figures.
  Supply three comparable numbers with sources, or it stays as prose.
- No illustration matches "digital addiction" — INDEX.md has no subject
  coverage. Section 4 ships without one.
```
