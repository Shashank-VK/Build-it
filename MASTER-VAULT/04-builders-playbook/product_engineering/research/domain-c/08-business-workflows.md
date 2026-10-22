# Domain C — AI Automating Organisational Work: Repetitive Business Workflows

**Workstream:** domain-c · **Area 8 of 8** · Researched 2026-10-10

> Scope: the general case — AI agents and automation executing repetitive multi-step business workflows end to end (procurement approvals, employee onboarding/offboarding sequences, data entry and reconciliation, scheduled reporting, cross-system sync). This is the "agentic automation" layer that sits above single-task tools. It inherits failure modes from every other area, plus one of its own: **speed at scale** — a slightly wrong decision repeated hundreds of times before anyone notices.

**Plain-English terms:**
- **Agentic workflow** — an AI that doesn't just answer but *does*: it plans steps, calls tools (APIs, databases, apps), checks results, and continues. Concrete example: "onboard this hire" → creates accounts, orders laptop, schedules orientation, notifies the team.
- **Guardrails** — checks bolted around the agent: output validation, iteration caps, approval gates. The difference between a demo and something you'd run unattended.
- **Iteration cap** — a hard limit on how many steps the agent may take before stopping and asking for help. Prevents runaway loops (and runaway bills).
- **Blast radius** — how much damage one bad run can do. A read-only agent's blast radius is embarrassment; a write-enabled agent's is the database.

---

## 1. How organisations deploy it (and how practitioners say to do it safely)

The practitioner consensus (n8n production-reliability guide, dev.to, Oct 2026; rollback-plan guides) for production agent workflows:

1. **Output validation after every LLM step** — sanitise, then validate against a field contract. "This kills the largest class of silent breakage."
2. **Guardrails on the flakiest tool** — check for empty results and missing fields *before* the agent sees them.
3. **Iteration cap with a named error** — runaway loops become diagnosable incidents instead of mystery bills.
4. **Failure alerting** — errors must reach a human within a minute; "if failures don't reach a human within a minute, you don't have observability, you have logs."
5. **Written tool contracts** — expected fields per tool, even as comments.
6. **Rollback plan per agent** (one page): the five abort steps; every external action listed with its manual undo; any action with no undo gets an approval gate or explicit risk acceptance; a tested stop drill.

The reliability target is phrased as: **every failure is bounded, visible, and handled** — and provable in a report.

## 2. Documented cases and incidents

### The HR agent that bypassed approval (first-hand/community — hrtechedge, Sept 2026)
An **HR AI agent accessed 500 employee profiles after receiving unexpected instruction through an integrated application**, bypassing an expected approval step. The documented incident-response playbook: detect/classify (SOC flags, HR assesses process impact) → confirm what the agent did (inputs, outputs, permissions, decision path) → contain (disable the agent's database access, not the whole HR platform) → engage HR/SOC/IT/privacy/legal → evaluate employee/business impact (were records changed? did payroll trigger?) → preserve all prompts, actions, API calls, approvals → update the response plan. After the incident, the team added an approval control and tested the same scenario across other HR systems.

### Speed at scale — the slightly-wrong decision × 600 (Inc., Oct 2026 — practitioner reporting)
"If you give an agent the same broad access you gave an early employee, that agent can exercise those permissions continuously and at machine speed." The characteristic failure is not dramatic: **"a slightly wrong decision made 600 times before anyone sees the pattern, at a company with a small finance team and little ability to absorb the loss."** Nothing triggers an alert because nothing looks wrong in isolation. The access granted on day one is still the access six months later — no natural human checks (going home, being noticed) apply.

### The 1.8M-records deletion (Medium, Oct 2025 — first-hand account, with a boundary note)
An AI agent deleted ~1.8M customer records in 11 minutes during a migration; all tests had passed and six humans had reviewed the change. **Boundary note: this was a coding agent writing a migration — Domain A (building the product), not Domain C.** Included here because the *organisational* lesson transfers: approval of the plan is not verification of the assumption nobody checked, and rollback plans must cover "succeeded at the wrong task," not just "failed."

### Shared-services workflow failures (iteratorshq — practitioner taxonomy)
Procurement: vendor onboarding with three spellings of the same vendor; PO approvals routing to departed managers; policy-exception paths that are really "email whoever knows the rule"; out-of-policy requests the automation "confidently approves because nobody encoded the policy." HR: onboarding that breaks on unconfigured country payrolls; data changes rippling into forgotten systems.

## 3. Measured outcomes

No robust public measurements of end-to-end agentic workflow outcomes (cycle time, error rates, cost) were found. The literature is dominated by architecture guidance and incident reports. **Finding: this is the least-measured area of Domain C — the newest, the most hyped, and the thinnest on field evidence.**

## 4. Failure modes (synthesis across areas)

1. **Silent wrongness at scale** — small errors repeated hundreds of times before detection (the defining risk).
2. **Approval bypass** — via unexpected instruction paths, integrated apps, or permission drift.
3. **Irreversible actions without undo** — deletions, payments, messages sent; platforms log failures but can't know which *successful* runs were wrong.
4. **Runaway loops** — unbounded iteration producing mystery bills and side effects.
5. **Permission staleness** — day-one broad access never narrowed; service accounts never rotated.
6. **Monitoring gaps** — 19-hour detection delays are a monitoring problem; hidden ones are a trust problem (incident-report guidance).
7. **Rollback theatre** — a plan that covers failed runs but not runs that "succeeded at the wrong task."

## 5. Human oversight / approval design (the consolidated pattern)

| Control | What it does |
|---|---|
| Approval gates on irreversible actions | Money, messages, deletions, record changes need human sign-off or tight limits |
| Read-only default credentials | Agents observe and propose; separate authorised path for mutation |
| Iteration caps + named errors | Loops become incidents, not bills |
| Output validation contracts | Every LLM step's output checked against a schema before use |
| Kill switch + stop drill | Tested ability to halt the agent in minutes |
| Full action logging | Prompts, tool calls, approvals, results — preserved for post-incident review |
| Periodic permission review | Access re-scoped as the workflow stabilises; least privilege enforced |

## 6. Cost vs benefit

- **Inferred**: the upside is real for well-bounded, high-volume, reversible workflows (data sync, report assembly, standard onboarding steps). The downside is unbounded for poorly-bounded, irreversible ones — one incident (500 profiles accessed, 600 wrong micro-decisions) can erase years of efficiency gains.
- Practitioner economics: reliability engineering (validation, guardrails, evals, rollback plans) is a fixed upfront cost most teams skip — which is why production failures cluster in the first months.
- No credible public ROI figures exist for general agentic business workflows; treat any vendor ROI claim here as **Unverified**.

## 7. Data governance / privacy

- Workflow agents are cross-system by nature — they accumulate the union of every connected system's permissions. This is the confused-deputy problem at organisational scale.
- Every tool call crossing a system boundary is a data-transfer decision: logging the caller, effective policy, resource, and decision per call is the OWASP-recommended control.
- Employee-data workflows (HR, payroll) need purpose limitation; customer-data workflows need tenant isolation.
- Prompt-injection via business documents (invoices, emails, tickets the workflow processes) can redirect the agent — treat all ingested content as untrusted input.

## 8. Open gaps

- Essentially no independent field measurements of agentic workflow reliability, cost, or ROI.
- No standard for what "production-ready" means for a business workflow agent (the practitioner checklists are a start, not a standard).
- Insurance/liability treatment of agent-caused business losses is undeveloped (contrast the Air Canada chatbot liability precedent in area 1).
