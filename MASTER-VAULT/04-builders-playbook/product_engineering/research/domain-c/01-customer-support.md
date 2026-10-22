# Domain C — AI Automating Organisational Work: Customer Support

**Workstream:** domain-c · **Area 1 of 8** · Researched 2026-10-10

> Scope: AI handling the company's own customer-support operations — answering tickets, resolving common requests, escalating to human agents. This is Domain C (an internal organisational function), distinct from Domain A (coding agents that build the product) and Domain B (AI features shipped inside the product itself). See `09-domain-boundaries.md`.

---

## 1. How organisations actually deploy it

The dominant production pattern in 2024–2026 is a three-layer setup:

1. **Knowledge layer** — help-center articles, macros, past resolved tickets indexed for retrieval (often RAG: retrieval-augmented generation — plain English: the bot searches company docs first, then drafts an answer from what it found, instead of answering from its training data).
2. **Front-line resolver bot** — handles chat/email/messenger, attempts end-to-end resolution (refunds, password resets, order changes), escalates on low confidence or policy boundaries.
3. **Agent-assist (copilot)** — drafts suggested replies, summaries, and tone fixes for human agents on the tickets the bot can't resolve.

Typical step-by-step rollout (drawn from vendor documentation and practitioner write-ups):
- Connect knowledge base and ticket history → train/fine-tune grounding content.
- Launch in "copilot-only" mode for humans first (low risk).
- Gradually move low-risk intents (password resets, order status, hours/location) to auto-resolve.
- Add tool actions behind approvals (e.g. refund issuing) with per-action limits.
- Track resolution rate, escalation rate, CSAT separately for AI vs human.

## 2. Documented cases

### Klarna — the flagship success-then-rollback
- **What happened [Verified — corroborated across Bloomberg, CX Dive, multiple outlets]:** Klarna partnered with OpenAI in 2023 and automated the bulk of customer support; ~700 customer-service staff were let go (workforce cut reported around 40% in some accounts), and the company stopped human hiring. The AI assistant reportedly handled millions of conversations in its first month, and the company touted ~$40M in profit improvement.
- **Company-reported metrics [Unverified — vendor/company claims, no independent audit]:** ~82% faster response times, 25% reduction in repeat issues, two-thirds of inquiries handled by AI.
- **The reversal [Verified — CEO on-the-record, May 2025]:** CEO Sebastian Siemiatkowski admitted the company "went too far" and that cost "seems to have been a too predominant evaluation factor," producing "lower quality." Klarna is rehiring human agents under an "Uber-style" flexible remote workforce model. Spokesperson Clare Nordstrom: "AI gives us speed. Talent gives us empathy." The AI assistant remains active — the endpoint is hybrid, not abandoned.
- **Engineering implication:** staffing cuts destroy the escalation capacity the bot needs; headline automation metrics can coexist with declining satisfaction in the long tail of complex cases.

### Air Canada — chatbot liability precedent
- **What happened [Verified — 2024 BCCRT 149, *Moffatt v. Air Canada*; covered by Guardian, BBC, ABA]:** The chatbot invented a bereavement-fare policy (book full fare, claim retroactive discount within 90 days) that did not exist. The customer relied on it; the airline refused the refund and argued the chatbot was "a separate legal entity responsible for its own actions." The tribunal called this "a remarkable submission," ruled the airline liable for negligent misrepresentation, and awarded CA$812.02.
- **Implication:** a support bot's statements carry the company's legal authority. No disclaimer about "AI" separates the two.

### Cursor "Sam" bot — invented policy incident
- **What happened [Corroborated — Ars Technica April 2025; co-founder Michael Truell confirmed on Reddit]:** Cursor's front-line AI support bot ("Sam") told users a new single-device-per-subscription policy existed. It did not. Users announced subscription cancellations on Reddit/HN before the correction arrived. Truell publicly confirmed it was "an incorrect response from a front-line AI support bot."
- **Implication:** policy-shaped hallucinations travel faster than corrections; community channels (Reddit/HN) amplify the invented policy before the company can retract it.

### German clinic chatbot — qualification claims
- **What happened [Corroborated — Lexology coverage via secondary press]:** A clinic's chatbot falsely claimed its doctors held specialist qualifications in plastic surgery. The Higher Regional Court of Hamm held the company responsible. Statements from the AI count as the company's own.

### Resolution-rate reality check (marketing vs measured)
- Intercom markets its Fin agent at ~76% average resolution (up from ~67% in 2025) [vendor claim, Unverified].
- An independent 2026 benchmark synthesising 40+ sources (Aissist.io, itself a vendor — treat as secondary interpretation) found: vendor headline rates of 67–90% come from high-structure case studies, while independent cross-program aggregates put the tier-1 automation median near **41%**, top quartile **59%**.
- Crucial methodological point from that benchmark: **resolution ≠ deflection**. Counting any conversation that never reached a human (including customers who gave up) inflates reported performance by **20–40 points** versus counting issues genuinely solved end-to-end.
- Forethought's 2025 AI-in-CX benchmark [vendor report, Corroborated methodology]: among agentic-AI adopters, top deflection rates by helpdesk were Freshdesk 66%, Kustomer 61%, HubSpot 60%; non-agentic AI sometimes *underperformed* no-AI baselines (e.g. Genesys dropped 42%).

