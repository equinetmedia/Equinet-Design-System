
---

## 5. CHANGELOG.md

```markdown
# Changelog

This repo has no live connection to the Equinet Module Development Claude.ai
Project. Every entry below represents a manual reconciliation pass — someone
asked Claude, in that Project, to fold new development work into
`tokens.css` / `README.md`, then committed the result here.

## 2026-09-23 — Full Figma variable reconciliation; complete file set rewrite

All five design system files rewritten as a unified set, reconciled against the
canonical Figma file (`A3XMvWX47Tf1191jomeEmH`) and all four variable
collections (brand, alias, mapped, responsive).

**tokens.css changes:**
- **Primitive scale added.** The full `brand/scale/*` collection (0–1600) is now
  tokenised as `--equinet-scale-*`, and spacing/border tokens alias into it via
  `var()` rather than repeating literals.
- **Colour ramps added.** Six complete ramps from Figma variables: blue
  (50–950), amber (100–bright), teal (50–950), night (100–default), charade
  (50–500), surface (100–400). Semantic UI colour tokens now alias these ramps
  via `var()` — each hex defined once.
- **CTA, neutral, and mapped aliases added.** From the `alias` and `mapped`
  Figma collections: `--equinet-cta-*`, `--equinet-neutral-*`,
  `--equinet-text-action`, `--equinet-surface-page`, `--equinet-icon-primary`.
- **Border system added.** `--equinet-border-width-*` (none/sm/md/lg) and
  `--equinet-border-radius-*` (none/sm/md/lg) from Figma `alias` collection.
- **Canonical Figma type scale added.** h1–h6 and body sm/md/lg font sizes,
  line heights, paragraph spacing, and text transforms — all from the
  `responsive` collection and local text styles. Module overrides (display 60px,
  h2 36px, etc.) kept separately with discrepancy notes.
- **Foundation paint styles tokenised.** `--equinet-foundation-blue-*` (10
  stops) from Figma local paint styles — interaction-state palette for UI
  chrome, separate from the variable ramp.
- **Additional effect style shadows.** `--equinet-shadow-node-drop` and
  `--equinet-shadow-circle-bg` from Figma effect styles.
- **Button link font size.** `--equinet-fontsize-btn-link` (20px) from Figma
  text style `body/button-md-link`.

**tokens.json changes:**
- Bumped to version 2.
- Added `figmaFileKey` and `variableCollections` metadata.
- Added `primitives` block with all six colour ramps.
- Added `alias` field on colour tokens mapping to Figma variable paths.
- Added `aliases` block documenting CTA, neutral, and mapped collections.
- Added `foundation` block for paint style interaction states.
- Added `figmaFontMapping` documenting actual Figma text style fonts.
- Added full heading type styles with `textTransform` and `letterSpacing`.
- Added `body-lg`, `body-sm`, `button-link` text styles.
- Added `paragraphSpacing` block.
- Added `border` block (widths and radii with scale references).
- Added `breakpoints` block.
- Added `figmaResponsiveMapping` for spacing name differences.
- Added additional shadow tokens (blue-label, node-drop, circle-bg).
- Added additional motion tokens (duration, ease, ui variants).

**README.md changes:**
- Added table of contents, governance, colour ramps, semantic aliases,
  foundation paint styles, Figma text style mapping, responsive type note,
  spacing mapping, border system, pictographs, technical diagrams, commercial
  systems, patterns library, Figma file structure, extended open decisions.

**HANDOFF.md changes:**
- Updated manifest, added Figma data-issue warnings, updated provenance.

## 2026-09-23 — Second marketing batch (9 files); two decisions resolved

- **`#FFE6DB` folded into `equinet-color-orange--pale`.**
- **New token: `equinet-color-diagram-line--neutral` (`#6C7074`).**
- Correction: `#F3F2F2` found in ABM file, joins cluster with `#ECEAEA`, `#F3F3F4`.
- Eight of nine files have real `<text>` elements declaring `font-family="Myriad Pro"`.

## 2026-09-23 — Diagram greyscale sanctioned from a seven-file marketing batch

Three new tokens: `equinet-color-diagram-line` (`#68728F`), `-tint`
(`#D6D8E1`), `-tint--pale` (`#ECEDF2`).

## 2026-09-23 — Font stack corrected; a data-viz exception added

Myriad Pro removed. `equinet-color-chart-blue-*` (three stops) sanctioned.

## 2026-09-22 — Brand wordmark added

`wordmark-light.svg` and `wordmark-dark.svg`.

## 2026-09-22 — Icon inventory started, no real assets yet

## 2026-09-22 — Reconciled against real module CSS

Card hover canonical, reduced motion both halves, shadow transposition resolved.

## 2026-09-22 — Repo created and pushed to GitHub

Private, HTTPS only.

## 2026-09-22 — Initial commit

<!--
Next entry template:

## YYYY-MM-DD — <short description>

What changed, which module or directive drove it, and which open item (if
any) this resolves. Note new open items the same way.
-->
