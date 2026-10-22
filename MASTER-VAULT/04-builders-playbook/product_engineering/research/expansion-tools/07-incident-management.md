# §30 — Incident Management, On-Call & Status (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## IM-01 — PagerDuty — ACTIVE (stagnant-growth, restructuring)
- Purpose / problem: On-call management, alert routing/escalation, event intelligence/AIOps, incident response automation (Operations Cloud, being rebranded "PD Reliability Platform").
- OSS/commercial: Commercial SaaS (NYSE: PD). Pricing historically per-user with paid AIOps add-ons; new usage-based pricing for Operations Cloud.
- Integration: Broad alert-source integrations; Slack; MCP (AWS Quicksuite / Glean AI ecosystem partner, 2026).
- Maintenance: Active. Q2 FY27 (ended Jul 31, 2026): ARR **$501M** (first time over $500M), revenue $124.4M (+0.8% YoY), 15,506 paid customers, 884 customers >$100k ARR, dollar-based net retention 98% (inflection after quarters of erosion), 5th consecutive GAAP-profitable quarter. **15% workforce reduction (~173 of 1,155) announced Aug 2026** — concentrated in non-customer-facing roles; restructuring charges $5.5–7.5M; guided FY27 revenue $491.5–496.5M (essentially flat YoY), non-GAAP operating margin 25–26%. New CEO John DiLullo (appointed Aug 2026); CFO Eric Prengel; board: Alex Shootman.
- Product moves 2026: industry-first end-to-end incident management AI Agent Suite; autonomous SRE agent upgrades; AI shift-management for on-call; CoreWeave and Anduril building on the platform; lands/expands include Anthropic, Palo Alto Networks, Delivery Hero, GM, Twilio, Perplexity AI.
- Limitations: Growth essentially flat; expensive add-on model vs newer bundled competitors; not Slack-native at its core.
- Security: Standard enterprise SaaS controls; usage-based pricing changes telemetry billing.
- Alternatives: Opsgenie (sunsetting), incident.io, Rootly, FireHydrant, Grafana OnCall/IRM, Squadcast, xMatters (acquired by Everbridge).
- Switching costs: Medium–high (on-call schedules, escalation policies, integrations embedded).
- Use: U(Verified) — Twilio, Anthropic, CoreWeave, Anduril, Palo Alto Networks, Delivery Hero, GM, Perplexity (vendor earnings).

## IM-02 — Atlassian Opsgenie — DEPRECATED (sunset Apr 5, 2027)
- Purpose / problem: Alerting and on-call scheduling with deep Atlassian integration.
- Maintenance: **End of sale Jun 4, 2025; service shutdown Apr 5, 2027.** Migrations directed to Jira Service Management alerting/ops.
- Alternatives: Jira Service Management, PagerDuty, incident.io, Rootly, Grafana IRM.
- Switching costs: Medium (Atlassian migration tooling provided).
- Use: U(Verified) — existing Atlassian shops in migration planning.

## IM-03 — incident.io — ACTIVE (independent)
- Purpose / problem: Slack-native all-in-one incident management: on-call (40+ alert sources), incident response, status pages; AI SRE for investigation, triage, RCA, drafted fixes, call transcription, auto post-mortems.
- OSS/commercial: Commercial SaaS, proprietary. Pricing: free Basic tier; $15–$25/user/month; AI SRE included from Pro.
- Integration: Slack + Microsoft Teams native; alert sources; status pages.
- Maintenance: Active; independent (not acquired). Cited customers: Netflix, Airbnb (per community sources, Corroborated-weak).
- Limitations: Proprietary; on-call is an add-on to per-seat pricing; no self-host.
- Security: SOC 2 typical for the tier; incident data (Slack transcripts) lives in vendor.
- Alternatives: Rootly, FireHydrant, PagerDuty, Grafana IRM.
- Switching costs: Medium (workflows, runbooks, on-call configs).
- Use: U(Proposed) — widely regarded in 2026 buyer's guides; named customers via vendor/community claims.

## IM-04 — Rootly — ACTIVE (independent, AI-native)
- Purpose / problem: AI-native incident management platform: Incident Response, On-Call, and a dedicated AI SRE product (confidence-scored RCA, similar-incident surfacing, suggested fixes, AI meeting bot for incident bridges, reasoning trace shown before acting).
- OSS/commercial: Commercial SaaS, proprietary. Pricing: ~$20/user/month per product; AI SRE via sales; free tier for non-paging stakeholders.
- Integration: Slack-native (also Teams); on-call; retrospectives; status pages.
- Maintenance: Active; independent. Cited users: NVIDIA, Replit, Canva, Cisco (per Rootly positioning; Corroborated-weak).
- Limitations: Proprietary; pricing sales-led for AI tier.
- Security: Enterprise controls per tier.
- Alternatives: incident.io, FireHydrant, PagerDuty.
- Switching costs: Medium.
- Use: U(Proposed).