### Practitioner voices (first-hand / community)
- HN "Ask HN: Are employers getting the returns from AI?" (May 2026): a manager reported an agent **authorised to suspend accounts** on customer tickets **incorrectly suspended an active, critical account** — "the support engineer who deployed that agent is writing the postmortem." [first-hand practitioner, community observation]
- HN (July 2026): one user found new AI support bots "more knowledgeable and honest... than human agents are" but predicted this changes once companies "lock down the AI to a 'safe script.'" [community observation]
- ChatMaxima vendor blog (citing Gartner, Feb 2026): **by 2027, half of the companies that cut customer service staff because of AI will rehire people to do similar work** [analyst prediction, Corroborated]. SMBs report being on their second or third bot attempt — the first failed because it had no way out to a human, or no boundaries on what it could say [vendor-sourced practitioner reports].

## 3. Measured outcomes (numbers only where documented)

| Metric | Value | Source / label |
|---|---|---|
| AI resolution rate, vendor headline claims | 67–90% | Vendor marketing (Intercom Fin ~76%) — **Unverified** |
| AI resolution rate, independent aggregates | median ~41%, top quartile ~59% | Aissist.io 2026 synthesis — **Corroborated**, methodology varies |
| Deflection inflation vs true resolution | +20–40 pts | Benchmark methodology note — **Corroborated** |
| Mature AI teams citing freed-up time as top ROI | ~73% | Intercom survey of 2,400+ support professionals (via Inc.) — **Corroborated**, vendor-commissioned |
| AI assist (not replace) → CSAT advantage | +36% higher CSAT | Industry report (allaboutai aggregation) — **Unverified** |
| Fin per-resolution price | $0.99/resolution | Intercom public pricing — **Verified** |
| Firms that have rolled back/shut down customer-facing AI agents at some point | ~75% | Survey reported via webpronews — **Corroborated**, source details thin |
| Gartner: agentic AI projects canceled by end 2027 | >40% | Aissist citing Gartner — **Corroborated**, prediction |
| Password-reset resolution (best case) | 98.2% | Industry aggregate — **Unverified** |
| Emotionally sensitive cases (worst case) | 61.2% | Industry aggregate — **Unverified** |

## 4. Failure modes and incidents

1. **Policy hallucination** (Air Canada, Cursor): bot invents policy-shaped text from underspecified knowledge. Root cause is usually content architecture, not model quality — one practitioner (kevinchamplin.com) traced an incident to *multiple sources of truth* and "helpful snippets" that were never packaged as machine-checkable statements.
2. **Unauthorised action** (account suspension incident): tool-use permissions wider than the task require. Blast radius scales with automation speed.
3. **Escalation-capacity collapse** (Klarna): headcount cuts remove the humans who handle the long tail; satisfaction drops on exactly the cases the bot can't do.
4. **Silent deflection**: customers who give up count as "resolved" in vendor dashboards — inflates metrics while eroding trust.
5. **Bot/agent talk-over**: bot keeps replying after a human joins the same thread [practitioner pattern].
6. **Second/third-attempt fatigue**: rigid bots with no human exit create lasting customer resistance to any automation.

## 5. Human oversight / approval design (what practitioners converge on)

- **Visible human exit**: "talk to a person" option always present; auto-handoff on low confidence, upset customer, or repeated questions.
- **Confidence thresholds** trigger handoff before the bot guesses.
- **Constrained answering**: answer only from approved content; "I'm not sure, let me connect you" instead of guessing; never let the bot promise refunds, discounts, or dates it can't verify.
- **Action approvals**: irreversible or money-touching actions (refunds, account suspension) require human approval or tight limits — the Cursor/Sam and account-suspension incidents show why.
- **Post-resolution sampling**: humans QA a sample of AI-resolved tickets (validation passes that check outputs against source documents).
- **Rollback plan**: written abort steps per agent — what to stop, how to reverse actions, who approves reactivation (corranforcedesigns practitioner guidance).

## 6. Cost vs benefit (where evidenced)

- Upside is best-evidenced for **high-volume, repetitive intents**: password resets, order status, hours — resolution rates are highest and human cost per ticket lowest to replace.
- Hidden costs: bot maintenance and knowledge upkeep; handling AI errors (33% of ITSM practitioners cite handling errors from AI automation as added work — see area 3); legal exposure (Air Canada); per-resolution pricing (Fin at $0.99) can make costs unpredictable at scale (Assembly comparison).
- Klarna's lesson: efficiency-first staffing decisions convert a support-quality problem into a brand problem; rehiring is more expensive than not cutting.

## 7. Data governance / privacy

- Support bots ingest full ticket history, customer PII, and order data — the retrieval index must respect per-customer data boundaries (confused-deputy risk: bot answering customer A with customer B's data if retrieval lacks tenant filtering).
- Retention of chat logs for training is a GDPR/purpose-limitation question; EU AI Act may add incident-reporting duties for high-risk systems.
- Third-party bot vendors become sub-processors with broad data access — audit their logging and data-use policies.

## 8. Open gaps (Unknown / needs follow-up)

- No independent, audited study of per-resolution economics at scale across vendors.
- Long-term CSAT trajectory of Klarna's hybrid model is not yet published.
- Resolution-rate definitions remain unstandardised; buyer-side measurement guidance is thin.
