---
id: changelog
status: historical
read_when: >-
  Tracing when and why a value, rule or decision changed. Never for current
  rules — entries describe the system on their own date and several record
  rules since reversed.
supersedes: none
superseded_by: README.md for anything stated as a rule
verified: 2026-10-13
---

# Changelog

> **Historical record. Do not read a rule from this file.**
> Entries describe the state of the system *on the date of the entry*. Several
> record rules that have since been reversed, counts that have since changed,
> and files that have since been renamed or deleted. They are kept so a
> decision can be traced back to the evidence that caused it — not so the
> decision can be re-derived from here.
>
> **The current rules live in `README.md` and `tokens.css`, and nowhere else.**
> Where this file and `README.md` disagree, `README.md` is right by
> definition. Entries are newest first.

This repo has no live connection to the Equinet Module Development Claude.ai
Project. Every entry below represents a manual reconciliation pass — someone
asked Claude, in that Project, to fold new development work into
`tokens.css` / `README.md`, then committed the result here.

<<<<<<< HEAD
## 2026-10-16 — The canonical type scale, and three DECISIONs resolved

Ten Figma typography exports added as `assets/type/`, a new `type-spec`
category. These are the source of record for typography: where a token and
one of these disagree, these win. Built as `.eq-h1` … `.eq-body`.

**Two families, and the split is the point.** Open Sans 800 at -0.07em,
uppercase, carries h1 (60px), h2 (40px) and h3-section (32px) — the display
tier, always shadowed. Source Sans carries h3-card (24/700), h4 (20/600),
lead (20/400), body (16/400) and the eyebrow (12/700) — the reading tier,
sentence case, tracking at or near zero. Every shadow is
`rgba(0, 0, 0, 0.15)`.

**`h3` was two different styles sharing a name.** The section heading is Open
Sans 32px; the card heading is Source Sans 24px. Conflating them is what put
a wrong value in the deployed token file.

**Light variants.** h2 and h3-section have a weight-300 form for contrast
against the 800, and **they carry no shadow — that is the variant, not an
omission in the export.** A hairline weight under a drop shadow reads as a
mistake. Open Sans 300 is already in the `@import`.

**Three of the five open DECISIONs resolved, and in every case the answer was
neither value in dispute:**

| | Repo | Deployed | Spec |
| --- | --- | --- | --- |
| `fontsize-h2` | 48px | 36px | **40px** |
| `lineheight-body` | 24px | 1.4 | **1.375** |
| `letterspacing-display` | -0.05em | -0.06em | **-0.07em** |

`fontsize-h3` resolved differently: **both disputed values were right**, for
two different styles. The repo's 32px is the section heading, the
deployment's 24px the card heading.

**Eight tokens added** for tracking, leading and shadows the spec defines and
`tokens.css` had no name for. One worth flagging:
`--equinet-shadow-heading--h4` is *not* `--equinet-shadow-heading--sm` —
same offsets, different blur and alpha (1px/0.15 against 2px/0.25).

**Deploying now moves live rendering.** `check-deployed-tokens.py` went from
0 conflicts to 4: h2 36→40, h3 24→32, lineheight-body 1.4→1.375,
letterspacing-display -0.06→-0.07em. That is the point — the spec beat two
sets of measurements taken off rendered artwork — but it is a deliberate
change to watch for, not a safe upload.

**Two conflicts this does not resolve.** The eyebrow colour: the type spec
sets it in `#242630` and the component export in `#E06730`. Both are Figma
exports and they disagree, and it is not cosmetic — orange is 3.41:1 and
fails, `#242630` is 15.05:1 and passes. If the heading colour is right, the
eyebrow leaves the "One unresolved" list entirely. `bundle.css` still ships
orange, because changing it on the strength of the other file would be
guessing. And `--equinet-fontsize-h1` is 56px where the display token and the
spec both say 60px — stale duplicate or unused role, untouched.

**Thirteen checks added** (47 to 60): every tier's size, weight and family;
the display tier uppercase and the reading tier not; the light variants at
300 with no shadow where the heavy form has one; lead and body in
`color-body` against the headings' `color-heading`; and the -0.07em tracking
resolving to -2.8px at 40px.

Caught while writing them: the new `TY` helper shadowed an existing `TY`
translateY helper further down the file, which broke a card-hover assertion
with a selector error. Renamed to `TYPO`.

Manifest at 118 assets.

## 2026-10-16 — `.eq-surface--dark`, and the one accent that works on it

A dark radial added: deep navy, darkest at the bottom-left, lifting to
`--equinet-color-navy` across the frame. **Used sparingly** — a section or a
card meant to stand apart, never a second default. It is excluded from the
sibling rotation by construction (that rule is scoped
`:not([class*="eq-surface--"])`), so a dark surface is only ever something
someone chose.

**Both stops were already tokens** — `#011420` is
`--equinet-color-blue-950`, `#00426C` is `--equinet-color-blue-default`.
Nothing new needed, again.

**A different signature from the light pair, and the light pair's rules do
not carry over.** Polarity is inverted: the light surfaces put white at the
centre, this puts the DARK stop at the centre and lifts outward. The axis
ratio is 2.385 : 1, not 2.023 : 1. The centre sits at 4.3% / 93.2%, almost
off-frame. And the extent is 77.8% x 442.5%, so the pool runs well past the
edges and only part of its range is ever visible — which is what makes it a
slow wash rather than a pool with a visible edge.

**CSS gets within 7/255 here, not 5/255.** The −20° rotation does more work
because the two stops genuinely differ in luminance, where white to #F6F5F5
barely does. The values shipped are a fitted approximation rather than a
transcription — found by searching centre and extent against the rendered SVG
rather than transcribing the matrix, which landed at 9/255. Mean 1.11/255.
The file stays in `assets/backgrounds/` if a build ever needs it exactly.

=======
## 2026-10-16 — `.eq-surface--dark`, and the one accent that works on it

A dark radial added: deep navy, darkest at the bottom-left, lifting to
`--equinet-color-navy` across the frame. **Used sparingly** — a section or a
card meant to stand apart, never a second default. It is excluded from the
sibling rotation by construction (that rule is scoped
`:not([class*="eq-surface--"])`), so a dark surface is only ever something
someone chose.

**Both stops were already tokens** — `#011420` is
`--equinet-color-blue-950`, `#00426C` is `--equinet-color-blue-default`.
Nothing new needed, again.

**A different signature from the light pair, and the light pair's rules do
not carry over.** Polarity is inverted: the light surfaces put white at the
centre, this puts the DARK stop at the centre and lifts outward. The axis
ratio is 2.385 : 1, not 2.023 : 1. The centre sits at 4.3% / 93.2%, almost
off-frame. And the extent is 77.8% x 442.5%, so the pool runs well past the
edges and only part of its range is ever visible — which is what makes it a
slow wash rather than a pool with a visible edge.

**CSS gets within 7/255 here, not 5/255.** The −20° rotation does more work
because the two stops genuinely differ in luminance, where white to #F6F5F5
barely does. The values shipped are a fitted approximation rather than a
transcription — found by searching centre and extent against the rendered SVG
rather than transcribing the matrix, which landed at 9/255. Mean 1.11/255.
The file stays in `assets/backgrounds/` if a build ever needs it exactly.

>>>>>>> 6bc8ca6622d77dfef0b77781179258bf68b49ff0
**Measured what can sit on it, against BOTH stops**, because a surface that
passes at one end and fails at the other has failed. White 10.52:1,
`surface--alt` 9.67:1, `orange--pale` 8.95:1 — all fine.
**`teal-default` at 4.96:1 is the one accent that passes AA for body text**,
which is the first time a compliant accent has existed anywhere in this
system. `orange--light` manages 4.15:1, large text and graphics only. And
**plain orange is 3.08:1 — it fails at any size and is not an accent on this
ground.** That is the fourth component or surface to hit the same orange
ceiling.

`.eq-surface--dark` sets `color` to `--equinet-color-surface`, so content
inherits something readable instead of every module remembering, and gives a
nested `.eq-eyebrow` its on-dark colour without the modifier.

**Four checks added** (43 to 47): navy underneath with blue-950 at the
centre, content inheriting white, the eyebrow taking its on-dark colour
unprompted, and the dark surface keeping its own geometry rather than being
caught by the rotation.

Manifest at 108 assets.

## 2026-10-16 — Four surface positions, rotating automatically

`.eq-surface` gains automatic variation, so a stack of sections doesn't
repeat the same pool.

**Two more positions, derived rather than invented.** `--03` mirrors `--01`
across the vertical axis and `--04` mirrors `--02`: the axes and the 2.02:1
ratio are untouched and only the side the pool sits on changes. 73.2% becomes
26.8%, 33.4% becomes 66.6%. Nothing was guessed.

**Siblings rotate through all four and repeat on the fifth.** Plain
`.eq-surface` with no variant class picks its position from
`:nth-of-type(4n+…)`, scoped `:not([class*="eq-surface--"])` so an explicit
`--01`…`--04` always wins and an editor's choice is never overridden by where
the section happens to sit.

**This only fires where the surfaces are actual siblings** — true inside one
module with stacked sections, false across a HubSpot dnd area, where each
module renders in its own wrapper. The README now documents the module path:
a `choice` field with `auto`, the four positions and a **`flat`** option,
because this is a surface treatment and an editor who wants a plain
background must be able to say so.

**`auto` across modules derives from the module's own `name`,** which is
unique per instance and stable forever. The HubL is written down with an
explicit instruction to verify the `md5` and base-16 `int` filters against
the live HubL version before shipping, and a stated fallback of `--01` rather
than a random pick. It does not guarantee two adjacent modules differ — four
positions means about a one-in-four chance of a match — which is exactly why
`auto` is a default and not the only option.

**Randomness is ruled out explicitly, in the digest and the skill.** A
background that changes between renders breaks caching, breaks screenshot
diffs, and makes a client think something is broken. The goal was never
variety for its own sake; it is that two surfaces seen together shouldn't
match, and that today's page renders the same tomorrow.

**Three checks added** (40 to 43): four consecutive siblings producing four
different pools, the fifth repeating the first so it is provably a cycle
rather than randomness, and an explicit `--01` in the sixth slot still
rendering `--01`.

## 2026-10-16 — `.eq-surface` radial gradients, built in CSS not placed

