# Architecture & Technical Planning (§9)

**Workstream:** spec-arch · **Research date:** 2026-10-10 · **Labels:** Verified / Corroborated / Inferred / Proposed / Unknown
**Evidence register:** `04-evidence-register.md`. No universal winners are declared; each matrix names *conditions* that tilt the choice.

---

## 0. How to use this document

An architecture decision is a bet placed under uncertainty. The discipline that makes bets survivable is:

1. **Name the decision, context, options, and trade-offs in writing** — an Architecture Decision Record (ADR): context, decision, alternatives considered, consequences, status (proposed/accepted/superseded/deprecated). Lightweight markdown in `docs/adrs/` (Corroborated across Google Cloud docs, software-architecture-guild guide, and multiple 2026 GitHub ADR examples — see register). ADRs stop re-litigation and make assumptions inspectable when context changes.
2. **Prefer reversible decisions** ("two-way doors"). Irreversible choices (data model shape, public API contracts, vendor lock-in points) deserve the ADR + prototype + review; reversible ones deserve a time-box, not a committee.
3. **Decide on pain, not fashion.** Recurring practitioner rule: extract/split/scale when the pain of *not* doing so clearly outweighs the cost of operating it — never because the current shape "feels slow" or a pattern is trending (Corroborated across modular-monolith migration guides).

---

## Matrix 1: Monolith vs Modular Monolith vs Microservices

**Plain-English definitions.**

- **Monolith (tangled or simple):** one codebase, one deployable, one (usually shared) database. Everything calls everything — cheap to start, tangling is the failure mode.
- **Modular monolith:** one deployable, but code is organized into bounded contexts (business-capability modules: Orders, Customers, Billing) with *enforced* boundaries — cross-module access only via published interfaces/contracts, no cross-module foreign keys, often schema-per-module in one Postgres. Extraction to services stays possible later.
- **Microservices:** many independently deployable services, each owning its data, communicating over the network (sync RPC or events).

### The matrix

