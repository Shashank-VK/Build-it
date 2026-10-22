# expansion-tools — Index

Workstream: expansion-tools · Research subagent · All records researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Sibling stream `cases-product` covered 24 tools in those companies' stacks. This workstream goes for **breadth beyond that**: 230 records across 18 lifecycle-stage files — niche, new, deprecated, abandoned, controversial, and hyped tools across the whole product-engineering lifecycle.

Status flags: **ACTIVE** / **MAINTAINED** / **EXPERIMENTAL** / **DEPRECATED** / **SUPERSEDED** / **UNAVAILABLE** / **CONTROVERSIAL**.
Use labels: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear.
Evidence labels: Verified / Corroborated / Inferred / Proposed / Unknown.

## Counts by status (230 records)

| Status | Count |
|---|---|
| ACTIVE | 195 |
| MAINTAINED | 18 |
| DEPRECATED | 11 |
| SUPERSEDED | 4 |
| EXPERIMENTAL | 1 |
| Unknown (status unverified) | 1 |
| **Total** | **230** |

## Files by lifecycle stage

| # | File | Stage | Records |
|---|---|---|---|
| 01 | [01-coding-agents.md](01-coding-agents.md) | Coding agents & AI IDEs | 15 |
| 02 | [02-agent-frameworks.md](02-agent-frameworks.md) | Agent frameworks & orchestration runtimes | 20 |
| 03 | [03-testing.md](03-testing.md) | Testing (E2E, unit, load) | 13 |
| 04 | [04-feature-flags-experimentation.md](04-feature-flags-experimentation.md) | Feature flags & experimentation | 13 |
| 05 | [05-cicd-gitops.md](05-cicd-gitops.md) | CI/CD & GitOps | 15 |
| 06 | [06-observability.md](06-observability.md) | Observability, monitoring & error tracking | 13 |
| 07 | [07-incident-management.md](07-incident-management.md) | Incident management, on-call & status | 10 |
| 08 | [08-design-prototyping.md](08-design-prototyping.md) | Design, prototyping & front-end generation | 16 |
| 09 | [09-documentation.md](09-documentation.md) | Documentation & developer portals | 12 |
| 10 | [10-analytics.md](10-analytics.md) | Product & web analytics | 10 |
| 11 | [11-ai-eval-harnesses.md](11-ai-eval-harnesses.md) | AI eval harnesses & LLM observability | 16 |
| 12 | [12-workflow-orchestration.md](12-workflow-orchestration.md) | Workflow orchestration & durable execution | 11 |
| 13 | [13-secrets-management.md](13-secrets-management.md) | Secrets management | 9 |
| 14 | [14-discovery-research.md](14-discovery-research.md) | Discovery & user research | 8 |
| 15 | [15-project-management.md](15-project-management.md) | Project management & issue tracking | 12 |
| 16 | [16-databases-caching.md](16-databases-caching.md) | Databases, caching & data infrastructure | 16 |
| 17 | [17-paas-deploy.md](17-paas-deploy.md) | PaaS, deploy platforms & self-hosted alternatives | 16 |
| 18 | [18-game-creative-runtimes.md](18-game-creative-runtimes.md) | Game engines & creative runtimes | 5 |
| — | [evidence-register.md](evidence-register.md) | Evidence register (sources, confidence, contradictions) | — |

## Status-flagged highlights

**DEPRECATED (11):** Amazon Q Developer (→Kiro), Continue.dev, Supermaven, AutoGen, BabyAGI, Travis CI, Opsgenie (sunset Apr 5, 2027), Adobe XD, TensorZero (archived Jun 2026), Height (shut down Sep 24, 2025), Pivotal Tracker (retired Apr 30, 2025).

**SUPERSEDED (4):** Semantic Kernel (→ Microsoft Agent Framework), Modyfi + Payload (→ Figma), Humanloop (acqui-hired by Anthropic).

