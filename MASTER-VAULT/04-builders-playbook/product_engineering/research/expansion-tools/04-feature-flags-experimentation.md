# §30 — Feature Flags & Experimentation (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## FF-01 — LaunchDarkly — ACTIVE
- Purpose / problem: Category-defining feature management: sophisticated targeting (rules, segments, scheduling), percentage rollouts, audit logging, experimentation add-ons.
- OSS/commercial: Commercial, proprietary SaaS (+ Relay Proxy for hybrid). Pricing: Foundation from ~$10/seat/mo; free trial; Guardian tier (guardrail metrics, auto-rollback) added 2026.
- Integration: Broad SDK coverage (server, mobile, web, edge); OpenFeature provider; Terraform provider.
- Maintenance: Active (2026).
- Limitations: Price reflects category leadership — expensive at scale; experimentation is an add-on, not native core.
- Security: Flags are a control plane: RBAC, approvals, audit trails on Enterprise/Guardian; never use client-side flags for access control (industry guidance).
- Alternatives: Unleash, Flagsmith, Split/Harness FME, GrowthBook, Statsig.
- Switching costs: Medium–high (flag checks permeate code; OpenFeature reduces this).
- Use: U(Proposed) — widely adopted; no single named customer verified in this pass.

## FF-02 — Split → Harness FME — ACTIVE (acquired, rebranded)
- Purpose / problem: Feature flagging + experimentation with statistical engine for comparative experiments in production; audience segmentation.
- OSS/commercial: Commercial. **Acquired by Harness Jun 11, 2024** (undisclosed; Split had raised $100M+); rebranded **Harness Feature Management & Experimentation (FME)**; lives at app.harness.io; no longer sold standalone — enabled as Harness module. SDKs/docs still carry Split names (`@splitsoftware/splitio`, `SplitFactory`).
- Integration: SDKs (naming retained); Harness platform modules (CI/CD, etc.).
- Maintenance: Active inside Harness; integration completed (Feb 2025: six new FME features announced).
- Limitations: Standalone Split customers must migrate into Harness platform; SDK naming lag creates confusion.
- Security: Harness permissioning/governance models apply.
- Alternatives: LaunchDarkly, Unleash, Statsig, GrowthBook.
- Switching costs: Medium (platform consolidation).
- Use: U(Proposed).

## FF-03 — Statsig — ACTIVE (acquired TWICE: OpenAI → Amplitude)
- Purpose / problem: All-in-one product experimentation: feature flags, A/B testing, product analytics, session replay; 1T+ events/day claimed; Warehouse Native mode (BigQuery/Snowflake/Databricks/Redshift).
- OSS/commercial: Commercial SaaS. Founded 2021 (Vijaye Raji, ex-Facebook); raised $153.4M (Sequoia, ICONIQ, Madrona).
- **Double acquisition:**
  1. **Sep 2, 2025: OpenAI acquires Statsig for ~$1.1B (all-stock)** — one of OpenAI's largest acquisitions; Raji becomes OpenAI CTO of Applications (reporting to Fidji Simo); Statsig to operate independently from Seattle. (GeekWire; Wikipedia; OpenAI announcement.)
  2. **May 2026: Amplitude takes over the Statsig brand and customer base**; the engineering team that built Statsig stays at OpenAI. Roadmap now set inside OpenAI/Amplitude, not an independent vendor. (GrowthBook migration blog; Spotify Confidence comparison page.)
- Limitations: Roadmap ownership uncertainty post-double-acquisition; competitor migration guides actively target Statsig customers.
- Security: Standard SaaS; warehouse-native mode reduces data movement.
- Alternatives: GrowthBook (open-source, warehouse-native), Eppo, LaunchDarkly, Split/FME, Spotify Confidence.
- Switching costs: Medium–high (experimentation history, SDK integration).
- Use: U(Verified) — Notion, Vercel named as customers (vendor/press); OpenAI itself used Statsig pre-acquisition.

