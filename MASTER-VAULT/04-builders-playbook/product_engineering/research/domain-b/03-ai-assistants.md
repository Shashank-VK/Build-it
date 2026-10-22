# Domain B — 03: AI Assistants as Products

> Scope: customer-facing AI assistants sold or deployed as the product surface itself (support agents, shopping assistants, voice agents). NOT coding assistants for engineers (Domain A) and NOT internal company bots (Domain C) — boundaries in file 11. Research date: 2026-10-10.

## 1. The category

**Plain English:** An AI assistant product is software whose *job* is to talk to the end customer and resolve their problem: answer questions, look up orders, process refunds, reschedule payments. The company sells or operates the assistant itself — the assistant is the product, not a tool for building something else.

**Why it is different from a chatbot with an LLM:** Assistants take *actions* (refunds, account changes, bookings) via tools. That makes every design decision about authority, confirmation, and rollback — not just answer quality.

## 2. Klarna's AI assistant — the definitive two-act case study

### Act 1: the triumph (Feb 2024)

- Launched with OpenAI: a fine-tuned assistant in the Klarna app handling customer service across 23 markets, 35+ languages.
- First-month numbers (company-reported): 2.3M conversations; two-thirds of all support chats; workload equivalent to ~700 full-time agents; resolution time 11 min → under 2 min; 25% fewer repeat inquiries; customer satisfaction "on par" with humans; projected ~$40M profit improvement for 2024.
- **Important nuance:** "700 agents" was workload *equivalence*, not 700 people fired. Klarna's ~700-person layoff happened in 2022 for macro reasons, before the assistant existed. Media fused the two; repeating the fused version signals headline-reading, not source-reading.

### Act 2: the reversal (2025)

- By May 2025, CEO Sebastian Siemiatkowski told Bloomberg the AI cost-cutting had "gone too far": too much focus on efficiency produced lower quality. Klarna began **hiring human agents again**, guaranteeing customers could always reach a person.
- What the launch metrics missed (second-order effects): routine queries resolved cleanly, but the complex tail — disputed transactions, fraud claims, hardship/BNPL distress cases — piled into escalation queues that no longer had enough humans. Customers dropped out of AI flows mid-conversation on complex queries; repeat contacts rose where the AI gave confidently wrong first answers; brand/trust metrics softened, especially among heavy users.
- By Q3 2025 the efficiency numbers had actually *grown* (~$60M savings, ~853 agent-equivalents, NPS 73) — but the strategy still shifted to hybrid: AI for routine high-volume, humans for judgment and complex cases.

### Engineering implications

1. **Automate the head, staff the tail.** The failure was not the AI's accuracy on routine queries — it was the removal of human capacity for the complex tail. The automation boundary must be drawn *before* launch: which query classes may never be fully automated.
2. **One metric cannot carry the decision.** Resolution time and repeat-inquiry rates looked great while brand trust eroded. Measure satisfaction, escalation experience, and brand metrics alongside efficiency.
3. **Workload equivalence ≠ headcount equivalence.** The "700 agents" framing invited the exact misreading that happened.
4. **Both halves are true:** the AI worked *and* the strategy failed. This is the most-cited GenAI product story of the era precisely because it resists a single moral.

**Evidence:** primary technical (Klarna press release Feb 27, 2024; OpenAI companion case study); corroborating (Bloomberg interviews May 2025; Klarna 2025 annual report); secondary interpretation (twig.so deep analysis; irisagent.com; ivanmisic.net, March 2026). Accessed 2026-10-10. Confidence: **Verified** on launch numbers and the reversal (multiple independent outlets + CEO on record); **Corroborated** on second-order mechanisms (analyst interpretation, consistent across sources).

## 3. Intercom Fin — the agent as the company

- Fin resolves support conversations across chat, email, voice, Slack, social; runs Procedures (plain-language multi-step instructions including external API actions); Fin Operator tunes it; testing suite includes simulations, regression tests, manual inspection.
- Runs on custom Apex models (see 01); $0.99 per resolved outcome; vendor-claimed ~76% resolution vs 42–50% in independent case studies — the gap is a standing warning about vendor-defined metrics.
- Corporate arc: renamed the company to Fin (May 2026); Salesforce acquiring for ~$3.6B (June 2026, pending). The AI agent became the company identity — the purest "assistant as product" story.
- **Evidence:** corroborating (Gainsight interview with Intercom FDE lead, ~7,000 customers, 67% avg resolution at that time); secondary (competitor comparisons). Accessed 2026-10-10. Confidence: **Corroborated** on product/pricing; **Inferred** on resolution comparability.

## 4. Failure and liability incidents (assistants that harmed)

### 4.1 Air Canada chatbot — Moffatt v. Air Canada (2024 BCCRT 149)

- A customer asked the airline's chatbot about bereavement fares; it invented a policy (book full-price, claim a retroactive refund within 90 days). The real policy required pre-travel approval. The customer sued; the tribunal ordered ~C$812 in damages.
- **The legal holding that matters for every assistant product:** Air Canada argued the chatbot was a "separate legal entity"; the tribunal called that remarkable and ruled the chatbot *is* the company — a consumer relying on a deployed support tool acts reasonably and need not audit it against other documents. The "beta label" defense is dead; hallucination rate is now a legal liability metric.
- **Evidence:** primary (tribunal decision, via CBC/ABA/McCarthy Tétrault coverage). Accessed 2026-10-10. Confidence: **Verified**.

