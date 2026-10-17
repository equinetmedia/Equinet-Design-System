---
id: handoff
status: current
read_when: >-
  Importing this system into Claude Design, or working out how a change gets
  from a Claude session into this repo and back out.
depends_on: README.md, tokens.css, assets/manifest.json
verified: 2026-10-13
---

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
| `tokens.json` | **Generated** from `tokens.css` by `tools/build-tokens-json.py`. Claude Design's own Design System schema — a top-level object with `color`, `type`, `spacing`, `duration`, `radius`, `size` and `shadow` families, each holding `{name, value, usage}` entries. Never hand-edit it | If the import flow asks for this shape instead of CSS. Read `tools/tokens-unrepresentable.md` for what the schema can't carry |
| `README.md` | Opens with a rules digest — the binding rules in one scannable table — then the full brand book: consumption pattern, colour, type, spacing, breakpoints, motion, buttons, cards, backgrounds/parallax, editor-controlled styling, icons, accessibility, the engineering contract, component inventory, and open decisions | Read first — everything else assumes it |
| `CHANGELOG.md` | Dated log of every reconciliation pass, what it resolved, and what it newly surfaced | Tracing when and why a value or decision changed |
| `skills/equinet-layout/` | A two-phase skill: content → approved layout brief → build. Maps content shapes to formats, assets and HubSpot elements | Planning any page from content; packaged as `equinet-layout.skill` for Claude chat |
| `PROMPT-TEMPLATE.md` | A ready prompt for generating pages in Claude Design, with the reasoning behind each constraint | Starting a new page; adapting the wording for a different brief |
| `components/bundle.css` | The pure-CSS component layer — three button variants with every state, plus `.eq-stagger` alternating content rows sized to the illustration ratios | The actual CSS; loads after `tokens.css` |
| `assets/icons/` | Four groups — root control icons, `nodes/`, `service-tiles/`, `service-marks/` — plus `ICON-REFERENCE.md` — the measured house style and how to match a Lucide or Phosphor substitute to it | Inlining an icon into a module |
| `assets/buttons/` | The ten Figma button exports, kept as the measurement source of record | Verifying a geometry claim against its origin |
| `assets/brand/` | Wordmark, light and dark variants | Any use of the logo |
| `components/motion.js` | Entrance motion for inline annotated graphics; pairs with "GRAPHIC MOTION" in `bundle.css` | Animating any graphic — no per-file code |
| `tests/components-test.py` | 19 browser checks for `.eq-card`, `.eq-faq` and `[data-reveal]` | Re-verifying after changing components |
| `tests/motion-test.py` | 14 browser checks for the motion layer | Re-verifying after changing motion code or graphics |
| `assets/illustrations/heroes/` | Four service-page hero compositions; card labels baked in | Page heroes — read the HubSpot-logo note first |
| `assets/charts/` | Seven sourced data charts, plus `data.json` holding every figure with source and verification status | Any page using statistics; rebuild charts live from `data.json` |
| `tools/build-manifest.py` | Regenerates `assets/manifest.json` from the files | After adding, renaming or editing any asset |
| `tools/build-tokens-json.py` | Regenerates `tokens.json` and `tools/tokens-unrepresentable.md` from `tokens.css` | After any change to `tokens.css`. `--check` fails if the JSON is stale |
| `tools/check-docs.py` | Eleven consistency checks across the prose, the tokens and the manifest | Before every commit; exits non-zero so it wires into a hook or an Action |
| `METHODOLOGY.md` | The reasoning behind the rules — scanning and layout (NN/g), affordance and targets (IxDF), the conversion path (Baymard), plus where the evidence is weaker than it sounds | When a rule needs applying to a case it doesn't cover, or looks wrong |
| `TYPE-ROLES.md` | The role contract — which token sizes what, why heading level and size are independent, the h2 ruling, the spacing ladder, known gaps | Before sizing any text |
| `tests/progress-test.py` | Reading-progress emphasis for unlinked content — reached is permanent, nothing hidden behind scrolling, no false affordance | After touching `[data-progress]` or the reveal logic |
| `tools/vendor-lucide.py` | Re-vendors the whole Lucide library into `assets/icons/lucide/` unmodified and regenerates its index | When Lucide ships a version worth taking, or a build reports a glyph it could not find |
| `tools/check-deployed-tokens.py` | Diffs the `/modules/tokens.css` HubSpot serves against this repo's `tokens.css` — conflicts, tokens missing from the deployment, tokens promoted in a module build that never came back | Before deploying `tokens.css`, and after any module build that promotes a token |
| `tools/check-built-page.py` | Audits a finished page: hardcoded px/shadow values where a token exists, whether `motion.js` is actually in the file, `data-asset` coverage, real `viewBox`, template bindings, FAQ/JSON-LD match. Unwraps a Claude Design bundle first | On every page a build hands back, before accepting it |
| `assets/manifest.json` | Machine-readable record of every asset — background, roles, palette→tokens, subject. Generated, so it is always the live count | Choosing and reworking assets programmatically |
| `assets/REWORKING.md` | How to adapt an asset to the data, by `data-role` | Editing a graphic to match content |
| `assets/RENAMES.md` | Old → new filename map from the 2026-09-26 rename | Resolving older references |
| `assets/comps/` | Five 1920px Figma comps — four complete modules plus the global navigation | Layout blueprints and parity QA; rebuild with live components, never embed as artwork |
| `assets/marketing/` | Seventeen infographics, with a per-file audit index | Provenance for the chart and diagram token categories |
| `assets/illustrations/` | Standalone graphics in six subgroups — `pictonodes/`, `scenes/`, `sectors/`, `systems/`, `flows/`, `heroes/` — plus `INDEX.md` — the per-file subject index an agent reads to choose artwork | Standalone graphics — not icons; one file has an unguarded infinite animation, see that folder's README |

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
- ~~Heading weight inconsistent~~ **Resolved 2026-09-24:** weight is
  family-dependent. Open Sans headings are 800, Myriad Pro / Source Sans 3
  headings are 900. The two modules were using different families, not
  drifting. (`sector-three-column-case-study` hardcoding
  `font-family: "Open Sans" !important` alongside weight 900 is still worth
  a look — that pairing contradicts the rule.)
- **Playfair Display** is used in two modules now but isn't in `tokens.css` —
  worth promoting to a system font if it's staying.
- ~~No `letterspacing` token category~~ **Resolved 2026-09-24:** six tokens
  promoted from live-text comps — kicker `0.2em` / `0.1em`, display
  `-0.05em` / `-0.07em`, h2 `-0.03em`. One conflict remains: both comps set a
  36px/900 section heading, but one tracks it `-0.03em` and the other `0em`.

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
