# Changelog

This repo has no live connection to the Equinet Module Development Claude.ai
Project. Every entry below represents a manual reconciliation pass — someone
asked Claude, in that Project, to fold new development work into
`tokens.css` / `README.md`, then committed the result here.

## 2026-09-24 — Substituted icons set to 1px stroke, 48px ceiling

Rule: every Lucide or otherwise substituted icon declares
`stroke-width="1"`, and no icon — substituted or Equinet's own — renders
above 48px. New tokens: `--equinet-icon-stroke` (2),
`--equinet-icon-stroke--substitute` (1), `--equinet-icon-size-max` (48px).

**This is a deliberate divergence, recorded as one.** Equinet's own icons are
2px on a 24 canvas — measured from the button exports — and Lucide ships 2px
natively, so 1px is not a match to the house style but an override of it.
Substitutes therefore read visibly finer than real Equinet artwork, which has
the useful effect of making a placeholder identifiable on sight rather than
only in a code comment.

Worked through the arithmetic before writing it, because the two constraints
interact: a 1px declaration renders 1.00px at 24, 1.33px at 32 and 2.00px at
48. At the 48px ceiling it coincidentally lands on the house 2px weight. The
rule says explicitly **not** to treat that as the target or scale the
declaration up at smaller sizes — the finer weight is the point.

**Corrected yesterday's service-tile contract**, which specified a 2px white
glyph. Substituted tile glyphs are 1px like any other substitute, so a
part-replaced set will look mixed against the delivered 2px glyphs — the
rule now says replace the whole set or none of it.

Also qualified the "Lucide is an exact match" heading in
`ICON-REFERENCE.md`. Canvas, caps, joins and colour handling still match
exactly; stroke no longer does, and saying otherwise would have been stale
the moment this rule landed.

## 2026-09-24 — Flows subgroup added; illustrations found to reuse a real UI token

Three 1209 × 675 step-flow diagrams filed as `assets/illustrations/flows/`,
bringing that folder to five subgroups and 32 files. Transparent, static, no
text. The most templated group in the set: all three share one composition
exactly — four 170.389px cards joined by arrows, terminating in an orange
accent box — differing only in glyphs.

**Zero new colours.** All five values are existing tokens, which is a first
for a new batch; every previous one surfaced at least a logged candidate.

**The interesting find: these are drawn from UI primitives.** Each card's
drop shadow is `-4.616px 39.236px 39.236px rgba(0,0,0,0.07)`. That is
`--equinet-shadow-card--hover` (`-4px 34px 34px`, same alpha) scaled by
exactly 1.154 on dx, dy and blur alike. Combined with the cards' gradient
being the module background gradient reversed, and their border being
`--equinet-color-border`, these illustrations were composed from the real
card pattern rather than drawn freehand.

That matters for the kit-of-parts model: a card lifted from one of these can
be rebuilt as a genuine `.eq-card` with live tokens instead of pasted as
artwork, because it already is the card pattern at a different scale.

Two palette distinctions recorded: `flows/` uses `#E06730` (primary orange)
where every other group uses `#F5844D` (amber-400), and it's the only group
where `--equinet-color-border`, a UI token, does illustration line work.

Also noted in `INDEX.md`: `make-your-technical-expertise-machine-readable` is
the only illustration in the entire set that directly depicts
machine-readability, so it's the one real match for an AEO or structured-data
subject — a gap the earlier AI-topic test exposed.

## 2026-09-24 — Service-tile glyphs made substitutable; earlier rule reversed

**Reverses a rule I wrote the day before.** `ICON-REFERENCE.md` had listed
`service-tiles/` alongside `nodes/` as un-substitutable brand marks, on the
reasoning that "the gradient, glyph and white ink are the asset itself". That
conflated two things. The *tile* is the brand asset — 65 × 65, `rx 10.3409`,
`#265D94` → `#002E4A` gradient. The white glyph inside it is iconography, and
follows the same rules as every other icon here.

**Substitution is clean because the geometry already matches.** Measured
across all eight tiles: 2px stroke, round caps, round joins, white, glyph
occupying roughly a 27px box inside the 65px tile. Lucide draws 2px on a 24
canvas with the same caps and joins — so a Lucide icon scaled into that box
needs no restyling. Second time this system's house style has turned out to
be Lucide's grid exactly; the first was the chevron that *is* `arrow-right`.

Recorded: the replacement contract (source, canvas, stroke, caps, fill, tile
untouched), a per-service mapping for all eight tiles, and two deviations to
normalise — `services-positioning-strategy` carries a `1.15385` stroke on one
path and `services-value-architecture` a `1.92308`, where the rest are 2.

