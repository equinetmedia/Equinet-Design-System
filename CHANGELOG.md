# Changelog

This repo has no live connection to the Equinet Module Development Claude.ai
Project. Every entry below represents a manual reconciliation pass — someone
asked Claude, in that Project, to fold new development work into
`tokens.css` / `README.md`, then committed the result here.

## 2026-09-23 — Illustration selection index added; opaque-background constraint found

**New file: `assets/illustrations/INDEX.md`** — a per-file subject and topic
table for all 29 illustrations, written so an agent can choose artwork on
subject rather than on how a filename sounds. Linked from both the main
README's AI-generation instructions and the illustrations README, so it's
reachable without being pointed at.

Its load-bearing rule is the negative one: **if nothing matches the page's
subject, use no illustration.** The set covers Equinet's own service lines,
sectors and generic business-process concepts, and nothing else. The index
states the exclusions explicitly (consumer tech, social platforms, AI ethics,
psychology, wellbeing, news, third-party products) so "nearest available" is
never mistaken for "suitable".

**Found while indexing: all 12 `scenes/` files are opaque.** Each has a
navy-to-blue gradient rect covering the full 641 × 360 artboard. Earlier
batches were audited for palette and dimensions but not for background, so
this had been missed. It's a real placement constraint — a scene dropped on a
white card leaves a hard dark rectangle — and it's now recorded in the index,
both READMEs and the selection rules. All 17 files in the other three groups
are transparent.

