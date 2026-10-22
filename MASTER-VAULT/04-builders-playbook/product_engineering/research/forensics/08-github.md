# GitHub — Forensic Supplement

**Workstream:** forensics · **Researched:** 2026-10-10 · Read-only research; no installation, building, ranking, or recommendation.
**Supplements:** `../cases-product/03-github.md` (Copilot telemetry, Rust migration, code-review metrics). This file reconstructs the reliability story the sibling missed — **GitHub's 2024–2026 availability decline under AI-driven load**, documented in a peer-reviewed paper — plus the Comment-and-Control exposure, and audits the metrics narratives.
**Confidence key:** **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown**. All sources accessed 2026-10-10.

---

## PART 1 — REVERSE-ENGINEER: how the machine actually works

### The reliability machine under AI load (MDPI peer-reviewed analysis)

**GH-R1 — "Trigger, Not Root Cause": the 2024–2026 availability decline.** A peer-reviewed paper (MDPI *Future Internet*, 2026, futureinternet-18-00377) re-examines GitHub's 2024–2026 incident record **using GitHub's own reports** and finds a consistent structure: *a trigger meets a shared or insufficiently protected dependency, and the failure spreads*. Representative incidents:
- **Oct 2024:** a routine database migration caused local DNS-resolution infrastructure to fail; recovery actions interacted badly with a shared dependency → ~4h of total code-search failure, 25% of Actions workflows delayed.
- **Apr 2025:** one compute-intensive database query starved a critical cluster → Actions, API, Pages deployments, git operations degraded (breadth from concentrating many services' fate in one shared cluster).
- **Jun 2025:** a load spike between internal Actions services exposed a throttling misconfiguration on the workflow-run critical path → 47.2% of runs delayed, 21% failed; spread to **60% of Copilot coding-agent sessions cancelled** and all branch-based Pages deployments blocked.
- **Aug 2025:** two incidents, same template (production database changes; the paper's excerpt cuts off mid-sentence in the captured text).
- **Aug 2026:** five separate incidents in one month — Aug 6 (>10h, internal Actions event-processing service), Aug 17 (~8h, traffic peak saturated Central US load balancers; Copilot down 6h44m; API/Issues/PRs/Actions down 2h+; ~20% web/API error rates, 50% for archive/raw downloads, spreading to SAML/OIDC auth). July 2026: eight incidents, incl. a 9h Actions delay July 9.
- The paper's thesis: **AI-agent-generated traffic is the rising trigger** — GitHub's own blog posts (April and Aug 12, 2026) called incident severity/frequency/duration "unacceptable." The company's stated rule — "availability first, then capacity, then features" — is acknowledged by executives as not matching recent performance. · **Corroborated (peer-reviewed paper built on GitHub's own incident reports)** · Sources: mdpi.com/1999-5903/18/7/377 (2026); techtarget.com (2026-08-19, on the Aug 17 outage: "network saturation on load balancers in Central US due to a new peak in traffic"); webpronews.com/github-actions-stumbles-again (2026-10). · *Engineering implication: the platform that hosts the world's CI is being degraded by the traffic profile of the AI agents it also sells — GitHub is both arsonist and firefighter in its own reliability story. The "trigger, not root cause" framing is the transferable artifact: stop asking what the trigger was; ask what the shared dependency was.*

**GH-R2 — The incident-response posture.** GitHub publishes availability reports with timelines and remediation steps; the Aug 2026 blog "walks through each case." The forensic observation: GitHub's transparency about incidents is high (detailed public write-ups), while the *recurrence* is the story — five incidents in August 2026 alone, after the April 2026 "unacceptable" post. · **Corroborated** · Source: webpronews.com (2026-10). · *Implication: transparency without remediation velocity is just narration. The paper's "trigger meets shared dependency" pattern repeating for 2+ years suggests architectural coupling, not bad luck.*

### The metrics machine (Copilot telemetry)

**GH-R3 — What the acceptance-rate numbers actually measure (sibling-covered; forensic framing).** 27% acceptance (MAPS 2022, peer-reviewed, Ziegler et al.) → ~30–34% in larger telemetry; acceptance predicts *self-reported productivity* better than persistence metrics. The forensic points: (a) acceptance is measured **only on IDE inline ghost-text** — CLI/Chat/agent actions tracked separately (sibling GH-05); (b) the 60M-reviews/71%-actionable code-review figures are **GitHub grading its own product** with no head-to-head vs human bug-catch rate; (c) the metrics that made Copilot look good (acceptance) are *feeling* predictors, not quality measures — the paper itself showed this. · **Verified (peer-reviewed) for the MAPS findings; Corroborated for the telemetry scope** · Sources: sibling GH-02/GH-05.

---

## PART 2 — POSTMORTEM: the public failure record

Sibling found none at incident level ("Unknown — gap, not clean record"). **This pass fills the gap:**

**GH-P1 — Aug 17, 2026 outage (network saturation, ~8h; Copilot 6h44m).** New traffic peak saturated Central US load balancers; 20% error rates on web/API, 50% on archive/raw downloads; spread to SAML/OIDC, Copilot, PRs, Issues, Actions. Postmortem cited "network saturation on load balancers in Central US due to a new peak in traffic." · Corroborated (TechTarget 2026-08-19; MDPI paper).

**GH-P2 — Aug 6, 2026 (>10h, Actions event-processing).** Internal Actions service handling event processing; part of the five-incident August. · Corroborated (webpronews 2026-10, citing GitHub's August 2026 blog).

**GH-P3 — July 2026: eight incidents, incl. 9h Actions delay (July 9)** hitting hosted runners, Pages builds, Copilot features. · Corroborated (same).

**GH-P4 — Jun 2025: throttling misconfiguration → 60% of Copilot coding-agent sessions cancelled.** · Corroborated (MDPI paper, from GitHub's own reports).

**GH-P5 — Oct 2024: DB migration → DNS failure → 4h code-search outage.** · Corroborated (MDPI paper).

**GH-P6 — Comment-and-Control exposure (Apr 2026).** GitHub's **Copilot Coding Agent** was one of the three agents vulnerable to PR/issue-comment prompt injection exfiltrating `GITHUB_TOKEN` (see 07-anthropic.md AN-P1). GitHub participated in the coordinated disclosure. · Corroborated (vectara/awesome-agent-failures; oddguan.com).

---

## PART 3 — DISMANTLE: narratives vs evidence

### D1 — "Availability first, then capacity, then features" vs the ledger
- **Official narrative:** GitHub's stated guiding rule; April and August 2026 blog posts called the incident pattern "unacceptable" and pledged improvements.
- **Contradiction:** The pledge post (April 2026) was followed by eight incidents in July and five in August 2026 — *worse* after the "unacceptable" declaration. The MDPI paper's structural finding (trigger meets shared dependency) describes an architecture that keeps producing the same shape.
- **Forensic verdict:** The rule is stated; the ledger shows it is not operational. The deeper point: **the capacity pressure comes from GitHub's own product strategy** — Copilot coding agents generate the traffic spikes that saturate the platform. "Availability first" is incompatible with "agent traffic growth at all costs" unless the shared dependencies get bulkheaded. The paper says exactly this structurally. · **Verdict: narrative dismantled — the company's growth engine and its reliability rule are in direct conflict (Corroborated, peer-reviewed).**

### D2 — "Copilot metrics prove productivity" vs what the metrics measure
- **Official narrative:** Acceptance rates (~30%), 60M reviews, 71% actionable feedback, Faros bakeoff wins.
- **Contradiction:** The foundational paper (Ziegler et al., peer-reviewed) shows acceptance predicts *perceived* productivity, not quality; the review metrics are vendor-graded with no human head-to-head; the telemetry excludes agent/CLI/Chat actions — i.e., the fastest-growing usage surface.
- **Forensic verdict:** The metrics program is sophisticated (Verified) and the *interpretation* sold with it exceeds what the metrics establish. This is the industry's cleanest example of Goodhart-adjacent metric marketing: the thing measured (acceptance) became the thing optimized, and the peer-reviewed caveat (it's a feeling predictor) didn't travel with the headline. · **Verdict: narrative qualified — metrics real, conclusions oversold.**

### D3 — The platform paradox (Proposed synthesis)
- GitHub sells the tools that generate the load (Copilot agents) that degrades the platform (Actions saturation) that developers need to ship the code the tools wrote. No single narrative captures this; the MDPI paper's "trigger, not root cause" is the closest. The forensic contribution: **GitHub's reliability problem is endogenous to its business model**, not exogenous bad luck. · **Proposed.**

---

## EVIDENCE REGISTER (forensics additions)

| ID | Claim | URL | Source type | Author/org | Pub date | Accessed | Confidence | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|
| GHFR-01 | "Trigger, Not Root Cause": 2024–2026 incident anatomy; trigger meets shared dependency; AI-agent traffic as rising trigger | https://www.mdpi.com/1999-5903/18/7/377 | Primary-technical (peer-reviewed paper, built on GitHub's own reports) | MDPI Future Internet | 2026 | 2026-10-10 | High (peer-reviewed; sources are GitHub's own reports) | Corroborated by techtarget, webpronews |
| GHFR-02 | Aug 17, 2026 outage: LB saturation, 20%/50% error rates, Copilot 6h44m; "few alternatives" for users | https://www.techtarget.com/it-infrastructure/news/366649459/GitHub-outage-had-users-weighing-options-but-finding-few | Secondary (press) | TechTarget (Beth Pariseau) | 2026-08-19 | 2026-10-10 | Medium | — |
| GHFR-03 | Aug 2026: five incidents; July: eight; "availability first" rule vs performance gap acknowledged by execs | https://www.webpronews.com/github-actions-stumbles-again-inside-the-latest-service-disruptions-and-mounting-reliability-questions/ | Secondary (press, citing GitHub blog) | WebProNews | 2026-10 | 2026-10-10 | Medium | Corroborates GHFR-01 |
| GHFR-04 | Copilot Coding Agent in Comment-and-Control (GITHUB_TOKEN exfil); coordinated disclosure | https://github.com/vectara/awesome-agent-failures/blob/HEAD/docs/case-studies/comment-and-control-prompt-injection.md | Secondary (incident archive) | vectara/community | 2026 | 2026-10-10 | Medium | See 07-anthropic.md AN-P1 |

## GAPS (this workstream, GitHub)
- GitHub's internal SRE/org mechanics (how the company that hosts everyone's CI runs its own reliability org) — thin public evidence.
- Whether the shared-dependency coupling identified by the MDPI paper is being architecturally addressed (only pledged).
- Actions/Codespaces internals (sibling scope note).
