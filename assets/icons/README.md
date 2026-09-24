# Icons

Three real icons, extracted from the Figma button exports on 2026-09-23 —
verbatim path data, with viewBoxes computed from true bounding boxes using a
path parser, not retyped coordinates. Each takes `currentColor`, so the
button's own colour change moves the icon with it.

**What belongs here:** small, single-ink glyphs that sit inside a control
beside a label, take `currentColor`, and read correctly at 16–26px. Anything
multi-colour, detailed, or meant to stand alone as a graphic is an
illustration — see `assets/illustrations/`, which holds the eight
"pictonode" spot illustrations added 2026-09-23 for exactly this reason.
The `currentColor` rule is the quick test: if flattening it to one ink would
ruin it, it isn't an icon.

| File | Size | Used by | Source export |
| --- | --- | --- | --- |
| `arrow-chevron.svg` | 24 × 24 | Textual button, navigation button | `button_textual_default.svg` |
| `arrow-solid.svg` | 15.627 × 13.129 | Primary button | `button_primary_large_default.svg` |
| `play-circle.svg` | 26 × 26 | Primary button, video variant | `button_primary_video_default.svg` |

The two arrows are genuinely different shapes, not one icon at two sizes:
the chevron is a 2px round-capped stroke pair, the solid arrow is a filled
path. That's what made "centralize the arrow" unanswerable before real source
existed — there was nothing to centralize *to*. Both now have a canonical
file; a module picks the one its button variant uses.

Sizes confirmed against two independent sources: `plain_hero_banner`'s CSS
comment records the solid arrow as "15.63 x 13.13", and
`single_narrow_text_column` sizes its play icon 26 × 26. The measured
bounding boxes match both.

## Usage

Inline the markup in `module.html` rather than linking the file — HubSpot
modules embed SVG directly, and `currentColor` only inherits from an inline
element. These files are the canonical copy to paste from.

Decorative icons carry `aria-hidden="true"` and `focusable="false"`; an icon
carrying meaning on its own needs an accessible name instead.

## Still missing

`close` (from `cim-methodology`'s video modal, 20 × 20 in a 44 × 44 circle),
`checkmark` / check-circle (from `workshop_one_column`'s bullet list, 26 × 26)
and `external-link` (from `cagr-four-column`'s pill, 16 × 16). Known from
their modules' CSS — size and colour behaviour — but no geometry, because no
`module.html` carrying them has been shared. The placeholder policy below
still applies to these three.

## Placeholder policy

Decided 2026-09-23. A neutral icon set (Lucide or similar) is an acceptable
stand-in where a design calls for an icon not listed above — but it must read
as a placeholder, not be presented as a real Equinet icon. Don't fabricate a
plausible-looking custom shape instead; the three icons above exist precisely
because real geometry was measured rather than guessed.
