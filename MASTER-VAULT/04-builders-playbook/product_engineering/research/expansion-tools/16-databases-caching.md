# §30 — Databases, Caching & Data Infrastructure (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## DB-01 — Supabase — ACTIVE (acquiring Turso; $1B+ raised)
- Purpose / problem: Open-source Postgres development platform: managed Postgres + auth, storage, edge functions, realtime, vector search (pgvector); "Firebase alternative on Postgres."
- OSS/commercial: OSS (Apache-2.0 core components) + commercial cloud (free tier; usage-based Pro/Team/Enterprise).
- Integration: Postgres wire-compatible; SDKs; integrates with the agent-era stack (Lovable auto-wires Supabase).
- Maintenance: Active; extreme growth. Verified timeline:
  - Oct 2025: $100M Series E at $5B valuation.
  - Jun 2026: $500M Series F at $10.5B (GIC-led); total raised crossed $1B.
  - **Oct 2, 2026: $150M round (GIC-led; CapitalG, IronArc, SquarePeg) + agreement to acquire Turso** (price undisclosed; not yet confirmed closed). Turso founder Glauber Costa → Head of Agentic Services; co-founder Pekka Enberg + team join. Turso platform keeps operating; graduation path Turso→Postgres via Multigres (petabyte-scale).
  - Reported scale (company claims, Corroborated across outlets): 13M+ developers; **1M+ users and 4M+ databases added per month; ~70% of new databases created by AI agents/tools** (Claude Code, Codex era).
- Limitations: Postgres-at-scale ops still surface (connection pooling, long-tail perf); usage-based billing can surprise at agent-driven scale; counting methodology for growth claims undisclosed.
- Security: SOC 2 (vendor); standard multi-tenant controls; RLS policies are the user's responsibility.
- Alternatives: Neon, PlanetScale, Firebase, AWS RDS/Aurora.
- Switching costs: Low–medium (Postgres wire-compatible — portable; Supabase-specific services add stickiness).
- Use: U(Verified) — Lovable integration; 13M developers claimed (company-reported).

## DB-02 — Turso — ACTIVE (being acquired by Supabase)
- Purpose / problem: SQLite rebuilt in Rust; edge-replicated, per-database isolation; "a single server can manage millions of databases" — the database-per-agent pattern (create/query/discard via API).
- OSS/commercial: OSS (MIT-licensed Turso Database; Rust rewrite replacing libSQL as direction, not yet 1.0 — libSQL self-hosters should plan for the shift). Cloud: free tier (100 databases) + $4.99 Developer plan (unlimited databases).
- Maintenance: Active; **acquisition by Supabase announced Oct 2, 2026** (terms/close date undisclosed). Turso says platform, APIs, workflows continue; no pricing/licensing change announced. Analyst guidance circulating: take independent backups, request 12-month price lock + change-of-control termination rights.
- Limitations: libSQL→Rust-rewrite transition incomplete (pre-1.0); post-acquisition roadmap/pricing uncertainty (standard).
- Security: Per-database isolation suits multi-tenant agent workloads.
- Alternatives: LiteFS, Cloudflare D1, Supabase Postgres.
- Switching costs: Low (SQLite files portable).
- Use: U(Proposed).

## DB-03 — Neon — ACTIVE
- Purpose / problem: Serverless Postgres (separate storage/compute, autoscaling, branching, scale-to-zero).
- OSS/commercial: Open-core (Apache-2.0) + commercial cloud (free tier; usage-based).
- Integration: Postgres wire-compatible; branching for dev/preview envs.
- Maintenance: Active (2026). (Depth debt on funding/valuation updates.)
- Limitations: Cold starts on scale-from-zero; connection handling (PgBouncer breaks LISTEN/NOTIFY — cited in the v10r ADR for pg-boss); egress costs.
- Security: Standard cloud controls.
- Alternatives: Supabase, PlanetScale, RDS.
- Switching costs: Low (wire-compatible).
- Use: U(Proposed).