**Path data is explicitly not to be transcribed from memory.** The rule says
to fetch each icon from Lucide itself and keep its root attributes. A
remembered path is a fabricated path — the exact failure the three root icons
were extracted with a parser to avoid.

**`nodes/` stay un-substitutable**, and the distinction is now stated rather
than assumed: a node has no enclosing brand container, so the mark *is* the
whole asset. Replacing one wouldn't swap a glyph inside a brand asset, it
would replace the brand asset.

Updated in four places so the system doesn't contradict itself:
`ICON-REFERENCE.md`, `assets/icons/README.md`, the main README's
AI-generation instructions, and `PROMPT-TEMPLATE.md`.

## 2026-09-24 — Prompt rules folded into the design system where they belong

Checked the prompt template against `README.md`'s AI-generation instructions
rather than assuming a gap. Most of it was already built in — illustrations,
icons, spacing, typography, contrast and hierarchy all had coverage. Three
things genuinely didn't, now added:

- **Section-heading size.** The instructions said "every h2 is uppercase with
  the heading shadow" but never which size token — the exact thing that caused
  the `bundle.css` 48px/36px bug. Now names
  `--equinet-fontsize-section-heading` and the family-dependent weight.
- **Layout.** No pointer to `.eq-stagger` existed in the instructions, so an
  agent had no reason to find it. Added, with permission to vary the rhythm
  and the two constraints that stay fixed.
- **"Say so rather than approximate."** The single most load-bearing rule in
  the prompt, and it wasn't in the system at all. A near-miss illustration, an
  invented hue or a fabricated glyph is worse than an honest omission because
  it looks finished and hides the problem. Now applies to every rule in the
  section.

**Deliberately kept out: the AEO guidance.** Answer-engine structure is
editorial — how a page is written and organised, not how the brand looks or
behaves. It doesn't belong in `tokens.css`, a component, or the design
system's instructions, and putting it there would blur what the system is
for. Same for anything subject-specific. Both stay in the prompt, which is
where brief-level direction belongs. Recorded in `PROMPT-TEMPLATE.md` so the
split is deliberate rather than an omission someone later "fixes".

## 2026-09-24 — Prompt template added

`PROMPT-TEMPLATE.md`: a reusable Claude Design prompt with `{CONTEXT}` as the
page subject, plus a table explaining why each constraint exists — most of
them trace to a specific failure found during these audits.

Two corrections to the draft it was built from. **"Pull the updated repo from
[URL]" was removed**: the repo is private and Claude Design reads it through a
configured import, so that instruction can only no-op or produce a false claim
that it succeeded. Refreshing is a setup step taken before prompting, and the
template says so. **"Enhance layout with assets" gained its negative rule**,
because as written it reads as an instruction to use an illustration, which is
how a near-miss gets chosen — exactly the failure mode the AI-addiction test
page would have produced.

The AEO section was made concrete rather than named: question-shaped H2s,
answer-first sections, terms defined on first use, genuinely enumerable
content in tables, explicit entity naming, one idea per section so a chunk
stands alone as an answer.

## 2026-09-24 — Illustrations reclassified as reference; a wrong rule corrected

**Correcting a rule I inferred wrongly.** Across several files the
illustrations had been written up as sealed, delivered artwork —
`INDEX.md` rule 5 read "Never recolour. These are delivered artwork",
`bundle.css` pinned `object-fit: contain` on the reasoning that "cropping one
cuts off deliberate composition", and the illustrations README said to place
via `<img>` only. That was inferred from audit evidence, not from any
instruction, and it was stricter than intended.

**The actual model is kit-of-parts.** Illustrations are artistic and styling
reference. A file may be placed whole, cropped, scaled, overlapped or
rearranged, and its elements may be pulled out and recombined into entirely
new compositions. Arrangement carries no authority.

Three things do, and must survive any recomposition: **colour** (token values
only), **typography** (the `tokens.css` scale and families) and
**iconography** (`assets/icons/`). Rearranging is licence to compose, never
licence to invent a hue, a typeface or a glyph.

Recorded in `INDEX.md` (a full "Recomposing" section plus revised selection
rules), the illustrations README, the main README's AI-generation
instructions, and `bundle.css`, where `object-fit` is now
`var(--media-fit, contain)` so cropping is a per-instance choice rather than
forbidden.

**Two traps the reclassification creates, both documented:**

