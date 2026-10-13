---
id: illustration-index
status: current
read_when: >-
  Choosing artwork for a section — the per-file subject and topic table. Read
  this before placing any illustration, and before deciding none matches.
depends_on: assets/manifest.json
verified: 2026-10-13
---

# Illustration selection index

For agents choosing artwork. One row per file: what it depicts, the topics it
suits, and how it can be placed. Read this before picking an illustration;
don't select on filename alone.

## These are reference, not sealed artifacts

The illustrations are **artistic and styling reference**. A file can be placed
whole, cropped, scaled, overlapped or rearranged — and its elements can be
pulled out and recombined into new compositions. Layout and formation are
free.

What is **not** free is the design language. Typography, iconography and
colour come from the source of truth regardless of how the graphics are
arranged:

| Free to change | Must follow source of truth |
| --- | --- |
| Arrangement, position, overlap | Colour — every value from `tokens.css` |
| Crop, scale, aspect ratio | Typography — `tokens.css` type scale, never the comp's own text |
| Which elements are used, and how many | Iconography — `assets/icons/`, and `ICON-REFERENCE.md` for substitutes |
| Combining elements across files | Spacing rhythm — the `equinet-space-*` scale |

## Selection rules

1. **Match on subject, not vibe.** Every row below has a Topics column. A file
   is a candidate when the page's subject is in one — whether you're placing
   it whole or taking parts from it.
2. **If no whole illustration fits, compose one — never ship nothing.**
   This set's *subject imagery* covers Equinet's service lines and sectors, so
   a page on another topic won't find a whole illustration that depicts it.
   Don't place a mismatched one. Instead, build a bespoke graphic from the
   set's **structural primitives** — cards, connectors, nodes, panels,
   line-work, accent — which carry no subject of their own and are usable for
   any topic. The distinction: a drawn wireframe depicts wireframing and only
   fits that subject; a card-connector-node flow depicts nothing until you give
   it content. See `skills/equinet-layout/references/visual-kit.md` for the
   primitives and composition recipes.
3. **Recolour only to a token.** Recomposition makes recolouring possible, and
   that's where drift gets in. Any colour on an extracted element must resolve
   to a token in `tokens.css`. Do not sample a colour out of the artwork and
   assume it's canonical — several files carry values that are *not* tokens:
   `#292D32` in the hero comp, and the unresolved near-white cluster
   (`#ECEAEA`, `#F3F2F2`, `#F3F3F4`). Copying one of those forward propagates
   an open question into new artwork.
4. **Extracting from `scenes/` means separating the element from its ground.**
   All 12 carry an opaque navy gradient across the full artboard. Pull an
   element out and it loses that background — which may be exactly what you
   want, but the element was drawn to read against dark. Check contrast
   against whatever surface it lands on.
5. **Don't extract from
   `sectors/sector-built-environment-animated.svg`.** It carries an
   embedded `2s linear infinite` animation with no `prefers-reduced-motion`
   guard. Taking parts from it carries that defect into new work. Use its
   static twin.
6. **Whole files: don't mix aspect ratios in one row.** `scenes/`, `sectors/`
   and `systems/` are all 16:9 and interchangeable. `pictonodes/` are square.
   This applies to placing files as-is; a recomposed graphic sets its own
   frame.

---

## `scenes/` — 641 × 360, OPAQUE dark gradient

| File | Depicts | Topics |
| --- | --- | --- |
| `scene-brand-consistency` | Consistency across brand touchpoints | brand, consistency, guidelines, identity |
| `scene-ideal-customer-profile` | Defining the target customer | ICP, targeting, audience, segmentation |
| `scene-market-clarity` | Clarifying market position | market, clarity, positioning, research |
| `scene-positioning-strategy` | Building a positioning strategy | positioning, strategy, differentiation |
| `scene-messaging-framework` | A single messaging framework | messaging, framework, copy, narrative |
| `scene-brand-ai-agent` | A brand-trained AI agent | AI agent, automation, brand AI |
| `scene-website-build` | Building the site | web build, development, implementation |
| `scene-journey-mapping` | Mapping the user journey | journey, UX, flow, mapping |
| `scene-monitoring-improving` | Measuring and iterating | analytics, monitoring, optimisation, CRO |
| `scene-prototyping` | Interactive prototypes | prototype, design, iteration |
| `scene-smart-goal-setting` | Setting measurable goals | goals, KPI, planning, metrics |
| `scene-wireframing` | Wireframe layout blocks | wireframe, layout, IA, structure |

## `sectors/` — 641 × 361, OPAQUE light gradient (`#F6F5F5` → white)

| File | Depicts | Topics |
| --- | --- | --- |
| `sector-b2b-software` | B2B software vertical | SaaS, software, B2B tech |
| `sector-built-environment` | Built environment vertical | construction, property, infrastructure |
| `sector-built-environment-animated` | As above, **animated** | — **see the warning in `README.md`: unguarded infinite animation** |
| `sector-networked-infrastructure` | Networked infrastructure vertical | networks, utilities, telecoms, connectivity |

## `systems/` — 460 × 259, transparent

| File | Depicts | Topics |
| --- | --- | --- |
| `system-account-expansion` | Account growth and expansion | account management, expansion, upsell, retention |
| `system-data-health-enrichment` | Data quality and enrichment | data health, enrichment, hygiene, CRM data |
| `system-insight-feedback-loops` | Insight and feedback cycles | insight, feedback loops, reporting |
| `system-crm-erp-integration` | Systems integration | CRM, ERP, integration, HubSpot, architecture |
| `system-sales-enablement` | Supporting sales execution | sales enablement, execution, sales ops |

