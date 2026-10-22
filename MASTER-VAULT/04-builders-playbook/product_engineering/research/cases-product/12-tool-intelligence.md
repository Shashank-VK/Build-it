# §30 — Tool Intelligence Register

Workstream: cases-product · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations. Status checked against public sources as of 2026-10-10.

Legend: **U(Verified)** = real company demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear.

---

## TI-01 — PostgreSQL
- Purpose / problem: Open-source relational database; transactional core for ChatGPT/API and Stripe's ledger-adjacent workloads.
- OSS/commercial: Open source (PostgreSQL licence).
- Integration: Standard SQL clients, drivers, ORMs; Azure Flexible Server / self-hosted.
- Maintenance: Active (community releases; PostgreSQL 17/18 line current in 2026 — general public record).
- Availability: Widely available, all major clouds.
- Version/doc date: Referenced via OpenAI eng disclosure Jan 2026.
- Limitations: Single-primary write scaling ceiling; MVCC bloat/vacuum under heavy writes; replica fan-out cost (per OpenAI).
- Security: Standard hardening applies; keep minor versions patched.
- Alternatives: MySQL/InnoDB, CockroachDB, Spanner, Aurora.
- Switching costs: High at scale (data gravity, sharding, app coupling).
- Use: U(Verified) — OpenAI (single-primary + ~50 replicas, Jan 2026 disclosure); U(Verified) — Stripe (sharded Postgres in data layer, per secondary architecture narrative).

## TI-02 — PgBouncer
- Purpose: PostgreSQL connection pooler; cut OpenAI's connection setup 50ms→5ms.
- OSS/commercial: Open source (ISC).
- Integration: Sits between app and Postgres; minimal app changes.
- Maintenance: Active (long-standing community project).
- Availability: OSS; managed by some cloud vendors.
- Limitations: Transaction-pooling mode restricts session-level features (prepared statements, advisory locks).
- Security: Runs with DB credentials; must be in the trust boundary.
- Alternatives: Pgpool-II, Odyssey, cloud-native poolers (RDS Proxy, AlloyDB).
- Switching costs: Low–medium.
- Use: U(Verified) — OpenAI (named in eng disclosure via reporting).

## TI-03 — Azure Cosmos DB
- Purpose: Globally distributed multi-model database; reported migration target for OpenAI's write-heavy/shardable workloads.
- OSS/commercial: Commercial (Microsoft Azure).
- Integration: Azure-native SDKs; multiple APIs (SQL, Mongo, Cassandra, Table).
- Maintenance: Active commercial service.
- Limitations: Cost model complexity; consistency/latency trade-offs per API.
- Security: Azure IAM, encryption at rest/in transit; standard cloud-shared-responsibility.
- Alternatives: DynamoDB, Spanner, CockroachDB, MongoDB Atlas.
- Switching costs: High (data model + cloud lock-in).
- Use: U(Proposed) — reported as OpenAI's migration direction for shardable workloads (single secondary source). Not verified as completed.

## TI-04 — Codex CLI (openai/codex)
- Purpose: OpenAI's terminal coding agent; reads repos, edits files, runs commands in sandboxed loops.
- OSS/commercial: Open source, Apache-2.0.
- Integration: Local CLI; `codex exec` for CI/scripting; MCP support; AGENTS.md instructions.
- Maintenance: Active as of 2026 (rewritten TypeScript→Rust mid-2025; ~0.155 line, 1,100+ releases per Oct 2026 secondary review). Notable: repo reportedly no longer accepts external pull requests — open-source in licence, not in governance.
- Availability: Public on GitHub; sign-in via ChatGPT plan or API key.
- Limitations: Trust-domain choices (sandbox modes); no external PR acceptance limits community fixes.
- Security: Sandboxed execution modes; `--yolo` disables approvals (dangerous by design).
- Alternatives: Claude Code, Cursor, Windsurf, Aider.
- Switching costs: Low (CLI-level).
- Use: U(Verified) — OpenAI uses it internally for its own development ("no private version," per product lead via press).