- *Elements lose the ground they were drawn against.* `scenes/` elements are
  navy and orange drawn for a mid-blue gradient; `systems/` and `sectors/`
  elements are near-black for a light ground. Relocating one changes its
  contrast, and the source file's background does not travel with it.
- *Not every colour in these files is sanctioned.* `#292D32`, `#F3F2F2`,
  `#ECEAEA`, `#F3F3F4`, `#444A60`, `#E3EFFC`, `#CFE0F4` and `#F49E78` are all
  logged but never promoted. Sampling from artwork rather than from
  `tokens.css` would propagate an open question into new work.

**One deliberate exception kept.** `assets/icons/service-tiles/` still may not
be recoloured or taken apart — those are finished brand marks whose gradient,
glyph and white ink are the asset itself, not reference material. Stated
explicitly in that folder's README so the difference doesn't read as an
inconsistency.

## 2026-09-24 — Live-text comps settle four open questions; letter-spacing category finally filled

The three comps filed yesterday were re-exported with live `<text>` elements
instead of outlined paths, and a fourth added
(`module__2-column-comparison.svg`, 1920 × 612). 60 text runs now carry real
family, size, weight and tracking. Yesterday's note that these files "cannot
settle the h2 question" is superseded — with live text, they can.

**Heading weight: resolved, and it was never drift.** Open Sans headings are
800 (hero 60px, methodology 56px); Myriad Pro headings are 900 (comparison
36px, sector 36px). The open item comparing `cagr-four-column`'s 800 against
`sector-three-column-case-study`'s hardcoded 900 was comparing two different
families. Recorded on both `--equinet-fontweight-display` and
`--equinet-fontweight-black`.

**Letter-spacing: the category is real now.** Flagged as missing entirely
since the first reconciliation — every module hardcoding its own tracking —
because outlined text made the values unreadable. Six tokens promoted from
declared values: kicker `0.2em` (12px, 3 of 4 comps) and `0.1em` (16px),
display `-0.05em` (56px, matching `plain_hero_banner`) and `-0.07em` (60px),
and h2 `-0.03em`. The Figma text styles' `-2px` works out to neither comp
value at the sizes actually used, so the px variables are kept for provenance
and the em declarations are what to use.

**h2 size: kept both, per decision.** `--equinet-fontsize-h2` stays 48px as
the canonical Figma variable; new `--equinet-fontsize-section-heading` (36px)
carries what every comp actually applies, matching `cagr-four-column`. Also
added `--equinet-fontsize-card-heading` (24px/600), the column heading in two
comps.

**Caught a live bug while wiring this up.** `components/bundle.css` set the
stagger heading to `var(--equinet-fontsize-h2, 36px)` — the fallback was 36
but the token is 48, so the heading would have rendered 12px larger than
intended whenever `tokens.css` loaded, and correct only when it didn't. Now
points at `--equinet-fontsize-section-heading`, with weight corrected to 900
and tracking tokenised. The eyebrow's hardcoded `0.1em` was also swapped for
the confirmed `0.2em` kicker token.

**Still unreconciled:** both comps set a 36px/900 section heading, but
`sector-three-column-case-study` tracks it `-0.03em` and
`2-column-comparison` sets `0em`. Both are live declarations, not
inferences — so this is a real inconsistency in the artwork, not a
measurement artefact.

**Myriad Pro confirmed again**, now in all four comps as declared
`font-family`. Design-level intent, unchanged conclusion: it can't ship in a
browser without a licence, so the Source Sans 3 substitution stands.

## 2026-09-23 — Module comps filed as a new category; one new colour logged

Three Figma module comps added as `assets/comps/` — `2-column-hero-banner`
(1920 × 714), `5_column_block_methodology` (1920 × 805) and
`sector-three-column-case-study` (1920 × 1276). A seventh asset category,
distinct from illustrations because they aren't page artwork: each pictures a
complete rendered module, headings and buttons included, so placing one in a
layout would embed a fake module as a flat image. Marked non-selectable in
`assets/illustrations/INDEX.md` for exactly that reason.

Their value is as reference — parity QA, token provenance (the
`2-column-hero-banner` entries in `tokens.css` date to 2026-08-07 and comp
is what they were measured from), and as a tiebreaker when a shipped module
and a token disagree.

**They cannot settle the h2 size question.** All text is outlined — zero
`<text>` elements across all three — so no font size is readable. Measuring an
outlined glyph's cap height would estimate a value, not read one, and this
system's whole measurement discipline exists to avoid exactly that. Recorded
explicitly so nobody assumes the comps closed a question they can't.

