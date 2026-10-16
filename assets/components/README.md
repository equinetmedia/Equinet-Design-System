---
id: component-sources
status: current
read_when: >-
  Building or checking the eyebrow. Holds the Figma exports these components
  were measured from, what the measurements are, and when the solid variant
  is allowed.
depends_on: components/bundle.css
verified: 2026-10-16
---

# `components/` — Figma exports of components, not artwork

These are the design source of record for a component, the same role
`assets/buttons/` plays for the buttons. **Never place one on a page.** They
carry live `<text>`, so the type renders from whatever font the viewer has;
the component is built in CSS and the export is what you measure against.

Added 2026-10-16.

## `eyebrow-plain` / `eyebrow-solid` — 115 × 32

The small uppercase label above a heading. Built as `.eq-eyebrow` and
`.eq-eyebrow--solid` in `components/bundle.css`.

| Measured | Value | Token |
| --- | --- | --- |
| Size | 12px | `--equinet-fontsize-kicker` |
| Weight | bold / 700 | `--equinet-fontweight-kicker` |
| Tracking | 0.2em | `--equinet-letterspacing-kicker` |
| Label | `#E06730` | `--equinet-color-orange` |
| Pill fill | `#FCE9E0` | `--equinet-color-orange--pale` |
| Pill radius | `rx="8"` | `--equinet-radius-pill` |
| Side inset | text at `x="24"` | `--equinet-space-md` |
| Frame | 115 × 32 | 10px + 12px line + 10px |

Everything resolves to an existing token. Nothing new was needed.

One thing not to copy from the export: it names the family **Source Sans
Pro**, which is the old name for what this system calls
`--equinet-font-body` (`'Source Sans 3'`). Use the token.

The pill height is built from padding rather than a fixed `32px`, so a long
label wraps instead of overflowing. The 0.2em of tracking hangs off the last
letter, so the CSS indents by the same amount to put it back on the left —
without that the label sits 2.4px right of centre in the pill, which is
visible at this size.

## When `--solid` is allowed

**Hero banners, CTA banners, and modules carrying exceptional value. Nothing
else.** The plain eyebrow is the default and is almost always the right one.

The pill is emphasis, and emphasis that appears on every section stops being
emphasis. If a page has more than one or two, they are decoration and the
plain variant was the right call.

## Contrast — unresolved, and now shipped

Measured, 12px at weight 700:

| Label on | Ratio | |
| --- | --- | --- |
| `orange--pale` (the pill) | 2.90:1 | fails |
| white | 3.41:1 | fails |
| `surface--alt` | 3.14:1 | fails |
| navy | 3.08:1 | fails |

12px bold is **not** large text — that needs 18.66px bold or 24px regular —
so the threshold is 4.5:1 and every ground fails it. This is the "One
unresolved" item in `README.md`, and these assets are what it was about.

Two compliant forms exist in `bundle.css` for when a build can't carry the
risk:

- `.eq-eyebrow--solid-safe` — the same pill with the label in
  `--equinet-color-text`: **12.93:1**. Navy would give 8.95:1.
- `.eq-eyebrow--on-dark` — `--equinet-color-orange--pale` as the label on a
  dark module ground, where orange fails against both navy and night.

There is precedent for accepting the orange: the white primary-button label
was accepted by the client at 3.4:1 on 2026-09-21. That exception was
explicitly scoped so it "does not extend to any other component", so this one
needs its own decision rather than inheriting that one.
