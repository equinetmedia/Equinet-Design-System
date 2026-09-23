# Equinet

A design system for HubSpot CMS modules, first built on 2026-09-22 from six
standing directive documents, `/modules/tokens.css`, and the CSS of
`cim-methodology` and `plain_hero_banner` (the only two modules with real CSS
available at that point). It was extended the same day once `cagr-four-column`,
`sector-three-column-case-study`, `pencil_testimonial` and `workshop_one_column`
were read in full — see **Component inventory** for exactly which of the
fourteen shipped modules are verified against real CSS versus named from
build history only. Every value here is traced to a Figma export, a
directive, or a shipped module — nothing is approximated.

Updated 2026-09-23 to incorporate the full Figma variable system (collections:
brand, alias, mapped, responsive) — colour ramps, border system, canonical type
scale, paragraph spacing, and responsive spacing modes are now reconciled against
the Figma file (key `A3XMvWX47Tf1191jomeEmH`).

The system serves one thing: drag-and-drop modules an editor can place, restyle
and reorder without breaking the design. That constraint — and the fact that
the "user" of most of these rules is a content editor, not a developer — shapes
almost everything below.

---

## Table of contents

1. [How it is consumed](#how-it-is-consumed)
2. [Governance](#governance)
3. [Colour](#colour)
4. [Data visualization](#data-visualization)
5. [Diagram illustration](#diagram-illustration)
6. [Foundation paint styles](#foundation-paint-styles)
7. [Type](#type)
8. [Spacing](#spacing)
9. [Border system](#border-system)
10. [Breakpoints](#breakpoints)
11. [Motion](#motion)
12. [Buttons](#buttons)
13. [Cards](#cards)
14. [Backgrounds and parallax](#backgrounds-and-parallax)
15. [Editor-controlled styling](#editor-controlled-styling)
16. [Icons](#icons)
17. [Brand mark](#brand-mark)
18. [Pictographs](#pictographs)
19. [Technical diagrams](#technical-diagrams)
20. [Commercial systems](#commercial-systems)
21. [Accessibility](#accessibility)
22. [Engineering contract](#engineering-contract)
23. [Component inventory](#component-inventory)
24. [Patterns library](#patterns-library)
25. [Figma file structure](#figma-file-structure)
26. [Open decisions](#open-decisions)

---

## How it is consumed

Modules load `/modules/tokens.css` on line 1 of `module.html` and read every
value through a custom property:

```html
{{ require_css(get_asset_url('/modules/tokens.css')) }}
