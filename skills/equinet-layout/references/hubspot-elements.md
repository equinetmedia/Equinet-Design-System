---
id: hubspot-elements
status: current
read_when: >-
  Choosing which shipped Equinet module or native HubSpot capability carries
  the reader's next step.
depends_on: skills/equinet-layout/SKILL.md
verified: 2026-10-13
---

# HubSpot elements

Every section should answer "what does the reader do next?" — and the answer
is carried by either an Equinet module or a HubSpot capability. This file maps
both. Pick the element from the reader's next action, not from what's
available.

## Equinet modules (built, reusable)

These are shipped custom modules. Prefer them — they already follow the
design system, and reusing one is cheaper and more consistent than building.

| Module | Carries | Use when |
| --- | --- | --- |
| `plain_hero_banner` | Eyebrow, headline, lead, CTA pair | Opening a page with one clear proposition |
| `2-column-hero-banner` | Hero with media column | Opening with a proposition plus a supporting visual |
| `EQ Workshop Hero Banner` | Event/workshop hero | Promoting a workshop or session |
| `cagr-four-column` | Four cards with stat rows | Several comparable figures, each with context |
| `growth_cards` | Card row, canonical lift hover | 3–5 equal-weight points |
| `2-column-comparison` | Side-by-side with divider | Two options, before/after |
| `5_column_block_process` | Five-step sequence | An ordered method |
| `2_column_intelligence_engine_steps` | Steps with explanation | A process that needs a paragraph per step |
| `2_column_commercial_diagnostics` | Diagnostic content | Assessment or audit framing |
| `sector-three-column-case-study` | Sector cards + case study | Proof by sector, real client outcomes |
| `pencil_testimonial` | Quote, avatar, attribution | A real, attributed endorsement |
| `tabbed_navigation`, `_v2` | Tabbed panels | Peer views of one topic |
| `workshop_one_column` | Single column with bullets | Focused explanation, checklist |
| `cim-methodology` | Methodology cards + modal | A named methodology, video walk-through |
| `EQNewsletterSubscription` | Newsletter sign-up | Ongoing-relationship CTA |

`2_column_intelligence_engine_steps` renders its styles inline rather than
through `module.css` — a known portal constraint, not an error. Don't
"correct" it.

## HubSpot capabilities

Native features a section can hand off to. Names and availability vary by
subscription tier — confirm in the portal before committing a brief to one.

| Reader's next action | HubSpot capability | Notes |
| --- | --- | --- |
| Give details, download something | **Form** | The standard conversion point. Keep fields to what the next step genuinely needs. |
| Book time with someone | **Meetings** scheduling embed | Strongest intent signal; place after proof, not before. |
| Watch an explanation | **Video** | Pairs with `.btn-primary--video` and the `play-circle` icon. |
| Get content matched to who they are | **Smart content** / personalisation rules | Varies a section by lifecycle stage, list membership, source or location. |
| Read related material | **Blog listing / related posts** | Supports a pillar page's topic cluster. |
| Search the site | **Site search** | Only on resource-heavy pages. |

## The CTA trade-off — raise it, don't resolve it silently

The design system **forbids `{% cta %}`**: Equinet buttons are native anchors
styled with `.btn-primary` and its variants, so they stay on-brand and fully
token-driven.

That has a real cost. HubSpot's current CTA editor supports **A/B testing and
smart (personalised) CTAs**; a hand-built `.btn-primary` anchor does neither.
HubSpot's legacy CTA editor sunset has been postponed and both editors remain
available, so the native tool is a live option, not a dying one.

So:

- **Default:** `.btn-primary` anchors. Correct for almost every section.
- **If a brief calls for testing or personalising a CTA,** flag it as a
  deliberate exception to the design system for the user to decide — the
  capability exists only in HubSpot's CTA tool, and building it means
  accepting HubSpot-styled output there. Never quietly swap in a `{% cta %}`.
- Smart content (above) can often personalise the *surrounding section*
  while leaving the button a standard `.btn-primary` — worth offering first,
  since it keeps the brand rule intact.

## AEO-supporting elements

- **FAQ / accordion** — the one format that is literally question-and-answer,
  so it maps directly onto how answer engines extract content. No Equinet
  component exists yet; build it and flag it as new. Keep each answer
  self-contained.
- **Tables** — extract cleanly when content is genuinely tabular.
- **Structured headings** — question-shaped H2s throughout.

## One CTA per section, one primary per page

A section asks for one action. A page has one primary goal; secondary actions
use `.btn-textual`. Three competing primary buttons at the end of a page
dilute every one of them.
