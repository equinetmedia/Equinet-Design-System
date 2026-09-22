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

## Why this isn't already in Claude Design

This system was built and rebuilt as a **claude.ai Artifact** (the Design
System artifact type), not through Claude Design's own import flow. Those are
two separate registries with no automatic bridge between them. Getting this
content live in Claude Design means running it through Claude Design's own
setup — a GitHub repo import, a design-file import, or a raw upload of the
files above — which on some plans requires the Claude Design Admin role.

## Before importing: known open items

These are unresolved, not oversights. Whoever imports this should decide them
rather than have Claude Design silently pick a side:

- **Card hover**: two treatments currently ship — a `translateY(-6px)` lift
  and a border/shadow "elevate." Neither is yet the system default.
- **Reduced motion**: the written rule says wrap motion in
  `prefers-reduced-motion: no-preference`; every shipped module instead
  declares motion unconditionally and withdraws it under `reduce`. Pick one.
- **Card shadow blur**: 5px in `tokens.css`, 10px in a shipped module. Needs
  checking against the Figma filter.
- **Primary button shadow tokens** may be transposed between the default and
  dark-hover states — both shipped modules use them the other way round.
- **Playfair Display** is used in two modules now but isn't in `tokens.css` —
  worth promoting to a system font if it's staying.
- **Primary button contrast**: white on the orange fills fails AA at 16px
  (3.4:1 default, 2.5:1 light hover, 4.4:1 dark hover). The client accepted
  this exception on 2026-09-21 — it's documented in `README.md`, not silently
  fixed, and it should stay a deliberate exception rather than spread to other
  components.

## Provenance

Built from: the six standing directives (parallax, padding, background,
button mapping, button interactive animation, button SVG hover theming),
`/modules/tokens.css`, the CSS of `cim-methodology`, `plain_hero_banner` and
`cagr-four-column`, and the fourteen-module build history recorded in the
Equinet Module Development project.
