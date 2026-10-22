# Domain B — 07: Tool-Using and Autonomous Systems as Products

> Scope: products where an AI system calls tools/APIs and takes actions — support agents issuing refunds, workflow agents (Zapier Agents), shopping assistants, "AI teammates." The agent *is* the product surface. Research date: 2026-10-10.

## 1. What "tool-using agent product" means (plain English → mechanics)

**Plain English:** A tool-using agent is an LLM wired to *do things*: look up an order, check a balance, issue a refund, file a ticket, post a message. The product defines which tools exist, what arguments they take, and — critically — which actions need human approval.

**Concrete example:** A refund agent. The customer says "my order never arrived." The agent calls `get_order_status(order_id)`, sees it's lost, checks the refund policy via retrieval, then calls `issue_refund(order_id, amount)`. Every step can fail: wrong order ID format, policy misread, refunding the annual subscription instead of the $12 add-on.

**Deeper mechanics:** The agent loop is: model reasons → emits a structured tool call (function name + JSON arguments) → harness validates → executes against the real API → returns the result as a message → model continues. Reliability multiplies *down*: an agent with 85% per-step accuracy completes a 10-step task only ~20% of the time (0.85^10). This compounding is why tool-use benchmarks look so much worse than single-call benchmarks.

## 2. How bad tool-use reliability actually is (benchmarks)

- **Sierra tau-bench** (customer-support tool-use benchmark): GPT-4o ~61% single-trial success on tool-use tasks; requiring consistency across 8 trials (a real user session) drops it to ~25%.
- **Salesforce MCP-Universe:** best model (GPT-5) succeeded on only 43.7% of real-world multi-tool tasks; most models below 30%.
- **Structured outputs (OpenAI, 2024):** constrained decoding took JSON-schema conformance from <40% to 100% *syntactic* conformance — but semantic errors (valid JSON, wrong values) still need a validation layer.
- **Task interference:** requiring JSON output reduced accuracy by ~27 percentage points on GSM8K in one study — format constraints compete with reasoning for the model's attention.
- **Engineering implication:** the harness around the model (schemas, validation, retries, confirmations) is doing most of the reliability work. "The model got smarter" is not a reliability strategy.
- **Evidence:** primary technical (Sierra benchmark blog; Salesforce MCP-Universe paper arXiv:2508.14704; OpenAI structured-outputs announcement) via practitioner synthesis. Accessed 2026-10-10. Confidence: **Corroborated** (numbers cited consistently across independent sources).

## 3. The five predictable tool-call failure modes

1. **Tool execution failure** — the API is down, rate-limited, or slow. Fix: return a descriptive error *to the model* as a structured message (not a raw stack trace); the model often recovers by rephrasing, retrying, or explaining to the user. Never crash the loop on a tool exception.
2. **Malformed arguments** — `"count": "5"` instead of `5`; missing required fields. Fix: validate with Pydantic/Instructor *before* execution; simple flat schemas beat clever nested ones.
3. **Hallucinated function names** — `get_customer_by_id` when the tool is `fetch_customer`. Fix: check names against an allow-list; rarer with modern models, still happens with open models.
4. **Timeouts** — one slow API hangs the whole turn. Fix: explicit timeouts at the API-client layer, with retries/backoff and circuit breaking *outside* the model.
5. **Unexpected results** — the tool returns 50MB of JSON, or empty. Fix: size limits, response translation into minimal model-shaped schemas, sanitization.

**The boundary-layer principle:** auth, timeouts, retries, and response shaping live in the API-client layer — never exposed to or handled by the model. Secrets are injected by the client layer; the model never sees keys.

## 4. Real product cases

### 4.1 Zapier Agents (2025–2026)