Two radial background exports added, `radial-background-01` and `-02`, both
1920 x 805. Each is one rect filled with a two-stop radial gradient — 449 and
439 bytes, the whole asset.

**Both stops were already tokens.** White is `--equinet-color-surface`,
`#F6F5F5` is `--equinet-color-surface--alt`, and `tokens.css` has called them
the "module gradient start/end stop" since 2026-08-07. These exports supply
the geometry for stops the system already had.

**Built as `.eq-surface` in CSS rather than shipped as files.** Rendered side
by side at 1920 x 805, the CSS version differs from the SVG by a maximum of
**5/255 on any channel and 1.07/255 on average** — below the threshold
`motion-test.py` already treats as identical. CSS costs no asset,
re-proportions to any module height, and leaves the surface tokens swappable.
The files stay in `assets/backgrounds/` as reference geometry, which makes
that folder hold two kinds of thing now: the draughtsman's line work, which
IS placed as a `background-image`, and these, which are never placed. The
README opens by saying which is which.

**The signature, from decoding both `gradientTransform` matrices.** `-01`
centres at 73.2% / 22.4% with semi-axes of 845.8px and 1710.9px; `-02` at
33.4% / 41.1% with 592.6px and 1198.6px. **Both have an axis ratio of
2.02 : 1** — not a coincidence, and it is what makes the pool read as a soft
wash rather than a spotlight. Neither centre sits at 50% 50%: `-01` pools
upper-right and `-02` upper-left, so alternating them down a page stops
consecutive sections matching. Both are skewed about 11 degrees off
perpendicular, which CSS `radial-gradient` cannot express — at a 4% luminance
delta between the stops it makes no visible difference, which is what the
pixel comparison measures.

**Sizes are percentages, not pixels**, so the pool re-proportions with the
module instead of staying a fixed ellipse in a box of unknown height. Four
custom properties — `--eq-surface-x/y/w/h` — are the documented way to invent
a variation, with the 2:1 ratio and the off-centre placement as the two rules
that keep it on-brand.

**The flat colour stays `background-color` and the pool is `background-image`,**
so an editor's background choice still shows through wherever the pool has
fallen away. The digest rule that padding and background are the editor's
holds.

**Seven checks added to `components-test.py`** (33 to 40): the flat colour
underneath, the pool being a gradient and not an image request, each variant
at its measured centre, the two variants differing, the 2.02:1 ratio, the
bare class carrying a usable default, and the custom properties actually
overriding.

Manifest at 107 assets.

## 2026-10-16 — `.eq-card--stacked` built from card-stacked-layout-01

A card layout comp added to `assets/components/` and built as a `.eq-card`
variant: full-bleed image, stats table, source links out, read-more. For a
card carrying more than a title and a line of text.

**Every measurement resolved to an existing token.** 391 x 528 frame around a
323 x 459.377 card at `rx="7"` (`--equinet-radius-card`); image 323 x 181.377
full-bleed, ratio 1.781, effectively 16:9; content running x 62 to 337 inside
a card at x 38 to 361, so 24px either side, `--equinet-space-md` unchanged;
heading 24/600 `#242630`; stat label 16px `#3B3F51`; stat value 18/600
`#E06730`; 1px `#B1B7C8` rule under each row, rows 34px tall and 10px apart;
sources 11px with baselines 24px apart; read-more 16/600. Icons are Lucide
`external-link` and `book-open` at the house substitute weight.

**`.eq-card` carries 24px padding and this variant needs the image to bleed**,
so the padding moves to `.eq-card__body`. `overflow: clip` was already on
`.eq-card`, which clips the image to the radius for free. The read-more is the
card's single `.eq-card__link`, so the whole card is the target and lifts —
the first component in this system where a card legitimately links somewhere,
after a GEO page shipped 17 that linked nowhere.

**Two things in the export deliberately not inherited.** The card's drop
shadow is `dx-4 dy34 std17 alpha .07` — that is `--equinet-shadow-card--hover`,
not the resting token, so either the comp was exported in its hover state or
it drifted; the component uses the resting shadow and lifts to the hover one
through `.eq-card`. And "CO-PACKER" is clipped mid-word in the export because
Figma gave the heading's drop-shadow filter a 120.426px region narrower than
the text — a bounding-box artifact, not a design decision.

**Third component on the same contrast failure.** Stat values at 18px/600 and
the read-more at 16px/600 are both **3.41:1** on white. 18px at 600 is not
large text — that needs 18.66px — so both want 4.5:1. `.eq-card__stat--aa` and
`.eq-card__action--aa` are the compliant forms and they **drop the orange**,
because no orange in this system reaches 4.5:1 on white:
`--equinet-color-orange--dark` is nearest at 4.37:1 and still short, so a
class called "safe" could not honestly use it. The first draft of this
component did call it `--safe` with `orange--dark` behind it; renaming it was
the correction. After the primary button and the eyebrow, three components now
hang off `README.md`'s "One unresolved".

**Eight checks added to `components-test.py`** (25 to 33): padding moving to
the body, the image clipped to the radius, the media holding the comp's exact
1.781 ratio, the stat row's rule and type, the value right-aligning against
its label, sources at 11px, the `--aa` variant dropping the orange, and the
card having exactly one link target.

Manifest at 105 assets.

**Self-inflicted, worth recording.** While editing the components README I
wrote `open(p,'w').write(open(p).read().replace(...))` — Python opens for
writing first, truncating the file, so the read returned nothing and the
README was wiped to zero bytes. `check-docs.py` caught it on the next run via
the missing-frontmatter check and the file was rebuilt. The frontmatter rule
added on 2026-10-13 for routing turned out to double as a tripwire for an
empty file.

## 2026-10-16 — tokens.css reconciled with the deployment: 227 tokens

The merge drafted against the deployed `/modules/tokens.css` is now this
file. 215 tokens to **227**.

**Twelve folded back from the deployment**, promoted during the
`image_resizer` and `2-column-page-accordion` builds and never returned: the
status palette (`success`, `caution`, `danger` and their pale grounds),
`--equinet-color-muted`, `--equinet-color-navy--pale`,
`--equinet-color-border--control`, `--equinet-font-mono`,
`--equinet-fontweight-medium`, `--equinet-lineheight-heading`. Reasoning
carried over verbatim — particularly why `border--control` exists at 4.17:1
where `--equinet-color-border` at 2.00:1 fails WCAG 1.4.11 for
non-decorative boundaries. That was real work sitting outside the repo.

**The five conflicts were resolved by holding the deployed value**, so
deploying this file moves nothing on the live site: `fontsize-h2` 48px → 36px,
`fontsize-h3` 32px → 24px, `lineheight-body` 24px → 1.4,
`letterspacing-display` -0.05em → -0.06em, and `font-body` regains
`'Myriad Pro'` ahead of Source Sans 3. **These remain open questions**, kept
in the file as `DECISION 1-5` blocks with both values and the reasoning.
Holding what ships is a safe default, not a ruling. The h2/h3 pair is the one
to look at: the repo's own comment called 48px "canonical, but unused in all
four live-text comps", and holding 36px ratifies that permanently. Note also
that h3 at 24px now collides with `--equinet-fontsize-h4`, so one of those
roles is redundant if 24 stands.

**Seven `--equinet-font-body` fallbacks in `bundle.css` were realigned** to
match the token's new value. A fallback that disagrees with its token is the
exact class of silent drift this whole pass was about, even though here it
renders identically because Myriad Pro isn't installed.

**Bug caught during promotion.** Adding the status palette immediately
changed two `nearest_token` suggestions in the manifest: a warm hex in
`chart-robotic-arms-roi` moved from `amber-100` to `caution--pale`, and one
in `marketing-hubspot-agents` to `danger--pale`. Nearest by RGB, wrong by
meaning — status colours are reserved for UI state and must never be proposed
as a replacement for ink in artwork. `build-manifest.py` now excludes them
from the suggestion pool, and the manifest is byte-identical to before the
promotion again.

`tokens.json` regenerated: 154 emitted, 73 unrepresentable. All checks green
— `check-docs.py` 0 problems, `check-deployed-tokens.py` **0 conflicts, 0
orphans**, tests 25 / 14 / 37, `bundle.css` 0 undefined tokens and 0 `var()`
without a fallback.

Still 151 tokens in this file that the deployment doesn't carry, and 10 that
differ cosmetically (aliases here, repeated literals there). Both clear the
moment this file is uploaded — which is now a safe thing to do.

## 2026-10-16 — Deployed tokens diffed: 5 conflicts, 151 missing, 12 orphans

The deployed `/modules/tokens.css` was read for the first time since this repo
was built. It carries **76 tokens against the repo's 215**, and the two have
drifted in both directions.

**Why nobody noticed.** Modules read every value as
`var(--equinet-…, <fallback>)`, and that fallback is deliberate — a module
whose token is missing from the deployed file renders at exactly the right
value anyway. The drift is invisible on every page you can look at. It
surfaces only when someone changes a token, expects the modules to follow,
and nothing moves.

**Five true conflicts — the same name resolving to different values.**
Deploying this repo's file as-is would change how live modules render:

| Token | Repo | Deployed |
| --- | --- | --- |
| `--equinet-fontsize-h2` | 48px | 36px |
| `--equinet-fontsize-h3` | 32px | 24px |
| `--equinet-lineheight-body` | 24px | 1.4 (22.4px on 16px) |
| `--equinet-letterspacing-display` | -0.05em | -0.06em |
| `--equinet-font-body` | `'Source Sans 3'` | `'Myriad Pro', 'Source Sans 3'` |

The h2/h3 pair is the Figma heading scale against values promoted from the
`cagr-four-column` build; this repo's own comment calls 48px "canonical, but
unused in all four live-text comps", which is the disagreement stated out
loud and never resolved. `--equinet-font-body` is the more interesting one:
the deployed file keeps Myriad Pro first so a licensed embed would be picked
up automatically, and this repo dropped it. None of the five has been ruled
on.

**151 tokens in the repo are not deployed at all** — the whole primitive
ramp, every border width and radius, all seven letter-spacings, the button
geometry, motion travel. Any module referencing one is on its fallback.