## `flows/` — 1209 × 675, transparent

Horizontal four-step sequences. Use where content genuinely has an ordered
progression; the form implies sequence, so don't use one for a set of
unordered items.

| File | Depicts | Topics |
| --- | --- | --- |
| `flow-data-source-of-truth` | Data cleaned into a single trusted source | data quality, source of truth, CRM data, governance |
| `flow-machine-readable-expertise` | Expertise structured for machines to parse | machine-readable, structured data, AEO, technical content |
| `flow-content-operations` | Content operations for manufacturers | content ops, manufacturing, publishing workflow |

These three suit AEO and structured-content subjects better than anything
else in the set — `flow-machine-readable-expertise` in
particular is the only illustration that directly depicts machine-readability.

## `pictonodes/` — 118 × 118 square, transparent

Small spot graphics. Use beside a heading or list item, not as a hero.

| File | Depicts | Topics |
| --- | --- | --- |
| `pictonode-line-graph` | Line graph on a panel | growth, trend, performance, metrics |
| `pictonode-multitask` | Connected work streams | multitasking, parallel work, coordination |
| `pictonode-paper-review` | Document under review | documentation, review, audit |
| `pictonode-pie-chart` | Segmented chart with nodes | data, share, distribution, analysis |
| `pictonode-review` | Review / approval cycle | review, approval, QA, iteration |
| `pictonode-stack` | Layered stack | stack, layers, architecture, tech stack |
| `pictonode-the-cde` | The CDE | CDE, common data environment, shared data |
| `pictonode-website` | Website / browser frame | website, web page, online presence |

## Also selectable: `assets/icons/service-tiles/`

Eight 65 × 65 white-on-navy tiles, one per service. Smaller and more compact
than a scene — use in a service list, a card row or beside a heading, where a
641 × 360 scene would dominate. Same selection rules apply.

| File | Topics |
| --- | --- |
| `tile-commercial-narrative` | narrative, story, commercial messaging |
| `tile-competitor-analysis` | competitors, benchmarking, landscape |
| `tile-digital-experience-alignment` | digital experience, UX alignment |
| `tile-ideal-customer-profile` | ICP, targeting, audience |
| `tile-positioning-audit` | positioning, audit, assessment |
| `tile-positioning-strategy` | positioning, strategy, differentiation |
| `tile-sales-enablement-alignment` | sales enablement, alignment |
| `tile-value-architecture` | value, pricing, architecture, offer design |

Three overlap in subject with `scenes/` (ICP, positioning strategy, sales
enablement). Pick by scale, not by preference: a tile for a list item, a scene
for a media panel.

---

## `heroes/` — 1200 × ~1092 (1.10), transparent

Service-page heroes. Near-square — never in a 16:9 row. They carry outlined
card text, so recompose by moving whole cards, not by editing labels.

| File | Depicts | Topics |
| --- | --- | --- |
| `hero-commercial-intelligence-engine` | Five service pillars around a central engine | commercial intelligence, methodology, services overview |
| `hero-commercial-data` | Interlocking gears with data cards | commercial data, rev ops, pipeline, market sizing, account records |
| `hero-account-based-marketing` | ABM tier gauge | account based marketing, ABM, one-to-one, targeting |
| `hero-why-hubspot` | HubSpot logo with dashboard cards | HubSpot, CRM, commercial systems, reporting |

`hero-why-hubspot` recolours HubSpot's logo against HubSpot's trademark
guidelines and shows mock dashboard figures — read its notes in
`README.md` before using it.

## Data charts: `assets/charts/`

Seven sourced charts on AI adoption in manufacturing. Selectable when the
page's subject is AI in manufacturing — but they're data, not illustration, so
different rules apply: **never edit or retype their figures.** The numbers are
outlined in the SVGs; rebuild the chart live from `assets/charts/data.json`,
which holds every figure with its source and a verified / transcribed /
not-quotable status. See `assets/charts/README.md` — one chart's bars aren't
drawn to scale and three carry source or label errors.

| File | Topics |
| --- | --- |
| `chart-ai-results-not-universal` | AI ROI, AI strategy, AI knowledge gap |
| `chart-ai-adoption-manufacturing-2025` | AI adoption stage, company size, manufacturing |
| `chart-ai-leaders-widening-gap` | AI leaders, competitive gap, KPI impact |
| `chart-ai-targets-achieved` | AI targets, AI success rate |
| `chart-robotic-arms-roi` | robotics, physical AI, cycle time, operational cost |
| `chart-ai-industry-output` | economic output, GVA, sector impact |
| `chart-ai-adoption-barriers` | AI barriers, expertise gap, integration, implementation cost |

## Layout blueprints: `assets/comps/`

Four 1920px module comps live in `assets/comps/`. They're real, shipped
Equinet compositions — use them as **layout blueprints**: reproduce their
structure, spacing and hierarchy with live components and this page's
content. The one thing not to do is embed a comp as a flat image, since each
pictures a whole rendered module with its own text and buttons. Rebuild what
it shows; don't paste it.

## Subject coverage, and what it excludes

This set covers Equinet's own service lines (brand development, website
design, commercial systems), its target sectors, and generic business process
concepts. It does **not** cover: consumer technology, social platforms,
AI ethics or AI-safety commentary, psychology or behavioural science,
addiction or wellbeing, news or current affairs, or anything about a
third-party product.

A page on one of those topics should ship with no illustration from this set.
Rule 2 exists for exactly that case — the nearest-looking file is still the
wrong file.
