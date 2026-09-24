# Equinet design system — export for Claude Design import

Prepared 2026-09-22. This is a clean export of the design system rebuilt in
the Equinet Module Development project, for import into Claude Design's
**native** design system — most likely updating the existing "Equinet Media
Design System" (org default), rather than adding a new one. See the note
below on why that distinction matters.

## How this stays in sync

Nothing here updates automatically. Every link in this chain is a deliberate,
manual step — this section is the actual recipe, confirmed working as of
2026-09-22.

1. New development work happens in the Equinet Module Development Claude.ai
   Project — a module ships, a token gets promoted, a directive gets
   resolved, an open decision gets settled.
2. In that Project, ask Claude to reconcile the change into `tokens.css` and
   `README.md`, the same way this system was built and rebuilt.
3. Drop the updated files into your local clone of this repo and push:

   ```bash
   git add -A
   git commit -m "describe what changed"
   git push
   ```

   Use the HTTPS remote — `https://github.com/equinetmedia/Equinet-Design-System.git`
   — not SSH. SSH fails on this machine with `Permission denied (publickey)`;
   no key is registered. Push through an editor's signed-in GitHub session
   (VS Code's Source Control panel worked) or a scoped personal access token.
   Ordinary pushes shouldn't need `--force` — that was only required once, to
   overwrite the repo's original unrelated history.
4. Add an entry to `CHANGELOG.md`, following the template at its bottom, so
   drift between this repo and the live doctrine stays traceable.
5. If a native Claude Design design system is linked to this repo, re-run its
   GitHub import to refresh it, or run `/design-sync` from Claude Code in a
   local clone to pull the update into the canvas.

**Why step 2 can't be skipped.** This repo is private by decision — see
`CHANGELOG.md`, 2026-09-22 — so nothing can fetch its current state directly
in a future session. The current file has to be handed back into the Project
chat each time, not pulled automatically.

## What's in this folder

| File | What it is | Use it for |
| --- | --- | --- |
| `tokens.css` | The real, production token file — the original `/modules/tokens.css` with the finalized spacing scale appended (dated 2026-09-22) | A codebase-style or raw-file import; the closest thing to ground truth |
| `tokens.json` | The same values, reshaped into the `{"tokens":[{"name","value","usage"}]}` format Claude Design's own Design System schema reads | If the import flow asks for this shape instead of CSS |
| `README.md` | The full brand book: consumption pattern, colour, type, spacing, breakpoints, motion, buttons, cards, backgrounds/parallax, editor-controlled styling, icons, accessibility, the engineering contract, component inventory, and open decisions | Read first — everything else assumes it |
| `CHANGELOG.md` | Dated log of every reconciliation pass, what it resolved, and what it newly surfaced | Tracing when and why a value or decision changed |
| `components/bundle.css` | The pure-CSS component layer — all three button variants, every state, token-driven with measured fallbacks | The actual CSS; loads after `tokens.css` |
| `assets/icons/` | Three real icons (`arrow-chevron`, `arrow-solid`, `play-circle`) extracted from the Figma button exports, plus an inventory of what's still missing | Inlining an icon into a module |
| `assets/buttons/` | The ten Figma button exports, kept as the measurement source of record | Verifying a geometry claim against its origin |
| `assets/brand/` | Wordmark, light and dark variants | Any use of the logo |
| `assets/marketing/` | Seventeen infographics, with a per-file audit index | Provenance for the chart and diagram token categories |

## Why this isn't already in Claude Design

This system was built and rebuilt as a **claude.ai Artifact** (the Design
System artifact type), not through Claude Design's own import flow. Those are
two separate registries with no automatic bridge between them. Getting this
content live in Claude Design means running it through Claude Design's own
setup — a GitHub repo import, a design-file import, or a raw upload of the
files above — which on some plans requires the Claude Design Admin role.

## Before importing: known open items

Updated 2026-09-22, after a reconciliation pass against `cagr-four-column`
and `sector-three-column-case-study` resolved four of the items originally
listed here. What's left is genuinely open — whoever imports this should
decide these rather than have Claude Design silently pick a side:

- **Icon centralization is partly unblocked.** Three icons now exist as real
  files (`assets/icons/`); `close`, `checkmark` and `external-link` still
  have no geometry — no `module.html` carrying them has been shared.
- **Two button class families coexist.** `.btn-primary` throughout, but
  `sector-three-column-case-study` also carries `.button_primary_large` and
  `.button_textual` as parallel selectors on the same rules — sanctioned
  aliases, or drift to retire?
- **Heading weight and family are inconsistent.** `cagr-four-column` uses the
  `--equinet-fontweight-display` token (800) via `--equinet-font-heading`.
  `sector-three-column-case-study` hardcodes `font-weight: 900 !important`
  and `font-family: "Open Sans" !important` directly, bypassing both tokens.
- **Playfair Display** is used in two modules now but isn't in `tokens.css` —
  worth promoting to a system font if it's staying.
- **A `letterspacing` token category doesn't exist.** Every module hardcodes
  tracking values (`0.1em`, `0.2em`, `-0.05em`) inline.

- **`5-column-block-process.css`, as uploaded, is a duplicate of
  `cim-methodology`'s CSS**, not the real five-column module. Its actual
  styling has never been provided under any filename.
- **`new_header_module_2026_v3.css` doesn't conform to this system** — an
  off-brand green palette, its own `:root` block, FontAwesome glyphs, no
  `--equinet-*` usage. Excluded from this system rather than treated as a
  fifteenth module; worth confirming whether it's meant to be on-brand.

**Resolved in the same pass, no longer open:** card hover pattern (a
`translateY(-6px)` lift is canonical; `cim-methodology`'s border/shadow
elevate is the outlier), reduced-motion gating (needs both a `no-preference`
wrapper and a `reduce` fallback — `cim-methodology` and `plain_hero_banner`
are missing the first half), card shadow blur (5px is correct; `10px` in
`cim-methodology` is a hardcoded drift), and the primary-button shadow
"transposition" (not a token problem — two modules hardcode a literal instead
of referencing the variable). Full detail in `README.md`.

**Still standing from the original commit:**
- **Primary button contrast**: white on the orange fills fails AA at 16px
  (3.4:1 default, 2.5:1 light hover, 4.4:1 dark hover). The client accepted
  this exception on 2026-09-21 — documented in `README.md`, not silently
  fixed, and it should stay a deliberate exception rather than spread to
  other components.

## Provenance

Built from: the six standing directives (parallax, padding, background,
button mapping, button interactive animation, button SVG hover theming),
`/modules/tokens.css`, and the fourteen-module build history recorded in the
Equinet Module Development project. CSS verified directly, as of 2026-09-22:
`cim-methodology`, `plain_hero_banner`, `cagr-four-column`,
`sector-three-column-case-study`, `pencil_testimonial`, `workshop_one_column`,
and `2_column_intelligence_engine_steps` (confirmed intentionally empty). The
remaining seven modules are named from build history only — see `README.md`,
"Component inventory," for the full breakdown including two file-integrity
problems that aren't real modules at all.