## FF-04 — Unleash — ACTIVE
- Purpose / problem: Open-source feature management platform (self-host or managed); gradual rollouts, variants, constraints, segments, environments.
- OSS/commercial: Open-core. **License note: current repo license reported as AGPL-3.0** (per GrowthBook's 2026 comparison page — older sources say Apache-2.0; treat license as verify-before-adopt). Enterprise editions commercial.
- Integration: SDKs; OpenFeature ecosystem participation (community providers; native provider support described as light).
- Maintenance: Active. **$35M Series B Mar 2026** (One Peak; total $51.5M); 500+ paying customers; 13k+ GitHub stars; "FeatureOps" positioning for AI-generated code governance. Customers cited: Prudential, Lloyds Banking Group, Wayfair, Lenovo.
- Limitations: Self-hosting ops burden; experimentation not native (flags-first).
- Security: Enterprise change-request workflows; SSO/SCIM on enterprise tiers.
- Alternatives: Flagsmith, Flipt, LaunchDarkly, GrowthBook.
- Switching costs: Low–medium.
- Use: U(Verified) — Prudential, Lloyds Banking Group, Wayfair, Lenovo (vendor-cited).

## FF-05 — GrowthBook — ACTIVE
- Purpose / problem: Open-source, warehouse-native experimentation + feature flags: Bayesian/frequentist/CUPED stats engine, sequential testing; no event-ingestion duplication (runs SQL against your warehouse).
- OSS/commercial: Open-core, MIT core. YC W22; **$22.6M Series A Jul 2025**; 43 employees (PitchBook). v5.0.0 (Jul 2026): governance tools, Product Analytics GA. Cloud Starter free (3 users); Pro $40/seat/mo; self-hosted free unlimited.
- Integration: SDKs (JS, Flutter, etc.); warehouse connectors.
- Maintenance: Active.
- Limitations: Most valuable with reliable warehouse/event data; governance/SSO on paid tiers; small-team overkill.
- Security: Data stays in your warehouse (warehouse-native = smaller exfil surface).
- Alternatives: Statsig, Eppo, LaunchDarkly, PostHog experiments.
- Switching costs: Low–medium (local SDK evaluation; manifest-based).
- Use: U(Proposed) — actively courting Statsig migrants post-acquisition.

## FF-06 — Flagsmith — ACTIVE
- Purpose / problem: Feature flags + remote config + segmentation with compliance/governance posture; self-hostable.
- OSS/commercial: Open-core, **BSD-3 core**; paid Enterprise (SSO, advanced governance). Hosted free tier (50k API req/mo); Startup from ~$45/mo.
- Integration: 15+ OSS SDKs; vendor-maintained OpenFeature provider; REST API; Terraform.
- Maintenance: Active (2026).
- Limitations: Self-hosting heavier (requires PostgreSQL); A/B testing leans on integrations (no built-in stats engine).
- Security: Audit logs, RBAC, approval workflows, scheduled changes, SAML SSO, SCIM; offline mode for no-outbound environments.
- Alternatives: Unleash, LaunchDarkly, Flipt.
- Switching costs: Low–medium.
- Use: U(Proposed).

## FF-07 — Flipt — ACTIVE
- Purpose / problem: Lightweight open-source feature flag service (Go); Git-backed/declarative config; gRPC streaming updates.
- OSS/commercial: OSS (license: verify — commonly cited as MIT; not confirmed in this pass).
- Integration: OpenFeature ecosystem; SDKs; container/K8s friendly.
- Maintenance: Active (2026); appears in OpenFeature provider evaluations.
- Limitations: Targeting less rich than LaunchDarkly/Unleash (per ADR comparison).
- Alternatives: flagd, Unleash, Flagsmith.
- Use: U(Proposed). (Depth debt: license + version verification.)

## FF-08 — flagd — ACTIVE
- Purpose / problem: Reference OpenFeature-native feature flag daemon (CNCF-adjacent); file-backed, gRPC streaming; simplest self-hosted OpenFeature provider.
- OSS/commercial: OSS.
- Maintenance: Active (2026); recommended as default self-hosted provider in recent ADRs.
- Alternatives: Flipt, Unleash.
- Use: U(Proposed). (Lightly researched — depth debt.)

## FF-09 — OpenFeature — ACTIVE (standard)
- Purpose / problem: Vendor-neutral feature-flag API/SDK standard (CNCF); swap providers without changing application code.
- OSS/commercial: Open standard/specification; OSS SDKs.
- Maintenance: Active — spec v0.8.0 (early 2026); Node SDK v1.20.2; CNCF incubating→graduated (one source says graduated; treat maturity as Incubating+).
- Limitations: Standardizes the read path only, not flag authoring/governance; provider-specific features may not surface through the abstraction.
- Security: Reduces vendor lock-in risk; flag hygiene (stale-flag cleanup) still the adopter's job.
- Alternatives: Direct vendor SDKs.
- Use: U(Proposed) — adoption pattern visible in 2025–2026 ADRs (LaunchDarkly→Flagsmith/Unleash/Flipt swaps).

## FF-10 — ConfigCat — ACTIVE
- Purpose / problem: Developer-centric feature flag SaaS; simple setup; unlimited team size positioning.
- OSS/commercial: Commercial SaaS, freemium.
- Maintenance: Active (2026).
- Alternatives: LaunchDarkly, Flagsmith.
- Use: U(Proposed). (Lightly researched — depth debt.)

## FF-11 — Eppo — ACTIVE
- Purpose / problem: Warehouse-native experimentation (stats engine on your data warehouse).
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026).
- Alternatives: GrowthBook, Statsig.
- Use: U(Proposed). (Lightly researched — depth debt.)

## FF-12 — Spotify Confidence — ACTIVE
- Purpose / problem: Spotify's internal experimentation platform (15 years) productized; flags, experiments, CUPED (Negi–Wooldridge estimator), group sequential tests, sample-ratio-mismatch checks.
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026).
- Limitations: Newer commercial entrant vs Statsig/GrowthBook mindshare.
- Alternatives: Statsig, GrowthBook, Eppo.
- Use: U(Verified) — Spotify (origin; 15 years internal).

## FF-13 — DevCycle — ACTIVE
- Purpose / problem: Feature management with OpenFeature built into SDKs; edge architecture, local bucketing.
- OSS/commercial: Commercial; open-source APIs/SDKs.
- Maintenance: Active (2026).
- Alternatives: LaunchDarkly, Unleash.
- Use: U(Proposed). (Lightly researched — depth debt.)

## Notable status findings (feature flags)
- Statsig — acquired **twice** (OpenAI Sep 2025 → Amplitude May 2026); roadmap ownership uncertain.
- Split — acquired by Harness Jun 2024, rebranded FME; standalone product gone.
- Unleash — license reported as AGPL-3.0 in 2026 sources (was Apache-2.0) — verify before adopting.
- OpenFeature — the standard de-risking vendor switches; flagd/Flipt as self-hosted defaults.
