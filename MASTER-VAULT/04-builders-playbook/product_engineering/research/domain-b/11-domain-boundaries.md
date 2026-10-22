# Domain B — 11: Domain Boundaries — A vs B vs C

> Purpose: keep Domain B ("products built USING AI") distinct from Domain A ("AI used TO BUILD products") and Domain C ("AI automating internal organisational work"). Note explicitly where sources blur them. Research date: 2026-10-10.

## 1. The three domains, precisely

| | Domain A: AI used TO BUILD products | Domain B: Products built USING AI | Domain C: AI automating internal org work |
|---|---|---|---|
| **Question answered** | How do engineers build software faster/better with AI? | How do teams ship products whose features *are* AI? | How does AI change how the company itself operates? |
| **The AI is…** | a tool in the builder's hands | a component of the shipped product | an internal capability/worker |
| **Who experiences it** | engineers, designers, PMs | end customers / users of the product | employees, internal teams |
| **Example** | Coding assistant helping an engineer write a feature | Duolingo Max's Roleplay; Klarna's support assistant; Netflix recommendations | AI triaging internal IT tickets; AI drafting internal reports |
| **Failure lands on** | engineering velocity/quality | customers, revenue, legal liability | employees, internal process integrity |
| **Success metric** | throughput, code quality, cycle time | resolution rate, retention, trust, unit economics | cost/efficiency of internal operations |

## 2. The bright-line test

Ask: **if you removed the AI, would the thing still be a product?**

- **Domain B:** No — the AI *is* the product value. Remove the LLM from Duolingo Max's Roleplay and there's no feature. Remove the ranker from TikTok and there's no feed.
- **Domain A:** Yes — the product still exists; it was just built slower or differently. Remove the coding assistant and the engineer still ships (eventually).
- **Domain C:** The company still exists; an internal process reverts to manual.

## 3. Where sources blur the lines (explicitly noted)

### 3.1 Coding agents: the A/B blur (the big one)

The task brief itself assigns "AI assistants and coding agents (as PRODUCTS)" to Domain B while Domain A covers "coding assistants for engineers." The blur is real and must be named:

- **GitHub Copilot / Cursor / Claude Code** are *products built using AI* (Domain B: they're sold to users; they have evals, pricing, UX, liability) **AND** *AI used to build products* (Domain A: engineers use them to ship software). Both framings are true simultaneously.
- **The distinguishing question is the research question, not the artifact:** studying Copilot's *model selection, eval harness, per-seat economics, and UX* = Domain B. Studying *how teams integrate Copilot into their SDLC and what it does to velocity* = Domain A.
- **Perplexity's Photon post** is a live example of the blur: a Domain B product (AI search) built partly *by* "a swarm of persistent coding agents" (Domain A practice). The product and the process touched.
- **Rule for this Atlas:** classify by *what is being studied*, and cross-reference rather than duplicate.

### 3.2 Support assistants: the B/C blur

- **Klarna's assistant / Intercom Fin** = Domain B (customer-facing product, sold/operated as the support experience).
- **An internal IT helpdesk bot** answering employees' laptop questions = Domain C (internal org automation), even if built on the same tech.
- **The trap:** vendors market internal-agent platforms with customer-support case studies. "Fin resolves conversations" (B) vs. "our agent platform automates your internal workflows" (C) — same underlying technology, different responsibilities, failure modes, and safety requirements. A customer-facing assistant that hallucinates creates *legal liability* (Air Canada); an internal bot that hallucinates creates *process corruption*. Different stakes, different guardrails.
- **Copilot-style products** (Fin Copilot, "Copilot for human teammates") sit on the line: an AI assisting a support *agent* (employee) is arguably C-flavored tooling inside a B product. Note the placement; don't force it.

### 3.3 "AI-first" company memos: the B/C confusion in the wild

- Duolingo's April 2025 "AI-first" memo (prove AI can't do the job before headcount) is a **Domain C** story (internal workforce automation) that got debated as if it were about the **Domain B** product (Duolingo Max). The product succeeded; the org policy generated backlash. Conflating them produces wrong lessons ("Duolingo's AI failed" — it didn't; their *headcount policy* was contested).

### 3.4 Evals, cost, security: shared machinery, different stakes

- Eval harnesses, prompt injection, and cost optimization appear in all three domains — but the *stakes* differ: a prompt injection in a Domain A coding agent risks the *developer's* machine (CVE-2025-59944); in Domain B it risks *customer data and legal liability* (EchoLeak, Air Canada); in Domain C it risks *internal systems and employee data*. Same technique, different blast radius. This file's job is to keep the stakes attached to the domain.

## 4. Decision rules for ambiguous cases

1. **Who is the user?** End customer → B. Builder → A. Employee doing internal work → C.
2. **What breaks if the AI is wrong?** Customer harm / legal / revenue → B. Slower shipping → A. Internal process damage → C.
3. **What is being studied?** The artifact's engineering (models, evals, UX, economics) → B even if builders also use it. The *practice of building with it* → A.
4. **When both apply, say so.** "Copilot-as-product (B) used in the SDLC (A)" is a complete and honest classification. Forcing a single label loses information.

## 5. Worked classifications

| Case | Classification | Rationale |
|---|---|---|
| Duolingo Max Roleplay | B | AI is the feature; customers pay for it |
| Duolingo "AI-first" headcount memo | C | Internal workforce policy |
| Klarna support assistant | B | Customer-facing; legal/revenue stakes |
| Klarna rehiring humans for the complex tail | B (product ops) + C (workforce) | Note both: the product's escalation design and the org's staffing |
| Intercom Fin | B | The assistant is the product (literally the company name) |
| Fin Copilot (drafts replies for human agents) | B/C boundary | AI assisting employees inside a B product — note placement |
| Perplexity Photon | B | Retrieval infra of an AI search product |
| "Swarm of coding agents" that built Photon | A | AI used to build the product |
| Zapier Agents acting across a user's apps | B | Customer-facing automation product |
| A company using Zapier Agents for internal ops | C (usage) of a B (product) | The product is B; the deployment is C |
| Netflix GenRec | B | The ranker is the product engine |
| Samsung engineers pasting code into ChatGPT | C (+ security incident) | Internal use; data-leak stakes |
| GitHub Copilot's eval harness and pricing | B | Product engineering of the assistant |
| A team measuring Copilot's effect on velocity | A | AI-in-the-build-process |

## 6. Why the distinction matters (engineering implications)

- **Safety requirements differ:** B needs customer-facing guardrails, legal review of commitments, and public incident communication. A needs developer-machine sandboxing. C needs internal data governance and employee recourse.
- **Metrics differ:** B optimizes resolution/retention/trust; A optimizes throughput/quality; C optimizes internal efficiency without breaking process integrity.
- **The Klarna lesson is a boundary lesson:** excellent B metrics (resolution time, repeat rate) masked C damage (hollowed escalation capacity) and brand damage. Measuring one domain's metrics while ignoring the others is how "the AI worked and the strategy failed" happens.
