# Cloudflare — product engineering case study

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Cloudflare is the exemplar for two things at once: ambitious distributed-systems product engineering (Workers, R2, edge network) and an unusually transparent postmortem culture. This file focuses on the incident/postmortem evidence because it is the strongest and most instructive; product-discovery and design-system material is thinner in public sources (marked Unknown where not found).

## Findings

### Product discovery / requirements
- Claim: Unknown from public engineering sources this pass. Label: **Unknown**.

### Design / UX
- Claim: Unknown specific. Label: **Unknown**.

### Architecture
- Claim: Cloudflare's control plane and analytics ran primarily on servers in three Hillsboro, Oregon data centres, designed to run active-active redundant data clusters so any one facility could go offline without impact. Label: **Verified** — fetched primary postmortem, blog.cloudflare.com, Nov 2023.
- Claim: Control plane was separated from the edge data plane: during the Nov 2023 outage the global network kept serving traffic while dashboard/API/analytics were down. Label: **Verified** (same postmortem).
- Claim: Despite the design, "some critical systems had non-obvious dependencies" on the single facility (PDX-04) — Kafka and ClickHouse, which power log processing/analytics, ran only in PDX-04 while services in the high-availability cluster depended on them. Label: **Verified** (same postmortem).

### Implementation
- Claim: Cloudflare engineers are unusually candid about shipping mistakes in their own generated configuration: the Nov 2025 outage came from a ClickHouse permissions change that made a Bot Management "feature file" exceed the 200-feature runtime limit, causing edge proxy panics every five minutes as correct/corrupted files alternated. Label: **Corroborated** — CEO postmortem via secondary reporting (lokmattimes, sdxcentral, Nov 2025); Cloudflare's own blog post not fetched this pass.
- Claim: Engineers initially misread the Nov 2025 symptoms as a massive DDoS attack (the Aisuru botnet, 15.72 Tb/s, revealed the same week) before identifying the internal cause. Label: **Corroborated** (same reporting).

### Testing / reviews
- Claim: The team had tested taking each (and both) of the *other two* Oregon facilities offline, and tested taking the HA portion of PDX-04 offline — but had "never tested fully taking the entire PDX-04 facility offline," which is what hid the dependency problem. Label: **Verified** — primary postmortem. Transferable lesson: DR tests that don't exercise the real failure (full facility loss, including "boring" stuff like access-control power and staffing) are fiction.
- Claim: The postmortem is explicit that "despite years of plans to make the control plane redundant across multiple data centres, the work had not been prioritised to completion." Label: **Verified** (primary) / **Corroborated** (myappapi secondary analysis).

### Security
- Claim: Flexential (the PDX-04 operator) failed over to generator power "counter to best practices" without informing Cloudflare; none of Cloudflare's observability detected the power-source change. Lesson: your vendor's degraded mode is your degraded mode — monitor the *inputs* to your redundancy, not just your own systems. Label: **Verified** (primary postmortem).
- Claim: During restoration, Flexential's access-control system wasn't on battery backup and the overnight shift had no experienced electrical expert (a technician one week on the job). Compounding human-factors failures at the vendor. Label: **Verified** (primary postmortem, noting Cloudflare flags some details as informed speculation).

### Deployment
- Claim: When failing over to the DR site in Europe, Cloudflare hit a thundering-herd problem: API calls that had been failing overwhelmed the services; rate limits were implemented to regain control. Lesson: DR failover must include demand-side protection, not just capacity. Label: **Verified** (primary postmortem).
- Claim: Cloudflare was "far too lax about requiring new products and their associated databases to integrate with the high availability cluster" before declaring them generally available — products shipped alphas on the default (non-redundant) location and migration to best practices was never formally required at GA. Label: **Verified** (primary postmortem).

### Monitoring
- Claim: Unknown specifics beyond the incident narratives above. Label: **Unknown**.

### User feedback / business outcomes
- Claim: HN thread commentary is split: praise for the transparency of the postmortem ("decent down to earth... transparency") alongside anger that initial comms understated the duration. Label: **Corroborated** — HN first-hand comments (news.ycombinator.com, Nov 2023).

