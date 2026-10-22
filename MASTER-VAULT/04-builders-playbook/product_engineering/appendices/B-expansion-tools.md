# Appendix B — Expansion Tools Digest

**Source:** `research/expansion-tools/` (18 lifecycle-stage files + index + evidence register), researched 2026-10-10. Read-only research; neutral records — no rankings, no recommendations. 230 records total: breadth beyond the 24 tools covered in the sibling `cases-product` stream — niche, new, deprecated, abandoned, controversial, and hyped tools across the whole product-engineering lifecycle.

Status flags: **ACTIVE** / **MAINTAINED** / **EXPERIMENTAL** / **DEPRECATED** / **SUPERSEDED** / **UNAVAILABLE** / **CONTROVERSIAL**. Use labels: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Evidence labels: Verified / Corroborated / Inferred / Proposed / Unknown. All labels preserved as assigned by the research.

---

## 1. Status counts (230 records)

| Status | Count |
|---|---|
| ACTIVE | 195 |
| MAINTAINED | 18 |
| DEPRECATED | 11 |
| SUPERSEDED | 4 |
| EXPERIMENTAL | 1 |
| Unknown (status unverified) | 1 |
| **Total** | **230** |

**DEPRECATED (11):** Amazon Q Developer (→Kiro), Continue.dev, Supermaven, AutoGen, BabyAGI, Travis CI, Opsgenie (sunset Apr 5, 2027), Adobe XD, TensorZero (archived Jun 2026), Height (shut down Sep 24, 2025), Pivotal Tracker (retired Apr 30, 2025).

**SUPERSEDED (4):** Semantic Kernel (→ Microsoft Agent Framework), Modyfi + Payload (→ Figma), Humanloop (acqui-hired by Anthropic).

**CONTROVERSIAL (flagged within records):** Cursor pricing backlash (Jun–Jul 2025); Vercel pricing (ongoing bill-shock saga); Datadog $65M bill + Delivery Hero → Grafana Cloud; Unity runtime fee (Sep 2023, cancelled Sep 2024); Figma AI-training class action (Khan v. Figma, Nov 2025); Inngest multi-day outage (Oct 2025).

---

## 2. The most surprising findings, grouped by lifecycle stage

### Coding agents & AI IDEs
- **The coding-agent acquisition cascade of 2025–2026.** SpaceX acquired Cursor/Anysphere ($60B, closed Aug 14, 2026); OpenAI's $3B Windsurf deal collapsed → Google's $2.4B acquihire → Cognition acquired Windsurf (Jul 2025) → rebranded Devin Desktop (Jun 2026); Cognition at a $48B valuation by Sep 2026. The agent-IDE layer consolidated into a handful of owners within a year.
- **Verified-absent narratives corrected:** LangChain is NOT dead (1.0 GA Oct 2025, $125M raise); AutoGPT is NOT dead (platform repo active Sep 2026 — only Auto-GPT-Plugins was archived, Jun 2024); FluxCD is NOT archived (CNCF graduated); MkDocs Material is NOT in maintenance mode (claim disputed).

### Agent frameworks & orchestration
- **AutoGen deprecated; Semantic Kernel superseded** by the Microsoft Agent Framework — the 2023–2024 agent-framework boom thinned fast, with even Microsoft consolidating its own two frameworks into one.
- Depth debt noted: Agno, SmolAgents, DSPy, Haystack, LlamaIndex, Flowise, Pydantic AI, Mastra, Strands, and the OpenAI/Claude Agent SDKs were lightly researched (1–2 secondary sources) — flagged for a follow-up pass.

### Feature flags & experimentation
- **Statsig was acquired TWICE.** Sep 2025: OpenAI acquired Statsig for ~$1.1B (all-stock) — Raji became OpenAI CTO of Applications; Statsig to operate independently from Seattle. May 2026: Amplitude took over the Statsig *brand and customer base* while the engineering team that built it stayed at OpenAI. Roadmap ownership is now split across two companies — a genuinely unusual acquisition structure, and competitor migration guides actively target the resulting uncertainty.