Also corrected a stale count in the illustrations README ("three subgroups,
24 files") left behind when `systems/` was added.

## 2026-09-23 — Commercial-systems batch filed; a near-white finally earns a token

Five 460 × 259 process diagrams filed as a new `assets/illustrations/systems/`
subgroup, bringing that folder to 29 files across four groups. Static, no
animation, no text elements.

**`#F1F1F1` sanctioned as `--equinet-color-diagram-surface`.** It appears in
all five files of this batch and in no token. That makes it the first of the
long-running near-white cluster to earn promotion on cross-file evidence —
the same standard `diagram-line` and the chart-blues were held to.

**`#8790A9` question closed.** Logged as "single-file, too weak to sanction"
in the earlier marketing batch; it's in all five of these plus two marketing
files, and was already a real token (`charade-400`) from the Figma import.

**The remaining near-whites stay unresolved, but are now better characterised.**
Plotting the cluster by relative luminance shows `#ECEAEA` (.826), `#F3F2F2`
(.890) and `#F3F3F4` (.897) all fall *between* two real tokens — `surface-200`
at .915 and `charade-100` at .848 — spanning just 0.07 total. Visually
indistinguishable, no two identical. Each is still single- or low-occurrence,
so none has earned what `#F1F1F1` did.

Also noted: the three 16:9 groups (`scenes` 1.781, `sectors` 1.776, `systems`
1.776) are the same ratio within rounding and interchangeable in one frame,
despite three different pixel sizes. `pictonodes` is square and is not.

## 2026-09-23 — Sixteen illustrations filed into subgroups; an animated file flagged

Sixteen SVGs audited and filed under `assets/illustrations/`, which now has
three subgroups and 24 files: `scenes/` (12), `sectors/` (4) and the existing
`pictonodes/` (8, moved into their own folder).

**`scenes/`** — 641 × 360, three service-line families: `brand-development-*`
(3), `create-*` (3), `website-design-*` (6). 4–10 paths each.

**`sectors/`** — 641 × 361, four vertical pictographs.

**Two palettes, not one, and it may be intentional.** `scenes/` uses
`#002E4A` (blue-900) and `#81ACD7` (blue-400); `sectors/` uses `#00426C`
(blue-default) and `#68728F` (charade-500 — which is also
`equinet-color-diagram-line`, already sanctioned for marketing illustration).
Both share `#F5844D`. Every value resolves to an existing token, so this is
not drift into new colour — but whether sector work is *meant* to read
differently from service work is an open question, recorded rather than
normalized away.

**Caught: an accessibility defect in delivered artwork.**
`equinet-sector-build-environment-pictograph-1.svg` looked like a duplicate of
`equinet-sector-build-environment-pictograph.svg` — different MD5, same
subject. It's the animated variant: an embedded `<style>` block running
`animation: kf_Vector_transform_0 2s linear infinite` with **no
`prefers-reduced-motion` guard**. The only animated file in the entire asset
set, and an indefinite loop with no way to stop it is precisely what this
system's motion rule exists to catch. Flagged in both READMEs with the fix,
not edited — altering delivered artwork is the designer's call.

## 2026-09-23 — Eight illustrations filed; new assets/illustrations group

Eight "pictonode" SVGs were added to `assets/icons/` locally. Audited and
**moved to a new `assets/illustrations/` group** — they aren't icons, and
leaving them in that folder would have broken its stated convention.

The evidence: 118 × 118 with 9–24 paths each (icons are 24 × 24 and 15 × 13
with 2–3), multi-colour by design, and a 1.84px stroke tuned to that size.
Decisively, none can take `currentColor` — the convention every icon in this
system follows so a control's hover state recolours text and glyph together.
Flattening these to a single ink would destroy them.

Their palette independently confirms the filing: all four colours resolve to
existing tokens, but two of them are the **chart-blue** values, sanctioned
for data-viz and marketing and explicitly ruled out for UI. No new colours,
no drift.

Both READMEs now carry the dividing line — if flattening a graphic to one ink
would ruin it, it's an illustration — so this filing decision doesn't have to
be re-derived next time.

Noted for later: six are 118 × 118 but `pictonode-thecde` is 119 × 117 and
`pictonode-website` 121 × 116. Worth normalizing if they ever share a grid.

## 2026-09-23 — Button SVGs audited; pure-CSS component layer added; two open items resolved

Ten Figma button exports audited (primary large ×3, primary video ×3,
navigation ×2, textual ×2). First real button source the system has had.

**Resolved: arrow travel is 16px, not 8.** The default export places the
chevron at x190, the hover export at x206, and the artboard widens by exactly
16. `sector-three-column-case-study` was right all along;
`plain_hero_banner` and `cim-methodology` ship 8px and have drifted. Token
added: `--equinet-motion-travel--arrow`.

**Resolved: icon centralization, partly.** Three real icons extracted with
verbatim path data and bounding boxes computed by a path parser, not retyped:
`arrow-chevron` (24 × 24), `arrow-solid` (15.627 × 13.129) and `play-circle`
(26 × 26), now in `assets/icons/`. The measured sizes independently match
comments in two shipped modules' CSS. Confirms the earlier finding that the
chevron and the solid arrow are genuinely different shapes, not one icon at
two sizes — which is why this couldn't be settled without real source.
`close`, `checkmark` and `external-link` still have no geometry.

**Corrected two assumptions the exports disproved.** The navigation button is
**54px tall, not 56** — it does not share `--equinet-btn-height`, and a new
`--equinet-btn-height--navigation` token now carries it. Its radius also does
**not** grow on hover: both navigation exports carry `rx 7`, unlike the
primary's 7 → 8. Both had been treated as uniform across variants.

**New: `components/bundle.css`** — the pure-CSS component layer. All three
button variants, every state (`:link`, `:visited`, `:hover`, `:focus-visible`,
`:active`), both reduced-motion halves, and the mobile full-width rule. No
build step, no preprocessor, no JavaScript; every value resolves to a token
with its measured literal as fallback.

**Flagged, not fixed:** `button_textual_default.svg` fills its label `#242630`
(= `--equinet-color-heading`), but `--equinet-btn-label--textual` resolves to
`#242530` (= `--equinet-color-text`), which is what the original 2026-08-07
measurement recorded. One green-channel digit apart and indistinguishable on
screen. Left as-is pending the open heading/text merge decision — but the
fresh export is evidence the two were never meant to be distinct.

**Schema re-audited** after the additions: no errors. No duplicate names, no
broken aliases, no unsupported fields on type styles, and every family is one
the page actually reads.

## 2026-09-23 — Uploaded files were a stale snapshot; tokens.json audited against Claude Design's real schema

**Four files uploaded, described as "the complete set of files from Figma,"
turned out to be an older snapshot, not a newer source.** Latest date inside
them: 2026-09-22. They had zero primitive-scale tokens, zero marketing-sourced
tokens (chart-blue, diagram-*), zero motion-duration tokens, and none of this
same day's lead-text or h2 fixes. Not merged in — doing so would have quietly
deleted real, evidence-backed work. Flagged rather than silently accepted or
silently discarded.

**tokens.json audited directly against Claude Design's documented token
grammar** (read from the Design System artifact type's own reference file,
not inferred). Two real compatibility problems found and fixed:

- **The `motion` family doesn't exist in the schema** — its own documentation
  states plainly "No motion family." Every token inside it (the two duration
  values) was being silently dropped. Renamed the family to `duration`,
  which the schema does read.
- **`textTransform` and `textShadow` aren't valid fields on a type style.**
  Added to the h2 entry the same day as the uppercase/shadow requirement;
  checked against the full grammar and neither field exists in it — they
  were being silently ignored. Removed; the h2 sample text is now written in
  caps as the closest structural hint the schema allows, and `README.md`
  now says plainly that this specific requirement can't be fully expressed
  in `tokens.json` and has to be read as prose or implemented directly in
  module CSS.

Also verified computationally, both clean: no duplicate token names across
any family (a duplicate silently drops per the same documentation), and
every colour alias resolves to a token that actually exists.

## 2026-09-23 — tokens.css rebuilt from a real Figma file; two live issues fixed

**tokens.css changed substantially outside this Project** — discovered when
the person uploaded "current" root files and it no longer matched what this
Project last produced. It now cites an actual Figma file
(`A3XMvWX47Tf1191jomeEmH`), its variable collections, local text styles, and
local effect styles, and layers a full primitive scale (`equinet-scale-*`)
and colour ramps (blue, amber, teal, night, charade, surface) underneath the
semantic tokens this Project already established — which it preserves and
correctly cross-references, including quoting back this repo's own
resolution language for the data-viz and diagram categories. Almost
certainly produced through Claude Design's Figma integration, not a person
hand-editing the file.

**`tokens.json` did not change and is now meaningfully behind `tokens.css`.**
The new primitives, colour ramps, canonical Figma type scale, real
letter-spacing values, paragraph-spacing category, and text-transform
category exist only in the CSS. Partial catch-up done in this pass (the
lead and h2 entries below); a full parity pass is still outstanding and
not done here.

**Fixed: lead text has no colour token and never did.** The shipped
module (`plain_hero_banner`) sets it via an editor-controlled inline field
with no CSS fallback — unlike padding, which always has one. Added
`equinet-color-lead` (aliasing `equinet-color-body`, per that token's own
long-standing "Lead-Text-Color" comment) as the missing default. Also added:
`equinet-fontstyle-lead` (italic — hardcoded in the module, absent from
`tokens.json` entirely) and a flagged, unreconciled discrepancy on
`equinet-fontsize-lead` (20px token vs. 22px actually shipped, sourced from
a different module than the one it's meant to describe).

**Confirmed: h2 uppercase + heading shadow.** Both tokens
(`equinet-text-transform-h2`, `equinet-shadow-heading`) already existed from
the Figma import. Marked as a firm requirement rather than descriptive
metadata, and added to `tokens.json`'s h2 style entry, which had neither
field.

## 2026-09-23 — Instructions for AI-generated design added; icon placeholder policy decided

New section in `README.md`, placed after **Brand mark**: a consolidated
mandate for any tool (Claude Design specifically) generating a mockup, page,
or component from this system — real assets only, token values only for
spacing/frame/type, general UI practice filling gaps rather than licensing
invention where tokens don't dictate an answer. Cross-references the
sections that already define the values rather than restating them.

**Icon placeholder policy resolved**, the open question from the earlier
Lucide-substitution finding: a neutral icon set is an acceptable stand-in
until real icons are sourced, provided it reads as a placeholder rather than
being presented as a real Equinet icon. Reflected in both `README.md` and
`assets/icons/README.md` so it's visible whether someone reads the brand
book or lands in that folder directly.

## 2026-09-23 — Second marketing batch (9 files); two decisions resolved, one correction to prior work

Batch of nine smaller marketing SVGs audited, bringing the cumulative total
to seventeen files. Two escalations from single-file to cross-file evidence
were resolved rather than left logged:

- **`#FFE6DB` folded into `equinet-color-orange--pale`.** Grew from one file
  to three (7 occurrences total — matching `orange--pale`'s own usage count
  exactly), which settled it as the same colour rather than a parallel one.
- **New token: `equinet-color-diagram-line--neutral` (`#6C7074`).** A
  neutral-grey variant of `diagram-line` with no blue cast, confirmed fill
  and stroke across 5 of 17 files.

**Correction to the original ABM audit:** re-checking that file during this
batch's cross-referencing turned up `#F3F2F2` (3 occurrences), missed
entirely in its first pass. It joins `#ECEAEA` (same file) and a newly-found
`#F3F3F4` (`The-Brand-Ops-Agent.svg`) as a cluster of three near-identical,
unresolved near-whites — reframed as one open decision rather than isolated
footnotes, since none matches `tokens.css` or each other exactly.

**New kind of evidence:** eight of the nine files in this batch have real
`<text>` elements declaring `font-family="Myriad Pro"` — the first
marketing files audited where text wasn't outlined to paths. Confirms Myriad
Pro as the genuine brand-intended typeface at the design level; doesn't
reverse dropping it from `tokens.css`, which was about browser-rendering
without a licensed embed, a separate and still-true problem.

Also logged, still too weak to act on: `#F49E78` (now 2 of 17 files),
and single-file values `#FF4800`, `#FBDDD2`, `#A4A4A4`, `#343330`,
`#F6F7F9`, `#8790A9`. Full per-file breakdown in `assets/marketing/README.md`.

## 2026-09-23 — Diagram greyscale sanctioned from a seven-file marketing batch

Three new tokens: `equinet-color-diagram-line` (`#68728F`), `-tint`
(`#D6D8E1`), `-tint--pale` (`#ECEDF2`). Same marketing-collateral exception
as the data-viz palette, but on stronger evidence — `-line` and `-tint--pale`
appear in all seven files audited, `-tint` in three of seven, not just one
file using one odd colour once.

Also logged, deliberately not promoted: five colours appearing in only one
file each (`#444A60`, `#E3EFFC`, `#CFE0F4`, `#F49E78`, `#6C7074`), and a
second near-miss discrepancy — `#FFE6DB` in one file, close to but distinct
from `equinet-color-orange--pale`. Full per-file breakdown in
`assets/marketing/README.md`.

## 2026-09-23 — Font stack corrected; a data-viz exception added to the colour rule

**Myriad Pro removed from `--equinet-font-body`, not just deprioritized.**
Confirmed dropped in Claude Design's own build (it hit the same
no-licensed-font-file wall independently and fell back to Source Sans 3
permanently) — `tokens.css` was still listing Myriad Pro first, so it had
drifted behind the system it's supposed to be the source of truth for.

**New sanctioned category: `equinet-color-chart-blue-*`** (three stops:
`#81ACD7`, `#5688BA`, `#3D71A5`), sourced from a published marketing
infographic rather than a shipped module — the first token category to come
from marketing collateral instead of product code. Scoped explicitly to
charts and data visualization; the "nothing outside the palette" rule in
`README.md` was amended to carry a narrow, named exception for this
category rather than being silently loosened.

Also logged, not resolved: the same infographic uses `#ECEAEA` for a panel
background, close to but distinct from `equinet-color-surface--alt`
(`#F6F5F5`). Not promoted to a token — flagged so it isn't lost before
someone decides whether it's deliberate or drift.

## 2026-09-22 — Brand wordmark added

`assets/brand/` now holds real SVG files — `wordmark-light.svg` and
`wordmark-dark.svg`, provided directly, not reconstructed. Identical
geometry, differing only by fill: white for dark grounds, `equinet-color-text`
(`#242530`) for light ones. Same light/dark selection logic as the button
hover toggle already in the system.

Noted in passing: the dark variant's fill matches `equinet-color-text`
specifically, not `equinet-color-heading`. Doesn't resolve the open question
of whether those two near-identical tokens should merge, but it's now on
record which one the brand mark itself was built against.

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
