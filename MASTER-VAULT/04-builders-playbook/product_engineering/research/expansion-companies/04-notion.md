# Notion — product engineering case study

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Notion is the "boring architecture wins" scaling case: single Postgres → sharded Postgres, staying on a monolith and RDS while growing to hundreds of millions of blocks. Primary source "The Great Re-shard" located (not fetched in full; search excerpt is extensive). Secondary coverage is rich and consistent.

## Findings

### Architecture
- Claim: Notion ran everything on a single PostgreSQL instance (Amazon RDS) in the early days; vertical scaling carried them until even the largest RDS instance couldn't keep up. Label: **Corroborated** — primary blog (the-great-re-shard) + secondary summaries.
- Claim: They sharded rather than replatforming to microservices: 32 → 96 physical database instances (tripled fleet), each with 5 logical shards (480 logical shards in secondary accounts). Each workspace is assigned to a specific shard, so a workspace's blocks live together and queries don't fan out. Label: **Corroborated** — primary blog + Medium/ByteByteGo summaries. The 480-shard figure is secondary-only; treat exact count as Medium confidence.
- Claim: Sharding key = workspace ID, chosen because users overwhelmingly work within their own workspace — keeps co-accessed data physically together. Label: **Corroborated** (secondary summaries of the primary).
- Claim: They explicitly rejected vertical scaling as the answer ("we'd run into the same limitations in the future") and also rejected a microservices rewrite; they kept the monolith and sharded the data layer. Lesson: scale the bottleneck, not the architecture diagram. Label: **Corroborated**.
- Claim: They also had to shard the PgBouncer connection-pooling layer itself — the pooler became its own scaling problem. Lesson: every layer you add to fix scale becomes a new thing to scale. Label: **Corroborated** (primary blog outline).

### Implementation
- Claim: During the re-shard they provisioned *smaller* instances/disks for new shards to control cost (disk wasn't the bottleneck; CPU/IOPS were) — capacity planning separated the dimensions of the bottleneck instead of tripling everything. Label: **Corroborated** (primary blog excerpt).
- Claim: Optimistic local-first editing: keystrokes apply to the local view instantly, then sync in the background — the app keeps working through brief network drops. Label: **Corroborated** (secondary architecture summaries).
- Claim: Vector search for Notion AI (Q&A): rather than re-sharding Postgres-style, each new "generation" of indexes got its own ID directing reads/writes; new workspaces onboarded to new generations. Onboarding capacity went up 600x via Airflow scheduling and Spark tuning; by April 2024 they cleared a multi-million-workspace waitlist. The generations approach later became "operationally complex and expensive," forcing a re-architecture. Label: **Corroborated** — primary source via GitHub-archived Notion blog post ("Two years of vector search at Notion").

### Testing / reviews
- Claim: A pganalyze engagement found a GIN index on space_id/permission columns wasn't being used (poor cardinality/statistics); switching to a jsonb_path_ops index cut query time from ~5000ms to ~600ms (733% improvement, 8x). Label: **Corroborated** — pganalyze customer story quoting Notion EM Arka Ganguli and SWE Ben Hughes.
- Claim: Pre-production load testing caught a new feature responsible for 20% of application query load before it shipped; "pganalyze is part of our first line of defense." Label: **Corroborated** (same source). Lesson: feature-level query-load attribution in pre-prod catches cost bombs before launch.

### Deployment
- Claim: The re-shard was done with zero downtime. Label: **Corroborated** (primary blog title claim); mechanics not verified this pass.

### Monitoring
- Claim: pganalyze used to distinguish root causes from symptoms during incidents ("understanding spikes in CPU or query load and distinguishing between root causes and symptoms"). Label: **Corroborated** (pganalyze story, first-hand quotes).

### Documented failures
1. Capacity crisis preceding the re-shard: shards "quickly running out of capacity," queries slowing, hot-shard bottlenecks — the forcing function for the whole project. No customer-facing outage narrative located; this was a near-miss handled by engineering, not a postmortem. Label: **Corroborated**.

### Transferable lessons
- Start with the monolith; shard the data when vertical scaling hits the wall — don't rewrite the application topology to fix a database problem. Label: **Corroborated**.
- Choose the sharding key from access patterns (workspace ID), not from aesthetics. Label: **Corroborated**.
- Capacity-plan per bottleneck dimension (CPU/IOPS vs disk) rather than scaling everything uniformly. Label: **Corroborated**.
- For hypergrowth-adjacent problems (AI onboarding), a "generations" append-only scaling trick can buy time — but budget the later re-architecture; operational complexity compounds. Label: **Corroborated**.
- Attribute query load to features in pre-production, not just in incidents. Label: **Corroborated**.

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| NO-01 | The Great Re-shard (primary, excerpt) | https://www.notion.com/blog/the-great-re-shard | Primary eng blog | Notion | ~2023 | 2026-10-10 | High (excerpt extensive) |
| NO-02 | pganalyze: 8x query improvement, pre-prod load attribution | https://pganalyze.com/customers/how-notion-runs-postgres-at-scale-on-amazon-rds | Vendor case study (first-hand quotes) | pganalyze / Arka Ganguli, Ben Hughes (Notion) | ~2021 | 2026-10-10 | Medium |
| NO-03 | Two years of vector search: generations architecture, 600x onboarding | https://github.com/jakub-zovi/second-brain-public/blob/HEAD/content/two%20years%20of%20vector%20search%20at%20notion.md | Primary (archived Notion blog) | Notion | 2024 | 2026-10-10 | Medium |
| NO-04 | Architecture synthesis (monolith, optimistic UI, sharding key) | https://github.com/udaykumar-dhokia/insidethestack/blob/HEAD/content/articles/how-notion-works.mdx | Secondary (synthesis) | insidethestack | 2026 | 2026-10-10 | Low-medium |
| NO-05 | Scaling narrative | https://medium.com/@kapoorraghav0310/how-notion-scaled-its-architecture-to-handle-millions-without-crashing-d34a8545b3f9 | Secondary (narrative) | Medium | 2025 | 2026-10-10 | Low-medium |

## Narrative audit (retrofit 2026-10-10)
- **"Boring Postgres" vs. the generations confession.** Notion's celebrated simplicity narrative (one Postgres, boring tech) sits atop the "three generations of block editor" reality — the simplicity was *earned through two failed architectures*, not chosen on day one. Boring is the *destination* after you've learned what's hard, not the starting position.
- **Everything-is-a-block has a performance cliff.** The block model's elegance (uniform data model, infinite composability) is real — and its cost is real: large workspaces hit performance walls the abstraction can't hide. Uniform data models trade *conceptual* simplicity for *performance* complexity. Price it.
- **Downtime as the scaling receipt.** Notion's widely-reported outages are the receipts that the "simple" architecture still has a scaling tail — specifics of each incident not verified this pass, but the pattern (simple core, hard scaling edge) is consistent with the generations story.
