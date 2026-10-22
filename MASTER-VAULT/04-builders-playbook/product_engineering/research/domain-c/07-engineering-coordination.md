# Domain C — AI Automating Organisational Work: Engineering Coordination

**Workstream:** domain-c · **Area 7 of 8** · Researched 2026-10-10

> Scope: AI coordinating the *work of running engineering as an organisation* — incident triage, on-call coordination, standup summaries, cross-team routing, status communication. This is Domain C, not Domain A: the AI is not writing code or building the product; it is doing the organisational overhead *around* engineering (who owns this incident, what happened, who needs to know). The distinction matters because the failure modes are coordination failures (wrong owner paged, misleading summary) rather than code defects.

**Plain-English terms:**
- **Triage** — deciding what an incident is, how bad it is, and who should handle it. Concrete example: 200 alerts fire at 2 AM; triage decides it's one database problem owned by the payments team, severity SEV2, page these three people.
- **MTTR** (mean time to resolution) — average time from incident start to fix. The headline metric for incident tooling.
- **Alerting vs triage** (incident.io's distinction) — alerting detects and notifies (the smoke detector); triage interprets and prepares (the fire crew that arrives knowing the building layout).
- **Incident commander / copilot** — an AI that gathers context during an outage so humans troubleshoot instead of assembling information.

---

## 1. How organisations deploy it

The incident-coordination stack, as documented by incident.io, Rootly, and practitioner guides:

1. **Detection** (unchanged): existing monitors (PagerDuty etc.) fire alerts — AI triage *consumes* alerts, it doesn't replace detection.
2. **AI triage**: classifies severity dynamically (weighing service criticality + history), deduplicates/clusters related alerts by probable shared root cause, routes to the likely-owning team with evidence attached.
3. **Coordination**: auto-creates incident channels, captures a timeline, assembles telemetry + deploy history + past incidents.
4. **Copilot during response**: answers "what's the current status?" for newcomers, drafts exec summaries (e.g. every 20 min on SEV2+), suggests missing action items from playbooks, drafts the resolution message.
5. **Post-incident**: summarises resolved incidents into knowledge-base articles; registers follow-up tasks in Jira so they aren't forgotten.

Standup/summary automation follows a template pattern (example: the AIWG "hypercare monitoring" skill): the agent reads daily SLO reports, incident lists, and user-feedback summaries, then generates a structured standup agenda — production health, incident summary, feedback review, blockers. The human facilitator runs the meeting from it.

A deeper technical approach (open-source eng-agent-os): the triage agent uses a **codebase map + impact map** to trace symptoms to the actual file, function, and commit — and writes findings into version-controlled incident state, so *an incident today makes the next incident faster*. Notably, this design enforces a **"read-only, always"** rule mechanically: credentials *cannot* mutate anything even if the prompt were bypassed.

## 2. Documented cases and evidence

**incident.io — AI triage vs alerting [vendor documentation — Corroborated as architecture, metrics Unverified]:**
Published comparison table: traditional alerting does threshold-based detection, static severity rules, rule-based routing, no context gathering. AI triage adds dynamic severity classification, root-cause clustering, ownership-aware routing with evidence attached, automatic telemetry/deploy/past-incident assembly. Key line: "PagerDuty is your smoke detector, and incident.io's Investigations is the fire response team that arrives already knowing the building layout."

**Rootly — AI Copilot in incident workflows [vendor documentation — Corroborated]:**
LLM summarisation keeps incident descriptions current without responder effort; exec updates automated on cadence; AI suggests missing action items from org playbooks; post-incident follow-ups auto-registered in Jira.

**MTTR claims [secondary/vendor — Unverified]:**
Enterprises adopting AI incident assistants report **30–40% MTTR improvements, particularly for recurring incidents** (dev.to practitioner/vendor piece). No independent audit found.

**Incident Triage Agent architecture guide (dev.to, Oct 2026 — practitioner/secondary):**
Codifies the coordination discipline: standardise per-team evidence (team identity, queried components, time range, evidence, gaps, possible ownership, recommendation); the coordinator answers four questions — which team has the strongest evidence of ownership, which observations are independently supported, what conflicts/missing data prevent confident assignment, **what an authorised human should verify before accepting the route**; never force a false single-owner result; record every revision (a timeline of proposals beats a final label).

**AI Incident Commander (hackathon project, Medium, Jul 2026 — builder first-hand):**
Example output: affected service, severity, most-likely root cause *with stated confidence* (e.g. 95%), evidence bullets (DB CPU 97%, SQL timeouts, deploy 7 min before failures, similar past incident), recommended action (roll back deploy, restart pool). The value proposition: "instead of spending twenty minutes finding the problem, engineers can spend those twenty minutes fixing it."

## 3. Measured outcomes

| Metric | Value | Label |
|---|---|---|
| MTTR improvement, AI incident assistants | 30–40% (recurring incidents) | Unverified (vendor/secondary) |

The public record here is notably thin on hard numbers — most evidence is architectural documentation and practitioner guides, not measured field studies. **Finding: incident-coordination AI is widely described, rarely measured.**

## 4. Failure modes

1. **Misrouting with confidence**: the triage agent pages the wrong team with a confident-sounding evidence summary — worse than no triage, because the real owner loses minutes and the wrong team loses trust in the system.
2. **Severity misclassification**: dynamic severity models can both over-page (alert fatigue returns through a new door) and under-page (a SEV1 treated as SEV3).
3. **False root-cause attribution**: correlating "deploy 7 minutes before failures" into "the deploy caused it" — post hoc reasoning presented at 95% confidence. Correlation assembled as evidence is not causation established.
4. **Summary drift**: auto-generated exec summaries that smooth over uncertainty; newcomers briefed by the copilot inherit its blind spots.
5. **Unauthorised remediation**: any step from "suggest rollback" to "execute rollback" without a human gate converts a coordination tool into an action tool with blast radius (see area 8 patterns).
6. **Timeline-revision loss**: if only the final assignment is kept, nobody can later explain why ownership changed or why time-to-engage increased.

## 5. Human oversight / approval design (the emerging standard)

- **Read-only by default**: triage and summarisation operate on read-only credentials; remediation actions require separate authorised paths (the eng-agent-os mechanical enforcement is the strongest form).
- **Human acceptance of routing**: the coordinator *proposes*; an authorised human verifies before the page goes out — especially for SEV1/SEV2.
- **Confidence is stated, not hidden**: root-cause hypotheses carry explicit confidence and evidence lists, so humans can discount them.
- **Revision history**: every proposal, evidence update, and human decision logged — the timeline is the audit trail.
- **Multi-owner support**: primary + secondary collaborators rather than forced single-owner when evidence is split.

## 6. Cost vs benefit

- The benefit case is *time-shift*: moving 20 minutes of context-gathering per incident into seconds, across every incident, without adding headcount. Plausible but unmeasured in public sources.
- The cost case: triage-model maintenance, integration upkeep across 70+ tools, and the risk cost of one confident misroute during a real SEV1.
- Net assessment: **Inferred** — coordination AI looks like a positive-ROI augmentation *if* kept read-only and human-gated; the evidence does not yet support autonomous remediation claims.

## 7. Data governance / privacy

- Incident timelines aggregate logs, deploy metadata, and sometimes customer-impact data — access control on the incident record matters (not everyone should see every incident's customer list).
- Copilot Q&A over incident history can surface past customer data in new contexts — retention and redaction policies needed.
- Webhook/posting integrations (Slack, Teams, Jira) spread incident data across systems; each is a data-residency decision.

## 8. Open gaps

- No independent field measurements of triage accuracy (routing precision/recall) or MTTR impact.
- Standup-summary automation is described in templates and skills, not in measured deployments.
- Unclear how dynamic severity models behave under novel failure modes (out-of-distribution incidents).
