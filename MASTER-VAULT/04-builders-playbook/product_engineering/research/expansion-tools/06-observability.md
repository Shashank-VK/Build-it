# §30 — Observability, Monitoring & Error Tracking (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## OB-01 — Datadog — ACTIVE (CONTROVERSIAL: pricing)
- Purpose / problem: All-in-one observability (infra, APM, logs, RUM, security); broadest integration catalog.
- OSS/commercial: Commercial SaaS. List: from $15/host/mo infra, $31/host/mo APM (annual).
- **CONTROVERSY (pricing, recurring):** the **$65M Datadog bill** case (widely cited 2024–2025); **Delivery Hero migrated to Grafana Cloud in 1H25** partly over cost (per summary). 2026 pricing guides still flag per-host/per-GB/per-series meters as where bills grow with cardinality.
- Maintenance: Active (2026).
- Limitations: Cost at scale is THE limitation; per-host metering punishes label cardinality.
- Alternatives: Grafana Cloud/LGTM, New Relic, Honeycomb, SigNoz, Last9.
- Switching costs: High (agents, dashboards, monitors everywhere).
- Use: U(Verified) — enterprise standard.

## OB-02 — Grafana (LGTM stack: Loki/Grafana/Tempo/Mimir) — ACTIVE
- Purpose / problem: OSS observability platform: metrics (Mimir/Prometheus), logs (Loki), traces (Tempo), dashboards; Grafana Cloud managed.
- OSS/commercial: Open-core; **core stack AGPLv3** (Grafana relicensed Apr 2021, OSI-approved). Cloud: $19/mo + $6.50/1k active series + $0.40/GB logs.
- Maintenance: Active (2026); k6 and Pyroscope under the same roof.
- Limitations: Three stores, three query languages (PromQL/LogQL/TraceQL) — correlation happens in the dashboard layer; self-operating the trio is real platform work (per Pydantic Logfire guide, 2026).
- Alternatives: Datadog, SigNoz, New Relic.
- Switching costs: Medium–high.
- Use: U(Verified) — Delivery Hero migration (1H25); de-facto OSS standard.

## OB-03 — SigNoz — ACTIVE
- Purpose / problem: OpenTelemetry-native, open-source Datadog alternative: traces, logs, metrics in one self-hosted app (ClickHouse-based, OTLP-native); APM views, dashboards, alerting; LLM observability over GenAI semantic conventions; SigNoz MCP + AI teammate (Cloud).
- OSS/commercial: Open-core (Apache-2.0 core + commercial enterprise features). Self-host free; Cloud from $49/mo ($49 usage incl.; then $0.30/GB logs/traces, $0.10/M samples metrics); startups $19/mo first year; no per-user/per-host fee.
- Maintenance: Active (2026).
- Limitations: You operate ClickHouse + ingestion yourself (or pay for Cloud); ad-hoc analysis beyond the query builder = ClickHouse SQL against their schema.
- Alternatives: Grafana LGTM, Datadog, Highlight, OpenObserve.
- Switching costs: Medium.
- Use: U(Proposed).

## OB-04 — Honeycomb — ACTIVE
- Purpose / problem: Trace-first debugging of high-cardinality systems: wide events, "group by any attribute" investigation; OTLP ingest.
- OSS/commercial: Commercial SaaS. Free to 20M events; Pro from $150/mo.
- Maintenance: Active (2026).
- Limitations: SaaS-only (data leaves your infra); proprietary query model (skills/questions are Honeycomb-shaped); pricing meters events + metric datapoints + processing separately.
- Alternatives: SigNoz, Lightstep (ServiceNow), Grafana Tempo.
- Switching costs: Medium–high (query-model lock-in).
- Use: U(Proposed).

## OB-05 — Sentry — ACTIVE (license saga)
- Purpose / problem: Error tracking + performance monitoring + session replay; dev-workflow native (issue → fix).
- OSS/commercial: License saga — **BSD-3 → BSL (2019) → FSL "Functional Source License" (Nov 2023)**; self-hostable source-available. Commercial SaaS.
- Maintenance: Active (2026).
- Limitations: Won't watch your servers (pairs with Grafana Cloud/Better Stack per 2026 guides); license restricts competitive hosting.
- Alternatives: Highlight, Rollbar, Bugsnag, GlitchTip (OSS).
- Switching costs: Low–medium (SDK swaps easy; workflow integrations stick).
- Use: U(Verified) — ubiquitous in web/mobile.