| Criterion | Monolith | Modular monolith | Microservices |
|---|---|---|---|
| Dev velocity (small team) | Highest: one repo, one debugger, one deploy | High: slight boundary discipline cost | Lowest: cross-service coordination, contract versioning |
| Onboarding | Days–1 week | ~1–2 weeks | Weeks (reported ~3 weeks in one migration account) |
| Debugging | One log, one stack | Bounded modules, still one process | Distributed traces across N services; causal ambiguity |
| Deploy risk | Single unit; all-or-nothing | Single unit; modules independently testable | Independent deploys, but coordinated rollouts and version skew |
| Failure isolation | Low — one bad deploy takes all | Medium — module boundaries limit blast radius in code, not runtime | High — service fails alone (if designed for it) |
| Independent scaling | None — scale the whole thing | None at runtime (accepted cost) | Yes — scale hot services only |
| Team autonomy | Low — shared codebase, merge coordination | Medium — clear ownership per module | High — if teams map to services (Conway's law as tool) |
| Operational cost | Lowest (single instance; e.g., one practitioner case: $180→$340/mo after reverting) | Low — same infra as monolith | Highest — N services × pipelines, brokers, dashboards |
| Data consistency | Easy — one DB, ACID transactions | Easy in-module; cross-module via events/outbox | Hard — sagas, eventual consistency, distributed transactions |
| Refactoring cost | Low (IDE-safe) early; rises as tangling grows | Low–medium; boundaries make it cheaper | High — cross-service refactors are migrations |
| Extraction path later | Painful from tangled code | Built-in — the seams already exist | N/A (already there) |
| Failure mode | Big ball of mud | Boundary erosion without CI enforcement | Distributed monolith (worse than monolith): sync chatty services with none of the autonomy benefits |

### Evidence & conditions

- **Corroborated (multiple first-hand practitioner accounts, 2025–2026):** teams that split mid-size SaaS apps into microservices and reverted report consistent patterns — feature time 1–3 days → 5–12 days, deploys/week 12 → 3, incidents up, MTTR up (12 → 47 min in one account), costs up 10–20× (e.g., $180 → $4,200/mo), onboarding 1 → 3 weeks. One survey-cited claim (73% of migrations fail or produce a distributed monolith; 42% of adopters consolidating back) comes from marketing-adjacent sources — **Unverified as precise statistics**, but directionally consistent with the first-hand accounts (**Corroborated** as a trend).
- **When microservices genuinely win (Corroborated):** components with *wildly different scaling profiles* (e.g., GPU inference vs CPU API vs bursty ingestion), genuine organizational scaling pain (teams blocked on each other's deploys), or distinct security/blast-radius boundaries (e.g., identity service split from platform — fusioniiit ADR). One controlled account: a team extracted only the inference service as a pilot, kept the rest monolithic, and succeeded.
- **Modular monolith as default for most production systems:** "extract a service when the pain of not doing so clearly outweighs the cost of operating it separately — not before." Enforcement must be *mechanical* (import-linter contracts, no cross-module FK checks in CI), not conventional — "a convention that must be mechanically guarded, not just documented" (fusioniiit ADR-0001, volunteer-portal ADR-0001, groundwork ADR-0002 — first-hand practitioner ADRs, 2026).
- **Unknown:** precise team-size threshold where microservices pay off; accounts vary (11-engineer team regretted it; 18-engineer AI startup succeeded with 2 services). Treat "team size" as a proxy for the real variables: deploy contention, scaling-profile divergence, operational maturity.

**Trade-off summary:** the monolith taxes you in *coordination* as it grows; microservices tax you in *operations* from day one. The modular monolith defers the operations tax while keeping the extraction option — at the price of boundary discipline enforced by tooling.

---

## Matrix 2: SQL vs NoSQL vs Hybrid (polyglot)

**Plain-English definitions.**

- **SQL (relational: Postgres, MySQL):** data in tables with fixed schemas and declared relationships; queries join tables at read time; ACID transactions (all-or-nothing multi-step writes).
- **NoSQL (document/key-value/wide-column: MongoDB, DynamoDB, Cassandra, Redis):** flexible or schema-less records, optimized for specific access patterns; horizontal write scaling; typically eventual consistency (replicas may briefly disagree).
- **Hybrid/polyglot:** SQL for the relational core + specialized stores for specific jobs (Redis cache, search index, time-series DB, object storage).

### The matrix

| Criterion | SQL (Postgres-class) | NoSQL | Hybrid |
|---|---|---|---|
| Data integrity | Strong: FKs, constraints, ACID | Application-enforced; "no single source of truth" when denormalized | Strong where it matters |
| Query flexibility | Joins, aggregations, ad-hoc analytics | Simple lookups fast; joins painful/manual | Best of both per workload |
| Schema evolution | Migrations; rigid but explicit | Flexible; "schemaless" shifts the work to app code | Explicit where it counts |
| Write scaling | Vertical + read replicas; sharding is work | Native horizontal write scaling | Scales per component |
| Consistency | Strong by default | Usually eventual | Chosen per store |
| Operational maturity | Very mature; "boring technology" | Varies by product | More components to run |
| Hiring/onboarding | SQL is near-universal | Vendor-specific knowledge | Broader skill surface |
| Cost at moderate scale | Low (single instance handles ~10M queries/day in one practitioner account) | Can be pricier per unit of correctness work | Pay per component |

### Evidence & conditions

- **Corroborated (practitioner accounts):** a startup that chose MongoDB for relational data paid ~$200K in rework; after migrating the relational core to Postgres: query times 6 min → 80 ms, infra $4,200 → $1,100/mo, support tickets 104 → 12/week. Their kept-MongoDB list (activity logs, analytics, session data) is the textbook hybrid. The core trade, well put by one guide: *"SQL pays at read time for one source of truth; document stores pay at write time for fast, self-contained reads."*
- **Decision rule (Inferred, corroborated):** choose by *data shape and access pattern*, not hype — relational data with meaningful relationships → SQL; standalone documents/variable shapes → NoSQL; time-series → time-series DB; search → search engine. "When in doubt, start with PostgreSQL; add specialized stores later for specific use cases" (Corroborated across guides).
- **Anti-patterns to name:** NoSQL-for-everything ("NoSQL is modern") ends with joins re-implemented in application code — fragile; SQL-for-everything with deeply nested/variable data ends in nullable-column bloat. Both are the same mistake: letting fashion choose the data model.
- **Unknown:** exact QPS crossover points (claims like "<100K QPS writes → SQL" are interview-guide heuristics, **Unverified** as measured thresholds).

**Trade-off summary:** SQL buys integrity and query power at the cost of scaling ceremony; NoSQL buys scaling and flexibility at the cost of integrity work moving into your code. Hybrid is the honest answer for most real systems — but each added store is an operational commitment; don't polyglot before you have two genuinely different workloads.

---

## Matrix 3: Synchronous vs Asynchronous / Event-Driven

**Plain-English definitions.**

- **Synchronous (request/response: REST, gRPC):** Service A calls B and waits. Like a phone call — you get an answer now, but you're stuck on the line.
- **Asynchronous (queues/events: SQS, RabbitMQ, Kafka):** A publishes a message and moves on; B processes it later. Like leaving a note — decoupled, but no immediate answer. Adds a broker (a middleman service that holds and routes messages).

### The matrix

| Criterion | Synchronous | Asynchronous / event-driven |
|---|---|---|
| Latency | Low, predictable per call | +broker hop (1–10 ms); end-to-end less predictable under backlog |
| Coupling | Tight — caller knows callee | Loose — producer doesn't know consumers |
| Failure spread | One slow dependency slows every caller (cascading) | Contained — producer succeeds even if consumer is down |
| Throughput under bursts | Bounded by callee capacity | Queue absorbs spikes; drains gracefully |
| Consistency | Immediate/strong | Eventual — product must tolerate temporary staleness |
| Observability | Easy — one trace, one call stack | Hard — correlate across events; causal ambiguity |
| Debugging | Follow the stack | Reconstruct distributed state across time; "coupling without a call stack" |
| Ordering | Natural per connection | Requires explicit design (partitions, FIFO queues) |
| Delivery semantics | Idempotent POST achievable | At-least-once default → duplicates; exactly-once needs careful design |
| Backpressure | Immediate (HTTP 503) | Queue depth is the signal — must be monitored |
| Schema evolution | Versioned APIs | Versioned events; old events live in the log — schema registry needed |

### Evidence & conditions

- **Corroborated (first-hand failure accounts, 2025–2026):** teams that made *everything* event-driven report: a customer charged 5× by retry logic without idempotency; 3-day debug sessions for 2-line fixes (out-of-order events, lagging consumers, accidental full replays duplicating data across 4 databases); schema drift to `UserCreatedEventV1…V4` with nobody knowing which to use; DLQs silently collecting failures for 9 months; inventory counts drifting for 6 weeks from one unpublished event. *"Event-driven systems don't fail loudly. They fail silently, slowly, and repeatedly."*
- **When async wins (Corroborated):** bursty traffic a queue can absorb (checkout spikes — horizontal scaling takes 30–120 s per pod; a queue absorbs instantly); fan-out (one event → many independent consumers: inventory, fulfillment, notifications); slow/non-critical work (emails, audit logs, analytics, search indexing, report generation); resilience where the producer must not fail when the consumer is down.
- **When sync wins (Corroborated):** the user or upstream needs an immediate authoritative answer; correctness-critical paths (payment authorization, balance deduction, permission checks) stay synchronous or transactionally protected.
- **Production prerequisites for async (Corroborated across guides):** idempotent consumers (assume at-least-once everywhere); bounded retries + dead-letter queues with alerting (never infinite retry); outbox pattern or transactional event publishing (avoid "DB wrote, event never published"); schema registry with compatibility enforcement; correlation/trace IDs across hops; queue-lag as a first-class alert metric; load-test consumers against *burst* patterns, not steady state.
- **Unknown:** whether a given team's "events" are genuinely decoupled workflows or just "service A telling service B to do one thing" — the latter is RPC with extra steps and all of the debugging cost. Name it before building it.

**Trade-off summary:** sync buys simplicity, immediacy, and debuggability at the cost of cascading failure; async buys resilience and burst absorption at the cost of eventual consistency and forensic difficulty. The common failure is choosing async for *style* and paying the debugging tax on workflows that needed an answer now. Hybrid is normal: sync core paths, async edges.

**Related: caching, queues, background workers (Inferred synthesis, corroborated individually).** Caching (Redis-class) trades freshness for speed — every cache needs an invalidation story or it becomes a stale-data bug factory. Background workers (job queues) are async's workhorse for slow tasks; they need the same idempotency/retry/DLQ discipline as event consumers. Introduce each when a measured bottleneck exists, not speculatively.

---

## Matrix 4: Self-Hosted vs Managed / Serverless

**Plain-English definitions.**

- **Self-hosted:** you run it — VPS, own Kubernetes, own database. Fixed costs, full control, you own the pager.
- **Managed:** the provider runs the undifferentiated parts — managed Postgres, managed Kubernetes, PaaS (Heroku/Render/Fly). You pay a premium over raw compute for deploys, TLS, backups, scaling handled.
- **Serverless (functions + managed services):** pay per request/invocation (Lambda, Cloud Run jobs, DynamoDB on-demand). Zero cost at idle; per-unit compute is pricier.

### The matrix

| Criterion | Self-hosted | Managed (PaaS/managed DB) | Serverless |
|---|---|---|---|
| Cost at low/sporadic traffic | Overkill — fixed cost for idle | Moderate fixed | Cheapest — pay per use, scale to zero |
| Cost at high steady traffic | Cheapest per unit (one practitioner case: $98.50 → $10/mo moving serverless→$10 VPS) | Premium over raw compute | Most expensive per unit (~2.1× Fargate per compute-unit in one analysis); egress/concurrency overages bite |
| Cost predictability | Fixed, predictable | Fixed-ish tiers | Spiky — bill follows traffic |
| Ops burden | Highest — patching, backups, on-call | Low — provider handles runtime | Lowest for code; but architecture complexity (cold starts, connection pooling) |
| Cold starts / latency jitter | None (always warm) | None | Real — P99 spikes (one case: 1,740 ms cold vs 124 ms warm) |
| Long-running work (workers, websockets) | Natural | Usually fine | Awkward — timeouts, connection limits (DB connection bottlenecks reported) |
| Control / data sovereignty | Full | Partial | Least — provider's substrate |
| Scaling effort | Manual or self-built autoscaling | Mostly automatic | Automatic, near-instant |
| Startup speed | Slowest (provision, harden) | Fast | Fastest for stateless |
| Lock-in | Low (your VMs) | Medium (APIs, add-ons) | Highest (event sources, IAM, proprietary services) |

### Evidence & conditions

- **Corroborated:** the "free DIY is the most expensive" effect — self-hosted TCO is dominated by engineer time (60–70% hidden costs per WP Engine-cited analysis; 3–5 hrs/mo maintenance at opportunity cost dwarfs a $20–40 VPS). Break-even math from Qovery (2026): a platform engineer at ~$180–200K fully loaded erases a $3K/mo infra saving for 5+ years, but is noise against $30K/mo savings — *the break-even is about spend, not technology*.
- **Corroborated:** Lambda's cost advantage is *not* cheap compute — it's zero idle billing; above ~47.6% duty cycle in one first-principles analysis, always-on compute wins. "Reasoning by convention ('serverless is cheaper') reaches the wrong answer for every workload above [the crossover]."
- **Negative evidence on 12-factor config purism (first-hand practitioner):** env-var-only config at 42 variables created local-dev nightmares (2-hour onboarding env setup, prod-only bugs from env drift). Their working compromise: version-controlled base config files + environment overrides + secrets-only in env/secret managers + startup validation. **Inferred as sound**; the "never commit config" rule stands for *secrets*, not for all config.
- **Conditions:** stay serverless when traffic is genuinely sporadic, no Linux-comfortable engineer exists, or the app is fully stateless. Move to fixed-cost hosting with a relational DB when you need predictable sub-100 ms latency, run workers/websockets, or the bill's variable portion exceeds the ops cost. Stay managed (PaaS/managed DB) when the team is small and product work outranks infra savings.

**Trade-off summary:** serverless buys zero-idle cost and instant scale at the price of per-unit cost, latency jitter, and lock-in; self-hosting buys unit cost and control at the price of engineer hours; managed buys team focus at a markup. The fair comparison always includes the *people* cost and the *whole* managed bill (deploys, TLS, backups, support) — bare-VM vs managed-platform comparisons are the classic rigged evaluation.

---

## Cross-cutting concerns (apply to every matrix choice)

- **Separation of concerns / maintainability:** module boundaries (bounded contexts), ports-and-adapters at the edges, domain code free of framework imports (e.g., "domain/ may not import Django" — fusioniiit ADR). **Corroborated** as the practice that keeps all four architectures changeable.
- **Data integrity:** integrity constraints live as close to the data as the architecture allows — FKs/constraints inside a module or monolith; application-layer + outbox + idempotency across service/event boundaries. Integrity doesn't disappear in distributed designs; it moves into code you must write and test.
- **Fault isolation:** bulkheads, timeouts, circuit breakers, and async boundaries around slow dependencies. The sync/async matrix is the primary lever.
- **Observability:** structured logs + metrics + traces + correlation IDs; queue-lag, DLQ depth, and retry counts as first-class alerts in async systems; error budgets (SLOs) to decide when reliability work preempts features. Cost note: observability itself bills — cardinality explosions in metrics/traces are a real line item (**Inferred** from community billing complaints; treat vendor pricing as **Unknown**/changing).
- **Security:** authN/authZ at boundaries, secrets in managers (never in repos — secret scanning as a required CI check), dependency/SCA scanning, least-privilege service identities. Dependency vulnerabilities are consistently cited as the top attack vector in practitioner CI guides.

---

## Anti-patterns (name them in ADRs so reviewers can flag them)

1. **Premature abstraction.** Building the general solution before the second and third use cases exist: interfaces around single implementations, generic registries for two callers, plugin systems for a known-fixed set. The three-time rule (write concretely → watch duplication → abstract at the third case) and the YAGNI test ("do I have two real, current call sites?") are the counterweights. Agents over-abstract *by default* — this needs explicit instruction in repo guidance (agents-playbook anti-overengineering; openwaggle antipatterns; jidechao AGENTS.md — first-hand practitioner sources, **Corroborated**).
2. **Unnecessary complexity / speculative scaling.** Sharding, multi-region, Kafka, and Kubernetes before a measured bottleneck. "You aren't Facebook; you have 1,000 users — use Postgres." Scale on pain, with the modular monolith preserving the option.
3. **Dependency sprawl.** Every dependency is a liability: supply-chain risk, upgrade burden, and API-surface you don't control. Declare explicitly, lock versions, scan (Dependabot/Renovate, `npm audit`/bandit), and justify additions in review.
4. **Fashion-driven architecture.** Choosing microservices/event-driven/NoSQL/serverless because it's the conference-talk default. The matrices above exist to replace vibes with conditions.
5. **Distributed monolith.** The worst of both: chatty synchronous calls between services with shared-database coupling. Usually the result of splitting by class size rather than by bounded context, without the operational maturity microservices demand.
6. **Shared-database addiction.** "We'll share the DB for now" becomes permanent coupling; cross-service joins bypass every boundary you drew.
7. **Big-bang rewrites over strangler migration.** Use interfaces, contract tests, feature flags, shadow traffic, and strangler patterns; modularize the monolith *first*, then extract (dev.to migration-patterns guide — practitioner).

---

## Reversible decisions: the ADR habit in miniature

Write ADRs for: framework/database/broker choices, module/service boundaries, auth strategy, sync/async per workflow, hosting model, and anything a future debugger will ask "why." Keep each to one decision, ~30 minutes of writing, in `docs/adrs/` next to the code — including *superseded* records so the history of reasoning survives. Link ADRs from PRs. Revisit when the context the decision assumed (scale, team, regulations) changes — that's the trigger, not the calendar.
