---
id: maintenance
status: current
read_when: >-
  Deciding what to work on next, onboarding someone, or checking whether a
  claim about the system is true. The state of the build to date, the rulings
  made, how a change actually travels, the gaps that make the system hard to
  maintain, and the open decisions.
depends_on: README.md, CHANGELOG.md, METHODOLOGY.md, TYPE-ROLES.md, HANDOFF.md
verified: 2026-10-22
---

# MAINTENANCE.md

Where the Equinet design system stands on 2026-10-22, how it is kept true, and
what is missing from that.

Every number below was measured from the repository on this date, not
recalled. Where something could not be verified, the last section says so.

---

## 1. State of the system

### Scale

| | |
| --- | --- |
| Tokens in `tokens.css` | 248 (164 expressible in `tokens.json`, 84 documented as not) |
| Assets with a manifest entry | 127, across 10 categories |
| Lucide glyphs vendored | 2,159, deliberately outside the manifest |
| Component classes in `bundle.css` | 93, in 2,231 lines |
| `motion.js` | 483 lines |
| Tools | 6 |
| Test suites | 5, 176 checks, all passing |
| Markdown documents | 27, counting this one |
| Changelog entries | 71, from 2026-09-22 to 2026-10-19 |

### What exists

**Tokens.** `tokens.css` is the single source for every name and value and owns
the only `:root` block. `tokens.json` is generated from it, never hand-edited.
Modules read every value as `var(--equinet-…, measured-fallback)`.

**Components.** Cards (`.eq-card`, `--stacked`, `--spotlight`, `--edge`); the
type scale (`.eq-h1` to `.eq-body`, `.eq-price`, with `--light` and `--sentence`
variants); the eyebrow and the tag; the status check (`.eq-check`,
`.eq-check--none`, `.eq-list--check`); surfaces (`.eq-surface`, four light
positions and a dark one); the FAQ accordion; buttons; and the motion layer:
entrance reveal, tab-set graphics, pointer tracking, reading-progress emphasis.

**Assets.** 36 illustrations, 25 icons of Equinet's own, 17 marketing
style references, 10 button sources, 7 charts, 7 component sources, 11 type
specs, 6 backgrounds, 5 layout comps and 3 brand marks.

**Knowledge.** The README rules digest. `METHODOLOGY.md`, which holds the
reasoning behind the rules, drawn from NN/g, IxDF and Baymard. `TYPE-ROLES.md`,
the rule that heading level and type size are independent. The layout skill,
whose Phase 1 plans, Phase 2 builds and counts, and Phase 3 asks sixteen
review questions before a build is handed back.

**Tooling.**

| Tool | What it does |
| --- | --- |
| `tools/build-manifest.py` | regenerates the asset manifest and maps every colour to a token |
| `tools/build-tokens-json.py` | generates `tokens.json` and lists what the schema cannot carry |
| `tools/check-docs.py` | 11 checks that the prose has not drifted from the files |
| `tools/check-built-page.py` | audits a finished page: hardcoded values, motion wiring, accessible names |
| `tools/check-deployed-tokens.py` | diffs the live `/modules/tokens.css` against this repo |
| `tools/vendor-lucide.py` | re-vendors the Lucide library unmodified |

**Verification.** Five suites run in headless Chromium: components 97,
graphics-interaction 37, pointer 15, motion 14, progress 13. They cover computed
styles against Figma exports, keyboard behaviour, reduced motion and the
no-JavaScript fallback.

### Rulings to date

| Date | Ruling |
| --- | --- |
| 2026-09-21 | White primary-button label accepted at 3.4:1, explicitly not extended to other components |
| 2026-10-13 | Chart palette is navy, orange and teal. The brief is the default; `build direct` is opt-in. Inline CSS and JS first |
| 2026-10-14 | Donuts allowed for a single share. Entrance motion scoped to graphics over 64px. Every multi-part graphic is a tab set |
| 2026-10-16 | Radial surfaces built in CSS. Type scale adopted from Figma specs, resolving h2, body leading and display tracking |
| 2026-10-17 | Eyebrow is orange. The pill takes no icon. Heading level and type size are independent. h2 is 40px, 36px is a sub-heading, 48px retired as a heading size. Progress motion is allowed on unlinked content |
| 2026-10-18 | h1 and h2 are uppercase, with their own caps tracking and leading |
| 2026-10-19 | Price is Source Sans 900 with old-style proportional figures. Card ground is 80% white. Checks follow the ground |