**`#292D32` logged, not promoted.** Eight occurrences in the hero comp, all as
stroke on fine line-art (0.69–1.38px) in an embedded illustration rather than
UI chrome. Single file, so held back by the same standard that kept `#8790A9`
logged until it reached five files.

**Two existing values got more complicated.** `#F1F1F1` — tokenised the same
day as `--equinet-color-diagram-surface` and scoped "marketing illustration
only, not UI" — also appears in the hero comp, as does `#F3F2F2`, one of the
unresolved near-whites. Both sit in the hero's embedded graphic rather than
its chrome, so the scoping isn't strictly wrong, but it's less clean than
recorded. The `diagram-surface` usage note now says so, and `#F3F2F2` is no
longer a single-file value. Neither promoted or re-scoped unilaterally.

Also confirmed: `5_column_block_methodology` carries a radial `white` →
`#F6F5F5` background, matching the module gradient `tokens.css` has described
since 2026-08-07.

## 2026-09-23 — Icon substitution reference; staggered content blocks

**New: `assets/icons/ICON-REFERENCE.md`.** The house icon style, measured
from `arrow-chevron.svg` rather than asserted: 24 × 24, 2px stroke, round
caps and joins, `fill="none"`, `stroke="currentColor"`.

That turned out to match Lucide's published design rules on every property —
and the match is literal, not stylistic. Lucide stores `arrow-right` as
`M5 12h14m-7-7l7 7l-7 7`; the chevron extracted from
`button_textual_default.svg` is `M5 12H19` plus `M12 5L19 12L12 19`. Same
path, different notation. The house arrow **is** Lucide's, which settles the
substitution library on evidence rather than preference.

Phosphor is documented as the fallback with its real cost stated: a 256 × 256
filled-path canvas in six weights, none of which is a 2px stroke on a 24
grid, so it needs rescaling and an optical check rather than trusting
numbers. The file also names a Lucide substitute for each of the three icons
still missing geometry (`close` → `x`, `checkmark` → `circle-check`,
`external-link` → `external-link`), and rules out substituting for `nodes/`
or `service-tiles/` at all — those are brand marks, not utility glyphs, and a
generic stand-in would misrepresent rather than fill a gap.

**New: `.eq-stagger` in `components/bundle.css`** — alternating media/text
rows built to the measured illustration ratios. Alternation is `:nth-child`,
not a modifier, so an editor adding a row can't break the rhythm; it reorders
by `grid-column` rather than `order` or `direction`, so DOM order stays the
reading order for assistive tech.

The part that would otherwise go wrong silently is encoded as three media
modifiers: `--scene` for the 12 opaque scenes (fills edge to edge; padding
would expose page colour around a hard dark rectangle), `--transparent` for
sectors and systems (needs a surface or the line work floats), and
`__row--compact` for the square pictonodes, which are too small to hold half
a row. Below 768px every row stacks media-first including the even ones —
alternation in one column reads as a bug, not rhythm.

## 2026-09-23 — Fourteen icon-scale files filed; a true duplicate dropped

Fourteen SVGs audited and filed under `assets/icons/`, not illustrations —
both families are icon-scale (43 × 43 and 65 × 65), far below the 118–641px
illustration range. That folder now has three groups and 16 files.

**`nodes/`** — five 43 × 43 concept marks (attract, connect, growth, hubspot,
verified). Two findings: the filenames say "black" but the ink is `#242630`
(`equinet-color-heading`), not true black — `equinet-color-black` (`#000000`)
exists separately, so the names shouldn't be read as a colour spec. And they
**hardcode that fill instead of using `currentColor`**, unlike the three root
icons, so as delivered they can't follow a control's hover or dark variant.
Flagged, not edited.

**`service-tiles/`** — eight 65 × 65 rounded tiles, white line glyph on a
`#265D94` → `#002E4A` gradient (both existing tokens). These are correctly
self-contained: the background is part of the artwork and `currentColor`
would be wrong for them. Added to `assets/illustrations/INDEX.md` so they're
selectable on subject alongside the illustrations — three overlap with
`scenes/` topics, differing by scale rather than subject.

**Dropped one file as a true duplicate.** `node-black-hubspot-1.svg` was
geometrically identical to `node-black-hubspot.svg`, differing only by
sub-0.001px floating-point rounding in the exported path. Unlike the animated
sector pictograph — which looked like a duplicate but carried real extra
behaviour — there was nothing here to preserve.

**Also corrected:** the main README's icon guidance still claimed
`assets/icons/` "has no real SVGs yet", which stopped being true two batches
ago when the button icons were extracted.

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
