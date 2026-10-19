---
id: type-roles
status: current
read_when: >-
  Sizing any text. The ruling that heading LEVEL and type SIZE are independent
  choices, the role token for each, the h2 ruling, the spacing ladder, and the
  three known gaps.
depends_on: tokens.css, assets/type/README.md
verified: 2026-10-17
---

# TYPE-ROLES.md

Role-based typography contract for the Equinet design system.
Companion to `tokens.css`. Ruling date: 2026-10-17.

---

## The rule

**Heading level and type size are independent choices.**

- Heading level (`<h1>`–`<h6>`) is decided by **document structure**. It must
  descend without skipping, and there is exactly one `<h1>` per page. This is a
  WCAG 2.1 AA requirement, not a style preference.
- Type size is decided by **visual role**. A role token names what a piece of
  text *is* (card heading, eyebrow, price), not where it sits in the outline.

These two decisions do not have to agree, and usually don't. On the pricing
page a single `<h3>` renders at four different sizes — 24px, 20px, 18px and
12px — because four different roles happened to sit at the same outline depth.

**Consequence:** never size text by reaching for `--equinet-fontsize-h3`
because the element is an `<h3>`. Pick the role token. The `hN` tokens below
are themselves roles, and they only coincide with the matching element when
the structure happens to line up.

Getting this backwards produces one of two failures, and both ship:
breaking the heading order to get the right size, or accepting the wrong size
to keep the order.

---

## Heading roles

| Role | Token | Size | Weight | Family | Typical element |
|---|---|---|---|---|---|
| Hero display | `--equinet-fontsize-display` | 60px | 800 | Open Sans | `<h1>` in a hero |
| Page title | `--equinet-fontsize-h1` | 56px | 800 | Open Sans | `<h1>` |
| **Section heading** | `--equinet-fontsize-h2` | **40px** | 800 | Open Sans | `<h2>` opening a section |
| **Section sub-heading** | `--equinet-fontsize-section-heading` | **36px** | 900 | Open Sans | `<h2>` *inside* a section |
| Block heading | `--equinet-fontsize-h3` | 32px | 700 | Open Sans | `<h3>` |
| Card heading | `--equinet-fontsize-card-heading` | 24px | 600 | Open Sans | `<h3>` / `<h4>` in a card |
| Minor heading | `--equinet-fontsize-h5` | 20px | 600 | Open Sans | `<h3>`–`<h5>` |
| Stat label | `--equinet-fontsize-stat` | 18px | 600 | Open Sans | `<h3>` / `<p>` |
| Eyebrow / kicker | `--equinet-fontsize-kicker` | 12px | 700 | Open Sans | `<p>` / `<span>` / `<h3>` |

## Non-heading roles

| Role | Token | Size | Weight | Family | Typical element |
|---|---|---|---|---|---|
| Price / headline figure | `--equinet-fontsize-price` | 48px | 800 | Open Sans | `<p>` — **never** an `<hN>`. Built as `.eq-price`; shadow `--equinet-shadow-heading--price`, tabular figures on |
| Lead paragraph | `--equinet-fontsize-lead` | 20px | 400 | Source Sans 3 | `<p>` after a heading |
| Body large | `--equinet-fontsize-body-lg` | 20px | 400 | Source Sans 3 | `<p>` |
| Body | `--equinet-fontsize-body` | 16px | 400 | Source Sans 3 | `<p>` |
| Button label | `--equinet-fontsize-btn` | 16px | 600 | Open Sans | `<button>` / `<a>` |
| Small | `--equinet-fontsize-small` | 14px | 400 | Source Sans 3 | `<p>`, `<figcaption>`, `<footer>` |
| Body small | `--equinet-fontsize-body-sm` | 12px | 400 | Source Sans 3 | `<p>` |
| Caption | `--equinet-fontsize-caption` | 11px | 600 | Source Sans 3 | `<span>` |

Weights and families above are what the shipped comps actually declare, not
estimates. Where a module needs a different weight for the same role, set the
weight explicitly and leave the size token alone.

---

## The h2 ruling

Three h2 values have been live at different points: 48px in the repo, 36px
deployed, 40px in `h2-fontstyle.svg`. As of 2026-10-17:

- `--equinet-fontsize-h2` **40px** is canonical. Any heading that *opens* a
  section takes it.
- `--equinet-fontsize-section-heading` **36px** is a sub-heading, used for a
  second-level heading *inside* a section.