---

## 2. How a change travels today

Written out because every gap in section 3 is a step in this chain that depends
on someone remembering.

1. A Figma export or a design decision arrives in a chat.
2. A chat session edits a working copy and runs the tools and tests by hand.
3. The result is zipped and copied over a local clone, then pushed.
4. The same files are re-uploaded by hand into the Claude Design project.
5. A build is made there, and its audit is run by hand, if at all.
6. A Notion mirror of some documents is updated by hand, by whichever session
   remembers.
7. `tokens.css` is deployed to HubSpot by hand.

Seven steps, no automation, three Claude surfaces plus Notion and HubSpot
each holding a copy of something. Most of the failures on record happened at
step 3, 4, 6 or 7.

---

## 3. Gaps, ranked

**Act now**

| # | Gap | Evidence | Fix |
| --- | --- | --- | --- |
| 1 | Live credentials in plaintext in Notion | The Design System (GitHub) page holds a GitHub personal access token and a third-party API key, and documents a force-push to main with the token embedded in the command | Revoke and reissue both now. Use a credential helper or SSH. Protect main against force-push |
| 2 | The deployed token file is far behind the repo | Against the copy I last saw: 4 value conflicts and 172 tokens missing. Because modules render on fallbacks, no page shows it | Deploy `tokens.css`, then re-run the diff. The 4 conflicts change live rendering, so do it deliberately |
| 3 | Copies of documents drift | The Notion Type Roles page still gave the price as 800 Open Sans; the repo corrected it to 900 Source Sans on 19 Oct. The repo lacked the 18 Oct case ruling the Notion page had. Both reconciled today | One canonical copy, the repo. Notion mirrors carry the commit and date and are never hand-edited |

**Structural: stops recurrence**

| # | Gap | Evidence | Fix |
| --- | --- | --- | --- |
| 4 | Nothing runs unless someone remembers | No CI workflow, pre-commit hook, CODEOWNERS, contributing guide or version file. No git tags | A GitHub Action running the three checks and five suites on every push. Branch protection. Tag each release |
| 5 | The tools are untested | None of the six is referenced by any test. Each has had bugs found by hand, including a normaliser that turned 20px into 20 | A suite of good and bad fixtures for each tool |
| 6 | The handoff to Claude Design is manual and unversioned | Stale or missing files caused repeated failed builds: twice confirmed by inspection (the 2 Oct snapshot; a screenshot showing only the HTML attached), more inferred from the symptom. A build cannot say which version it used | Stamp a version into the shipped files, require the build to echo it, and script the zip |
| 7 | The contract with the module generator is not in the system | `PROMPT.md` v34 expects Claude Design comps to carry `data-field` and `data-module`. Neither string appears anywhere in this repo or its skill. `PROMPT.md` itself is not in this repo | Decide where it lives. Add a comp contract to the skill from its field grammar |
| 8 | The reading load has no budget | The layout skill was trimmed to 12.5 KB on 14 Oct and is 29.5 KB now, in eight days. README is 64 KB. The core files total 278 KB | A byte budget per file, failing in `check-docs.py`. Rationale to the changelog, not the skill |

**Quality of builds**

| # | Gap | Evidence | Fix |
| --- | --- | --- | --- |
| 9 | The builder grades itself | Phase 3 is answered by the same session that built the page. Every serious miss so far (no motion, no icons, inert cards) was invisible to that session | Make the auditor an acceptance gate run outside the builder. Add automated accessibility and screenshot comparison, with the GEO page as the first golden |
| 10 | Typography is tested without the fonts | The sandbox has no network, so web fonts never load; tests confirm declared values, not rendered glyphs. Whether Source Sans 3 exposes old-style figures is unverified. Fonts load from Google's CDN at runtime | Self-host WOFF2 files in the repo. It makes the tests true and removes a runtime dependency |