## OB-06 — Highlight — ACTIVE
- Purpose / problem: Open-source full-stack monitoring: error monitoring, session replay, logging, distributed tracing.
- OSS/commercial: OSS (license verify — historically Apache-2.0) + cloud.
- Maintenance: Active (2026). (Depth debt on versions.)
- Alternatives: Sentry, LogRocket, PostHog (replay).
- Switching costs: Low.
- Use: U(Proposed).

## OB-07 — New Relic — ACTIVE
- Purpose / problem: All-in-one observability, usage-based; 100 GB free ingest/mo; no per-host fee.
- OSS/commercial: Commercial SaaS. Beyond free: $0.40/GB; per-user seats (Standard first full user $10, extra $99 capped at 5; Pro $349).
- Maintenance: Active; PE-owned since **$6.5B take-private (Jul 2023)**.
- Alternatives: Datadog, Grafana Cloud.
- Switching costs: High.
- Use: U(Proposed).

## OB-08 — Lightstep (ServiceNow) — MAINTAINED
- Purpose / problem: Distributed-tracing-first observability (OpenTelemetry pioneers).
- OSS/commercial: Commercial; acquired by **ServiceNow (2021)**.
- Maintenance: Maintained inside ServiceNow's observability story (2026). (Depth debt.)
- Alternatives: Honeycomb, Grafana Tempo.
- Use: U(Proposed).

## OB-09 — OpenTelemetry — ACTIVE (standard)
- Purpose / problem: The vendor-neutral telemetry standard (traces/metrics/logs; Collector; semantic conventions incl. GenAI).
- OSS/commercial: Open standard (CNCF).
- Maintenance: Active (2026); the substrate everything above integrates with.
- Alternatives: Proprietary agents.
- Use: U(Verified) — industry standard.

## OB-10 — Better Stack — ACTIVE
- Purpose / problem: Uptime monitoring + on-call + status pages + telemetry bundles; the "two-person team" pick in 2026 guides.
- OSS/commercial: Commercial. Free: 10 monitors, 1 status page, 100k exceptions, 3GB logs (3-day retention); paid from $29/responder/mo; telemetry $25/mo for 40GB each of logs/traces/metrics.
- Maintenance: Active (2026).
- Alternatives: Pingdom, Checkly, Grafana Cloud.
- Use: U(Proposed).

## OB-11 — Last9 — ACTIVE
- Purpose / problem: BYOC observability: high-cardinality telemetry with cost control at ingestion; one license, infra on your cloud bill; no charge per label/metric name.
- OSS/commercial: Commercial (BYOC).
- Maintenance: Active (2026).
- Alternatives: Grafana Cloud, Chronosphere.
- Use: U(Proposed). (Lightly researched — depth debt.)

## OB-12 — Pydantic Logfire — ACTIVE
- Purpose / problem: LLM/Python-native observability from the Pydantic team; OTel-based.
- OSS/commercial: Commercial SaaS + OSS SDK.
- Maintenance: Active (2026).
- Alternatives: Langfuse, LangSmith.
- Use: U(Proposed). (Lightly researched — depth debt.)

## OB-13 — Checkly — ACTIVE
- Purpose / problem: Synthetic monitoring + API checks as code (Playwright-based checks).
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: Better Stack, Datadog Synthetics.
- Use: U(Proposed).

## Notable status findings (observability)
- Datadog — the **$65M bill** + **Delivery Hero → Grafana Cloud (1H25)** are the canonical cost-migration stories.
- Sentry — **BSD-3 → BSL → FSL** license saga (2019 → 2023).
- Grafana — **AGPLv3** (2021); LGTM is the OSS default stack.
- 2026 pricing reality: the meter (per-host, per-GB, per-series, per-event) is the product decision, not the feature list.

---

### Per-record metadata (condensed)
- Pricing landscape: last9.io "Best Observability Tools in 2026" (Oct 2026); pydantic.dev "Best OpenTelemetry Backends in 2026" (Aug 2026); editorialge.com (Oct 2026). Confidence: Medium (vendor-adjacent + editorial).
- Sentry license saga: summary evidence (BSD-3→BSL 2019→FSL Nov 2023). Confidence: High.
- Datadog $65M bill / Delivery Hero: summary evidence. Confidence: Medium–High.
- New Relic $6.5B PE: summary evidence. Confidence: High.
- selfhost.directory/sentry (Oct 2026): alternatives list incl. Highlight, SigNoz, Coroot, OpenObserve. Confidence: Low–Medium (directory).
