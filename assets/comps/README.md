# Module comps

Figma exports of full HubSpot modules — the design source of record the
modules were built from. Three files, added 2026-09-23.

**Use these as layout blueprints.** Each is a real, shipped Equinet module
composition — reproduce its structure, spacing and hierarchy with live
components and new content. They're also the reference for parity QA. The one
thing not to do is embed a comp as a flat image: each pictures a whole
rendered module, its own heading and buttons included, so it must be rebuilt,
not pasted.

| File | Canvas | Module | Text runs |
| --- | --- | --- | --- |
| `module__2-column-hero-banner.svg` | 1920 × 714 | `2-column-hero-banner` | 9 |
| `module__2-column-comparison.svg` | 1920 × 612 | `2-column-comparison` | 7 |
| `module__5_column_block_methodology.svg` | 1920 × 805 | `5_column_block_process` / methodology | 21 |
| `module__sector-three-column-case-study.svg` | 1920 × 1276 | `sector-three-column-case-study` | 23 |
| `Global-Navigation.svg` | 1920 × 100 | global header / navigation | 0 — outlined |

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

## `Global-Navigation.svg` — the site header

Added 2026-10-02. The global navigation bar: a full-width 1920 × 100 band in
`#242630`, carrying a centred **1280px content container** in `#242530`, with
the Equinet Media wordmark in white, five two-line service links, a 1px white
vertical divider, an About dropdown, and an orange CTA (`#E06730`). Every
colour is a token. Kept under its Figma name, like the other comps.

Measured from the file:

| Element | Value |
| --- | --- |
| Band | 1920 × 100, `#242630` (`--equinet-color-heading`) |
| Content container | 1280 wide, centred, `#242530` (`--equinet-color-text`) |
| Divider | 1 × 50, white |
| CTA | 148 × 50, `rx 6`, `#E06730` |

**Two findings from those numbers.** The band and its container use the two
near-identical greys *side by side* — `#242630` and `#242530`, one unit apart
and indistinguishable on screen. That's the clearest evidence yet on the open
question of whether `--equinet-color-heading` and `--equinet-color-text`
should merge. And the CTA is a **third button size**: 50px tall with a 6px
radius, unlike the primary (56px, `rx 7`) and navigation (54px, `rx 7`)
buttons. It isn't tokenised; worth deciding whether it's a header-specific
variant or drift.

Its text is outlined, so the labels are recorded here as text:

| Position | Label | Treatment |
| --- | --- | --- |
| Left | Equinet Media | Wordmark (`assets/brand/wordmark-light.svg`) |
| Nav 1 | Commercial / **Positioning** | Two lines, second line bold |
| Nav 2 | Commercial / **Systems** | Two lines, second line bold |
| Nav 3 | Commercial Data / **& Rev Ops** | Two lines, second line bold |
| Nav 4 | Account Based / **Marketing** | Two lines, second line bold |
| Nav 5 | Website / **Design** | Two lines, second line bold |
| — | Vertical divider | |
| Nav 6 | **About** ▾ | Single line, dropdown chevron |
| CTA | Commercial / **Diagnostic** | `.btn-primary`, two-line label |

**This is the reference an earlier header module should have followed.**
`new_header_module_2026_v3.css` was excluded from the system for an off-brand
green palette, its own `:root` block and FontAwesome glyphs. Its two-line
"top / bottom" label structure matches this comp exactly — so it was built for
this design, with the wrong colours — and its `.container-1280` matches this
comp's 1280px container exactly. Rebuild the header against this comp: dark
band, 1280px container, white labels, orange CTA, Lucide for the dropdown
chevron.

The navigation also maps the site's service pages, which is what
`assets/illustrations/heroes/` provides artwork for.