## TI-05 — Claude Code
- Purpose: Anthropic's agentic coding harness (CLI/desktop/IDE).
- OSS/commercial: Commercial/proprietary harness (ships with Claude subscriptions/plans).
- Integration: Terminal, IDE extensions; MCP; filesystem-coordinated agent teams (experimental).
- Maintenance: Active; Dynamic Workflows research preview with Opus 4.8 (May 2026, single secondary source).
- Limitations: Context-window management is the discipline (per Anthropic's own guidance).
- Security: Sandboxed sessions; privacy controls that also slow debugging (per Anthropic postmortem).
- Alternatives: Codex CLI, Cursor, Aider.
- Switching costs: Low–medium (workflow lock-in).
- Use: U(Verified) — Anthropic's own product; agent-team filesystem pattern documented by community.

## TI-06 — MCP (Model Context Protocol)
- Purpose: Open protocol for connecting agents to tools/data (servers expose schemas).
- OSS/commercial: Open specification (Anthropic-originated, community-maintained).
- Integration: Client (agent) ↔ MCP servers; schema definitions consumed as context.
- Maintenance: Active; growing ecosystem in 2026.
- Limitations: Schema bloat inflates context/cost (Uber's 2026 cost work targeted exactly this); each server is new attack surface.
- Security: Central policy enforcement via gateway recommended (Uber pattern); tool permissions per server.
- Alternatives: OpenAPI function-calling, custom tool APIs, LSP-style integrations.
- Switching costs: Medium (tooling standardisation).
- Use: U(Verified) — Uber routes 1,000+ MCP server interactions through a unified gateway (Sep 2026, via Uber eng blog reporting).

## TI-07 — Chaos Monkey / Simian Army (Netflix)
- Purpose: Random instance termination to force failure-tolerant design.
- OSS/commercial: Open source, Apache-2.0.
- Integration: AWS; Spinnaker + MySQL dependencies (community docs).
- Maintenance: **SimianArmy: RETIRED** (official repo status, read 2026-10-10). Standalone Netflix/chaosmonkey exists but shows sparse recent activity — treat as low-maintenance; verify before use.
- Limitations: AWS/Spinnaker-coupled; retired suite has no support.
- Security: Terminates production instances by design — needs tight scoping/ RBAC.
- Alternatives: LitmusChaos, Chaos Mesh, Gremlin, AWS Fault Injection Simulator, Steadybit.
- Switching costs: Medium (experiment design, safety rails).
- Use: U(Verified) — Netflix (historical; suite retired, functionality moved to other Netflix projects).

## TI-08 — Security Monkey (Netflix)
- Purpose: AWS security-posture monitoring.
- OSS/commercial: Open source, Apache-2.0.
- Maintenance: **Archived by owner Sep 17, 2021 — read-only.** Deprecated; do not adopt.
- Alternatives: Prowler, CloudSploit, AWS Security Hub, Wiz.
- Use: U(Verified) — Netflix (historical).

## TI-09 — Backstage (Spotify → CNCF)
- Purpose: Internal developer portal framework (service catalog, golden-path templates, docs-as-code).
- OSS/commercial: Open source, Apache-2.0; CNCF Incubation.
- Integration: React/TypeScript frontend, Node backend (New Backend System stable since Sep 2024); plugins for CI/CD, K8s, observability.
- Maintenance: Active — monthly releases (as of Sep 2026), 1,000+ contributors.
- Availability: Public; Spotify for Backstage marketplace (commercial add-ons).
- Version/doc date: Monthly cadence; legacy backend removed Dec 2024.
- Limitations: Real adoption cost (React/Node platform team); golden-path secrets handling needs care (see CVE-2025-55285).
- Security: CVE-2025-55285 (Scaffolder fetch:template log flaw, fixed 2.1.1, Aug 2025) — keep updated; audit template inputs.
- Alternatives: Port, Cortex, OpsLevel, Roadie, custom portals.
- Switching costs: High (catalog modelling, plugin development, cultural adoption).
- Use: U(Verified) — Spotify (origin, ~90% daily internal usage reported); 3,400+ orgs per 2026 reporting.

## TI-10 — Sorbet (Stripe)
- Purpose: Gradual type checker for Ruby.
- OSS/commercial: Open source (Apache-2.0).
- Integration: Ruby codebases; gradual sigils; VS Code extension.
- Maintenance: Open-source project from Stripe; 2026 activity not verified in this pass — **status check incomplete (debt)**.
- Limitations: Gradual-typing overhead; ecosystem smaller than TS.
- Security: Build-time tool; low runtime surface.
- Alternatives: RBS/Steep, TypeScript (with JS), gradual typing via tests.
- Switching costs: Medium (annotation effort; codemod-assisted).
- Use: U(Verified) — Stripe (Ruby monolith; first-party SED transcript + ex-employee accounts).

## TI-11 — TypeScript
- Purpose: Typed superset of JavaScript.
- OSS/commercial: Open source, Apache-2.0 (Microsoft).
- Integration: Universal in JS toolchains.
- Maintenance: Active.
- Limitations: Migration suppression debt (Stripe: 97k→37k suppressions); type-system soundness gaps.
- Security: Build-time; supply-chain via npm as usual.
- Alternatives: Flow (declining), JSDoc checking, ReScript.
- Switching costs: Medium–high at millions of lines; codemods help.
- Use: U(Verified) — Stripe Dashboard (3.7M+ lines migrated from Flow/JS).

## TI-12 — React Native
- Purpose: Cross-platform mobile (React → native).
- OSS/commercial: Open source, MIT (Meta).
- Integration: iOS/Android; New Architecture (Fabric/JSI/TurboModules) from 0.76+.
- Maintenance: Active.
- Limitations: 2018-era bridge issues (async init, debugging) are the ones behind Airbnb's sunset; New Architecture changes the calculus.
- Security: Standard mobile-app concerns; bridge/native-module review.
- Alternatives: Flutter, native Swift/Kotlin, KMP.
- Switching costs: High (Airbnb's 3-platform-support lesson).
- Use: U(Verified) — Airbnb (2016–2018, sunset); U(Verified) — Shopify/Discord/Meta/Coinbase ship RN at scale per 2025 counter-analysis (Corroborated, not independently verified here).

## TI-13 — Apache Kafka
- Purpose: Distributed event streaming; Uber's GPS-ping shock absorber.
- OSS/commercial: Open source, Apache-2.0.
- Integration: Broad client ecosystem; needs ZooKeeper/KRaft ops.
- Maintenance: Active.
- Limitations: Operational complexity; exactly-once semantics need care.
- Security: ACLs, TLS, SASL; schema registry governance.
- Alternatives: Pulsar, Redpanda, Kinesis, Pub/Sub.
- Switching costs: High (pipeline rewiring).
- Use: U(Verified) — Uber (driver location ingestion).

## TI-14 — H3 (Uber)
- Purpose: Hexagonal hierarchical geospatial index.
- OSS/commercial: Open source, Apache-2.0.
- Integration: Libraries in multiple languages.
- Maintenance: Active (public repo; 2026 activity not re-verified this pass — minor debt).
- Limitations: Approximation by design; edge cases at cell boundaries.
- Security: N/A (library).
- Alternatives: S2 (Google), geohash, quadtrees.
- Switching costs: Low (library).
- Use: U(Verified) — Uber (matching/ETA).

## TI-15 — Schemaless (Uber)
- Purpose: Internal key-value-over-sharded-MySQL with buffered writes, triggers, global indexes.
- OSS/commercial: Internal/proprietary — no public open-source release located; treat as not publicly available.
- Integration: Internal only.
- Maintenance: Internal (Uber).
- Limitations: Not adoptable externally; schema-flexibility traded for query power.
- Alternatives: Vitess, PlanetScale, CockroachDB, DynamoDB.
- Switching costs: N/A externally.
- Use: U(Verified) — Uber (internal datastore; first-party eng blog).

## TI-16 — EVCache (Netflix)
- Purpose: Distributed in-memory cache (memcached-based) for low-latency reads.
- OSS/commercial: Open source (Netflix).
- Integration: Memcached protocol; Netflix control plane.
- Maintenance: Public repo exists; 2026 activity not verified — debt.
- Limitations: Cache-consistency design burden.
- Alternatives: ElastiCache, Memorystore, Redis.
- Switching costs: Medium.
- Use: U(Verified) — Netflix.

## TI-17 — Spinnaker (Netflix-origin)
- Purpose: Multi-cloud continuous delivery.
- OSS/commercial: Open source (now community-governed; Netflix-origin).
- Integration: Kubernetes/VM targets; Chaos Monkey historically integrated.
- Maintenance: Active community project.
- Limitations: Heavyweight to operate.
- Alternatives: Argo Rollouts, Flux, Harness.
- Switching costs: High.
- Use: U(Verified) — Netflix (chaos tooling dependency per community docs).

## TI-18 — nginx / OpenResty + Lua
- Purpose: Edge throttle (leaky bucket), queue page, signed cookies for flash-sale protection.
- OSS/commercial: Open source.
- Integration: Reverse proxy / edge.
- Maintenance: Active.
- Limitations: Lua scripting ops burden.
- Alternatives: Envoy, Cloudflare Workers, AWS WAF rate limiting.
- Switching costs: Low–medium.
- Use: U(Verified) — Shopify (edge throttle per playbook citing Shopify eng blog).

## TI-19 — MySQL / InnoDB
- Purpose: Relational store under Schemaless and Shopify pods.
- OSS/commercial: Open source (GPL); commercial editions exist.
- Integration: Universal.
- Maintenance: Active.
- Limitations: Feature set vs Postgres for some workloads; operational sharding needed at scale.
- Alternatives: Postgres, MariaDB, TiDB.
- Switching costs: High at scale.
- Use: U(Verified) — Uber (Schemaless substrate); U(Verified) — Shopify (pod databases).

## TI-20 — Linear / Slack / Notion / Databricks / Datadog (agent context sources)
- Purpose: Issue tracking, comms, docs, data, observability — consumed as agent context by OpenAI's Codex.
- OSS/commercial: All commercial SaaS.
- Integration: APIs/webhooks; MCP servers increasingly.
- Maintenance: Active commercial.
- Limitations: Context bloat; access-permission sprawl when agents read everything.
- Security: Agent access = new insider-threat surface; scope tokens, audit reads.
- Alternatives: Jira, Confluence, etc.
- Switching costs: High (organisational).
- Use: U(Verified) — OpenAI (Codex context sources per Pragmatic Engineer interview).

## TI-21 — Replit Agent platform (dev/prod separation, Neon Postgres)
- Purpose: In-browser agentic development with managed databases.
- OSS/commercial: Commercial SaaS; Neon Postgres commercial.
- Integration: Web IDE; database provisioning.
- Maintenance: Active; post-incident guardrails (automatic dev/prod separation, staging envs, chat-only mode) rolled out Jul 2025.
- Limitations: Agent root-cause ability at infra layer is weak (Helium postmortem); pre-2025 design allowed prod DB access from dev.
- Security: Destructive-action permission boundaries now systemic; verify current state before use.
- Alternatives: GitHub Codespaces, Cursor cloud agents, Codex web.
- Switching costs: Medium.
- Use: U(Verified) — Replit (own product; incident record).

## TI-22 — GitHub Copilot (product + metrics APIs)
- Purpose: AI pair programmer; code review agent.
- OSS/commercial: Commercial (GitHub).
- Integration: IDE plugins, CLI, metrics APIs (org/enterprise/user reports).
- Maintenance: Active; Rust runtime migration 2026 (single secondary source).
- Limitations: Acceptance ≠ quality; vendor-graded review metrics need independent benchmarks.
- Security: Code-suggestion filtering exists; enterprise audit via metrics APIs.
- Alternatives: Cursor, Amazon Q, Codeium/Windsurf, Tabnine.
- Switching costs: Medium (workflow + training data habits).
- Use: U(Verified) — GitHub (own product; telemetry published in peer-reviewed research).

## TI-23 — Observability/plugin ecosystem around Backstage (Prometheus, Grafana, Datadog, PagerDuty, Kubernetes plugin)
- Purpose: Monitoring/alerting/orchestration surfaced inside the developer portal.
- OSS/commercial: Mixed (Prometheus/Grafana/K8s OSS; Datadog/PagerDuty commercial).
- Maintenance: All active.
- Use: U(Verified) — surfaced as Backstage plugins in production IDPs (Corroborated via Backstage docs/ADR evidence).

## TI-24 — Toxiproxy
- Purpose: Chaos/fault-injection proxy for Game Days (Shopify).
- OSS/commercial: Open source (Shopify-origin, MIT).
- Integration: TCP proxy with toxic behaviours (latency, down, bandwidth).
- Maintenance: Community-maintained; check activity before adoption (not re-verified 2026 — debt).
- Use: U(Verified) — Shopify (Game Days).

## Notable status findings (deprecated / superseded / governance caveats)
- Netflix/SimianArmy — **RETIRED** (official).
- Netflix/security_monkey — **archived Sep 2021, read-only**.
- openai/codex — active but **external PRs not accepted** (open licence, closed governance) — verify before contributing.
- TypeScript implementation of Codex CLI — **superseded by Rust implementation** (same repo).
- Schemaless — internal only, **not publicly available**.
- Sorbet, EVCache, Toxiproxy, H3 — **2026 activity not re-verified**; treat as maintenance-check debt.