**12 tokens are deployed and absent here**, promoted during the
`image_resizer` and `2-column-page-accordion` builds and never brought back:
the status palette (`success`, `caution`, `danger` and their pale grounds,
each documented at ≥ 4.5:1), `--equinet-color-muted`,
`--equinet-color-navy--pale`, `--equinet-color-border--control` (4.17:1,
added because `--equinet-color-border` at 2.00:1 fails WCAG 1.4.11 for
non-decorative boundaries), `--equinet-font-mono`,
`--equinet-fontweight-medium` and `--equinet-lineheight-heading`. On these
the repo is behind the deployment, not ahead of it.

**Ten more differ only cosmetically** — the repo aliases a primitive
(`var(--equinet-color-amber-default)`) where the deployment repeats the hex
(`#E06730`). Same resolved value, no rendering difference.

**New: `tools/check-deployed-tokens.py`.** Takes the deployed file as an
argument and sorts the differences into conflict, missing, orphan and
cosmetic, resolving aliases first so an alias and its literal aren't reported
as a difference. Conflicts and missing tokens fail the run; orphans don't —
they are a backlog, not a breakage. Documented in `README.md` under "How it
is consumed" and in the `HANDOFF.md` tools table.

Nothing was changed in `tokens.css`. The five conflicts are decisions, and
making them silently by uploading a file is how a heading scale moves under a
live site.

## 2026-10-16 — The eyebrow built as a component; `--solid` rationed

`eyebrow-plain.svg` and `eyebrow-solid.svg` added as `assets/components/`, a
new category for Figma exports a component is measured from — the role
`assets/buttons/` already plays. Both 115 x 32, both carrying live `<text>`,
so neither is ever placed on a page: the type would render from whatever font
the viewer has.

**Every measurement resolved to an existing token.** 12px to
`--equinet-fontsize-kicker`, bold to `--equinet-fontweight-kicker`, 0.2em to
`--equinet-letterspacing-kicker`, `#E06730` to `--equinet-color-orange`,
`#FCE9E0` to `--equinet-color-orange--pale`, `rx="8"` to
`--equinet-radius-pill`, the `x="24"` text inset to `--equinet-space-md`.
Nothing new was needed. One thing deliberately not copied from the export: it
names the family **Source Sans Pro**, the old name for what this system calls
`--equinet-font-body` (`'Source Sans 3'`).

**Built as `.eq-eyebrow` in `bundle.css`.** `.eq-stagger__eyebrow` already
carried the same type treatment scoped to that one component and is left
alone so nothing breaks; new work uses the unscoped class, which adds the
solid variant. The pill's vertical padding is derived — `(32px - 1em) / 2`
from the scale token — rather than hardcoded at 10px, which is off the 4px
scale and has no token. `check-docs.py` caught the first attempt inventing
`--equinet-scale-250` to paper over that.

**`--solid` is rationed: hero banners, CTA banners, modules of exceptional
value.** The plain eyebrow is the default and is almost always right. The
pill is emphasis, and emphasis on every section is not emphasis — more than
one or two on a page means it is decoration.

**The contrast problem is no longer hypothetical.** The "One unresolved" note
in `README.md` said orange eyebrow text on the pale pill measures 2.9:1. The
full picture, measured: 2.90:1 on the pill, 3.41:1 on white, 3.14:1 on
`surface--alt`, 3.08:1 on navy. At 12px / 700 none is large text — that needs
18.66px bold — so the threshold is 4.5:1 and **every ground this system has
fails it**. That note is now attached to a shipped component, and two
compliant forms exist for builds that can't carry the risk:
`.eq-eyebrow--solid-safe` puts the label in `--equinet-color-text` at
12.93:1, and `.eq-eyebrow--on-dark` uses the pale amber where orange fails
against navy and night. Still not raised with the client. The 2026-09-21
button exception was scoped so it does not extend to another component, so
this needs its own ruling rather than inheriting that one.

**Six checks added to `components-test.py`** (19 to 25), measuring the
rendered component against the export: size, weight, tracking and case; the
orange label; the pill's fill, radius and side inset; its 32px height; that
the plain variant has no pill; and that `--solid-safe` carries the compliant
colour.

**Bug fixed in `build-manifest.py`.** Light versus dark was a whitelist of
three literals — WHITE, #FFFFFF, #F6F5F5 — so it filed the pale `#FCE9E0`
pill as "opaque dark". It is a luminance question and now uses the same
threshold the gradient branch already used. No existing asset's
classification changed; verified against the previous manifest.

Manifest at 104 assets.

## 2026-10-16 — `backgrounds/` added: draughtsman's line work for modules

Three files added as a new asset category: `draftmans-background-hero-banner`,
`-process-flow` and `-market-amplification`. Construction circles, arcs,
dashed centre lines and crosshairs — a technical drawing before anything is
dimensioned. They sit behind a module as texture. The first group in this
system whose job is to be ignored.