- **What changed:** Zapier (8,000+ app integrations) moved from linear trigger-action Zaps to autonomous agents that observe inputs, decide which tools to use, and take multi-step actions without a predefined sequence; plus Copilot (natural-language workflow builder), MCP support, and enterprise governance (Admin Hub, SSO, audit logs).
- **Adoption signal:** 1.2M workflows created in H1 2026 included at least one AI agent step (+340% YoY); natural-language creation = 28% of new Zaps by first-time users; enterprise = 34% of revenue.
- **The honest limitation (even in vendor-adjacent coverage):** AI features feel layered onto the original product rather than native; task-based pricing gets unpredictable at scale; agents are independent executors, not multi-agent orchestration; per-workflow secrets configuration is a governance problem at enterprise scale.
- **Safety design:** Human-in-the-Loop workflow control (2025) — approval gates for consequential actions.
- **Evidence:** secondary (digitalapplied, gmtasoftware, techintelpro, Zapier's own compare page). Accessed 2026-10-10. Confidence: **Corroborated** on features/pricing; **Inferred** on the adoption stats (vendor-reported via third parties).

### 4.2 The $63 runaway loop (first-hand incident, Oct 2026)

- An agent loop polling GitHub review state burned 31M tokens (~$63) overnight: the freshness check lived on an unreachable code path, the attempt counter reset to 0 every pass (disarming the safety latch), and branch order made recovery impossible after one approval.
- **Lesson:** when an expensive actuator (LLM tokens) sits on a loop, every pass must earn itself — hard spend/token ceilings on the actuator, alerts on repeated identical states. "Harmless redundancy" stops being a category once each pass is metered.
- **Evidence:** first-hand practitioner (devtalk forum postmortem, 2026-10-09). Accessed 2026-10-10. Confidence: **Verified** (first-hand with numbers).

### 4.3 Polly Harness — reference architecture for a refund agent

- A 9-layer harness around a support refund agent: instructions → RAG context → typed tools (8 MCP tools) → sandboxed execution → durable state → LangGraph orchestration with interrupt-before-execute approval gates → fraud sub-agent → injection/jailbreak/abuse gates → 8 judges + 229-case eval + Langfuse traces. Plus a 10th loop: every verification failure becomes a structured incident feeding new prompts/skills/rules.
- Measured (self-reported): 98.7% injection resistance, 100% jailbreak resistance on stable runs, 97% tone/escalation — with honest documentation of axes that *didn't* pass (policy correctness 60%, tool-decision safety 42% on stress cases).
- **Engineering implication:** "production-grade" is a measured threshold per axis, not an adjective. The honest failure documentation is the signal of seriousness.
- **Evidence:** primary technical (GitHub repo + production-grade postmortem). Accessed 2026-10-10. Confidence: **Corroborated** (self-reported; methodology is public).

## 5. Guardrail architecture (the doctrine)

- **Control lives outside the LLM.** Never let the model decide whether an action is safe. The interception layer checks the action against hard rules *before* execution: intent classification → plan validation → tool-schema validation → authorization → execution limits → output validation → runtime monitors → human approval for asymmetric risk.
- **Concrete pattern:** hard transaction limits (auto-process refunds under $50; over $50 pauses for manager sign-off); isolated tool scope (read billing, but never edit payment methods, in the same loop); state rollbacks (log pre-execution state; auto-clean failed multi-step mutations).
- **Max iterations is the essential guardrail:** every agent loop must have a hard iteration cap — without it, a confused model loops forever.
- **Prompts fail as guardrails:** "be careful with refunds" is probabilistic; production needs deterministic rules, hard limits, and human fallback triggers.

## 6. MCP-era attack surface (2025–2026 incidents)

The Model Context Protocol turned tool *descriptions* and retrieved content into injection vectors:

- **CVE-2025-32711 (EchoLeak):** indirect prompt injection against Microsoft 365 Copilot via email/calendar content → zero-click data exfiltration; CVSS 9.3; fixed server-side June 2025.
- **Supabase/Cursor (mid-2025):** malicious repo README injected an MCP-enabled IDE; hidden instructions accessed the developer's Supabase credentials invisibly.
- **CVE-2025-59944 (Cursor):** injection in an MCP tool description → unauthorized code execution.
- **OpenClaw/ClawHavoc (Feb 2026):** supply-chain poisoning — 1,184 malicious agent skills, ~4,000 developer machines compromised.
- **Pattern:** any content the agent retrieves — web pages, docs, emails, repo files, *tool descriptions the user never reads* — is an ingestion surface. The attacker needs no access to the conversation.
- Detail in 10; evidence table there.

## 7. Evaluations for agents

- **Task benchmarks:** tau-bench, MCP-Universe (multi-tool, multi-trial — the honest shape of agent eval).
- **Harness evals:** per-axis thresholds (policy correctness, injection resistance, jailbreak resistance, tool safety, tone/escalation) on hundreds of cases; 8-judge panels; trace-level review.
- **Production mining:** failed/low-rated traces → golden dataset; regression-check every template/tool change before deploy.
- **The metric that matters:** cost per *successful* task, with anomaly detection — not per-call averages (a session fanning out into 40 calls is the failure mode averages hide).

## 8. UX: agents that act

- **Show the plan before executing; show alternatives considered.** Progress legibility is the trust mechanism.
- **Approval gates for high-stakes actions** — propose → preview → confirm → execute → track, with Cancel as prominent as Confirm.
- **Interrupt and override at any point.** The user must be able to stop the agent mid-run.
- **Blast-radius UX:** refunds under a threshold auto-process; over it, the agent says "I've prepared this refund — a manager needs to approve" and routes to a human queue.

## 9. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| tau-bench: GPT-4o 61% single-trial → ~25% across 8 trials; MCP-Universe best 43.7% | https://github.com/kchia/production-llm-patterns/blob/HEAD/patterns/orchestration/tool-call-reliability/README.md | practitioner synthesis (cites Sierra, Salesforce) | 2026-04 | 2026-10-10 | Corroborated | corroborating |
| Five tool-call failure modes + boundary-layer principle | https://techsy.io/en/blog/llm-function-calling-guide | practitioner / techsy.io | 2026-03 | 2026-10-10 | Corroborated | first-hand practitioner |
| Zapier Agents: 8k integrations, 1.2M agent-step workflows H1 2026, HITL, MCP | https://www.digitalapplied.com/blog/ai-workflow-automation-agentkit-make-zapier | secondary / digitalapplied | 2025 | 2026-10-10 | Corroborated | secondary interpretation |
| $63 / 31M-token runaway loop; disarmed attempt counter | https://forum.devtalk.com/t/a-63-mistake-in-production-how-an-ai-agents-loop-escaped-without-guards/250506 | first-hand practitioner | 2026-10-09 | 2026-10-10 | Verified | first-hand practitioner |
| Polly Harness: 9 layers, 229-case eval, per-axis thresholds | https://github.com/jonnydubowsky/polly_harness | primary technical | 2026-08 | 2026-10-10 | Corroborated | primary technical |
| Layered defense: earliest deterministic layer stops the mistake | https://dev.to/hosseinhezami/when-an-ai-agent-makes-a-mistake-in-production-which-layer-should-stop-it-4m0b | practitioner / DEV | 2026-09 | 2026-10-10 | Corroborated | first-hand practitioner |

**Gaps / Unknowns:** production tool-success rates for any named commercial agent (none publish); Zapier's internal agent eval methodology; independent verification of Polly's self-reported scores.
