# Icon inventory

This folder is the shared home for Equinet's icon SVGs — one file per icon,
referenced by every module instead of each one carrying its own copy.

**Nothing is in here yet.** Every icon below is known only from what its
module's CSS says about it — size, colour behaviour, hover transform. None
of it is the actual `<svg>` markup, because that lives in each module's
`module.html`, which hasn't been shared in this project. Adding a real file
here means pasting in that module's actual inline SVG, not a plausible
recreation of it.

## Known icons, by evidence in CSS

| Icon | Seen in | Size | Colour | Hover |
| --- | --- | --- | --- | --- |
| Arrow (primary CTA) | `plain_hero_banner` | 15.63×13.13px | fixed white on fill | none |
| Arrow (textual CTA) | `plain_hero_banner` | 16×16px, stroke | `currentColor` | `translateX(8px)` |
| Arrow (textual CTA) | `sector-three-column-case-study` | unspecified | `currentColor` | `translateX(16px)` |
| Arrow (primary CTA) | `workshop_one_column` | 20×20px | `currentColor` | none noted |
| Arrow (textual CTA) | `single_narrow_text_column` (ESCATEC) | 14×14px, stroke-width 2, round caps | `currentColor` | `translateX(4px)` |
| Checkmark / check-circle | `workshop_one_column` bullet list | 26×26px | `currentColor` | none |
| Close (X) | `cim-methodology` video modal | 20×20px icon in a 44×44px circle | `currentColor`, stroke | none |
| External-link (pill) | `cagr-four-column` | 16×16px | `currentColor` | colour shift on parent hover |
| Play | `single_narrow_text_column` (ESCATEC) | 26×26px | — | — |

## A real problem, not just a gap

**The arrow isn't one icon.** Across five sightings it has three different
geometries — a small filled arrow (~15×13), a couple of stroke-based arrows
at different sizes and cap styles (14–16px), and a distinct 20px version —
plus the already-open disagreement on hover travel distance (8px vs. 16px).
Centralizing "the arrow" means picking one canonical shape first, the same
way card-hover and reduced-motion needed picking one pattern. That's a design
decision, not something resolvable from CSS alone.

## In the meantime: placeholder policy

Decided 2026-09-23. A neutral icon set (Lucide or similar) is an acceptable
stand-in where a design calls for an icon that isn't listed above yet — but
it must read as a placeholder, not be presented as a real Equinet icon.
Don't fabricate a plausible-looking custom shape instead; that's the same
invention this file's whole approach exists to avoid, just committed by hand
rather than by guessing at path data. See `README.md`, "Instructions for
AI-generated design," for the full rule.

## What's needed to fill this folder in

For each icon above: the module's `module.html` (or just the inline `<svg>…
</svg>` block for that one icon, pasted directly). Once real markup exists
for at least the arrow, checkmark and close icon, this file gets replaced by
the actual `.svg` files plus a short index describing which module used to
own each one.