All three are 1619 wide (820 / 784 / 735 tall, aspects 1.97 / 2.07 / 2.20),
transparent, one ink each: the hero uses `--equinet-color-charade-400`
(#8790A9), the other two `--equinet-color-charade-500` (#68728F). Both
already tokens; nothing unsanctioned.

**They go in CSS, not in the markup — and that is not a preference.** Each
file is 15–21 paths of mostly dashed strokes, well over the 64px graphic
gate, which is precisely what the connector draw-on targets. Inlined and
annotated, a background would redraw itself on every scroll. As a
`background-image` it also stays invisible to assistive technology for free,
where inline SVG needs an `aria-hidden` somebody has to remember. **Never
`data-asset`, never `data-role`, under any circumstances.**

**Measured contrast, because one combination fails.** Body text `#242530`
over the line work on white: charade-400 gives 4.77:1 at full opacity and
7.10:1 under the 0.7 group; charade-500 gives **3.18:1 at full opacity** —
below AA — and 5.55:1 under the group. Each file has one group at
`opacity="0.7"` and the rest at full strength, so body copy crossing a
full-opacity charade-500 line is non-compliant. The strokes are hairlines and
the touched area is tiny, but WCAG has no exemption for that. The fix costs
nothing: all three were drawn with large open areas, and the README names
which side is open for each. Never behind a stat, a chart, or anything a
reader has to decode.

**How they are drawn**, recorded so another could be matched: one ink, no
fills, no gradients, no text; hairline strokes mostly at 0.5 with 0.3,
0.37621, 0.526694, 1.15893 and 2 for emphasis, deliberately inconsistent the
way a real construction drawing is; a dash family of 7.52, 9.03, 12.16, 13,
14.06, 52 and one 293.57 recurring across all three files, which is the
signature; two `<clipPath>` per file so arcs run off the edge rather than
resolving inside it; one group at `opacity="0.7"` for the second plane,
giving depth without a second colour. Below about 900px the finest strokes
disappear — crop a region rather than scaling the whole frame down.

`tools/build-manifest.py` gained the category and the manifest went to 102
assets with both colours resolving cleanly. `check-docs.py` then caught two
mistakes of mine in the same pass: the new README cited a digest rule by
number, the exact pattern banned on 2026-10-13, and `README.md` still claimed
99 assets. Both fixed. The checker earning its keep on its author is the
point of having it.

## 2026-10-14 — Donuts allowed for a single share

`content-to-format.md` ruled out pies outright and told builds to use a
stacked bar for anything parts-of-a-whole. Meanwhile
`assets/charts/chart-ai-results-not-universal` is three donuts, shipped. The
rule and the artwork disagreed, and the artwork was right.

**The objection to pies was always about comparison.** People read lengths
more accurately than angles, so a multi-segment pie makes a reader work
harder to see what a bar shows at once. None of that applies to a **single
share**: there is nothing to compare, the ring is a gauge, and the number in
the middle does the reading. Donuts are now the format for one percentage.
Several shares that sum to 100% stay a stacked bar. A multi-segment pie is
still wrong.

**House style written up from the real file rather than invented.** Measured
in `chart-ai-results-not-universal`: 17 filled arc paths, zero `<circle>`,
zero `stroke-dasharray` — the ring is drawn as arcs, not as a stroked circle
with a dash offset, which is the obvious way and not the Equinet way. Paint
order is track then value: a full-circle track in `--equinet-color-night-100`
(#F6F7F9) with the value arc over it in `--equinet-color-blue-default`
(#00426C). Starts at twelve o'clock, clockwise, square-cut ends, band about a
seventh of the diameter. The figure sits large in the middle in
`--equinet-color-text`; caption below in sentence case, source smaller again
in `--equinet-color-night-700`. Three across, separated by thin rules.

Added as its own row in the format table — "A single share" — above the
existing parts-of-a-whole row, so a build reaches for it by content shape
rather than by remembering an exception. Plus one rule worth keeping: a donut
with no number in it is a decoration, and a figure not worth setting large
doesn't need a chart.

Also fixed: the "Change over time" row still cited `chart-blue-*`, the last
reference to the superseded palette after the 2026-10-13 ruling.

## 2026-10-14 — Motion scoped to graphics; composed-graphic substance rule

A second GEO page came back clean on every mechanical check — `motion.js`
inlined, 54 of 54 SVGs annotated, no `<img>`, no template bindings, real
`viewBox` throughout, one hardcoded value in the whole page — and still read
as boring and jerky with nothing responding to the cursor. All three
complaints were true, and none of them was a mechanical failure.

**Motion is now scoped to graphics, not icons.** 50 of the page's 54 SVGs
were icons 64px or smaller — nine `lucide-circle-check`, six
`arrow-chevron` — each one annotated and animated because the rule said
"inline every SVG, `data-role` on every drawn element". That put **149 of 234
animated elements inside line art a few pixels across**. The rule never
scoped itself; it was written for a handful of illustrations. Icons are now
inlined but not annotated, and `motion.js` enforces the same 64px gate itself
so an over-annotating build still produces a smooth page.

**Cards must be decided before they are built.** The page carried 17
`.eq-card` elements and zero `.eq-card__link`, so not one lifted. That is the
rule working — no link, no lift — but seventeen inert cards plus eight flat
graphics is most of the page's surface, and it reads as broken. Either give a
card a destination or make the content a panel. If most cards end up inert,
that is a layout problem, not a styling one.

**Every multi-part graphic should be a tab set.** Phase 2 already counted
them; counting was not enough, because this build would have answered "2, of
which 1" and shipped. It is a threshold now, and `check-built-page.py` fails
when a multi-part graphic is left flat.

**New: composed graphics must hold their own.** Measured across the 36
illustration assets: median **16 drawn elements**, 2 filters, 1 gradient,
2 clip paths. The page shipped a `hero-answer-spine` of **2 elements** — a
rect, a line and a circle — and a `method-five-step-flow` of 10 bare `<line>`
elements **with no arrowheads at all**. Equinet draws arrowheads as filled
paths at the line end, never with `marker-end`; across 53 real assets there
is not one `<marker>`. A bare line between two nodes is an unfinished
connector, and it is the most visible tell that a graphic was sketched rather
than drawn. The skill now states the benchmark and what the real assets do
that a thin composition doesn't: arrowheads, depth from `<filter>` and
gradients, caps and joins, overlap rather than a flat row, labels inside the
artwork.

**Never crop a whole asset's `viewBox` to fit a slot.** The build narrowed
`flow-machine-readable-expertise` from `0 0 1209 675` to `20 200 1180 300`,
which silently removed all four of its labels — "Unstructured Commercial
Data", "Machine-Readable Structure", "Verified Commercial Data", "Found,
Understood, Cited". Rendering the source and the built copy side by side was
the only way to see it. Changing the viewBox is not resizing.

**`check-built-page.py` gains three checks:** thin composed graphics against
the 16-element benchmark, `<line>` connectors with no arrowheads, and
multi-part graphics left flat. Two false positives were found and fixed while
calibrating: transparent hotspot overlays are not artwork, and the substance
threshold sits at 96px rather than 64 because brand marks and service tiles
run to 69 x 69 and are meant to be simple.

Also fixed: `references/content-to-format.md` still told builds to draw bar
charts from `chart-blue-*`, superseded by the 2026-10-13 navy/orange/teal
ruling.

Measured, for the record: hover states were **not** broken. Primary buttons
scale and shift shadow, textual buttons go orange, FAQ summaries go navy,
hotspot hit rects go transparent to orange. Only `.eq-card` did nothing, for
the reason above.

## 2026-10-14 — Skill trimmed back; built-page auditor added

A GEO page built against the 2 October system came back with the styling
wrong, and the skill was fairly accused of bloat. Both were true, and they
were separate problems.

**The skill had grown 71%** — 1,489 words to 2,553 — and every word of it had
gone into motion, interaction and reporting. The asset kit, AEO structure and
charts sections, which decide what a page actually looks like, were untouched
at 2,343 / 447 / 659 bytes. Headings, spacing and shadows aren't in the skill
at all; they come from the README digest, which had to compete with a 6.9 kB
section about animation.

**Trimmed to 1,898 words (+27% over the original, down from +71%).** What came
out was rationale, not rules: why a silent failure is worse than a loud one,
which changelog entry each rule came from, the three reasons literal HTML
matters, why a roving tabindex beats eight tab stops. That belongs here, in a
file written to be read by a person investigating. The skill is read at build
time by a model deciding what to do next, and rationale there is dilution. No
rule was dropped; the remaining growth is the interactive-graphics contract
and its HTML example, which are genuinely new.

**What the page actually showed, measured:**

- `tokens.css` fully inlined — 215 tokens defined, 104 used, zero undefined —
  and then **100 hardcoded font sizes, 81 hardcoded spacings and 20 hardcoded
  radii**, every one of them a literal that a token already held.
- **Six `box-shadow` rules were `--equinet-shadow-card` and
  `--equinet-shadow-card--hover` pasted into one declaration**, so six cards
  sat permanently in their hover state.
- `bundle.css` inlined in full, `motion.js` not at all: no
  `IntersectionObserver` anywhere in the file. The CSS classes were present
  and nothing ever applied them. The no-JS fallback is clean, so the page
  looked entirely normal.
- 2 of 32 SVG roots carried `data-asset`; 4 graphics were `<img>`.
- 32 SVGs carried a runtime `viewBox` spelling and 0 carried a real one; 130
  template bindings remained.

**New: `tools/check-built-page.py`.** Audits a finished page rather than the
repo, and names the token each literal should have been. It reads a Claude
Design bundle by unwrapping it first — the 977 kB file is a loader, and
auditing the wrapper tells you nothing. Three bugs were found and fixed while
building it, each one a wrong answer rather than a crash: value matching that
suggested `--equinet-scale-300` for a `font-size`, a zero-unit normaliser that
turned `20px` into `20`, and element counts that read `<img>` out of
`bundle.css`'s own comments and reported two images that didn't exist.

**New rule in the skill: use the tokens.** Once `tokens.css` is in the page,
every size, space, radius and shadow comes from `var(--equinet-…, fallback)`.
Writing the literal when a token holds that value is how a page drifts
off-system while still looking roughly right — which is exactly what happened.
Phase 2's count now includes it.

## 2026-10-13 — Graphics become navigable: tab sets with detail panels

Reworked the interactive-graphics component the same day it landed. The first
version offered a link or an independent toggle; what was actually wanted is a
diagram a reader works through — each part revealing context, nothing
navigating away. Rebuilt on the WAI-ARIA Authoring Practices **tabs** pattern,
because that is literally what it is: select one of several related panels.

**`.eq-graphic--tabs` is now the default for any multi-part graphic.** Each
part is `.eq-graphic__hotspot[role="tab"]` controlling a
`.eq-graphic__panel`; the SVG is the `tablist`.

**Roving tabindex, because eight tab stops is not accessible, it is just
operable.** The whole graphic takes ONE tab stop. Arrow keys move between
parts, Home and End jump to the ends, and moving selects — automatic
activation, which APG sanctions where switching is instantaneous and local.
Arrowing across a flow and watching the detail change is the behaviour that
makes a diagram worth the space it takes.

**Panels are written visible; only the script hides them.** With no JavaScript
every panel reads as plain prose and an answer engine gets all of the detail,
which is the reason the detail is on the page. Panels carry `tabindex="0"` so
a reader can tab from the graphic into the content, `role="tabpanel"` and
`aria-labelledby` pointing at their tab — all applied by `motion.js`, so the
author writes four attributes, not twelve.

**Selection outranks hover.** The selected hotspot stays navy; an unselected
one highlights orange under the cursor. Unselected siblings are deliberately
NOT dimmed, because dimming needs `opacity`, which `motion.js` animates on
`[data-role]` elements during entrance.

**The panel has a reserved min-height** on desktop so switching tabs doesn't
jump the page under the reader's cursor — the commonest complaint about tab
sets — released at mobile width where the reserve would just be a gap.

`.eq-graphic__link` survives as the rare third form, for a graphic that really
is a link somewhere. `role="button"` survives as the disclosure variant for a
lone hotspot with no one-of-several relationship to express.

**`tests/graphics-interaction-test.py` grows to 37 checks**, all passing. It
pins the tab semantics (tablist/tab/tabpanel wired, panels labelled by their
tab), the roving tabindex, arrow/Home/End including wraparound, automatic
activation revealing one panel and hiding the last, Space never scrolling the
page, selection outranking hover, panels surviving with no JS, and reduced
motion withdrawing the lift while keeping colour feedback and full function.
`components-test.py` (19) and `motion-test.py` (14) unchanged.

Skill and digest rule 7 rewritten around the tab set, with a note on what a
panel should contain: the context the graphic cannot draw, not a caption
restating the label. A part with nothing worth revealing is not a hotspot.

## 2026-10-13 — Interactive graphics allowed; .eq-graphic built and tested

The rule forbidding hover motion on a graphic not inside a link is withdrawn.
It had been read as "don't add interactivity" twice — the 2026-10-02 entry
names that misreading and kept the rule anyway, and it came up again. The
reason behind it survives: something that responds to a cursor promises that
something happens. The conclusion changes. Build the interaction properly
instead of avoiding it.

**New in `bundle.css`: INTERACTIVE GRAPHICS.** Two patterns, nothing else.

- **`.eq-graphic` + `.eq-graphic__link`** — the whole graphic is a link.
  Mirrors `.eq-card` exactly: 6px lift, shadow to `--equinet-shadow-card--hover`,
  0.3s in and 0.6s out. The transform sits on the HTML wrapper, never on the
  SVG, so it cannot collide with the `transform` *attribute* that 44 annotated
  elements carry — the trap that forced every motion rule to be scoped
  `:not([transform])` on 2026-09-26.
- **`.eq-graphic__hotspot`** — parts of the graphic are controls. Either an
  SVG `<a href>`, keyboard-operable with no script, or
  `<g tabindex="0" role="button" aria-expanded aria-controls>` for an in-page
  toggle.

**Every hotspot carries `<rect data-role="hit">`** — transparent, at least
24 × 24 user units. One element doing three jobs: a target big enough to hit
(WCAG 2.5.8), one predictable shape to highlight, and a focus ring that
doesn't depend on `outline` behaving over arbitrary SVG geometry.

**Highlights use stroke and fill only — never `transform` or `opacity`.**
`motion.js` animates both of those on `[data-role]` elements during entrance,
so a hover rule touching either would fight the entrance mid-flight. Hover is
orange (3.4:1 on white, above the 3:1 graphical-object threshold); focus is
navy, this system's focus colour, drawn thicker so it still reads under a
hover state.

**New in `motion.js`: HOTSPOT ACTIVATION.** Only the toggle form needs it —
an SVG `<a>` is already keyboard-operable, but a `<g role="button">` is not a
button to the browser and has no implicit activation, so Enter and Space do
nothing unless handled. The block also defaults `aria-expanded`, syncs the
controlled panel's `hidden` attribute, and warns in the console when a hotspot
has no accessible name. It runs regardless of `prefers-reduced-motion`:
reduced motion means less movement, never less function.

**New: `tests/graphics-interaction-test.py`, 24 checks in headless Chromium.**
It caught one real defect before this shipped: the lift fired on hover but not
on keyboard focus when the wrapper itself was the anchor rather than
containing one. Both authoring shapes are now supported, so there is no way to
write a graphic that silently never lifts. The suite also pins the things that
would ship invisibly wrong — hover not touching transform or opacity, Space
activating without scrolling the page, panels staying in the document with no
JS so answer engines still read them, and reduced motion withdrawing the lift
while keeping the colour feedback.

`components-test.py` (19) and `motion-test.py` (14) still pass unchanged.
Digest rule 7 and the layout skill both rewritten. Still forbidden: looping or
ambient animation, and any response on a graphic that does nothing. A hover
state is a promise — keep it or don't make it.

## 2026-10-13 — Chart palette ruled; brief made explicit; builds now report gaps

Three changes that move standing rules out of prompts and into the system.
Each had been carried in prompt text, which is how they went missing.

**1. The chart palette is decided: navy, orange and teal.**
`--equinet-color-navy`, `--equinet-color-amber-400`,
`--equinet-color-teal-default`. Open since 2026-09-30, when the charts folder
recorded that all seven real charts use these while the sanctioned palette was
the three `--equinet-color-chart-blue-*` tokens, drawn from a single published
infographic. Seven files of evidence beat one; the rule now follows the
charts. The chart-blue tokens stay in `tokens.css` — a real measured family
from a real file — but are no longer the default. Reach for them only when
matching that infographic.

Recorded in four places so a reader can't land on the old ruling: the charts
README (its "open question" heading is now "ruled"), the root README's data
visualization section, the layout skill's Charts section (which previously
told a model to ask the user), and the `tokens.css` comment above the three
tokens. No token value changed; the chart-blue usage prose in `tokens.json`
was rewritten and carried through the generator.

**2. The brief is the default, and saying so.** Phase 1 ended with "stop and
ask for approval" but never said what to do when a prompt asks to skip it, so
"skip the brief" was being read as "skip the planning" — which is how a build
goes straight to markup and arrives as headings and paragraphs. Now stated:
the brief is the default and is never skipped unasked; `build direct` is the
opt-in exception, and it skips only step 5's approval stop. Steps 1–4 still
run, and the build opens with the section plan as a short list so the thinking
stays visible and correctable.

**3. Every build closes with three lists, not one.** Phase 2 asked for new
components. It now also asks for **data gaps** — including any `data.json`
value left unused because it is `transcribed` or `not-quotable` — and **needs
confirmation**: placeholder links, invented service wording, claims about the
client, anything written to fill a hole rather than supplied. The GEO build
reported its `#book` placeholder and its own wording of the Commercial
Diagnostic by good judgement; that shouldn't depend on judgement. Silence on
these reads as "checked", which is the one thing it never means.

The GEO prompt drops from 46 lines to 14 as a result, and what remains is a
brief rather than a rulebook: topic, audience, goal, CTA, the named assets and
the one fact about this subject the system can't know (no GEO-specific
statistics exist).

## 2026-10-13 — The GEO page audited; literal-HTML rule added

The rebuilt GEO landing page was checked against the six items it claimed to
fix. All six held: 19 inline SVGs with `data-asset` on every root, 139
`data-role` elements, 23 `data-reveal` blocks, no `<img>`, nine `.eq-card`
panels with no `eq-card__link` (so none lifts, which is correct for cards that
link nowhere), `motion.js` inlined at 7.2 kB with the run-once guard removed,
and a five-item FAQ whose `FAQPage` JSON-LD matches every question *and* every
answer word for word. 112 tokens used, none invented. The FAQ chevron is
path-identical to `assets/icons/arrow-chevron.svg`.

**The defect was in what the page was, not in what it contained.** The
delivered file is a self-extracting bundle: a 948 kB loader wrapping the real
174 kB page, unpacked by JavaScript at runtime, with a `<noscript>` reading
"This page requires JavaScript to display." The HTML source carries no
content. For a page whose subject is being cited by AI answer engines, that is
the argument undone by the delivery.

**Two runtime constructs also block the HubSpot port.** All 19 SVGs carried
`sc-camel-view-box` rather than `viewBox` — zero had a real one, so every
graphic loses its scaling on paste. And the content was template-bound: 12
loops and 22 `{{ }}` bindings, with the FAQ expressed as a loop over a data
array rather than five `<details>` elements.

**New rule in the skill: literal HTML, not a template.** Real elements, real
`viewBox`, no loops over data arrays, with the three reasons stated — the AEO
argument, the port, and the fact that JSON-LD bound to an array can't be
diffed against the visible text by reading the file. Where the surface
rewrites markup on export, the build must say so and name the rendered DOM as
the deliverable rather than the saved file.

**Phase 2's count gains two lines:** SVGs with a real `viewBox` out of the
total, and template bindings left in the markup, which must read zero. Both
are things that look completely normal in a screenshot.

Also noted, not a defect: 54 `var()` calls carry no fallback. Harmless in that
file, since all 215 tokens are inlined in a `:root` block — but those are
exactly the ones that break when markup is lifted into HubSpot without
`tokens.css`.

## 2026-10-13 — A Claude Design page shipped dead again; two changes to stop it

Reported: a GEO landing page built from `equinet-layout` came out with no
animation and no interaction on the graphics. Same report as 2026-10-02, which
is the point — that pass made motion, interaction states and the FAQ part of
every build *without being asked*, and the skill has said so ever since. It
still didn't happen.

**The rule was right; its placement was wrong.** The instruction to inline
`bundle.css` and `motion.js` sat at the *end* of "Built into every page",
written as a conditional — "if the page can't reference repository files". A
Claude Design page, a standalone HTML file, an artifact and an emailed
deliverable can none of them resolve a repo path, so that conditional is the
normal case, not the edge. Phrased as an exception, it reads as one.

**It is now the first instruction in the section**, ahead of all three, and
says plainly that these surfaces do not resolve repository paths and that
inlining is the default. The trailing conditional is gone, and rule 2 now says
"inlined per the rule above" rather than "load", so the two can't drift apart.

**Why this failure mode needs special handling.** A `<link>` or `<script src>`
that doesn't resolve fails *silently* — no console error, no broken layout,
nothing visibly absent. Every other rule in the skill can be followed
perfectly and the page still arrives dead, and a screenshot of a dead page
looks completely normal. There is no symptom to notice.

**So Phase 2 now ends with a count, not a claim.** New step 5: before
finishing, state five numbers — SVG roots and how many carry `data-asset`;
drawn elements and how many carry `data-role`; blocks carrying `data-reveal`;
whether `motion.js` is inlined and its byte count; FAQ items and whether the
`FAQPage` JSON-LD matches them word for word. A count reading "0 of 9" is
visible before the page is ever opened, where "motion applied throughout" is
not. Any zero means fix it before replying — not report it as a caveat.

Nothing was added to `bundle.css`, `motion.js` or the tokens. This was a
documentation failure, not a code one: the components worked, and the page
never loaded them.

## 2026-10-13 — tokens.json generated from tokens.css; 145 tokens, up from 60

`tokens.json` and `tokens.css` were both hand-kept and only one was true. The
JSON carried **60** of the CSS's **215** variables — every token promoted since
2026-09-23 was invisible to anything reading it, including the entire primitive
scale, all seven letter-spacing values, the button geometry and
`motion-travel--arrow`. Flagged that day as "a full parity pass is still
outstanding"; it had widened since, because a transcription pass fixes one day
and nothing after it.

**`tokens.json` is now generated.** `tools/build-tokens-json.py` reads
`tokens.css` and emits the JSON. Never hand-edit it again — edit the CSS and
rerun.

**It merges rather than overwrites, which is the whole design.** `tokens.css`
owns every name and value; the generator invents neither. But `tokens.json`
owns the hand-written `usage` prose — the contrast measurements, the "this
module has drifted" warnings, the provenance notes — and none of that is
derivable from CSS. All **62** existing usage strings were carried forward by
token name and verified unchanged, byte for byte. Two more came from CSS
comments that said something; comments that only restate the value (`/* #F5844D
*/`, `/* 4px */`) are dropped rather than emitted as a `usage` that tells a
reader nothing.

**Coverage: 145 emitted, 70 genuinely unrepresentable.** Colour 89, spacing 26,
shadow 9, radius 8, size 8, duration 5. The other 70 are typography (the `type`
block is a curated structure of named styles, not a token array), paragraph
spacing, text transforms, easing curves and unitless values like
`--equinet-btn-scale--hover` — none has a form in this schema.

**The schema fails silently, so the omissions are written down.** An
unsupported family or field is dropped without an error, which is how the
`motion` family and the h2 `textTransform` were both lost on 2026-09-23. A
token missing from `tokens.json` would therefore look identical whether it was
a schema limit or an oversight. `tools/tokens-unrepresentable.md` is generated
alongside the JSON and lists all 70 with the reason for each, so the gap is
visible rather than assumed.

**The `type` block is preserved, then validated.** There is no 1:1 mapping from
the CSS's `fontsize`/`fontweight`/`lineheight` variables to Claude Design's
grouped type styles, so the generator carries the block through unchanged and
checks it instead: every declared `fontSize`, `fontWeight` and `letterSpacing`
must exist as a value somewhere in `tokens.css`, and `textTransform` or
`textShadow` on a style is rejected outright. The 48px/36px section-heading bug
of 2026-09-24 was exactly the shape this catches.

**Three guards, each tested against a deliberately broken `tokens.css`:**

- a name declared twice — the schema silently drops duplicates, so the
  generator refuses to emit one;
- a `var()` reference to a token the CSS doesn't define, including one with a
  typo'd case that an earlier draft of the alias regex read as a literal;
- an unroutable name — a new token whose prefix matches no rule stops the
  build rather than being quietly skipped. Adding a category means adding a
  routing rule, deliberately.

The run is idempotent and `--check` fails when the committed file is stale, so
`tools/check-docs.py` now delegates its parity check to the generator instead
of re-deriving the mapping. Three existing colour aliases whose names don't
start with `color-` (`--equinet-text-action`, `-hover`, `--equinet-icon-primary`)
surfaced during routing and are now carried.

One fidelity improvement worth noting: `equinet-color-navy` was stored as a
literal `#00426C`. The CSS defines it as an alias of
`--equinet-color-blue-default`, and the generated file now says so — the
palette's one-definition-per-literal rule is visible in the JSON for the first
time.

## 2026-10-13 — Documentation audited for machine readability; a checker added

An audit of whether an agent reading this repo reads something true. The code
layer held up: `assets/manifest.json` regenerates byte-identically from its
generator, every `--equinet-*` token named anywhere in prose resolves in
`tokens.css`, and `components/bundle.css` uses 69 tokens with no undefined
reference and no `var()` without a fallback. Every problem found was in the
prose.

**Eight fixes, all of them things a model would have read as fact:**

- **Seven stale counts.** `HANDOFF.md` claimed 81 assets (99), 32
  illustrations in five subgroups (36 in six) and 16 icons in three groups
  (four groups). `README.md` claimed 24 illustrations, three comps (five) and
  45 reworkable assets. `SKILL.md` said "the four comps". Where a count was
  genuinely useful it was corrected; where it was decoration it was removed
  and the reader pointed at the manifest, which cannot go stale.
- **`HANDOFF.md` described `tokens.json`'s shape wrongly** — as a flat
  `{"tokens":[…]}` array. It is family-grouped. Anyone writing a parser from
  that description would have written a broken one.
- **A malformed table row.** The `assets/comps/` row of `HANDOFF.md`'s file
  table had two cells in a three-column table, so anything parsing it dropped
  or misaligned that record.
- **Two dangling section pointers.** `README.md` and `bundle.css` both sent a
  reader to **Module anatomy**; no such section exists — repointed at
  **Engineering contract** > CSS scoping. `README.md` sent a reader to
  **Surface** for corner radius; also absent — the two radius tokens are now
  named inline.
- **Digest rules cited by number, again.** `README.md` said "digest rule 7"
  and `PROMPT-TEMPLATE.md` "rules 8–11". The 2026-10-02 pass fixed exactly
  this class of breakage and it came straight back, because nothing stopped
  it. Both now cite rules by name, and `check-docs.py` refuses the pattern.
- **`CHANGELOG.md` was out of order and unlabelled.** Its top entry was
  2026-09-24 while the newest was 2026-10-02, so a model skimming the top for
  current state landed on a stale entry. Worse, the file states reversed
  rules in the present tense — "if nothing matches the page's subject, use no
  illustration", "`assets/icons` has no real SVGs yet" — with nothing marking
  them historical. Reordered newest-first and given a header that says
  plainly: do not read a rule from this file.
- **No routing layer.** `README.md` is 961 lines and this file is longer; an
  agent had no way to decide which file answers which question without
  reading them. Seventeen markdown files now carry frontmatter with `id`,
  `status`, `read_when`, `verified` and, where it applies, `depends_on`.

**Two files deliberately exempt from frontmatter, because it would break
them.** `README.md`: the design-system format treats its first `---` as the
author/generated boundary, and YAML frontmatter opens with one — the exact
bug caught on 2026-09-24, which would have been reintroduced by the fix.
`SKILL.md`: its frontmatter is validated against the Agent Skills schema, a
YAML error there stops the skill loading (2026-09-26), and its `description`
already does what `read_when` does. Both exemptions are encoded in the
checker with their reasons, so neither reads as an oversight.

**New: `tools/check-docs.py`.** Companion to `build-manifest.py` — that one
makes the assets machine-readable, this one stops the prose contradicting
them. Eleven checks, each corresponding to a class of error this repo has
actually produced: stale counts against the manifest, token names that don't
resolve in `tokens.css`, `tokens.css`↔`tokens.json` parity, dangling section
and file references, malformed tables, digest rules cited by number,
changelog ordering and framing, frontmatter presence and YAML validity,
illustrations missing from `INDEX.md`, and horizontal rules in `README.md`.
Exits non-zero, so it wires into a pre-commit hook or an Action. It found
every problem above independently of the hand audit.

**Not done, still open:**

- ~~**`tokens.json` carries 60 of `tokens.css`'s 215 tokens.**~~ **Resolved
  the same day** — see the entry above. The JSON is generated now.
- **No SVG carries a `<title>` or `<desc>`** — zero of 99. Lifted out of the
  repo, every asset is anonymous path data; the subject lives only in the
  manifest. Not done unilaterally: it edits delivered artwork, which is the
  designer's call, and it would end the byte-for-byte non-destructiveness
  proof that currently backs the `data-role` annotations.
- **Counts still live in prose** where they were genuinely useful. The
  durable fix is a generated block in `README.md` that `build-manifest.py`
  rewrites on each run; for now `check-docs.py` catches them going stale.

## 2026-10-02 — Interaction, motion and an FAQ accordion, built into every page

Reported: a Claude Design page came out with no animation, motion or
interactivity. Cause: the prompt didn't ask — an earlier prompt rewrite had
dropped the "pay attention to" list — and nothing in the system made those
things happen by default. Motion was opt-in by design, composed graphics carry
no `data-role`, and the skill told models not to add hover motion to graphics,
which reads easily as "don't add interactivity".

**Now part of every build, without being asked.** Digest rule 7 rewritten and
the layout skill given a "Built into every page" section:

- **Interaction states** on every control and linked card.
- **Entrance motion** via `motion.js` — SVGs inlined with `data-asset` and
  `data-role` (now required on composed graphics too), and `data-reveal` on
  blocks.
- **An FAQ accordion** with matching FAQPage JSON-LD, now required in the
  brief template.

**New components** in `bundle.css`:

- **`.eq-card`** — the documented card lift had never been built; `.eq-card`
  appeared only in README examples. Lifts 6px (in 0.3s, out 0.6s) and deepens
  its shadow, but only when it contains `.eq-card__link`, stretched over the
  whole card so keyboard focus lifts it exactly as hover does. A card that
  goes nowhere doesn't lift — that would be a false affordance.
- **`.eq-faq`** — on native `<details>`/`<summary>`: no JavaScript, keyboard
  operable, and answers stay in the document when collapsed, so answer
  engines can still read them. Eases open where `::details-content` is
  supported, opens instantly elsewhere. The chevron is Equinet's own
  `arrow-chevron`, rotated — not a Lucide path written from memory. Hover is
  navy, because orange text fails AA at that size.
- **`[data-reveal]`** — entrance motion for HTML blocks. `motion.js` removes
  the reveal classes after the entrance, so a revealed card's hover doesn't
  inherit the reveal's stagger delay — the transition-list cascade trap this
  system has hit before.

`motion.js` also had an early exit when a page had no annotated SVGs, which
would have skipped reveals entirely. Restructured.

**FAQPage markup, described honestly.** Google added a deprecation notice for
FAQ rich results on 7 May 2026, after restricting them in 2023. The markup
remains valid Schema.org and does no harm. Claims that it boosts AI citations
come mostly from SEO vendors, so the docs present it as clean machine-readable
Q&A, not a ranking lever.

**Tested: `tests/components-test.py`, 19 checks in headless Chromium.** The
first run passed 19/19 — and two of the checks didn't prove what they claimed:
"opening animates" only checked the final height, and "expanded state" passed
by matching the word *group*. Rewritten: the accordion now has to pass through
intermediate heights (measured 75 → 92 → 111 → 130 → 147px), and the browser's
real accessibility tree must report expanded `true` open and `false` closed.
Both pass. Motion regression still 14/14.

**`PROMPT-TEMPLATE.md` gains a shortest prompt** — topic, audience, goal and
build mode — with optional lines for a brief, a spin-off, supplied figures and
variations.

## 2026-10-02 — Service-page heroes, the engine emblem, the site navigation, and a fifth mark

Six files filed: four service-page heroes as `assets/illustrations/heroes/`,
the Commercial Intelligence Engine emblem in `assets/brand/`, and the global
navigation in `assets/comps/`. Plus one asset derived rather than delivered.

**They form one set.** The navigation lists the service pages — Commercial
Positioning, Commercial Systems, Commercial Data & Rev Ops, Account Based
Marketing, Website Design — and the heroes are artwork for those pages.

**A fifth service mark, derived from real geometry.** The engine hero shows
five pillars; `service-marks/` had four. Its card icons turned out to be those
marks exactly — identical geometry, identical absolute placement in identical
68.12px tiles, measured to within 0.01. Card 03 carried the missing
**Commercial Systems** glyph, so `mark-commercial-systems.svg` was built by
the same transform: verbatim path, standard tile, placement within 0.06px of
its siblings. Marked DERIVED in the file pending designer confirmation. A
first render showed square corners — traced to the preview script, not the
file — and then exposed a real error: the mark tile is 68.12px inside a 69px
artboard, not 69px. Corrected.

**The navigation resolves an old exclusion.** `new_header_module_2026_v3.css`
was excluded for an off-brand green palette. Its two-line labels and its
`.container-1280` match this comp exactly — it was built for this design with
the wrong colours. The comp is now the reference to rebuild it against; its
outlined labels are transcribed in the comps README.

**Strongest evidence yet on heading vs text.** The navigation's 1920px band is
`#242630` and its centred 1280px container is `#242530` — the two
near-identical tokens side by side in one component, visually
indistinguishable.

**The emblem is a brand mark, not an icon** — 284 × 275, nearly six times the
48px ceiling, single ink. It matches the engine hero's centre glyph (16 of 24
path shapes). Its 4px stroke drops below 1px under ~72px, so that's its
minimum size.