- 48px is retired as a heading size. It survives only as
  `--equinet-fontsize-price`, which is a different role entirely.

**Migration note.** Existing comps predate this ruling. All seven `<h2>`
elements on the pricing page currently render at 36px, and
`2-column-comparison`, `sector-three-column-case-study` and
`cagr-four-column` all shipped 36px section headings. Under the ruling these
are section headings and belong at 40px. Treat the 36px in those comps as
drift to correct at build time, not as the design intent to reproduce.

This is the one place where **the comp is not ground truth.** Everywhere else
it is.

---

## Spacing roles

Spacing tokens follow a t-shirt ladder resolving to `--equinet-scale-*`
primitives:

| Token | Value | Role |
|---|---|---|
| `--equinet-space-3xs` | 4px | label-to-value gap; tight stack |
| `--equinet-space-2xs` | 8px | heading accent-line gap |
| `--equinet-space-xs` | 12px | modal close inset |
| `--equinet-space-sm` | 16px | laptop card gap; icon box |
| `--equinet-space-md` | 24px | gutter, grid gap, card padding — the workhorse |
| `--equinet-space-lg` | 32px | inter-CTA gap; heading-to-lead |
| `--equinet-space-xl` | 40px | eyebrow-to-heading gap |
| `--equinet-space-2xl` | 48px | cards-to-CTA gap |
| `--equinet-space-3xl` | 56px | mobile section padding (off-scale) |
| `--equinet-space-4xl` | 96px | desktop section padding (off-scale) |
| `--equinet-space-grid-column` | 80px | wide multi-column grid column-gap (off-ladder) |

---

## Known gaps

**1. 20px spacing is undecided.** The pricing page uses `20px` nine times —
`gap: 20px` (5), `padding: 20px 16px` (3), `padding: 16px 20px` (1). It sits
between `sm` (16px) and `md` (24px), both of which already exist and are both
used heavily on the same page.

Treat this as drift until someone rules otherwise. **Default: collapse to
`--equinet-space-md` (24px).** If 20px turns out to be a genuine role, name it
here before adding a token, not after.

**2. The ladder cannot absorb 80px.** 80px falls between `3xl` (56px) and
`4xl` (96px). Inserting it would mean resequencing every t-shirt name, which
breaks every module already consuming them. It is named by role instead
(`--equinet-space-grid-column`). If a third off-ladder value appears, the
ladder itself is the wrong abstraction and should be replaced with
scale-numbered space tokens in one deliberate breaking change.

**3. Line-height is not yet role-mapped.** The table above covers size,
weight and family only.

**4. This document and `assets/type/` disagree on family and weight.** Added
2026-10-17 when the two were put side by side. Every SIZE agrees; nothing
below is a size dispute.

| Role | This document | `assets/type/` export |
|---|---|---|
| Block heading (32px) | 700, Open Sans | **800**, Open Sans |
| Card heading (24px) | 600, Open Sans | **700, Source Sans** |
| Minor heading (20px) | 600, Open Sans | 600, **Source Sans** |
| Eyebrow (12px) | 700, Open Sans | 700, **Source Sans** |
| Section sub-heading (36px) | 900, Open Sans | not in the export set |

The two have different provenance and both are legitimate: this table is what
the shipped comps declare, `assets/type/` is what the Figma type styles
declare. Under this document's own rule the comp is ground truth everywhere
except the 36px h2 — which would settle it in favour of Open Sans — but a
Figma type style is the more deliberate artefact, and the gap is wide enough
(a whole family, on four roles) that it reads as two different intentions
rather than drift.

**It is already visible in `bundle.css`.** `.eq-card__title` sets Open Sans
600, built from `cagr-four-column`. `.eq-h3-card` sets Source Sans 700, built
from `h3-fontstyle-card-heading.svg`. Both ship, and a card heading renders
differently depending on which class a module reaches for. **Needs a ruling
before the next module build**, because this one is not cosmetic — it is two
different typefaces for the same role.

---

## How modules consume this

Per `token-conventions.md`, every module references tokens with a measured
fallback:

```css
.eq-card__title {
  font-size: var(--equinet-fontsize-card-heading, 24px);
  font-weight: 600;
}
```

The fallback is the value measured from the comp. It is a safety net for a
missing token, never a reason to skip the variable.

Off-scale values genuinely unique to one module stay local to that module and
are **not** promoted here. A value earns a token when it appears in a second
module, not the first.
