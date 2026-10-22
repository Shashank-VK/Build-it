# Slack — product engineering case study (Flannel, incident-driven architecture, cellular)

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Slack is the messaging-scale exemplar: **Flannel** (application-level edge cache, 2017-era: 4M concurrent connections, 600K qps), **Vitess** for MySQL sharding, and the **cellular architecture** adopted after the Jan 2021 incident. The evidence is secondary-technical (engineering-blog summaries, ByteByteGo, SRE-world docs) — Slack's primary engineering blog posts are cited via these; direct primary fetches are a verification debt.

## 1. Forensic reconstruction — how the machine actually works

### Flannel: the application-level edge cache
- Claim: **Flannel** is Slack's edge-caching layer: a man-in-the-middle on the WebSocket connection that maintains a **team-organized cache** at the edge, pushing updates **just-in-time** to clients. Reported 2017 scale: **4M concurrent connections, 600K queries/sec**. Label: **Corroborated** — abundant-ai/sre-world Slack PRD (GitHub); bytebytego ("how Slack supports billions of daily"); snowan/kuma-blog design doc. Confidence: medium-high on the architecture; medium on the exact figures (2017-era, via secondary sources).
- Claim: The design insight: cache by *team* (the natural locality unit — members of a team read the same channels) rather than by user or globally; the edge node holds the team's working set and pushes diffs over the persistent WebSocket. Label: **Corroborated** (same sources). Plain-English: put a smart cache near the user that already knows what their team is looking at, and only send changes.

### The data layer: Vitess-sharded MySQL
- Claim: Slack shards MySQL with **Vitess** (the YouTube-derived sharding middleware) — the standard answer to "MySQL at Slack scale" without abandoning the relational model. Label: **Corroborated** (sre-world; kuma-blog). Confidence: medium-high.

### Incident-driven architecture: the cellular turn
- Claim: After a major incident (Jan 2021 — a gray failure in an AWS transit-center-adjacent dependency; Slack down ~5 hours), Slack moved toward a **cellular architecture**: the service is partitioned into cells (isolated stacks serving subsets of teams) so a failure in one cell can't cascade to all. Combined with **Envoy** as the service-mesh data plane. Label: **Corroborated** — sre-world docs; widely reported incident. Confidence: medium-high on the direction; medium on current completion (cellular migrations take years — current state Unknown).

## 2. Postmortem record — failures, dissected
- **Jan 2021 outage (~5 hours):** a gray failure (not hard-down — degraded in ways health checks didn't catch) in infrastructure Slack depended on cascaded into a global outage. The postmortem response was architectural: cellular isolation so no single dependency failure can take down all teams. Label: **Corroborated** (secondary; primary Slack postmortem cited but not fetched — verification debt).
- **Feb 2020 incident:** HAProxy slot exhaustion during a traffic surge — the connection layer ran out of capacity in a way that auto-scaling didn't cover. (Reported in secondary sources; not deep-dived — **Corroborated** directionally.)
- **The pattern:** Slack's incidents are *edge/connection-layer* incidents (Flannel's territory) and *dependency* incidents (the cellular motivation) — the failure surface of a real-time messaging system is the connection fan-out and the blast radius, not the database. The architecture evolution (Flannel → cellular) tracks the incident history exactly. Label: **Inferred** (pattern synthesis) on **Corroborated** incidents.

## 3. Narrative audit — dismantling with receipts
- **"Incident-driven architecture" — the honest name for it.** Slack's architecture didn't come from a visionary blueprint; it came from outages (Flannel from connection-scale pain, cellular from the 2021 gray failure). The audit credit: this is how real architectures form — *the incident history is the architecture document*. Teams writing architecture vision docs should instead write the incident history and derive the architecture from it. The risk: incident-driven architecture over-fits to the *last* failure (cellular solves 2021's failure; the next one will be elsewhere). Label: **Inferred** (audit synthesis).
- **The gray-failure lesson is the deepest one.** The 2021 incident wasn't a clean outage — it was *degraded*, which health checks missed. The receipts point to the hardest monitoring problem: binary health checks can't see gray. The transferable lesson isn't "adopt cellular" (expensive, multi-year) — it's **monitor the user-visible behavior** (message send latency, delivery success) rather than the infrastructure's self-report. Cellular is the structural answer; user-centric SLOs are the cheap answer everyone should copy first. Label: **Inferred** on **Corroborated** incident character.
- **4M connections / 600K qps — date the numbers.** The Flannel figures are 2017-era and widely repeated as current; Slack's scale today is far larger and the architecture has evolved (cellular changes the topology). Quoting 2017 numbers as "Slack's scale" is the kind of staleness this corpus exists to prevent — always date scale figures. Label: **Inferred** (method note); the figures' date is **Corroborated**.
- **Primary-source debt.** This file leans on secondary technical summaries (ByteByteGo, sre-world, kuma-blog) of Slack's engineering blog rather than the primary posts. The architecture claims are convergent across independent secondaries (confidence medium-high), but the primary posts should be fetched before quoting specifics. Recorded as verification debt, not fact. Label: **Unknown** (primary not fetched).

## Transferable lessons
1. **Cache by the natural locality unit.** Flannel caches by *team* — find your product's equivalent (the group whose members read the same data) and put the cache there.
2. **Let the incident history write the architecture.** Derive architectural bets from postmortems, not vision docs — but watch for over-fitting to the last failure.
3. **Monitor user-visible behavior, not infrastructure self-reports.** Gray failures defeat health checks; message-delivery SLOs catch what infra monitoring misses.
4. **Cellular architecture bounds blast radius** — partition into isolated cells serving subsets of users so no single failure is global. Price: years of migration.
5. **Date your scale figures.** 2017's 4M connections is history, not spec. Every scale claim needs a timestamp.

## Sources
| ID | Claim | URL (verbatim) | Type | Author/Org | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| SL1 | Flannel design; team-organized cache; 4M connections/600K qps (2017) | https://github.com/abundant-ai/sre-world/blob/HEAD/substrates/slack-spine/design/slack-prd.md | Secondary technical (GitHub) | abundant-ai/sre-world | n.d. | 2026-10-10 | Medium |
| SL2 | Slack messaging-system scale and design | https://blog.bytebytego.com/p/how-slack-supports-billions-of-daily | Secondary technical | ByteByteGo | n.d. | 2026-10-10 | Medium |
| SL3 | Slack system-design doc (Flannel, Vitess, Envoy, cellular) | https://github.com/snowan/kuma-blog/blob/HEAD/AI-blogs/design-slack-messaging-system.md | Secondary technical (GitHub) | snowan/kuma-blog | n.d. | 2026-10-10 | Low-medium |
| SL4 | Jan 2021 outage; cellular architecture response | (cited via SL1/SL3; primary Slack postmortem not fetched — verification debt) | Secondary | Multiple | 2021 | 2026-10-10 | Medium |

**Gaps:** Slack primary engineering-blog posts (not fetched — verification debt); current cellular migration state (Unknown); Flannel current design (Unknown — 2017 snapshot only); Feb 2020 HAProxy incident (noted, not deep-dived).