### Documented failures
1. Nov 2023 control-plane/analytics outage (Nov 2–4): Flexential PDX-04 total power failure (PGE maintenance → ground fault → generators tripped → UPS failed after ~4 min of a 10-min rating) + untested full-facility DR + hidden Kafka/ClickHouse dependencies. ~41 hours to full resolution; control plane mostly restored same day via DR site.
2. Nov 2025 edge outage: internal ClickHouse permissions change → oversized Bot Management feature file → edge proxy panics; ~3 hours of intermittent global errors; initially misdiagnosed as DDoS.
3. Sept 2025 dashboard/API outage (tenant-service overload from a dashboard bug) — referenced in incident index, not investigated this pass. Label: **Unverified**.

### Transferable lessons
- Test the *actual* disaster: partial-facility tests missed the dependencies that only a full-facility test would reveal. Label: **Verified**.
- Redundancy you haven't finished building is not redundancy; the postmortem says so explicitly. Label: **Verified**.
- Require HA integration *before* GA, not as a later migration — "innovate quickly" cultures need a gate, or the default path becomes the permanent path. Label: **Verified**.
- Monitor your vendors' state transitions (power source, staffing), not just your own metrics. Label: **Verified** (as an inference from verified facts — the postmortem states they couldn't detect the change).
- Failover needs demand-side defences (rate limits) as well as capacity. Label: **Verified**.
- A CEO-authored, same-week postmortem that names specific internal decisions ("we should have caught them," "that was a mistake") builds more trust than the outage destroys. Label: **Corroborated** (community reception).

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| CF-01 | Nov 2023 postmortem (primary, fetched) | https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/ | Primary eng blog | Matthew Prince / Cloudflare | Nov 2023 | 2026-10-10 | High |
| CF-02 | Outage summary | https://www.theregister.com/on-prem/2023/11/07/cloudflare-issues-postmortem-report-on-two-day-outage/1054867?td=rt-3a | Secondary (press) | The Register | Nov 2023 | 2026-10-10 | Medium |
| CF-03 | Community reception (praise + anger) | https://news.ycombinator.com/item?id=38127313 | Community (first-hand) | HN commenters | Nov 2023 | 2026-10-10 | Medium |
| CF-04 | CliffsNotes: test DR for real | https://blog.ipSpace.net/2023/11/worth-reading-comments-cloudflare-outage/ | Secondary (expert commentary) | Ivan Pepelnjak / ipSpace | Nov 2023 | 2026-10-10 | Medium |
| CF-05 | Nov 2025 ClickHouse/bot-management outage | https://www.lokmattimes.com/technology/global-outage-was-caused-by-internal-error-not-cyberattack-cloudflare-ceo-1/ | Secondary (press, via IANS) | lokmattimes | Nov 2025 | 2026-10-10 | Medium (official blog not fetched) |
| CF-06 | Nov 2025 postmortem analysis | https://www.sdxcentral.com/news/cloudflare-post-mortem-highlights-ai-agent-networking-pitfalls/ | Secondary (trade press) | SDxCentral | Nov 2025 | 2026-10-10 | Medium |

## Narrative audit (retrofit 2026-10-10)
- **Transparency as brand moat.** Cloudflare's postmortems are exemplary — and they're also marketing. No other CDN vendor writes at this depth; the candor *is* the differentiation. That doesn't make them dishonest, but the sample is selected: we see the incidents they choose to narrate, framed by the narrator. Treat the corpus as excellent but non-random.
- **"We misread it as a DDoS first."** The Nov 2025 incident's early misdiagnosis (the Aisuru botnet, 15.72 Tb/s, revealed the same week) is the honest detail most vendors would cut: even Cloudflare's on-call confused an internal config failure with a record attack. Monitoring tells you *something is wrong*; attribution is still hard at the edge.
- **DR theater, confessed.** "We tested taking each of the other two facilities offline, and the HA portion of PDX-04 — but never the entire PDX-04 facility." The audit: their DR testing was *designed around what was convenient to test*, not the real failure. If your DR test has never produced a scary result, it isn't testing anything.
- **Blameless vs. consequence-less.** Across the postmortems, no executive lost their job and no team was reorganized (contrast Apple file 15, Atlassian file 31). Blameless culture is real here — and the open question is whether blamelessness without personnel consequences produces the urgency that firings do. Unknown; both models ship software.