## IM-05 — FireHydrant — ACTIVE (acquired by Freshworks)
- Purpose / problem: Incident management with service-catalog-driven runbook automation; Signals (on-call); status pages; AI summaries/transcription/retrospectives.
- OSS/commercial: Commercial SaaS, proprietary. ~$25/responder/month Pro (annual); AI features on Enterprise tier only.
- **Acquisition: Freshworks announced acquisition Dec 16, 2025; closed Jan 2026** (undisclosed amount; FireHydrant had raised ~$32.5M, est. revenue $5–25M, 25–100 employees).
- Limitations: AI locked to Enterprise; no autonomous investigation; roadmap now inside Freshworks.
- Security: Standard SaaS.
- Alternatives: incident.io, Rootly, PagerDuty.
- Switching costs: Medium.
- Use: U(Proposed).

## IM-06 — Grafana OnCall / IRM — ACTIVE (consolidated)
- Purpose / problem: OSS-friendly on-call + incident response inside the Grafana stack (now Grafana IRM: on-call, incidents, status pages).
- OSS/commercial: OSS (AGPL-3.0 core) + Grafana Cloud managed.
- Maintenance: Active (2026).
- Limitations: Narrower than PagerDuty feature set; best inside Grafana shops.
- Security: Self-hostable.
- Alternatives: PagerDuty, incident.io, Squadcast.
- Switching costs: Low–medium inside Grafana stack.
- Use: U(Proposed). (Depth debt — verify current naming: OnCall → IRM consolidation.)

## IM-07 — Squadcast — ACTIVE
- Purpose / problem: SRE-focused on-call + incident response (Squadcast Reliability Workflow).
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026).
- Alternatives: PagerDuty, Rootly.
- Use: U(Proposed). (Lightly researched — depth debt.)

## IM-08 — xMatters (Everbridge) — ACTIVE
- Purpose / problem: Intelligent alerting/on-call; Everbridge critical-event management.
- OSS/commercial: Commercial.
- Maintenance: Active (2026).
- Alternatives: PagerDuty, Opsgenie (sunsetting).
- Use: U(Proposed). (Lightly researched — depth debt.)

## IM-09 — Statuspage (Atlassian) — ACTIVE
- Purpose / problem: Hosted status pages + incident communication.
- OSS/commercial: Commercial (Atlassian).
- Maintenance: Active (2026).
- Alternatives: incident.io status pages, Instatus, Cachet (OSS), cState (OSS).
- Use: U(Proposed). (Lightly researched — depth debt.)

## IM-10 — Cachet / cState — MAINTAINED (OSS status pages)
- Purpose / problem: Self-hosted open-source status pages (Cachet: PHP; cState: static/Hugo-based).
- OSS/commercial: OSS (BSD/MIT family).
- Maintenance: Community-maintained (2026).
- Alternatives: Statuspage, Instatus.
- Use: U(Proposed). (Lightly researched — depth debt.)

## Notable status findings (incident management)
- Opsgenie — **sunset Apr 5, 2027** (end of sale Jun 2025).
- FireHydrant — **acquired by Freshworks** (Dec 2025 / closed Jan 2026).
- PagerDuty — profitable but flat: **15% layoffs Aug 2026**, new CEO, flat FY27 revenue guide (~$494M), ARR $501M milestone.
- incident.io and Rootly — both independent; the two Slack-native AI-SRE leaders.

---

### Per-record metadata (condensed)
- PagerDuty Q2 FY27 results + 15% layoffs: BusinessWire press release Aug 27, 2026 (primary); stocktitan 8-K; Insider Monkey Sep 1, 2026; ainvest analysis. Accessed 2026-10-10. Confidence: High. Corroboration: multiple independent outlets + SEC filing.
- FireHydrant→Freshworks: Benzinga/Owler Dec 16, 2025 announcement; Arvo comparisons (Jul 2026) confirm closed Jan 2026. Confidence: High.
- incident.io / Rootly / FireHydrant comparison: Arvo (aurorasre.ai) 2026 comparisons; Rootly vendor page; dev.to social mentions. Confidence: Medium (vendor + community, some self-serving).
- Opsgenie sunset: Rootly 2026 guide (secondary); primary Atlassian notice recorded in summary (end of sale Jun 4 2025, shutdown Apr 5 2027). Confidence: High.