## DB-04 — PlanetScale — ACTIVE
- Purpose / problem: Serverless MySQL (Vitess-based): branching, non-blocking schema changes, scale-to-zero.
- OSS/commercial: Commercial (proprietary control plane on Vitess OSS).
- Maintenance: Active (2026). (Depth debt on current status.)
- Limitations: MySQL-only; no stored procedures/triggers in some tiers historically.
- Alternatives: Neon, Supabase, TiDB Cloud.
- Switching costs: Low–medium.
- Use: U(Proposed).

## DB-05 — Redis — ACTIVE (license saga: BSD → RSALv2/SSPLv1, then AGPLv3 added)
- Purpose / problem: In-memory data store (caching, queues, streams, vectors).
- License saga (verified in summary): **Mar 20, 2024: BSD-3 → dual RSALv2 + SSPLv1** for all future versions ("end of an open source era" coverage); **May 2025: AGPLv3 added** for Redis 8.0 (dual RSALv2/SSPLv1/AGPLv3). Community fork **Valkey** (Linux Foundation, backed by AWS/Google/Oracle) won distro and AWS defaults.
- Maintenance: Active (Redis Inc./Redis Ltd.).
- Limitations: License complexity for distributors/cloud providers; ecosystem split with Valkey.
- Alternatives: Valkey, Dragonfly, KeyDB, Garnet (Microsoft, MIT).
- Switching costs: Low (protocol-compatible alternatives).
- Use: U(Verified) — still ubiquitous; Valkey winning new defaults.

## DB-06 — Valkey — ACTIVE (the fork that won)
- Purpose / problem: BSD-licensed Redis fork (Linux Foundation, Mar 2024) preserving open-source Redis trajectory.
- OSS/commercial: OSS (BSD-3).
- Maintenance: Active (2026); adopted as default by major distros and AWS.
- Alternatives: Redis, Dragonfly.
- Switching costs: Low (drop-in protocol compatibility).
- Use: U(Verified) — AWS/distro defaults. (Corroborated.)

## DB-07 — Dragonfly — ACTIVE (source-available)
- Purpose / problem: Drop-in Redis replacement (multi-threaded, higher throughput).
- OSS/commercial: **Launched under BSL 1.1 (2022)** — source-available, converts to Apache-2.0 after 4 years. No verified license change found in this pass (mark: Unknown for 2024–2026 changes).
- Maintenance: Active (2026) per community standing. (Depth debt — verify current releases.)
- Alternatives: Valkey, Redis, Garnet.
- Switching costs: Low.
- Use: U(Proposed).

## DB-08 — KeyDB — MAINTAINED (Snap-owned)
- Purpose / problem: Multithreaded Redis fork (Snap Inc. acquired May 2022).
- OSS/commercial: OSS (Apache-2.0/BSD family).
- Maintenance: Maintained under Snap; slower public cadence than Valkey/Dragonfly. (Depth debt — verify 2026 commits.)
- Alternatives: Valkey, Dragonfly, Redis.
- Use: U(Proposed).

## DB-09 — Garnet (Microsoft) — ACTIVE
- Purpose / problem: MIT-licensed Redis alternative from Microsoft Research (high performance).
- OSS/commercial: OSS MIT.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: Valkey, Dragonfly.
- Use: U(Proposed).

## DB-10 — TimescaleDB — ACTIVE (dual-license model)
- Purpose / problem: Time-series on Postgres (hypertables, compression, continuous aggregates).
- OSS/commercial: Apache-2.0 core + **Timescale License (source-available, no DBaaS) for advanced features since Dec 2018** — multi-node free under TSL (not paid-only). No verified license change found in this pass.
- Maintenance: Active (2026). (Depth debt on versions.)
- Alternatives: InfluxDB, QuestDB, ClickHouse.
- Switching costs: Low–medium (Postgres-native).
- Use: U(Proposed).