### Databases, caching & data infrastructure
- **Supabase agreed to acquire Turso** (announced Oct 2, 2026 — eight days before the research date): a $150M round (GIC-led; CapitalG, IronArc, SquarePeg) paired with the acquisition (price undisclosed; close not yet confirmed). Turso founder Glauber Costa becomes Head of Agentic Services; the thesis stated in coverage is the "agent database" — 70% of new databases created by AI agents — with Postgres + SQLite (Turso's libSQL/MIT) under one roof and a Turso→Postgres graduation path via Multigres. Turso's platform keeps operating; analyst guidance circulating: take independent backups, request 12-month price locks and change-of-control termination rights.

### Design, prototyping & front-end generation
- **The Figma arc.** $20B Adobe acquisition killed Dec 2023 ($1B breakup fee) → $68B IPO Jul 2025 → stock ~$19 by Jun 2026. Figma also acquired Modyfi and Payload (2026), and faces a Nov 2025 AI-training class action (Khan v. Figma). Adobe XD — the product Adobe chose over the deal — is deprecated.

### Game engines & creative runtimes
- **Godot overtook Unity** — GMTK Game Jam 2026: Godot #1 for the first time with 47% (4.9k games) vs Unity 34%, the first time in 9 years Unity didn't lead. Five-year trajectory: 16% (2022) → 19% → 37% → 39% → 47%. Commercial proof: Slay the Spire 2 moved from Unity to Godot (2026); Brotato, Buckshot Roulette, Cassette Beasts, Dome Keeper shipped on Godot. The causal backdrop is the Sep 2023 per-install runtime-fee announcement — massive backlash, cancelled Sep 2024, CEO departed, ~15% of US advertisers reportedly left. Unity 6.0 LTS reaches end of support Oct 2026. Godot's limitations are recorded too: no official console export (platform SDK NDAs vs. open license — must go through W4 Games' W4 Consoles), C# web export unsupported in 4.6, less mature mobile monetization tooling.

### CI/CD & GitOps
- **Travis CI deprecated** — the former default CI of open source is a deprecated record. Depth debt: Depot, Buildkite, CircleCI, Harness, Spacelift, Tekton, Drone, and Jenkins current state were lightly researched.

### Incident management, on-call & status
- **Opsgenie sunsets Apr 5, 2027** — Atlassian is killing its own on-call product (consolidating into Jira Service Management/Ops). FireHydrant was acquired by Freshworks (Dec 2025/Jan 2026).

### Observability
- **Datadog's $65M bill** and Delivery Hero's migration to Grafana Cloud are the flagged cost-controversy records — observability pricing as a line item large enough to drive vendor switches.

### AI eval harnesses & LLM observability
- **Eval-harness consolidation was the fastest in the set:** Promptfoo → OpenAI, Langfuse → ClickHouse, Helicone → Mintlify (maintenance mode), Humanloop → Anthropic (acqui-hire), Portkey → Palo Alto Networks, W&B → CoreWeave. The LLM-observability layer was largely absorbed by larger platforms within the research window.

### Secrets management
- **The license saga cluster:** Vault BSL → OpenBao fork; Terraform BSL → OpenTofu; Redis RSAL/SSPL → Valkey (won); Elasticsearch SSPL → OpenSearch (LF) + AGPLv3 added; MongoDB SSPL → DocumentDB; Sentry BSD-3 → BSL → FSL. k6 is AGPL-3.0; Grafana AGPLv3. Unleash reported AGPL-3.0 in 2026 sources (was Apache-2.0 — verify). The 2023–2026 relicensing wave is the through-line: open-core vendors tightening licenses, communities forking.

### Workflow orchestration
- **Inngest multi-day outage (Oct 2025)** — cited in a 2026 ADR; independent outage reports not pulled, flagged for verification.

### Project management & issue tracking
- **Height shut down Sep 24, 2025; Pivotal Tracker retired Apr 30, 2025** — two product-management tools exited in the research window. Sprig's status is entirely unverified (flagged).

### PaaS & deploy platforms
- Vercel pricing bill-shock saga ongoing (flagged CONTROVERSIAL); Fern acquired by Postman (Jan 2026).

---

## 3. The 18 stage files (pointers)

All files in `research/expansion-tools/`; each contains per-tool records (purpose, status, maintenance, limitations, real-vs-proposed use) with evidence labels:

1. `01-coding-agents.md` — Coding agents & AI IDEs (15 records)
2. `02-agent-frameworks.md` — Agent frameworks & orchestration runtimes (20)
3. `03-testing.md` — Testing: E2E, unit, load (13)
4. `04-feature-flags-experimentation.md` — Feature flags & experimentation (13)
5. `05-cicd-gitops.md` — CI/CD & GitOps (15)
6. `06-observability.md` — Observability, monitoring & error tracking (13)
7. `07-incident-management.md` — Incident management, on-call & status (10)
8. `08-design-prototyping.md` — Design, prototyping & front-end generation (16)
9. `09-documentation.md` — Documentation & developer portals (12)
10. `10-analytics.md` — Product & web analytics (10)
11. `11-ai-eval-harnesses.md` — AI eval harnesses & LLM observability (16)
12. `12-workflow-orchestration.md` — Workflow orchestration & durable execution (11)
13. `13-secrets-management.md` — Secrets management (9)
14. `14-discovery-research.md` — Discovery & user research (8)
15. `15-project-management.md` — Project management & issue tracking (12)
16. `16-databases-caching.md` — Databases, caching & data infrastructure (16)
17. `17-paas-deploy.md` — PaaS, deploy platforms & self-hosted alternatives (16)
18. `18-game-creative-runtimes.md` — Game engines & creative runtimes (5)
- `00-index.md` — counts, M&A/consolidation findings, narrative corrections, honest gaps (reproduced above)
- `evidence-register.md` — per-record sources, confidence, contradictions

---

## 4. Honest gaps (from the research)

- **Lightly researched records** (1–2 sources, mostly secondary) are flagged throughout the stage files: OpenCode, SWE-agent, Tabnine named customers; Rasa ownership; Agno, SmolAgents, DSPy, Haystack, LlamaIndex, Flowise, Pydantic AI, Mastra, Strands, OpenAI/Claude Agent SDKs; Dify license; Flipt/flagd licenses; ConfigCat, Eppo, DevCycle; Dyad, Framer, Webflow, Lunacy; VitePress, MkDocs, Scalar, DocsGPT, GitBook, ReadMe, llms.txt; Fathom, Matomo, Heap, Pendo, June; DBOS, Camunda, Step Functions, BullMQ, Airflow, Dagster, Prefect, pg-boss; sops, ESO, Akeyless; Maze 2023–2026 status; **Sprig — status entirely unverified**; UserTesting, Hotjar, Clarity, Optimal Workshop, Great Question; Shortcut, Plane, Asana, Monday, ClickUp, Notion, OpenProject, Taiga; Dragonfly/KeyDB 2026 releases; Neon, PlanetScale, DuckDB, Garnet, TimescaleDB versions; Unreal, GameMaker, Bevy; Depot/Buildkite/CircleCI/Harness/Spacelift/Tekton/Drone/Jenkins current state; Squadcast, xMatters, Statuspage, Grafana IRM naming.
- LinkedIn's login wall prevented independent verification of public posts (GMTK/LinkedIn excerpt used with limitation noted).
- The Inngest Oct 2025 outage is cited in a 2026 ADR; independent outage reports were not pulled — flagged for verification.
- Wayback Machine not needed (no dead-tool pages required it); non-English sources not used (no case required them).

Workspace path: `~/workspace/your_files/atlas/product_engineering/research/expansion-tools/`
