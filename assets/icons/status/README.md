---
id: icon-status
status: current
read_when: >-
  Marking something as included, approved, achieved or true — in a comparison
  table, a table, a bullet list or a chart. The four check exports, how they
  map to .eq-check, which one each ground takes, how absence is marked, and
  the accessible-name rule.
depends_on: components/bundle.css, tokens.css
verified: 2026-10-19
---

# `status/` — the check, and the system's touch of teal

Four Figma exports of one icon: a check in a circle, 32 × 32. They are the
reference geometry for `.eq-check` in `components/bundle.css`. **Don't inline
them directly** — their colours are hard-coded hex, so they cannot follow the
ground they sit on. The component takes the same geometry and reads its
colours from custom properties instead.

Added 2026-10-19. The first group in `assets/icons/` that exists to carry a
signal rather than depict a subject.

## When to use it — the trigger

Mark a thing with a check when it is **included, approved, achieved or true**,
in one of four places:

| Where | What gets the check | Never |
| --- | --- | --- |
| **Comparison table** | a cell where the option has the feature | a cell where it doesn't — that gets `.eq-check--none` |
| **Table** | a status or approval column | a column that is only a count or a label |
| **Bullet list** | a list where *every* item is included, achieved or approved — `.eq-list--check` | an ordinary list. Five neutral facts with checks claims all five are approvals |
| **Chart** | a series or data point that meets a *stated* target, in the legend or an annotation, with the target named in text | decoration, or a point with no target |

It is a **signal, never decoration.** A page that scatters checks to look
positive teaches readers to stop reading them.

## The four exports

| File | Class | Ring | Fill | Mark |
| --- | --- | --- | --- | --- |
| `CheckCircle-Outline.svg` | `.eq-check--ink` | `heading` | none | `heading` |
| `CheckCircle-Outline-600.svg` | `.eq-check` *(default)* | `teal-600` | none | `teal-600` |
| `CheckCircle-Dutone.svg` | `.eq-check--duotone` | `teal-600` | `teal-200` | `teal-600` |
| `CheckCircle-Fill.svg` | `.eq-check--fill` | none | `teal-default` | `blue-950` |

Every colour already had a token; nothing was added. `#2A7989` is
`--equinet-color-teal-600`, which is what the "600" in the filename means.
The `Dutone` spelling is the Figma layer name and is kept so the export stays
traceable.

The default is the lightest touch — a teal outline with no fill. Reach for
`--duotone` when a list or table needs more presence, and `--ink` where teal is
not wanted.

## The ground decides the variant

Measured as non-text contrast. WCAG 1.4.11 asks for 3:1 on a graphic the
reader needs in order to understand the content.

| Variant | White | `surface--alt` | Card over navy | Navy | `blue-950` |
| --- | --- | --- | --- | --- | --- |
| `teal-600` outline / duotone ring | 5.01 | 4.60 | 3.48 | **2.10** | 3.74 |
| `ink` | 15.05 | 13.83 | 10.46 | **1.43** | **1.24** |
| `teal-default` (fill circle) | **2.12** | **1.95** | **1.47** | 4.96 | 8.82 |

The fill variant's mark is 8.82:1 against its own fill, which is why it works
on dark. On light the mark still carries the meaning but the circle's edge
doesn't, so **fill is a dark-ground form.**

**This is enforced, not just stated.**
- `.eq-surface--dark` forces the fill form whatever variant was named.
- A `.eq-card` inside a dark surface resets to the light form, because a card
  is a light panel even there: 80% white over navy renders `#CCD9E2`, where
  the teal-default circle would measure 1.47:1. It is the same trap as the card
  title colours fixed on 2026-10-19, and it would have shipped the same way.

**A gap, not papered over.** No outline or duotone was supplied for dark
grounds, so on dark every variant collapses to fill. If a quieter dark-ground
form is wanted — a teal-default outline, say — it needs designing.

## Absence is marked, never blank

An empty cell in a comparison table reads as *not included*, *not applicable*
or *not known*, and a reader cannot tell which. `.eq-check--none` is a plain
dash with its own accessible name. It is muted grey on light (5.99:1 on white)
and `charade-300` on dark (5.25:1 on navy). Added by me alongside the check
because a check is unusable in a comparison table without it; it was not in the
exports.

## The accessible name

- **Beside visible text → decorative.** `aria-hidden="true"`.
- **The only indicator, a table cell → named.** `role="img"` and an
  `aria-label`. Without it a screen reader meets an empty cell. Colour and
  shape are not a name.

```html
<span class="eq-check" role="img" aria-label="Included"><svg viewBox="0 0 32 32"
  aria-hidden="true" focusable="false"><circle class="eq-check__ring" cx="16"
  cy="16" r="13.3333"/><path class="eq-check__mark"
  d="M21.3334 12L14 19.3333L10.6667 16"/></svg></span>

<span class="eq-check eq-check--none" role="img" aria-label="Not included"></span>
```

Colour is never the only signal either: inclusion is a check shape and absence
is a dash, so a reader who cannot tell teal from grey still gets both
(WCAG 1.4.1).

`tools/check-built-page.py` fails a page where a `.eq-check` has neither, and
where a table marks inclusion with checks but leaves cells blank.

## The bullet list

`.eq-list--check` keeps the markup a clean `<ul><li>` with no SVG in each item.
The circle is a bordered pseudo-element and the mark a masked one, because a
mask carries no colour and so can still take a token. The variant class goes
on the `<ul>`:

```html
<ul class="eq-list--check eq-check--duotone">
  <li>Scoped before set-up</li>
</ul>
```

The check is decorative there — the list's own heading says what it is. A
list with some items included and some not is a comparison table, not a check
list.

## Open question: teal now means two things

The chart palette was ruled on 2026-10-13 as navy, orange and teal, with teal as
a plain categorical series colour. A check makes teal a *status* signal. A
reader who has learned that teal means good from the checks on the page may
read a teal bar as a good bar. **Until this is ruled on:** in a chart that
carries a check, don't draw a series in teal unless it is the one that
achieved the target.

## Limits

- The list's circle and mark are CSS-drawn, so anti-aliasing differs very
  slightly from the inline SVG.
- `1lh`, which centres the list icon on the first line of text, is recent. A
  browser without it keeps the icon at the top of the item, a pixel or two off.
