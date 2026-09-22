# Changelog

This repo has no live connection to the Equinet Module Development Claude.ai
Project. Every entry below represents a manual reconciliation pass — someone
asked Claude, in that Project, to fold new development work into
`tokens.css` / `README.md`, then committed the result here.

## 2026-09-22 — Initial commit

Rebuilt in full from:

- Six standing directives: parallax, padding customization, background
  customization, primary button styling & mapping, primary button interactive
  animation, primary button SVG hover theming.
- `/modules/tokens.css`, the real production token file.
- The CSS of three shipped modules: `cim-methodology`, `plain_hero_banner`,
  `cagr-four-column`.
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
