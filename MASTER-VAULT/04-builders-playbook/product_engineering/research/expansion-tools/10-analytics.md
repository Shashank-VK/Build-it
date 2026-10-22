# §30 — Product & Web Analytics (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## AN-01 — PostHog — ACTIVE
- Purpose / problem: All-in-one product analytics for developers: event tracking/autocapture, funnels, session replay, feature flags, experiments, surveys, data warehouse — one SDK.
- OSS/commercial: Open-core. Self-host option exists (MIT-licensed components historically) but **as of mid-2026 PostHog directs production users to cloud** rather than supporting large self-hosted clusters. Cloud free tier: 1M analytics events, 5k recordings, 1M flag requests, 100k exceptions/mo, 1 project, no card, usage stops at limits; 1-year retention free (7 years PAYG).
- Maintenance: Active. **Sacra (2026): $57.5M revenue, $1.4B valuation, $182M raised, 138% YoY growth.**
- Limitations: Event volume (not users) drives cost — cap volume early; self-host production path de-emphasized.
- Security: EU/US cloud options; session replay = PII surface (masking controls).
- Alternatives: Amplitude, Mixpanel, Plausible (web-only), June.
- Switching costs: Medium (event taxonomy, flags, experiments).
- Use: U(Verified) — ADRs in real repos (thaichess ADR-0003, Jul 31, 2026: chose PostHog free cloud over Plausible Cloud/Umami; ResumeSpyWeb issue #65, May–Jun 2026: Plausible/Umami + PostHog stack adopted).

## AN-02 — Amplitude — ACTIVE (absorbed Statsig brand)
- Purpose / problem: Enterprise product analytics: behavioral cohorts, experimentation, CDP; aggressive AI-agent push in 2026 (agents sifting usage data, auto-recommendations).
- OSS/commercial: Commercial SaaS. Free tier; Plus from $49/mo.
- Maintenance: Active; **took over the Statsig brand and customer base (May 2026)** while Statsig's engineering team stayed at OpenAI.
- Alternatives: Mixpanel, PostHog, Heap.
- Switching costs: High.
- Use: U(Proposed).

## AN-03 — Mixpanel — ACTIVE
- Purpose / problem: Self-serve event analytics: funnels/retention, AI Copilot, **warehouse-native (Mirror)**.
- OSS/commercial: Commercial SaaS. Free; Growth from ~$25/mo.
- Maintenance: Active (2026).
- Alternatives: Amplitude, PostHog.
- Switching costs: High.
- Use: U(Proposed).

## AN-04 — Plausible — ACTIVE (bootstrapped, EU)
- Purpose / problem: Privacy-first web analytics: cookieless, no consent banner, 2.5KB script, single-page dashboard.
- OSS/commercial: OSS **AGPL** Community Edition (self-host free; needs Postgres + ClickHouse + your ops) + commercial Cloud (EU-hosted, Hetzner Germany; 30-day trial then paid). **Self-funded/bootstrapped, no investors** (Estonia entity) — explicitly no acquisition risk, no pressure to monetize data.
- Maintenance: Active (2026).
- Limitations: CE self-host is "free of licensing cost, not free of operating cost" (ClickHouse + Postgres + backups); funnels only on top tiers.
- Security: EU data residency; minimal collection.
- Alternatives: Umami, Fathom, Simple Analytics, Matomo.
- Switching costs: Low.
- Use: U(Verified) — thaichess ADR evaluated Plausible (consent-gated wiring existed); ResumeSpyWeb adopted Plausible/Umami for pageviews.

## AN-05 — Umami — ACTIVE
- Purpose / problem: Minimal self-hosted web analytics (deliberately bare); deploys to Vercel/Railway in minutes.
- OSS/commercial: OSS MIT (self-host always free); Cloud: 14-day trial then billed.
- Maintenance: Active (2026).
- Limitations: Bare feature set (no funnels/replay depth).
- Alternatives: Plausible, Fathom.
- Switching costs: Low.
- Use: U(Verified) — ResumeSpyWeb issue #65 (2026).

## AN-06 — Fathom — ACTIVE
- Purpose / problem: Simple privacy-first analytics; entry $15/mo (100k pageviews, 50 sites).
- OSS/commercial: Commercial.
- Maintenance: Active (2026).
- Alternatives: Plausible, Simple Analytics.
- Use: U(Proposed). (Depth debt.)

## AN-07 — Matomo — ACTIVE
- Purpose / problem: Full-suite self-hostable analytics (heatmaps, session recording, goals); 15-year track record; the regulated-industry pick.
- OSS/commercial: OSS (on-premise free) + cloud.
- Maintenance: Active (2026).
- Limitations: Heaviest of the group to run.
- Alternatives: Plausible, PostHog.
- Use: U(Proposed). (Depth debt.)

## AN-08 — Heap — ACTIVE
- Purpose / problem: Automatic data capture (autocapture) product analytics.
- OSS/commercial: Commercial. Free 10k sessions/mo; Growth from $3,600/yr.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: PostHog, Amplitude.
- Use: U(Proposed).

## AN-09 — Pendo — ACTIVE
- Purpose / problem: B2B product analytics + in-app guides, NPS, roadmaps.
- OSS/commercial: Commercial. Free up to 500 MAU.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: Appcues, PostHog.
- Use: U(Proposed).

## AN-10 — June — ACTIVE
- Purpose / problem: Lightweight B2B product analytics on top of Segment.
- OSS/commercial: Commercial.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: PostHog, June's warehouse-native peers.
- Use: U(Proposed).

## Notable status findings (analytics)
- PostHog — **$57.5M revenue / $1.4B valuation / 138% growth** (Sacra 2026); production self-host de-emphasized mid-2026.
- Plausible — bootstrapped, EU-hosted, AGPL; the anti-acquisition-risk pick.
- Amplitude — absorbed Statsig's brand/customers (May 2026); AI-agent analytics push.
- The 2026 practitioner stack pattern: **Plausible/Umami (pageviews) + PostHog (funnels)** — seen in real ADRs.

---

### Per-record metadata (condensed)
- PostHog metrics: sacra-pdfs.s3.us-east-2.amazonaws.com/posthog.pdf (2026). Confidence: Medium (Sacra estimates).
- PostHog/Plausible/Umami free tiers + self-host economics: github.com/fringe4life/van-life instrumentation doc (Sep 11, 2026); dev.to self-hosting economics (Oct 2026); litlyx.com; observix.ai. Confidence: Medium.
- PostHog ADRs: github.com/chindanainakub/thaichess ADR-0003 (Jul 31, 2026); github.com/feifeijin/resumespyweb issue #65 (May–Jun 2026). Confidence: High (primary).
- Plausible company facts: plausible.io (self-published). Confidence: Medium–High.
- Amplitude/Mixpanel/Heap/Pendo: openaiagent.io (Sep 2026). Confidence: Low–Medium (editorial).
