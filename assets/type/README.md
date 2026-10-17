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
| h1 | Open Sans | 60px | 800 | -0.07em | 55px (0.9167) | `#242630` | -2px 2px 4px |
| h2 | Open Sans | 40px | 800 | -0.07em | 36px (0.9) | `#242630` | -2px 2px 4px |
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
