---
id: type-spec
status: current
read_when: >-
  Setting any heading or body copy. The canonical hierarchy — ten Figma
  exports with every size, weight, tracking, leading, colour and shadow, plus
  the light heading variants and the two conflicts they expose.
depends_on: components/bundle.css
verified: 2026-10-16
---

# `type/` — the canonical hierarchy

Ten Figma exports, one per style. These are the source of record for
typography: where a token and one of these disagree, these win. Built as
`.eq-h1` … `.eq-body` in `components/bundle.css`.

Like `assets/components/`, they carry live `<text>` and are never placed.

## The scale

| Style | Family | Size | Weight | Tracking | Leading | Colour | Shadow |
| --- | --- | --- | --- | --- | --- | --- | --- |
| h1 | Open Sans | 60px | 800 | ~~-0.07em~~ **-0.04em** | ~~0.9167~~ **1.0** | `#242630` | -2px 2px 4px |
| h2 | Open Sans | 40px | 800 | ~~-0.07em~~ **-0.04em** | ~~0.9~~ **1.0** | `#242630` | -2px 2px 4px |
| h2 light | Open Sans | 40px | **300** | -0.07em | 36px | `#242630` | **none** |
| h3 section | Open Sans | 32px | 800 | -0.07em | 29px (0.90625) | `#242630` | -1px 1px 1px |
| h3 section light | Open Sans | 32px | **300** | -0.07em | 29px | `#242630` | **none** |
| h3 card | Source Sans | 24px | 700 | -0.01em | — | `#242630` | -1px 1px 1px |
| h4 | Source Sans | 20px | 600 | -0.015em | — | `#242630` | -0.5px 0.5px 1px |
| lead | Source Sans | 20px | 400 | 0em | 26px (1.3) | `#3B3F51` | none |
| body | Source Sans | 16px | 400 | 0em | 22px (1.375) | `#3B3F51` | none |
| eyebrow | Source Sans | 12px | 700 | 0.2em | — | ~~`#242630`~~ **`#E06730`** | none |

Every shadow is `rgba(0, 0, 0, 0.15)`.

## Two families, and the split is the point

**Open Sans 800 at -0.07em** carries h1, h2 and h3-section — the display
tier. Uppercase in every export, always shadowed.

**Source Sans** carries h3-card, h4, lead, body and the eyebrow — the reading
tier. Sentence case, tracking at or near zero.

`h3` is a name shared by two different tiers. The section heading is Open
Sans 32px; the card heading is Source Sans 24px. They are not variants of
each other, and conflating them is what put a wrong value in the deployed
token file for weeks.

## The light variants

h2 and h3-section have a weight-300 form, for contrast against the 800.

**They carry no shadow, and that is the variant, not an omission.** A
hairline weight with a drop shadow under it reads as a mistake. Alternate
light against heavy where two display headings would otherwise stack —
breaking up a run of 800s is what it is for.

Open Sans 300 is already in the `@import`, so nothing needs adding to load it.

## What this resolved

Three of the five open `DECISION` items in `tokens.css`, and in every case
the answer was neither value that was in dispute:

| | Repo had | Deployment had | Spec says |
| --- | --- | --- | --- |
| `fontsize-h2` | 48px | 36px | **40px** |
| `lineheight-body` | 24px | 1.4 | **1.375** (22px on 16px) |
| `letterspacing-display` | -0.05em | -0.06em | **-0.07em** |

`fontsize-h3` resolved differently: **both disputed values were right.** The
repo's 32px is the section heading and the deployment's 24px is the card
heading. One token was carrying two styles.

Eight tokens were added for tracking, leading and shadows the spec defines
and `tokens.css` had no name for — including `--equinet-shadow-heading--h4`,
which is *not* `--equinet-shadow-heading--sm`: same offsets, different blur
and alpha (1px/0.15 against 2px/0.25).

## `price-fontstyle` — 149 × 53

The headline figure. **48px / 900 / Source Sans**, tracking **-0.05em**, in
`--equinet-color-heading`. Built as `.eq-price`.

