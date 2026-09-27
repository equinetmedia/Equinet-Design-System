# Asset renames — 2026-09-26

Every asset outside `buttons/`, `comps/` and `brand/` was renamed to one convention:
**lowercase kebab-case, group-prefixed, globally unique** — `<group>-<subject>.svg`.

Why group-prefixed rather than bare subjects: stripping the prefix causes collisions.
`ideal-customer-profile` exists as both a scene and a service tile, as does
`positioning-strategy`. Globally unique names let any file be cited unambiguously.

**Not renamed, deliberately:** `buttons/` and `comps/` keep their Figma layer-ID names
(`button_primary_large_default`, `module__2-column-hero-banner`). Those names *are* the
Figma layers, and PROMPT.md's build process maps back to Figma through them. `brand/` and
the three root icons were already clean.

`CHANGELOG.md` entries written before this date use the old names — this table resolves them.

## Typos corrected

| Was | Now | |
| --- | --- | --- |
| `narritive` | `narrative` | service tile |
| `verfied` | `verified` | node |
| `accuracye` | `accuracy` | marketing |
| `t0` | `to` | marketing |
| `rack` | `track` | marketing — "Using AI to track ABM engagement" |
| `GTPs` | `GPTs` | marketing — Custom GPTs (and Gems) |
| `build-environment` | `built-environment` | sector — the industry term is *built environment* |
| `node-black-*` | `node-*` | the ink is `#242630`, not black |

## Full map