**CONTROVERSIAL (flagged within records):** Cursor pricing backlash (Jun–Jul 2025); Vercel pricing (ongoing bill-shock saga); Datadog $65M bill + Delivery Hero → Grafana Cloud; Unity runtime fee (Sep 2023, cancelled Sep 2024); Figma AI-training class action (Khan v. Figma, Nov 2025); Inngest multi-day outage (Oct 2025).

**Narrative corrections (verified against primary sources):** FluxCD is NOT archived (CNCF graduated); LangChain is NOT dead (1.0 GA Oct 2025, $125M raise); AutoGPT is NOT dead (platform repo active Sep 2026; only Auto-GPT-Plugins archived Jun 2024); MkDocs Material is NOT in maintenance mode (claim disputed).

## Headline M&A / consolidation findings

- SpaceX acquired Cursor/Anysphere ($60B, closed Aug 14, 2026); OpenAI's Windsurf $3B deal collapsed → Google $2.4B acquihire → Cognition acquired Windsurf (Jul 2025) → rebranded Devin Desktop (Jun 2026); Cognition $48B valuation Sep 2026.
- Statsig acquired TWICE: OpenAI $1.1B (Sep 2025) → Amplitude took brand/customers (May 2026).
- Supabase raised $150M and agreed to acquire Turso (announced Oct 2, 2026 — 8 days before research date).
- Figma: $20B Adobe deal killed Dec 2023 ($1B fee) → $68B IPO Jul 2025 → stock ~$19 by Jun 2026.
- Eval-harness consolidation: Promptfoo → OpenAI, Langfuse → ClickHouse, Helicone → Mintlify (maintenance mode), Humanloop → Anthropic, Portkey → Palo Alto Networks, W&B → CoreWeave.
- FireHydrant → Freshworks (Dec 2025/Jan 2026); Split → Harness (Jun 2024, now FME); Fern → Postman (Jan 2026); Modyfi + Payload → Figma (2026).
- License sagas: Vault BSL→OpenBao; Terraform BSL→OpenTofu; Redis RSAL/SSPL→Valkey (won); Elasticsearch SSPL→OpenSearch (LF) + AGPLv3 added; MongoDB SSPL→DocumentDB; Sentry BSD-3→BSL→FSL; k6 is AGPL-3.0; Grafana AGPLv3; Unleash reported AGPL-3.0 in 2026 sources (was Apache-2.0 — verify).

## Honest gaps (depth debt)

- Lightly researched (1–2 sources, mostly secondary): OpenCode, SWE-agent, Tabnine named customers; Rasa ownership; Agno, SmolAgents, DSPy, Haystack, LlamaIndex, Flowise, Pydantic AI, Mastra, Strands, OpenAI/Claude Agent SDKs; Dify license; Flipt/flagd licenses; ConfigCat, Eppo, DevCycle; Dyad, Framer, Webflow, Lunacy; VitePress, MkDocs, Scalar, DocsGPT, GitBook, ReadMe, llms.txt; Fathom, Matomo, Heap, Pendo, June; DBOS, Camunda, Step Functions, BullMQ, Airflow, Dagster, Prefect, pg-boss; sops, ESO, Akeyless; Maze 2023–2026 status; **Sprig — status entirely unverified**; UserTesting, Hotjar, Clarity, Optimal Workshop, Great Question; Shortcut, Plane, Asana, Monday, ClickUp, Notion, OpenProject, Taiga; Dragonfly/KeyDB 2026 releases; Neon, PlanetScale, DuckDB, Garnet, TimescaleDB versions; Unreal, GameMaker, Bevy; Depot/Buildkite/CircleCI/Harness/Spacelift/Tekton/Drone/Jenkins current state; Squadcast, xMatters, Statuspage, Grafana IRM naming.
- LinkedIn: login wall prevented independent verification of public posts; GMTK/LinkedIn excerpt used with limitation noted.
- Wayback Machine: not needed — no dead-tool pages required it (archived repos' GitHub pages sufficed).
- Non-English sources: not used; no case required them.
- Inngest Oct 2025 outage: cited in a 2026 ADR but independent outage reports not pulled — flagged for verification.
