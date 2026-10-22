# §30 — Workflow Orchestration & Durable Execution (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## WO-01 — Temporal — ACTIVE
- Purpose / problem: Durable workflow execution at infrastructure scale: workflows as code with replay-based state recovery, timers, signals, sagas; polyglot SDKs (Go/Java/Python/PHP/.NET/TypeScript); self-hostable cluster or Temporal Cloud.
- OSS/commercial: Open-core. Server SDKs Apache-2.0 / MIT; server itself under a source-available license family (Temporal historically used MIT for SDKs and a BSL-style license for parts of the server — verify current LICENSE before self-hosting). Commercial: Temporal Cloud.
- Integration: Helm/K8s self-host; visibility via Elasticsearch/Postgres; OpenTelemetry.
- Maintenance: **Very active — verified directly from primary source.** Server **v1.32.0** (Sep 2026; api v1.63.5; go 1.26.8); SDK versions mid-2026: sdk-go 1.41.1, sdk-python 1.33.0; PRs merged within days of 2026-10-10 (e.g., auto-scaled-workers binary-size cut Sep 28, 2026; ~23.4k stars on temporalio/temporal). Third-party upgrade PRs (shepherdjerred monorepo) show real-world adoption tracking releases.
- Limitations: Operational complexity (cluster ops, visibility store); learning curve (determinism constraints on workflow code); Build-ID versioning being removed in v1.33 — migration to Worker Deployment APIs required.
- Security: mTLS, namespace isolation, auth interceptors (1.27.x auth fixes cherry-picked — CVE-adjacent hardening visible in PR history); data residency via self-host.
- Alternatives: Inngest (serverless DX), Trigger.dev (managed compute), AWS Step Functions, Camunda/Zeebe, DBOS.
- Switching costs: High (workflow code is infrastructure).
- Use: U(Verified) — third-party repos tracking upgrades; Temporal Cloud customers (vendor). GitHub PR evidence: real production usage (upgrade discipline documented).

## WO-02 — Inngest — ACTIVE (CONTROVERSIAL: 2025 outage)
- Purpose / problem: Durable functions in your own app: event-driven step functions (`step.run()`, `step.waitForEvent()` human-in-the-loop), automatic retries, concurrency controls, built-in scheduling; runs on Vercel/Cloudflare/any serverless host — no workers to run.
- OSS/commercial: Commercial SaaS (Inngest Inc.). Open-source SDKs; core platform proprietary. Pricing (Sep 2026): Free 50k executions; Pro $99/mo (1M executions); Business $499/mo (10M). Note: executions = runs + steps (a 5-step function = 6 executions).
- Integration: `/api/inngest` route handler; SDKs TS/Python/Go/Kotlin.
- Maintenance: Active (2026); longest track record in the class; official SvelteKit support cited in ADRs.
- **CONTROVERSY: multi-day partial outage Oct 2025** — documented as precedent in a 2026 ADR (foundryai ADR-0016) for rejecting managed durable-execution vendors in v1; teams cite it when choosing self-hosted alternatives.
- Limitations: Hosted pricing scales with chattiness (step count); self-hosting "more involved than the managed service suggests"; managed-service outage = your jobs pause.
- Security: Events/functions traverse vendor; signing keys per app.
- Alternatives: Trigger.dev, Temporal, DBOS.
- Switching costs: Medium (function code portable; event plumbing is Inngest-specific).
- Use: U(Verified) — ADRs in real repos (v10r jobs.md, Sep 2026: chosen for reactive job orchestration; foundryai ADR-0016 evaluated and rejected for v1 on sovereignty grounds).

## WO-03 — Trigger.dev — ACTIVE
- Purpose / problem: Long-running background tasks on managed compute (or self-hosted): durable runs, retries, delays/schedules, batching; TypeScript-first; AI-workload friendly (tasks that break serverless timeouts — AI agents, media processing, big syncs).
- OSS/commercial: OSS (Apache-2.0, self-hostable) + managed Trigger.dev Cloud. Pricing (Sep 2026): free tier ($5 usage incl.), Hobby $10/mo, Pro $50/mo — per-run $0.000025 + per-second compute (0.25 vCPU $0.0000169/s); dev-environment runs uncharged; no base fee since Sep 14 (2026).
- Integration: trigger.dev SDK + CLI; Next.js/Remix/Express/Hono; OpenAI/Anthropic/Supabase/Stripe integrations.
- Maintenance: Active (2026); v3 is the durable-execution rewrite (use v3 in 2026).
- Limitations: Compute-time billing punishes slow/waiting tasks (holding a machine while waiting on a slow API); Trigger.dev v3 CLI requires Node (friction in Bun-first projects; experimental Bun runtime has broken OpenTelemetry — per v10r ADR).
- Security: Self-hostable for data control.
- Alternatives: Inngest, Temporal, BullMQ (self-managed).
- Switching costs: Low–medium (task code portable; triggers SDK-specific).
- Use: U(Proposed) — evaluated in ADRs; community skill repos (agentic-awesome-skills) treat it as standard.

