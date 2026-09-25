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
2. **If nothing fits, use nothing.** This set covers Equinet's own service
   lines and sectors. A page about a topic outside that — general technology
   commentary, consumer trends, third-party products — has no matching
   illustration here, and the correct output is a layout with no illustration
   rather than a loosely-related one. Recomposition doesn't rescue a subject
   mismatch: rearranged parts of the wrong illustration are still the wrong
   illustration.
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
   `sectors/equinet-sector-build-environment-pictograph-1.svg`.** It carries an
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

## `flows/` — 1209 × 675, transparent

Horizontal four-step sequences. Use where content genuinely has an ordered
progression; the form implies sequence, so don't use one for a set of
unordered items.

| File | Depicts | Topics |
| --- | --- | --- |
| `turning-your-commercial-data-into-an-uncorrupted-source-of-truth` | Data cleaned into a single trusted source | data quality, source of truth, CRM data, governance |
| `make-your-technical-expertise-machine-readable` | Expertise structured for machines to parse | machine-readable, structured data, AEO, technical content |
| `smarter-content-operations-for-manufacturing-growth` | Content operations for manufacturers | content ops, manufacturing, publishing workflow |

These three suit AEO and structured-content subjects better than anything
else in the set — `make-your-technical-expertise-machine-readable` in
particular is the only illustration that directly depicts machine-readability.

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

## Also selectable: `assets/icons/service-tiles/`

Eight 65 × 65 white-on-navy tiles, one per service. Smaller and more compact
than a scene — use in a service list, a card row or beside a heading, where a
641 × 360 scene would dominate. Same selection rules apply.

| File | Topics |
| --- | --- |
| `services-commercial-narritive` | narrative, story, commercial messaging |
| `services-competitor-analysis` | competitors, benchmarking, landscape |
| `services-digital-experience-alignment` | digital experience, UX alignment |
| `services-ideal-customer-profile` | ICP, targeting, audience |
| `services-positioning-audit` | positioning, audit, assessment |
| `services-positioning-strategy` | positioning, strategy, differentiation |
| `services-sales-enablement-alignment` | sales enablement, alignment |
| `services-value-architecture` | value, pricing, architecture, offer design |

Three overlap in subject with `scenes/` (ICP, positioning strategy, sales
enablement). Pick by scale, not by preference: a tile for a list item, a scene
for a media panel.

---

## Not selectable: `assets/comps/`

Three 1920px module comps live in `assets/comps/`. They are **never** a
choice here — each pictures an entire rendered module, headings and buttons
included, so placing one in a page embeds a fake module as a flat image. They
are reference for parity QA only.

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
