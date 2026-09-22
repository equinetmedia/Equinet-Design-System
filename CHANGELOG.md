# Changelog

This repo has no live connection to the Equinet Module Development Claude.ai
Project. Every entry below represents a manual reconciliation pass — someone
asked Claude, in that Project, to fold new development work into
`tokens.css` / `README.md`, then committed the result here.

## 2026-09-22 — Icon inventory started, no real assets yet

Added `assets/icons/README.md`: an inventory of every icon referenced across
module CSS (arrow, checkmark, close, external-link, play), each with its
known size and colour behaviour. No actual SVG markup exists yet — CSS only
describes how an icon behaves, not its geometry, and no `module.html` has
been shared in this project to source real paths from.

Surfaced a real design decision in the process: the "arrow" used across CTAs
is not one shape. At least three distinct geometries exist (~15×13 filled,
14–16px stroke variants with different cap styles, a 20px version), on top
of the already-open 8px/16px hover-travel disagreement. Centralizing it
requires choosing a canonical arrow first — this can't be resolved from CSS,
it needs a decision the same way card-hover and reduced-motion did.

## 2026-09-22 — Reconciled against real module CSS, not secondhand values

Nine files uploaded; two were integrity problems rather than new modules —
see `README.md`, "Component inventory," for both. Of the rest, `cagr-four-column`
and `sector-three-column-case-study` were read in full for the first time
(previously only quoted in `tokens.css` comments), and they resolved three
questions that had been sitting open since the first rebuild:

- Card hover is a lift (`translateY(-6px)`), confirmed canonical by
  `cagr-four-column`'s own code comment. `cim-methodology`'s elevate is the
  outlier.
- Reduced motion needs both a `no-preference` wrapper and a `reduce`
  fallback. `cim-methodology` and `plain_hero_banner` are missing the first
  half, not using a second valid pattern.
- The "transposed shadow tokens" question wasn't a token problem —
  `cim-methodology` and `plain_hero_banner` hardcode a literal box-shadow
  instead of referencing the CSS variable. Fix those modules, not the token.

New open items surfaced by the same two files: an arrow-travel distance
disagreement (8px vs. 16px), two coexisting button class families
(`.btn-primary` vs. `.button_primary_large` / `.button_textual`), and a
heading weight/family inconsistency (`800` via token vs. hardcoded `900
!important`). Also promoted: `--equinet-motion-duration--slow` (0.6s) and
`--equinet-motion-duration--wipe` (0.45s), both already in use as `var()`
fallbacks before being named. A `letterspacing` token category is flagged as
missing entirely — every module hardcodes tracking values inline.

## 2026-09-22 — Repo created and pushed to GitHub

- Pushed to `equinetmedia/Equinet-Design-System` (private), replacing a
  pre-existing placeholder `getting-started` file via a one-time force push.
  No further `--force` should be needed for ordinary updates — that was only
  to overwrite unrelated history on first push.
- **Working method: HTTPS, not SSH.** SSH failed with `Permission denied
  (publickey)` — no SSH key is registered on this machine for GitHub. Use the
  `https://github.com/equinetmedia/Equinet-Design-System.git` remote, either
  through an editor's own signed-in GitHub session or a scoped personal
  access token. Don't leave a token embedded in the remote URL or shell
  history longer than the push itself.
- **Decision: repo stays private.** It documents client-specific calls —
  the accepted button-contrast exception in particular — that are reasonable
  to make privately but shouldn't be a public record. Consequence: future
  reconciliation passes need the current `tokens.css` pasted or uploaded back
  into the Equinet Module Development project; it can't be fetched directly
  from a private repo.
- Claude Design GitHub-import setup steps were provided for linking this repo
  to a native Claude Design design system; not yet confirmed complete.

## 2026-09-22 — Initial commit

Rebuilt in full from:

- Six standing directives: parallax, padding customization, background
  customization, primary button styling & mapping, primary button interactive
  animation, primary button SVG hover theming.
- `/modules/tokens.css`, the real production token file.
- The CSS of two shipped modules — the only two with real CSS available at
  this point: `cim-methodology`, `plain_hero_banner` — plus confirmation that
  `2_column_intelligence_engine_steps` is intentionally empty.
- The fourteen-module build history recorded in project memory.
- The anti-drift colour rule, added after Claude Design introduced
  off-palette purple and teal accents on a categorical infographic.

Open items carried into this commit, unresolved: card hover pattern (lift vs.
elevate), reduced-motion gating pattern, card shadow blur (5px vs. 10px),
possibly-transposed primary-button shadow tokens, Playfair Display's status,
and whether `equinet-color-heading` / `equinet-color-text` should merge. See
`README.md`, "Open decisions."

<!--
Next entry template:

## YYYY-MM-DD — <short description>

What changed, which module or directive drove it, and which open item (if
any) this resolves. Note new open items the same way.
-->