### The second export corrected three things

The first export was outlined text, so only its size, colour and shadow could
be read and the rest came from `TYPE-ROLES.md` — which was wrong on two of
them. This one is live text and declares its own attributes:

| | Assumed from TYPE-ROLES | The export says |
| --- | --- | --- |
| Family | Open Sans | **Source Sans** |
| Weight | 800 | **900** |
| Tracking | inherited -0.07em | **-0.05em** |

The size holds. **The price belongs to the reading tier, not the display
tier** — which is why it reads as a figure being stated rather than as a
shouted heading. `TYPE-ROLES.md`'s price row is corrected.

### Old-style, proportional figures — ruled 2026-10-19

Old-style figures sit on the baseline with ascenders and descenders like
lowercase letters, instead of all standing at cap height. At 48px they read
as part of the prose rather than as a number stamped into it, which is the
point: a price is a fact being stated, not a label.

**The trade-off is deliberate.** Proportional figures do not line up in a
column. A table of prices wants tabular figures, and that is a different
component from this one.

**Not verified here.** This environment cannot reach `fonts.googleapis.com`,
so whether Google's served Source Sans 3 exposes `onum` and `pnum` could not
be tested — a first attempt fell back to a serif and reported a false
positive. The desktop family has both. If the web font does not, the
declaration is inert and the figures render lining, so it fails safe. Worth
ten seconds in a browser to confirm.

**Never an `<hN>`.** `TYPE-ROLES.md` is explicit: the price is a role, not an
outline level, and wrapping a number in a heading tag to make it large breaks
the document structure for a visual effect. It is a `<p>`.

**Its shadow is a value of its own** — `-1px 1px 3px` at alpha .15, now
`--equinet-shadow-heading--price`. Same offsets as the h3's with three times
the blur, and shallower than the h1/h2's 4px: it sits between them, which is
where a 48px figure sits in the hierarchy.

**Its shadow is still its own value** — `-1px 1px 3px` at alpha .15,
unchanged between the two exports.

## Superseded 2026-10-18: uppercase h1/h2 metrics

The exports above give -0.07em tracking and 0.9167/0.9 line-height for h1 and
h2. Both are superseded for the **uppercase** forms, which is all of them:
`--equinet-letterspacing-caps` (-0.04em) and `--equinet-lineheight-caps`
(1.0). Capitals need more air than lowercase at the same optical size, and
0.9 clips them. Applied with `!important` in `bundle.css`, because module CSS
loads afterwards and a descendant selector there outranks a bare class —
which silently killed the caps line-height on a first render.

The sizes, weights, colours and shadows in the table stand.

## Where this and `TYPE-ROLES.md` disagree

Every size agrees. Family and weight do not, on four roles — the block
heading (800 here, 700 there), the card heading (Source Sans 700 here, Open
Sans 600 there), the minor heading and the eyebrow (Source Sans here, Open
Sans there). `TYPE-ROLES.md` reports what the shipped comps declare; these
files are the Figma type styles. See that file's "Known gaps" item 4 — and
note the disagreement already ships, in `.eq-h3-card` against
`.eq-card__title`.

## Two conflicts this does not resolve

**1. ~~The eyebrow colour.~~ RULED 2026-10-17: `#E06730`, orange.**
`eyebrow-fontstyle.svg` in this folder sets it in `#242630` and
`assets/components/eyebrow-plain.svg` sets it in orange; the two exports
disagreed and the designer has ruled for orange. **The `#242630` in this
folder's export is superseded — do not use it.** Everything else in that file
stands.

The contrast cost is unchanged and accepted: orange at 12px/700 is 3.41:1 on
white, below the 4.5:1 threshold. `.eq-eyebrow--solid-safe` still exists for
a build that must be compliant, but it is **not** the default and must not be
reached for on its own initiative.

**2. `--equinet-fontsize-h1` is 56px** while the display token and this spec
both say 60px. Either it is a stale duplicate or it is a role nothing uses.
Untouched here.