| Old | New |
| --- | --- |
| `illustrations/scenes/Equinet-Media-brand-development-brand-consistency-v1.svg` | `illustrations/scenes/scene-brand-consistency.svg` |
| `illustrations/scenes/Equinet-Media-brand-development-ideal-customer-profile-v1.svg` | `illustrations/scenes/scene-ideal-customer-profile.svg` |
| `illustrations/scenes/Equinet-Media-brand-development-market-clarity-v1.svg` | `illustrations/scenes/scene-market-clarity.svg` |
| `illustrations/scenes/Equinet-Media-create-a-clear-positioning-strategy-v1.svg` | `illustrations/scenes/scene-positioning-strategy.svg` |
| `illustrations/scenes/Equinet-Media-create-a-unified-messaging-framework-v1.svg` | `illustrations/scenes/scene-messaging-framework.svg` |
| `illustrations/scenes/Equinet-Media-create-your-own-brand-ai-agent-v1.svg` | `illustrations/scenes/scene-brand-ai-agent.svg` |
| `illustrations/scenes/Equinet-Media-website-design-building-v1.svg` | `illustrations/scenes/scene-website-build.svg` |
| `illustrations/scenes/Equinet-Media-website-design-journey-mapping-v1.svg` | `illustrations/scenes/scene-journey-mapping.svg` |
| `illustrations/scenes/Equinet-Media-website-design-monitoring-improving-v1.svg` | `illustrations/scenes/scene-monitoring-improving.svg` |
| `illustrations/scenes/Equinet-Media-website-design-prototyping-v1.svg` | `illustrations/scenes/scene-prototyping.svg` |
| `illustrations/scenes/Equinet-Media-website-design-smart-goal-setting-v1.svg` | `illustrations/scenes/scene-smart-goal-setting.svg` |
| `illustrations/scenes/Equinet-Media-website-design-wireframing-v1.svg` | `illustrations/scenes/scene-wireframing.svg` |
| `illustrations/sectors/equinet-sector-b2b-software-pictograph.svg` | `illustrations/sectors/sector-b2b-software.svg` |
| `illustrations/sectors/equinet-sector-build-environment-pictograph.svg` | `illustrations/sectors/sector-built-environment.svg` |
| `illustrations/sectors/equinet-sector-build-environment-pictograph-1.svg` | `illustrations/sectors/sector-built-environment-animated.svg` |
| `illustrations/sectors/equinet-sector-networked-infrastructure-pictograph.svg` | `illustrations/sectors/sector-networked-infrastructure.svg` |
| `illustrations/systems/Account-management-expansion-enablement-c.svg` | `illustrations/systems/system-account-expansion.svg` |
| `illustrations/systems/Commercial-data-health-enrichment-c.svg` | `illustrations/systems/system-data-health-enrichment.svg` |
| `illustrations/systems/commercial-insight-and-feedback-loops.svg` | `illustrations/systems/system-insight-feedback-loops.svg` |
| `illustrations/systems/CRM-ERP-integration-d.svg` | `illustrations/systems/system-crm-erp-integration.svg` |
| `illustrations/systems/Sales-enablement-execution-support-c.svg` | `illustrations/systems/system-sales-enablement.svg` |
| `illustrations/flows/turning-your-commercial-data-into-an-uncorrupted-source-of-truth.svg` | `illustrations/flows/flow-data-source-of-truth.svg` |
| `illustrations/flows/make-your-technical-expertise-machine-readable.svg` | `illustrations/flows/flow-machine-readable-expertise.svg` |
| `illustrations/flows/smarter-content-operations-for-manufacturing-growth.svg` | `illustrations/flows/flow-content-operations.svg` |
| `illustrations/pictonodes/pictonode-linegraph.svg` | `illustrations/pictonodes/pictonode-line-graph.svg` |
| `illustrations/pictonodes/pictonode-paperreview.svg` | `illustrations/pictonodes/pictonode-paper-review.svg` |
| `illustrations/pictonodes/pictonode-piechart.svg` | `illustrations/pictonodes/pictonode-pie-chart.svg` |
| `illustrations/pictonodes/pictonode-thecde.svg` | `illustrations/pictonodes/pictonode-the-cde.svg` |
| `icons/service-tiles/services-commercial-narritive.svg` | `icons/service-tiles/tile-commercial-narrative.svg` |
| `icons/service-tiles/services-competitor-analysis.svg` | `icons/service-tiles/tile-competitor-analysis.svg` |
| `icons/service-tiles/services-digital-experience-alignment.svg` | `icons/service-tiles/tile-digital-experience-alignment.svg` |
| `icons/service-tiles/services-ideal-customer-profile.svg` | `icons/service-tiles/tile-ideal-customer-profile.svg` |
| `icons/service-tiles/services-positioning-audit.svg` | `icons/service-tiles/tile-positioning-audit.svg` |
| `icons/service-tiles/services-positioning-strategy.svg` | `icons/service-tiles/tile-positioning-strategy.svg` |
| `icons/service-tiles/services-sales-enablement-alignment.svg` | `icons/service-tiles/tile-sales-enablement-alignment.svg` |
| `icons/service-tiles/services-value-architecture.svg` | `icons/service-tiles/tile-value-architecture.svg` |
| `icons/nodes/node-black-attract.svg` | `icons/nodes/node-attract.svg` |
| `icons/nodes/node-black-connect.svg` | `icons/nodes/node-connect.svg` |
| `icons/nodes/node-black-growth.svg` | `icons/nodes/node-growth.svg` |
| `icons/nodes/node-black-hubspot.svg` | `icons/nodes/node-hubspot.svg` |
| `icons/nodes/node-black-verfied.svg` | `icons/nodes/node-verified.svg` |
| `marketing/Custom-GTPs-and-GEMs.svg` | `marketing/marketing-custom-gpts-and-gems.svg` |
| `marketing/Deploy-AI-to-generate-and-schedule-personalised-sequences.svg` | `marketing/marketing-ai-personalised-sequences.svg` |
| `marketing/GEO-Ops.svg` | `marketing/marketing-geo-ops.svg` |
| `marketing/HubSpot_Agents.svg` | `marketing/marketing-hubspot-agents.svg` |
| `marketing/TAMbot.svg` | `marketing/marketing-tambot.svg` |
| `marketing/The-Brand-Ops-Agent.svg` | `marketing/marketing-brand-ops-agent.svg` |
| `marketing/Use-AI-driven-scoring-to-focus-on-leads-most-likely-to-convert.svg` | `marketing/marketing-ai-lead-scoring.svg` |
| `marketing/Using-AI-t0-Trigger-workflows-from-account-activity.svg` | `marketing/marketing-ai-account-triggered-workflows.svg` |
| `marketing/Using-AI-to-rack-ABM-engagement-across-buying-groups-and-channels.svg` | `marketing/marketing-ai-abm-engagement-tracking.svg` |
| `marketing/commercial-systems-aeo-rewards-structure-and-accuracye-blue.svg` | `marketing/marketing-aeo-rewards-structure-and-accuracy.svg` |
| `marketing/commercial-systems-construction-and-deployment.svg` | `marketing/marketing-construction-and-deployment.svg` |
| `marketing/commercial-systems-hubspot-as-your-operational-core.svg` | `marketing/marketing-hubspot-operational-core.svg` |
| `marketing/commercial-systems-the-knowledge-base_091526.svg` | `marketing/marketing-knowledge-base.svg` |
| `marketing/equinet-media-abm-loop-marketing-hubspot.svg` | `marketing/marketing-abm-loop-hubspot.svg` |
| `marketing/equinet-media-the-infinity-loop.svg` | `marketing/marketing-infinity-loop.svg` |
| `marketing/how-equinet-media-enables-ai-augmented-sales.svg` | `marketing/marketing-ai-augmented-sales.svg` |
| `marketing/putting-your-market-map-to-work.svg` | `marketing/marketing-market-map.svg` |

Also removed earlier, not renamed: `icons/nodes/node-black-hubspot-1.svg`, a true
duplicate of `node-black-hubspot.svg` (now `node-hubspot.svg`).