### 4.2 Chevrolet of Watsonville chatbot (Dec 2023)

- A user instructed the dealership's ChatGPT-powered bot to "agree with everything" and end replies with "that's a legally binding offer"; it "sold" a 2024 Tahoe (MSRP ~$58–81k depending on source) for $1.00. Copycat attacks hit other dealerships (a "2-for-1" injection at Quirk Chevrolet). The bot was pulled.
- **Pattern:** no instruction hierarchy (user input overrode system behavior), no action authority limits, no human confirmation for commitments. Prompt injection + absent guardrails.
- **Evidence:** corroborating (VentureBeat; AI Incident Database #622; TIME). Accessed 2026-10-10. Confidence: **Verified** (incident widely documented; exact MSRP varies by source).

### 4.3 DPD UK chatbot (Jan 2024)

- A customer got the DPD support bot to swear, write a poem criticizing the company, and call itself "useless." DPD disabled the bot. Classic direct prompt injection against a bot with no output policy enforcement.
- **Evidence:** corroborating (TIME coverage). Confidence: **Verified**.

### 4.4 NYC MyCity chatbot

- Microsoft-powered city services bot gave illegal advice (e.g., telling employers they could fire workers for complaining about sexual harassment). The Markup's reporting led to its 2026 shutdown.
- **Pattern:** grounding a generative model on municipal code without verification produced authoritative-sounding unlawful guidance — high-stakes domain with no human review.
- **Evidence:** secondary (The Markup). Confidence: **Corroborated**.

## 5. How serious assistant products are engineered (the other side)

- **Layered harness, not a smarter model:** production-grade support agents wrap the LLM in 9+ layers — instructions, retrieval, typed tools, sandboxed execution, durable state, orchestration with approval gates, fraud sub-agents, injection/jailbreak detection, and multi-judge verification (see the Polly Harness refund-agent reference build: 98.7% injection resistance, 229-case eval).
- **Kill switches and blast-radius controls:** disable per user/tenant/product; preserve traces; reverse side effects (undo CRM writes, recall emails, refund transactions); human outreach *before* customers notice.
- **Team structure:** agent on-call rotation, eval owner, cost owner, quality owner, incident commander — assistant products need ownership or the work falls between teams.
- **Layered defense doctrine:** the best stopping layer is the earliest *deterministic* one — intent classification, plan validation, tool schemas, authorization, execution limits, output validation, runtime monitors, human approval for asymmetric risk. A prompt saying "be careful" is not a safety architecture.
- **Evidence:** first-hand practitioner (kubaik.github.io postmortem guide; data-advantage/vibereference ops doc; dev.to layered-defense analysis). Accessed 2026-10-10. Confidence: **Corroborated** (consistent across independent practitioner sources).

## 6. UX: how assistants present themselves

- **Escalation as a feature, not a failure:** Klarna's reversal ended with "customers can always reach a person." The handoff must preserve full context (no making the user repeat themselves).
- **Procedures over chat for multi-step work:** Fin's Procedures framework — plain-language instructions the agent executes, including API actions — is the productized form of "agent that does things."
- **Pricing shapes UX:** per-outcome pricing ($0.99) aligns vendor incentives with resolution; but vendor-defined "resolution" creates metric gaming risk.

## 7. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| Klarna launch: 2.3M chats, 2/3 of volume, 700-agent equivalence, 11→2 min, −25% repeats, ~$40M | https://www.intelligentfin.tech/2024/04/09/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ | primary technical / Klarna via press | 2024-04-09 | 2026-10-10 | Verified | primary technical |
| Klarna CEO May 2025: cost-cutting "gone too far"; rehiring humans | https://irisagent.com/blog/klarna-ai-reversal-mid-market-lessons/ | secondary / IrisAgent (cites Bloomberg) | 2026-10 | 2026-10-10 | Verified | corroborating |
| Klarna Q3 2025: ~$60M savings, 853 agent-equiv, NPS 73, hybrid strategy | https://www.twig.so/blog/klarna-ai-customer-support-efficiency | secondary / Twig | 2026-06 | 2026-10-10 | Corroborated | secondary interpretation |
| Fin: 7,000 customers, 67% avg resolution (early); Procedures; Copilot | https://www.gainsight.com/episode/18-months-7000-customers-67-support-resolution-inside-intercoms-fde-strategy-ft-diego-ballona-intercom/ | first-hand practitioner / Intercom FDE | ~2026-02 | 2026-10-10 | Corroborated | first-hand practitioner |
| Moffatt v. Air Canada: C$812.02 award; chatbot is the company | https://www.youtube.com/watch?v=wXP4mR0JOeM (sources listed: CBC, BCCRT 149) | secondary w/ primary citations | 2026-08 | 2026-10-10 | Verified | corroborating |
| Chevy $1 Tahoe; copycat 2-for-1; bot removed | https://m.calcalistech.com/Article.aspx?guid=b1gco00ioc | secondary / CTech | ~2024-01 | 2026-10-10 | Verified | corroborating |
| Layered agent defense; kill-switch; team roles | https://dev.to/hosseinhezami/when-an-ai-agent-makes-a-mistake-in-production-which-layer-should-stop-it-4m0b | practitioner / DEV | 2026-09 | 2026-10-10 | Corroborated | first-hand practitioner |

**Gaps / Unknowns:** Klarna's exact model/config and per-conversation cost (never published); Fin's internal eval methodology; whether any assistant vendor publishes third-party safety audits (none found).