**A trademark issue.** `hero-why-hubspot` draws HubSpot's logo in Equinet's
`#F5844D`. HubSpot's trademark guidelines forbid changing the logo's colour;
its brand orange is `#FF7A59`. Added as digest rule 15 — third-party marks
are never altered — because this is a legal constraint, not a style one. The
same hero has seven off-palette colours, the most of any asset: HubSpot's own
dashboard chart colours. Whether depicting HubSpot's interface faithfully is a
sanctioned exception is left as a decision.

**Mock dashboard figures are not data.** "611" and "51,937" in that hero are
placeholder UI and must never be quoted.

**Heroes deliberately not annotated.** The illustration roles would give the
engine hero 38 "accents" and tag HubSpot's logo as Equinet's accent. Recorded
as needing a hero-aware role set instead.

**Recurring colours.** `#343330`, `#ECEAEA` and `#F3F2F2` have each reached
three files; `#1973AD` appears in a hero and in `workshop_one_column`'s
shipped button shadow. Below the five-file bar used for earlier promotions,
so logged in `tokens.css`, not promoted.

**Smaller:** the navigation's CTA is a third button size (148 × 50, `rx 6`),
distinct from primary and navigation buttons; the heroes introduce a fourth
aspect ratio (1.10).

## 2026-10-02 — Charts category added; data checked against its sources