## DB-11 — MongoDB — ACTIVE (SSPL originator)
- Purpose / problem: Document database.
- License saga: **SSPL Oct 2018** (AGPL→SSPL); AWS responded with **DocumentDB (Jan 2019)**. SSPL never OSI-approved.
- Maintenance: Active (MongoDB Inc., public).
- Alternatives: DocumentDB, FerretDB (OSS), Postgres/JSONB.
- Use: U(Verified) — enterprise standard.

## DB-12 — Elasticsearch — ACTIVE (SSPL saga resolved toward openness)
- Purpose / problem: Search + analytics engine.
- License saga: **SSPL Jan 2021** → AWS forked **OpenSearch** (→ Linux Foundation Sep 2024); **Elastic added AGPLv3 Aug 2024** (tri-license SSPL/Elastic License/AGPLv3).
- Maintenance: Active.
- Alternatives: OpenSearch, Typesense, Meilisearch.
- Use: U(Verified).

## DB-13 — OpenSearch — ACTIVE
- Purpose / problem: Apache-2.0 Elasticsearch fork (AWS → Linux Foundation Sep 2024).
- Maintenance: Active (2026).
- Alternatives: Elasticsearch, Typesense.
- Use: U(Proposed).

## DB-14 — CockroachDB — ACTIVE (BSL; free Core retired)
- Purpose / problem: Distributed SQL (Postgres-compatible).
- License saga: **BSL Jun 2019**; **free self-hosted Core retired Aug 2024** (Enterprise/Cloud only for new).
- Maintenance: Active.
- Alternatives: YugabyteDB, TiDB, Postgres.
- Use: U(Proposed).

## DB-15 — ClickHouse — ACTIVE
- Purpose / problem: Columnar OLAP database; acquirer of Langfuse (Jan 2026); $400M Series D @ $15B.
- OSS/commercial: OSS Apache-2.0 + Cloud.
- Maintenance: Active (2026).
- Alternatives: DuckDB, Pinot, Druid.
- Use: U(Proposed).

## DB-16 — DuckDB — ACTIVE
- Purpose / problem: In-process analytical SQL (the "SQLite for analytics").
- OSS/commercial: OSS MIT.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: ClickHouse, Polars.
- Use: U(Proposed).

## Notable status findings (databases)
- **Supabase acquiring Turso (announced Oct 2, 2026)** — the agent-database thesis: 70% of new databases created by AI agents; Postgres + SQLite under one roof.
- Redis license saga: BSD → RSALv2/SSPLv1 (Mar 2024) → AGPLv3 added (May 2025); Valkey won the fork war.
- Elasticsearch: AGPLv3 added Aug 2024; OpenSearch → Linux Foundation Sep 2024.
- MongoDB SSPL (2018) → DocumentDB (2019); CockroachDB BSL (2019) + free Core retired (2024); TimescaleDB dual-license since 2018.
- Dragonfly: BSL 1.1 from launch; no verified change in this pass (Unknown for 2024–2026).

---

### Per-record metadata (condensed)
- Supabase/Turso: appstackinsider.com, sourcetrail.com, beri.net, blog.codercops.com, verdict.co.uk, runtimewire.com, bitcoinversus.tech — all Oct 2–6, 2026; primary: Supabase announcement/PR Newswire. Accessed 2026-10-10. Confidence: High (multi-outlet, company announcement).
- Redis/Valkey/Elastic/MongoDB/CockroachDB/TimescaleDB licenses: thenewstack.io, linuxiac.com, thestack.technology, zdnet.com, news.ycombinator.com (Timescale CEO clarification, 2020), lists.gnu.org. Confidence: High for the historical changes; Medium for "no change since" (absence of evidence).
- Dragonfly/KeyDB current status: no 2026 primary source pulled — marked Unknown/depth debt.
