# Illustration selection index

For agents choosing artwork. One row per file: what it depicts, the topics it
suits, and how it can be placed. Read this before picking an illustration;
don't select on filename alone.

## Selection rules

1. **Match on subject, not vibe.** Every row below has a Topics column. If the
   page's subject isn't in one, the illustration doesn't fit.
2. **If nothing fits, use nothing.** This set covers Equinet's own service
   lines and sectors. A page about a topic outside that — general technology
   commentary, consumer trends, third-party products — has no matching
   illustration here, and the correct output is a layout with no illustration
   rather than a loosely-related one. A mismatched graphic reads as filler and
   undermines the page.
3. **Respect the background constraint.** `scenes/` are **opaque**, with a
   baked-in navy-to-blue gradient covering the full artboard. They work as
   media panels, hero blocks and card headers. They do **not** work dropped on
   a white surface as if transparent — there'll be a hard dark rectangle. Every
   other group is transparent and sits on any background.
4. **Don't mix aspect ratios in one row.** `scenes/`, `sectors/` and `systems/`
   are all 16:9 and interchangeable. `pictonodes/` are square.
5. **Never recolour.** These are delivered artwork. If the palette clashes with
   the section, change the section, not the file.

---

## `scenes/` — 641 × 360, OPAQUE dark gradient

| File | Depicts | Topics |
| --- | --- | --- |
| `Equinet-Media-brand-development-brand-consistency-v1` | Consistency across brand touchpoints | brand, consistency, guidelines, identity |
| `Equinet-Media-brand-development-ideal-customer-profile-v1` | Defining the target customer | ICP, targeting, audience, segmentation |
| `Equinet-Media-brand-development-market-clarity-v1` | Clarifying market position | market, clarity, positioning, research |
| `Equinet-Media-create-a-clear-positioning-strategy-v1` | Building a positioning strategy | positioning, strategy, differentiation |
| `Equinet-Media-create-a-unified-messaging-framework-v1` | A single messaging framework | messaging, framework, copy, narrative |
| `Equinet-Media-create-your-own-brand-ai-agent-v1` | A brand-trained AI agent | AI agent, automation, brand AI |
| `Equinet-Media-website-design-building-v1` | Building the site | web build, development, implementation |
| `Equinet-Media-website-design-journey-mapping-v1` | Mapping the user journey | journey, UX, flow, mapping |
| `Equinet-Media-website-design-monitoring-improving-v1` | Measuring and iterating | analytics, monitoring, optimisation, CRO |
| `Equinet-Media-website-design-prototyping-v1` | Interactive prototypes | prototype, design, iteration |
| `Equinet-Media-website-design-smart-goal-setting-v1` | Setting measurable goals | goals, KPI, planning, metrics |
| `Equinet-Media-website-design-wireframing-v1` | Wireframe layout blocks | wireframe, layout, IA, structure |

## `sectors/` — 641 × 361, transparent

| File | Depicts | Topics |
| --- | --- | --- |
| `equinet-sector-b2b-software-pictograph` | B2B software vertical | SaaS, software, B2B tech |
| `equinet-sector-build-environment-pictograph` | Built environment vertical | construction, property, infrastructure |
| `equinet-sector-build-environment-pictograph-1` | As above, **animated** | — **see the warning in `README.md`: unguarded infinite animation** |
| `equinet-sector-networked-infrastructure-pictograph` | Networked infrastructure vertical | networks, utilities, telecoms, connectivity |

## `systems/` — 460 × 259, transparent

| File | Depicts | Topics |
| --- | --- | --- |
| `Account-management-expansion-enablement-c` | Account growth and expansion | account management, expansion, upsell, retention |
| `Commercial-data-health-enrichment-c` | Data quality and enrichment | data health, enrichment, hygiene, CRM data |
| `commercial-insight-and-feedback-loops` | Insight and feedback cycles | insight, feedback loops, reporting |
| `CRM-ERP-integration-d` | Systems integration | CRM, ERP, integration, HubSpot, architecture |
| `Sales-enablement-execution-support-c` | Supporting sales execution | sales enablement, execution, sales ops |

## `pictonodes/` — 118 × 118 square, transparent

Small spot graphics. Use beside a heading or list item, not as a hero.

| File | Depicts | Topics |
| --- | --- | --- |
| `pictonode-linegraph` | Line graph on a panel | growth, trend, performance, metrics |
| `pictonode-multitask` | Connected work streams | multitasking, parallel work, coordination |
| `pictonode-paperreview` | Document under review | documentation, review, audit |
| `pictonode-piechart` | Segmented chart with nodes | data, share, distribution, analysis |
| `pictonode-review` | Review / approval cycle | review, approval, QA, iteration |
| `pictonode-stack` | Layered stack | stack, layers, architecture, tech stack |
| `pictonode-thecde` | The CDE | CDE, common data environment, shared data |
| `pictonode-website` | Website / browser frame | website, web page, online presence |

---

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