Eleven SVGs filed: seven data charts as a new `assets/charts/` category, and
four service-line icons as `assets/icons/service-marks/`. Renamed on filing to
the convention (`chart-*`, `mark-*`), correcting a typo (`Perectage`).

**Charts are data, not illustration.** They carry real statistics with cited
sources, so they're governed by the never-invent-data rule rather than by the
kit-of-parts freedom. Each was rendered in a headless browser and read, its
geometry measured against its own labels, and where possible its figures and
sources checked against the publisher.

**Every chart has zero live text** — figures, labels and sources are all
outlined. So every figure is now transcribed into **`assets/charts/data.json`**
with its source and a status: verified (checked against the source),
transcribed (read from artwork, source cited, not independently checked) or
not-quotable (positions plotted without values — don't quote readings off the
geometry). Charts are to be rebuilt live from it, never retyped.

**Findings, most important first:**

- **The barriers chart is labelled "% illustrative" — but its data is real.**
  Its 2023 (49, 43, 37) and 2024 (45, 44) figures match Rootstock Software's
  published survey releases exactly. The label wrongly discredits genuine data.
- **The adoption chart's bars aren't drawn to scale.** 12 of 15 deviate by
  more than 1.5 points from their labels, worst 62% drawn as 69.2%, in both
  directions — sized by eye. Ordering is preserved.