**Governance**

| # | Gap | Evidence | Fix |
| --- | --- | --- | --- |
| 11 | No decision register | 71 changelog entries hold the rulings, and 170 KB is not a register. Open questions are scattered | Section 4 is the first version. Keep it in the repo with an owner and a date on each line |
| 12 | Accepted contrast misses have no ledger | At least eight component states sit under 4.5:1, each documented in its own README. The project's stated standard is WCAG 2.1 AA | One ledger: component, ratio, ground, who accepted, when, and the compliant alternative that already exists |
| 13 | No token lifecycle | 133 of 248 tokens are referenced by no component in this repo. Many are primitives by design, but nothing distinguishes a primitive from an orphan. Four tokens arrived with no documented purpose | Mark each token as primitive, semantic or deprecated, and fail on an undocumented one |

---

## 4. Open decisions

Each is open because nobody has ruled on it, not because it is hard.

| Decision | Why it matters |
| --- | --- |
| Card heading typeface: Open Sans 600 (`.eq-card__title`) or Source Sans 700 (`.eq-h3-card`) | Both ship; a card heading changes typeface with the class chosen |
| Does teal mean "achieved" now that checks use it, or stay a plain chart series colour? | A reader who learns teal means good may misread a teal bar |
| `--equinet-fontsize-h1` is 56px; the display token and the spec say 60px | A stale duplicate or a role nothing uses |
| `--equinet-font-body` keeps Myriad Pro first (the one remaining open item from the 16 Oct reconciliation) | Dropping it loses the hook for a licensed embed |
| `--equinet-letterspacing-caps` -0.04em is "proposed, not measured" | The h1 and h2 tracking rests on a judgement pending a render check |
| Whether WCAG 2.1 AA is a hard constraint with logged exceptions or a default | Decides whether gap 12 is a ledger or a backlog |
| A quieter dark-ground form of the check | On dark, every variant collapses to the fill form |
| 20px spacing, the 80px ladder gap, and role-mapped line-height | Recorded in `TYPE-ROLES.md`, unruled |
| What four tokens are for: `--equinet-btn-fill--ghost`, `--equinet-shadow-field`, `--equinet-shadow-field--error`, `--equinet-shadow-heading--name` | They arrived with an upload; nothing here uses them |

---

## 5. Roadmap

**This week.** Revoke and reissue the two credentials (gap 1). Deploy
`tokens.css` and re-run the diff (gap 2). Rule on the card-heading typeface and
the AA policy, since two other items wait on them.

**Next two weeks.** The GitHub Action and branch protection (gap 4). Fixture
tests for the six tools (gap 5). A version stamp and a zip script (gap 6). Byte
budgets in `check-docs.py` (gap 8). Move this register to its own file
(gap 11).

**This quarter.** Self-hosted fonts (gap 10). Automated accessibility and
screenshot comparison outside the builder (gap 9). The comp contract with
`PROMPT.md` (gap 7). A token lifecycle (gap 13).

---

## 6. What this document could not verify

- **The current deployed `/modules/tokens.css`.** The drift figures are against
  the copy I was given on 2026-10-16. Re-run the diff against today's file.
- **The Claude Design project.** I cannot see what files it currently holds, so
  gap 6 rests on the repeated symptom, not on inspection.
- **`PROMPT.md`.** It is not in this repo and I could not find it elsewhere. What
  I know of v34 comes from its Notion changelog.
- **Other Notion pages.** I read three pages under Design System (GitHub); the
  rest of the workspace may duplicate or contradict this.
- **Live HubSpot rendering.** Nothing here has been checked against a deployed
  module.
- **Web fonts.** Untestable from the sandbox, as gap 10 says.