## WO-04 — DBOS — ACTIVE
- Purpose / problem: Durable execution on Postgres (workflows as code backed by transactional state).
- OSS/commercial: OSS (license verify) + commercial cloud.
- Maintenance: Active (2026).
- Alternatives: Temporal, Inngest.
- Use: U(Proposed). (Lightly researched — depth debt.)

## WO-05 — Camunda / Zeebe — ACTIVE
- Purpose / problem: BPMN-based process orchestration (Zeebe: cloud-native workflow engine).
- OSS/commercial: Open-core (Zeebe historically Apache-2.0; Camunda 8 SaaS commercial).
- Maintenance: Active (2026).
- Alternatives: Temporal, AWS Step Functions.
- Use: U(Proposed). (Lightly researched — depth debt.)

## WO-06 — AWS Step Functions — ACTIVE
- Purpose / problem: Serverless state-machine orchestration inside AWS.
- OSS/commercial: Commercial (AWS).
- Maintenance: Active.
- Alternatives: Temporal, Inngest.
- Use: U(Verified) — AWS ecosystem standard. (Lightly researched — depth debt.)

## WO-07 — BullMQ — ACTIVE
- Purpose / problem: Node.js queue on Redis (job queues, not durable workflows per se).
- OSS/commercial: OSS MIT.
- Maintenance: Active (2026).
- Limitations: Needs persistent Redis (serverless-hostile); not durable execution (no replay).
- Alternatives: pg-boss, graphile-worker, Trigger.dev.
- Use: U(Verified) — standard Node queue. (Lightly researched — depth debt.)

## WO-08 — pg-boss — MAINTAINED
- Purpose / problem: Postgres-backed job queue for Node.
- OSS/commercial: OSS MIT.
- Maintenance: Maintained (2026).
- Limitations: Neon PgBouncer breaks LISTEN/NOTIFY + advisory locks silently (per v10r ADR); polling worker has up-to-60s delay.
- Alternatives: BullMQ, graphile-worker.
- Use: U(Proposed).

## WO-09 — Airflow — ACTIVE
- Purpose / problem: Batch/data-pipeline orchestration (DAGs).
- OSS/commercial: OSS Apache-2.0 (Apache Software Foundation).
- Maintenance: Active (2026).
- Alternatives: Dagster, Prefect, Temporal (different model).
- Use: U(Verified) — data-engineering standard. (Lightly researched — depth debt.)

## WO-10 — Dagster — ACTIVE
- Purpose / problem: Data orchestration with software-defined assets.
- OSS/commercial: Open-core (Apache-2.0 core) + Dagster+ cloud.
- Maintenance: Active (2026).
- Alternatives: Airflow, Prefect.
- Use: U(Proposed). (Lightly researched — depth debt.)

## WO-11 — Prefect — ACTIVE
- Purpose / problem: Pythonic workflow orchestration.
- OSS/commercial: Open-core (Apache-2.0 core) + Prefect Cloud.
- Maintenance: Active (2026).
- Alternatives: Airflow, Dagster.
- Use: U(Proposed). (Lightly researched — depth debt.)

## Notable status findings (workflow orchestration)
- Temporal — **server v1.32.0 Sep 2026**, active weekly development; Build-ID versioning removed in v1.33 (migration required).
- Inngest — **multi-day partial outage Oct 2025** is now a cited precedent in ADRs rejecting managed durable execution.
- Trigger.dev v3 — OSS + durable execution; compute-time billing is the cost trap to watch.

---

### Per-record metadata (condensed)
- Temporal activity: github.com/temporalio/temporal — PRs #12263 (Sep 28, 2026), #10234, #11265, #10949; sdk-python 1.33.0 release; s2s-proxy v1.32.0 upgrade (Sep 25, 2026); shepherdjerred/monorepo 1.32.0 upgrade PR (Sep 2026). Accessed 2026-10-10. Confidence: High (primary source).
- Inngest outage: solvane-hub/foundryai ADR-0016 (Aug–Sep 2026) — secondary citation of Oct 2025 incident. Confidence: Medium (ADR asserts it; independent outage reports not pulled in this pass — flag for verification).
- Inngest/Trigger.dev pricing + comparison: appstackbuilder.com (Sep 2026), alexcloudstar.com, stacknotice.com. Confidence: Medium.
- Trigger.dev v3 Bun issue: apedevil/v10r docs/blueprint/architecture/jobs.md (Sep 2026). Confidence: Medium (single ADR).
- Trigger.dev skills: khaitrang1995/agentic-awesome-skills (Feb 2026). Confidence: Low–Medium (community).