- **The two other bar charts are accurate** — industry output within 0.1,
  barriers within 0.4 points. Arcs and the dumbbell weren't measured, and make
  no claim either way.
- **Two misspelled sources:** "MIT NANDO" is MIT Media Lab's Project NANDA;
  "Rootsock" is Rootstock Software.
- **The 95% statistic is broader than its source.** The chart says "AI
  pilots"; the MIT NANDA study covers generative AI pilots, in a preliminary
  report with a limited sample.
- Smaller: "HPI" for KPI in one subtitle (both footnotes say KPI); "20/30%"
  for a range; inconsistent % sign sizing in one chart; one rounded bar among
  square ones; `#FEE8D6`, a pale-orange near-miss.

None corrected in the artwork — that's the designer's call — but recorded in
the charts README and `data.json` so fixes can be made at source.

**An open palette question.** All seven charts use navy, orange and teal for
their series. The sanctioned data-viz palette is `chart-blue-*`, sanctioned
from a single infographic; none of the seven uses it. Recorded as a decision
needed, not assumed either way.

**Charts deliberately not annotated with `data-role`.** The illustration
classifier would tag every orange bar as the single accent and every navy bar
as a glyph, and generic data motion grows elements upward — wrong for
horizontal bars and arcs. Left unannotated, so motion.js ignores them.

**Service marks:** four 69px dark tiles with white glyphs — nodes'
construction at a larger size. Annotated (tile + glyph), proven
non-destructive; glyph substitutable, tile fixed.

**Also fixed:**

- **The manifest had no generator.** The README told people to regenerate it,
  but the code existed only in a past session. Now `tools/build-manifest.py`.
  Running it surfaced a further error in the old manifest: every
  un-annotated file defaulted to "transparent", so the four comps and nine
  marketing graphics — which have full-artboard light gradients — were
  misrecorded. Same class of error as the earlier sectors mistake.
- **The digest gained rule 14, "Never invent data"** — it previously lived
  only in the skill.
- **Four references called the digest "13-rule"**, already stale at 14.
  Made count-free so they can't drift again.
- **The motion test's draw-on check was marginal.** It took one sample at
  420ms, which lands where the entrance easing has barely started — it had
  passed by catching a single connector on the cusp, then failed
  consistently. Sampled across the whole entrance, the draw works exactly as
  designed (offsets fall 61 → 54 → 17 → 1.5 → 0 over ~400–1,100ms); the code
  was never broken. The check now polls the entrance and sees all 12
  connectors drawing at once. 14/14 on repeated runs.

## 2026-09-26 — Graphic motion, verified in a real browser

New: `components/motion.js` and a "GRAPHIC MOTION" section in `bundle.css` —
a once-only, scroll-triggered entrance for any inline annotated graphic,
driven entirely by `data-role`. New tokens: `--equinet-motion-ease--enter`
(the ease-out curve from `sector-three-column-case-study`'s shipped reveal
wipe, not invented) and `--equinet-motion-stagger` (60ms, capped at 480ms).
New: `tests/motion-test.py`, 14 checks run in headless Chromium.

**Three findings shaped it before any code was written:**

- 76 of 117 connectors are filled outline shapes, not strokes, so the usual
  `stroke-dashoffset` draw-on works on only 41. Stroked ones draw; filled
  ones fade.
- 44 annotated elements carry an SVG `transform` attribute, some mirrored
  matrices. A CSS `transform` replaces the attribute — even `transform: none`
  — so every transform rule is scoped `:not([transform])` in both hidden and
  visible states.
- CSS can't reach inside an `<img>`; animation requires inline SVG.

**Testing caught four real bugs — the first version looked right and wasn't:**

1. **Lines never drew.** Arming triggered a *reverse* transition:
   `getTotalLength()` forces a style pass, so the visible state was on record,
   and adding the class *animated into* the hidden state. On a live page a
   graphic visible on load would flicker out and back. Fixed by arming with
   transitions disabled for one frame.
2. **A unitless `--len`.** Chrome rejects a bare number for
   `stroke-dashoffset` in CSS and silently uses 0. Now carries `px`.
3. **Collision with self-animating artwork.**
   `sector-built-environment-animated` has drawable connectors and its own
   keyframe loop; two animation systems would have fought. Now skipped.
4. **Resting state off by up to 35/255.** All 43 affected pixels sat on drawn
   connectors, and a fresh clone of the same node rendered identically —
   proving it was Chrome's retained raster from the dashed paint, not the DOM.
   The graphic is now swapped for a fresh copy after the entrance. Worst case
   fell from 35/255 to 4/255.

Two test bugs were also found and fixed rather than papered over: the
first harness used graphics with no stroked connectors, so the draw-on path
was never exercised; and a position check compared viewport-relative boxes
across different scroll offsets.

**Final: 14/14.** The resting state matches the static artwork within 4/255 —
two graphics identical, two differing by 1–4 levels on under 0.1% of pixels.
Reported as that, not as "pixel-identical", because two aren't.

Deliberately not added: looping or hover motion on graphics. A graphic isn't
a control, and hover motion signals that something can be clicked.

## 2026-09-26 — Lead text: a missing component, and a fix that didn't work

Reported: lead text not pulling through. Three causes, one of them an error in
an earlier fix.

- **No component consumed the lead tokens.** `--equinet-color-lead`,
  `-fontsize-lead`, `-lineheight-lead` and `-fontstyle-lead` all existed, but
  `bundle.css` had no lead rule — its only "lead" was the word *leads* in a
  comment. Tokens with no consumer render nothing. Same gap as the unused
  chart tokens. Added `.eq-lead`.
- **The 2026-09-23 fix failed on its own motivating case.** That fix added
  `--equinet-color-lead` because lead text was invisible on
  `plain_hero_banner`'s navy — then aliased it to body grey `#3B3F51`, which
  measures **1.01:1 on navy**. Still invisible. Added
  `--equinet-color-lead--on-dark` (white, 10.5:1). White is a decision matching
  that module's own heading on the same ground, not a measurement — no comp
  shows a lead on a dark ground — and is recorded as such.
- **Lead colour is two-valued, not one.** The live-text comps give every lead
  as italic 20px, but split on colour: `#3B3F51` in two comps, navy `#00426C`
  in the other two. Added `--equinet-color-lead--accent` and
  `.eq-lead--accent`.

**Also resolved: the 20px vs 22px question** flagged 2026-09-23. Three of four
comps set leads at 20px; 22px is the methodology module's larger lead, now
`.eq-lead--lg`. Not a conflict.

All six variant/ground pairings measured, all 9.6:1 or better.

## 2026-09-26 — Full asset review: naming, editability, documentation

A review against one goal: a language model should be able to rework the
graphics in `assets/` to fit the data being presented. That tests more than
naming — it tests whether the files are editable by a model at all.

### Naming — 58 files renamed

One convention: lowercase kebab-case, group-prefixed, globally unique
(`<group>-<subject>.svg`). 31 files had defects — mixed casing, underscores,
export cruft (`-v1`, `-c`, `-d`, `_091526`, `-blue`, `-1`), redundant brand
prefixes — and seven genuine typos: `narritive`, `verfied`, `accuracye`,
`t0`, `rack` (track), `GTPs` (GPTs), `build-environment` (the industry term is
*built* environment). `node-black-*` lost "black", which misdescribed a
`#242630` ink.

Group prefixes were kept on purpose: stripping them makes `ideal-customer-profile`
and `positioning-strategy` collide between scenes and service tiles.

**Not renamed:** `buttons/` and `comps/` keep their Figma layer-ID names —
those names *are* the layers PROMPT.md maps back to. Renames used `git mv`, so
file history survives. Every current document was updated; `CHANGELOG.md` was
deliberately left with the names as they were, and `assets/RENAMES.md` maps
all 58 so old references still resolve.

The rename itself introduced one error, caught in verification: a note
recording that `node-black-hubspot-1.svg` had been deleted was rewritten by
the substitution into a reference to a file that never existed. Restored.

### Editability — the real blocker

Measured first: **scenes, systems, pictonodes, service tiles and nodes had
zero live text and zero semantic IDs.** A model opening one saw only anonymous
path data and couldn't tell a connector from a card. Only `comps/` and
`marketing/` carried live text.

But every element's role was recoverable from its colour token, so structure
was added deterministically: a `data-role` on each drawn element (background,
tile, card, panel, connector, node, glyph, accent, data) and `data-asset` /
`data-group` on each root, across all 45 reworkable files. Classifier was
dry-run, its unclassified residue inspected and resolved, then applied.
**Proven non-destructive: stripping the added attributes reproduces all 45
originals byte-for-byte, and all 45 parse.** Only six elements remain
generic — invisible bounding rects.

Illustrations turned out to be **pure structure with no text at all**, which
became the central rule for reworking: labels go in HTML, never in the SVG.

### Two errors of mine the review uncovered

- **Sectors were recorded as transparent. They're opaque-light** — each has a
  full-artboard `#F6F5F5` → white gradient. My original background check only
  matched solid hex fills and missed `fill="url(…)"`. The error had spread to
  `INDEX.md`, the README digest, the stagger table, the skill and the prompt
  template — and `bundle.css` routed sectors to `--transparent`, which pads
  them onto a surface they already carry. Corrected everywhere; added an
  `--opaque` media modifier (with `--scene` kept as an alias).
