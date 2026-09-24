# Module comps

Figma exports of full HubSpot modules — the design source of record the
modules were built from. Three files, added 2026-09-23.

**These are not page artwork.** Don't place one in a layout, and don't treat
one as an illustration; each is a picture of an entire rendered module,
including its own heading, body copy and buttons. Dropping one into a page
would embed a fake module as a flat image. They're here to be *compared
against*, not used.

| File | Canvas | Module | Text runs |
| --- | --- | --- | --- |
| `module__2-column-hero-banner.svg` | 1920 × 714 | `2-column-hero-banner` | 9 |
| `module__2-column-comparison.svg` | 1920 × 612 | `2-column-comparison` | 7 |
| `module__5_column_block_methodology.svg` | 1920 × 805 | `5_column_block_process` / methodology | 21 |
| `module__sector-three-column-case-study.svg` | 1920 × 1276 | `sector-three-column-case-study` | 23 |

## What they're for

- **Parity QA.** The delivery gate compares a live screenshot against the
  Figma PNG; these are that reference, in vector form.
- **Provenance.** When a token's comment cites a module coordinate — the
  `2-column-hero-banner` entries in `tokens.css` date to 2026-08-07 — this is
  the artwork those measurements came from.
- **Settling disputes.** Where a shipped module and a token disagree, the comp
  is the tiebreaker, the way the button exports settled the 8px/16px arrow.

## Live text — re-exported 2026-09-24

The first versions filed here had all text outlined to paths, which made
typography unreadable. **They were replaced on 2026-09-24 with exports
carrying live `<text>` elements**, and a fourth comp
(`module__2-column-comparison.svg`, 1920 × 612) was added. Between them they
declare 60 text runs with real family, size, weight and letter-spacing.

That turned several long-open questions from unanswerable into settled —
see `CHANGELOG.md` for the full list. The short version:

| Question | Resolution |
| --- | --- |
| Heading weight: 800 or 900? | **Both — it's family-dependent.** Open Sans headings are 800, Myriad Pro headings are 900. Never was drift. |
| Eyebrow tracking | `0.2em` at 12px, `0.1em` at 16px — both now tokens |
| Display tracking | `-0.05em` at 56px, `-0.07em` at 60px |
| h2 size | Figma variable says 48px; every comp applies 36px. Kept both, as two tokens |

The one thing still not readable: these comps use **Myriad Pro**, the licensed
Adobe face that can't render in a browser. The live text confirms it as the
design-level intent — but the substitution to Source Sans 3 in `tokens.css`
stands, for the same reason as always.

## Colour audit

Every colour resolves to an existing token except one. Confirmed present:
`#242630`, `#3B3F51`, `#E06730`, `#F5844D`, `#FCE9E0`, `#00426C`, `#002E4A`,
`#5688BA`, `#68728F`, `#B1B7C8`, `#E6E6E6` (`--equinet-color-surface-400`).

`module__5_column_block_methodology` confirms the module background gradient
documented in `tokens.css`: a radial `white` → `#F6F5F5`, start and end stops
matching `--equinet-color-surface` and `--equinet-color-surface--alt`.

### Three values worth noting

**`#292D32` — new, not a token.** Eight occurrences in
`module__2-column-hero-banner`, all as `stroke` on fine line-art paths
(0.69–1.38px). Luminance 0.0258, sitting between `color-heading` (0.0197) and
`color-body` (0.0508). It's the line work of an illustration embedded in the
hero's right-hand column, not UI chrome. Single file, so it's logged rather
than promoted — the same standard that held `#8790A9` back until it appeared
across five files.

**`#F1F1F1` and `#F3F2F2` appear here too**, which complicates their existing
scoping. Both sit in the hero's right-hand region: `#F1F1F1` as a large arc at
80% opacity, `#F3F2F2` as strokes on three small rounded rects. That still
reads as embedded illustration rather than page chrome — but `#F1F1F1` is
currently tokenised as `--equinet-color-diagram-surface` and described as
"marketing illustration only, not UI", and appearing inside a module comp
puts pressure on that wording even if the usage is technically still
illustrative. `#F3F2F2` remains one of the unresolved near-whites and has now
been seen in two contexts rather than one.

Neither is changed here. Flagged so the next person deciding the near-white
cluster has the full picture.
