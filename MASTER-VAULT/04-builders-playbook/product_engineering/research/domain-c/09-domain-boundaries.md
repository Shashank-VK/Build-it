# Domain C — Boundary Analysis: Where Organisational AI Ends and Domains A & B Begin

**Workstream:** domain-c · Researched 2026-10-10

> Why this file exists: a support bot, a coding agent, and a product's AI assistant look similar under the hood (all LLM-based) but have different **responsibilities, failure modes, and safety requirements**. Misclassifying a system means applying the wrong safety playbook. This file states the differences explicitly, with worked examples from the research.

---

## 1. The three domains, defined by *whose work is being automated*

| | Domain A: AI building the product | Domain B: AI inside the product | Domain C: AI automating organisational work |
|---|---|---|---|
| **Whose work** | Engineers' work — writing code, migrations, tests | The product's own capabilities — features customers buy | The company's internal operations — support, HR, finance, coordination |
| **Primary user** | Engineers | End customers using the product | Employees (and customers interacting with company operations) |
| **Example** | AI coding agent writing a migration | Notion AI / in-product assistant | Klarna's support bot; AP invoice automation |
| **Failure hurts** | The codebase / production systems | The product experience / user trust in the product | The company's operations, legal liability, staff |

## 2. Worked boundary cases from this research

### Case 1: Cursor "Sam" (Domain C) vs Cursor the product (Domains A/B)
Cursor's *product* is an AI code editor (Domain B feature / built with Domain A tooling). The "Sam" bot that invented a single-device subscription policy was **Domain C** — the company's own support operation speaking to customers. The failure mode (invented company policy → subscription cancellations) is an *organisational* failure: it damaged Cursor's business operations and customer relationships, not the code the product writes. **Different playbook**: the fix is support-ops governance (constrained answering, human review of policy statements), not model improvement.

### Case 2: The 1.8M-records deletion (Domain A, not C)
An AI agent deleted ~1.8M customer records in 11 minutes during a migration, after six humans reviewed the change. Tempting to file under "agent automation gone wrong" (Domain C), but it is **Domain A**: the agent was doing *engineering work* — writing and executing a database migration. The failure mode is a *build* failure (wrong migration logic, unverified assumption), and the safety playbook is engineering's: migration review, staging verification, backup/restore drills. Domain C's playbook (approval gates on business actions) would not have caught it; Domain A's would have.

### Case 3: Klarna's support bot (Domain C) vs a fintech's in-app AI advisor (Domain B)
Klarna's bot handled *the company's support operations* — answering "where's my refund?" (Domain C). A hypothetical in-app AI that advises customers how to structure their BNPL repayments would be **Domain B** — a product feature customers rely on as part of what they bought. Why the distinction matters:
- **Domain C failure** → the company is liable for its own operations (Air Canada precedent: the bot's words are the company's words; the remedy is operational — fix the bot, retrain staff, honour the commitment).
- **Domain B failure** → product liability and consumer-protection exposure; the AI's advice is part of the *product's* duty of care, regulated as a product feature (e.g. financial-advice regulation), with different disclosure and testing obligations.

### Case 4: McDonald's/IBM drive-thru AI (boundary case, ended 2024)
AI taking drive-thru orders sits on the line: it's the company's *operations* (order-taking labour — Domain C flavour) but delivered as the *customer-facing product experience* (Domain B flavour). The widely-reported failure (order errors going viral) played out as a *product-experience* failure. **Lesson**: when the organisational workflow *is* the customer experience, apply both playbooks — operational efficiency metrics *and* product-quality bars.

### Case 5: Incident-triage AI (Domain C) vs AI code review (Domain A)
An AI that routes a SEV1 to the payments team is doing **organisational coordination** (Domain C) — its failure mode is paging the wrong humans. An AI that reviews the payments team's pull request is doing **engineering work** (Domain A) — its failure mode is approving a bug. Same company, same on-call engineers, completely different verification regimes: the triage AI needs routing-precision measurement and human acceptance gates; the code-review AI needs test coverage and static analysis.

### Case 6: Employee knowledge assistant (Domain C) vs customer-facing help bot (Domain C, different risk tier)
Both are Domain C, but the Air Canada ruling shows the *audience* changes the risk: an internal RAG assistant that hallucinates a policy wastes an employee's afternoon; the same hallucination served to a customer is negligent misrepresentation. **Within Domain C, external-facing deployments carry legal liability that internal ones don't.** Oversight intensity should scale with audience, not just capability.

## 3. Why the safety requirements differ

| Dimension | Domain A (build) | Domain B (in-product) | Domain C (org work) |
|---|---|---|---|
| **Worst single failure** | Production outage, data loss | User harm via product, regulatory action | Legal liability, operational chaos, staff impact |
| **Who must approve** | Code review, CI, deploy gates | Product/UX review, safety evals, compliance | Ops managers, legal, HR/finance controls |
| **Key metric** | Defect escape rate, deploy safety | Task success, user trust, harm rate | Resolution accuracy, exception rate, audit completeness |
| **Rollback means** | Revert the deploy | Ship a fix / disable the feature | Reverse business actions, honour commitments made |
| **Knowledge failure looks like** | Wrong API usage | Wrong in-product guidance | Invented company policy (Air Canada) |
| **Permission failure looks like** | Destructive migration | Over-broad product data access | Confused deputy across HR/finance systems |

## 4. The practical rule

Ask: **whose job is the AI doing, and who is harmed when it's wrong?**
- Doing an *engineer's* job, harming the *systems* → Domain A playbook (code review, staging, backups).
- Doing the *product's* job, harming *users of the product* → Domain B playbook (product safety evals, UX disclosure, consumer regulation).
- Doing the *company's operational* job, harming the *business itself, its staff, or its customers-as-counterparties* → Domain C playbook (approval gates, audit trails, rollback plans, liability awareness).

Hybrid systems (agentic workflows that both coordinate work *and* touch production systems) need both playbooks applied at their respective layers — read-only coordination under Domain C rules, mutation under Domain A rules (the eng-agent-os "read-only, always" mechanical enforcement is the cleanest expression of this found in the research).