- **Nodes were recorded as single-ink `#242630` marks. They're white glyphs on
  dark `#242630` tiles.** The `#242630` was the container, not the ink. This
  mattered: when asked to swap "the white icons on the dark nodes" for Lucide,
  I applied it to service tiles only and declared nodes "not substitutable —
  the mark is the whole asset". That reasoning rested on the bad audit. Nodes
  have exactly the container-plus-glyph structure that makes tiles
  substitutable, so their glyphs now are too — except `node-hubspot`, verified
  by inspection to be the HubSpot sprocket logo, a third-party brand mark.

### Documentation — three new files

- **`assets/manifest.json`** — all 81 assets, generated from the files:
  category, dimensions, aspect, background, live-text count, roles, and palette
  mapped to tokens. Untokened colours are marked `unsanctioned` with a
  `nearest_token`; the folded `#FFE6DB` maps to `orange--pale`. Illustrations
  and tiles carry their subject and topics.
- **`assets/REWORKING.md`** — which categories may be edited, each role's
  purpose, per-group recipes, and a worked example built from measured
  geometry: flow cards sit at a constant 271.508 pitch, so a fifth step
  appended at that pitch ends at x 1307 — past the 1209 artboard. Adding a
  step means rescaling, not appending.
- **`assets/RENAMES.md`** — the full old → new map, plus the typo list.

README gained digest rule 13 (rework by role, from the manifest) and a section
on all three; the layout skill now reads the manifest and reworks by role.

## 2026-09-26 — Layout skill rewritten; design system's omission rules corrected

**The first version of the skill made output worse.** Reported on first use:
no assets from icons, illustrations, comps or marketing; no Lucide icons;
overall poor UI. Diagnosed rather than patched, and the cause was the skill's
own construction, not Claude Design.

**Measured the bias.** Across the skill, restrictive instructions outnumbered
directive ones **26 to 6**. It told the model what not to do in nearly every
paragraph and almost never what to do; a model given that balance does less.
Specifically:

- It **never mentioned `comps/` or `marketing/`** — they went unused because
  nothing asked for them.
- It **contradicted the kit-of-parts decision.** "If nothing matches, use
  none" is a rule about placing a *whole* illustration; the skill applied it to
  everything, so any topic outside Equinet's service lines got nothing.
- It **framed Lucide as a grudging placeholder**, so icons were avoided.
- Its **brief template modelled omission** — the worked example ended
  "Section 4 ships without one," which a model copies.

The skill had been built to avoid errors, and avoided them by doing less. It
conflated caution about facts with caution about visuals.

**The fix, in the skill:**

- Rewritten around a **four-way asset kit** for every section: place a whole
  illustration on subject match; otherwise **compose** a bespoke graphic from
  parts; borrow layouts from `comps/`; match the style of `marketing/`. The
  answer is never "nothing".
- New **`references/visual-kit.md`**: the actual primitives measured from the
  illustration files (card, connector, node, accent, panel, line-work, data
  fill), each with its tokened page-scale rebuild, plus seven composition
  recipes (step flow, hub and spoke, feedback loop, layer stack, stat panel,
  comparison split, icon grid), each traced to its source file. Replaces
  `equinet-assets.md`.
- Lucide reframed as the **active iconography source**, used generously.
- Brief template now requires a Visual entry per section — "none" is not
  valid — and its unmatched-subject example composes rather than skips.
- **One hard limit kept, deliberately: never invent data.** That's about
  factual accuracy, not visual caution, and it was correct. A section lacking
  figures gets a composed graphic instead of a fake number.

After: **17 restrictive to 50 directive**, and all four asset folders
referenced.

**The fix, in the design system.** The skill had inherited the omission bias
from the repo itself, and Claude Design reads the repo — so fixing only the
skill would have left `INDEX.md` overriding it. Corrected in `INDEX.md`
(rule 2 and the comps section), both asset READMEs, the main README (digest
rule 10 and three instruction passages) and `PROMPT-TEMPLATE.md`.

The key resolution, in `INDEX.md` rule 2: the old rule said "recomposition
doesn't rescue a subject mismatch." That confused two things. **Subject
imagery** — a drawn wireframe, a depicted sector — only fits its subject.
**Structural primitives** — cards, connectors, nodes, panels — depict nothing
until given content, and are usable for any topic. A mismatched whole
illustration is still wrong; a composed graphic from primitives isn't.

Comps reclassified from "never use" to **layout blueprints**: rebuild their
structure with live components, don't embed them as flat images.

**Caught during validation:** a colon in the rewritten skill description broke
its YAML frontmatter, which would have stopped the skill loading at all.
Fixed before packaging.

## 2026-09-26 — Layout skill added (`skills/equinet-layout/`)

A skill combining the design system with page-planning judgement: given
content, it produces a section-by-section layout brief, waits for approval,
then builds. Chosen as brief-then-build so layout decisions get reviewed while
they're cheap to change.

**Lives in the repo, not only as an installed skill.** Claude chat installs
`.skill` packages; Claude Design reads this repo. Rather than keep two copies,
the folder sits here — versioned with the tokens and assets it depends on —
and is packaged for chat from the same source. The repo copy is canonical.

**Four references:** `content-to-format.md` (a content-shape → format matrix,
plus the close calls — bar vs line, sequence vs flowchart, cards vs table,
why not pies), `hubspot-elements.md` (Equinet's 15 modules and native HubSpot
capabilities, by the reader's next action), `equinet-assets.md` (a pointer
summary of illustrations, icons, components and chart tokens) and
`brief-template.md` (the exact brief format, with a worked section and an
honest gap).

**Two findings from building it.**

- *No chart, stat, table, flowchart or FAQ component exists.* `bundle.css`
  holds buttons and `.eq-stagger` only, and the three chart-blue tokens have
  nothing consuming them. The skill says so, builds those from tokens when
  needed, and flags them as new so they can be promoted instead of living as
  one-offs. This is the clearest next piece of design-system work.
- *The CTA rule has a real cost.* The design system forbids `{% cta %}`, but
  HubSpot's current CTA editor has A/B testing and smart (personalised) CTAs,
  which a `.btn-primary` anchor can't do — and HubSpot has postponed the
  legacy editor's sunset, so the native tool is live, not dying. The skill
  defaults to `.btn-primary`, offers smart content on the surrounding section
  first, and raises native CTAs as a deliberate exception rather than
  swapping one in.

**Its central guardrail: never invent data to fill a format.** A layout skill
is exactly where a plausible "73% of buyers…" gets fabricated to fill a slot
that looked good in the plan. No number in the content, no stat block — and
missing data goes in the brief as a gap for the user.

Validated with the skill-creator checker, and every asset count, token value
and filename it cites was verified against the repo before packaging (18/18).

## 2026-09-24 — Removed a `---` that would have marked the brand book as regenerable

Checked the design-system format spec to answer whether the prompt could be
built in, and found a bug introduced an hour earlier by the rules digest.

**The format treats the first `---` in `README.md` as the boundary between
author text and generated sections, and rewrites everything below it on
save.** The digest ended with a `---` separator before the introduction —
the only horizontal rule in the file — which marked the entire 815-line brand
book as regenerable content. A save from the page, or a `make.ts` build,
could have replaced all of it with generated "Consuming this system" and
"Index" sections.

Replaced with an `## About this system` heading, and added a warning in the
file itself so the rule isn't reintroduced. Zero horizontal rules in
`README.md` now.

Other docs carry `---` rules (`PROMPT-TEMPLATE.md`, two asset READMEs,
`INDEX.md`) and are unaffected — only `README.md` is parsed for that
boundary.

Also confirmed from the same spec, which answers the original question:
agents **read `README.md` first**, so design-system rules genuinely are
built in rather than needing restatement each session. What can't be is
brief-level direction — the AEO structure and `{CONTEXT}` — which describes
a page, not the brand.

## 2026-09-24 — Minimum viable prompt recorded

Checked the original four-line Claude Design prompt against the system line by
line rather than answering in general terms. Three of the four substantive
lines are already encoded — asset usage (with the use-none fallback and the
1px/48px icon rule), UI/UX practice (contrast, alignment, hierarchy, density),
and layout reordering (kit-of-parts plus the `.eq-stagger` pointer). Only the
AEO guidance isn't, and that's deliberate: it's editorial, not design.

The fourth line, "pull the updated repo from [URL]", works neither as a rule
nor as a prompt — the repo is private and read through a configured import, so
refreshing is a setup action taken beforehand.

`PROMPT-TEMPLATE.md` now carries a **minimum viable prompt**: the subject plus
the AEO brief plus the escalation rule, nothing else. The full template is
reframed as a fallback for when output drifts, not the default.

Recorded with one honest caveat: a rule in the repo is *available* to the
model, a rule in the prompt is *in front of* it, and those aren't the same.
That gap is what the README digest narrows, but doesn't close. The guidance is
to restate a single rule when it drifts rather than revert to pasting
everything.

## 2026-09-24 — Rules digest hoisted to the top of README; DESIGN.md declined

Asked whether a `DESIGN.md` would improve accuracy. Measured rather than
assumed, and the measurement pointed elsewhere: the operative rules
("Instructions for AI-generated design") sat at **line 604 of an 816-line,
6,400-word README, behind 23 section headings** — 74% of the way in. An agent
reading the design system reads the README, and the rules it must follow were
at the back.

**Declined the new file.** This system already carries 11 markdown documents,
and drift between them is a demonstrated failure mode here, not a theoretical
one — the `cagr-four-column` provenance error propagated across three files
before being caught, and the "assets/icons has no real SVGs yet" line went
stale for two batches. A twelfth file restating the rules would be a new
surface for exactly that.

**Did the cheaper, stronger thing instead:** a 13-row rules digest at the very
top of `README.md`, above the introduction. Same single source of truth, no
duplication, read first rather than last. Each row is one binding rule —
tokens only, no invented hues, three typefaces, section-heading spec,
editor-owned padding and background, parallax, both reduced-motion halves,
icon stroke and ceiling, illustrations as reference, subject-matched
selection with the use-none fallback, the opaque/transparent/square split,
measured AA, and the escalation rule.

Every factual claim in the digest was verified against `tokens.css` and the
folder structure before committing — a wrong summary at the top of the file
would be worse than no summary at all. All 13 checks passed.

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
