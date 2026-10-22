# §14 — Product Adoption & Business Viability

**Workstream:** build-ship · **Researched:** 2026-10-10 · **Scope:** distribution, onboarding, activation, retention, usability, customer support, pricing, monetisation, cost-to-serve, long-term maintenance; AI-product specifics (inference cost, human review, failed tasks, correction costs, support burden, value of completed outcomes); distinguishing a successful technical release from a product that genuinely solves a problem. Read-only research only.

**Labels:** **Verified** = primary source · **Corroborated** = multiple independent sources · **Inferred** = reasoned from evidence · **Proposed** = single-sourced practitioner prescription · **Unknown** = not established. Evidence classes noted per finding.

---

## 1. The adoption funnel: AARRR

**Plain English:** "Pirate metrics" (Dave McClure's AARRR) organize the user lifecycle into five stages, each with a leading metric and an owner. Used as a *diagnostic* funnel: the lowest-converting stage is the current bottleneck, and growth investment goes there first.

| Stage | Question | Leading metrics | Typical owner |
|---|---|---|---|
| Acquisition | How do users find the product? | Visits, sign-ups, cost per visitor, channel attribution | Marketing |
| Activation | Do they experience the first value ("aha moment")? | Activation rate, time-to-value, % reaching the activation event within 7 days | Product + onboarding |
| Retention | Do they come back? | W1/W4/W12 retention, DAU/MAU stickiness, cohort curves | Product |
| Revenue | Do they pay and expand? | Free→paid conversion, ARPU, expansion MRR | Product + sales |
| Referral | Do they invite others? | K-factor (invites × conversion), NPS promoter share | Growth |

**Worked intuition (Corroborated** practitioner example): 1,000 visitors → 200 signups (20%) → 80 activated (40%) → 32 retained at D30 (40%) → 10 paid (31%) → 3 referrals. A 40% improvement at a 2% activation rate is worth more than a 40% improvement at a 20% paid-conversion rate — fix the bottleneck stage first.

**Benchmarks that circulate (Corroborated** as practitioner consensus; exact numbers vary by source and segment): B2C SaaS D1 40–60%, D7 20–40%, D30 10–20%; activation goal >60% of signups reaching the event in the first session; D30 retention >20% consumer / >40% B2B SaaS; freemium conversion 2–5% average, 5–8% excellent, 8%+ best-in-class (Slack, Spotify). Treat these as *orientation*, not targets — the diagnostic use matters more than the number.

---

## 2. Onboarding, activation, and the "aha moment"

**Plain English:** onboarding exists to shorten *time-to-value* — the gap between signup and the moment the user first gets real value from the product. Everything before that moment is friction the user hasn't yet been paid for enduring.

**Practices (Corroborated):** shorten onboarding (fewer steps); show value immediately (skip empty states — e.g., a seeded example project instead of a blank dashboard); progressive onboarding (don't teach everything at once); define the activation event precisely per product (Slack: first message sent; Dropbox: first file uploaded; Figma: first design created).

**Negative evidence — the AI-era failure mode (Corroborated** via 2026 startup postmortem analysis): *false product-market-fit signals*. The AI-curious early adopter — tries every new AI product, engages enthusiastically, generates usage metrics that look like PMF — is a meaningfully different person from the mainstream customer required for a sustainable business. AI products are falling into this gap at high rates because their early-adopter profiles are unusually distinct from mainstream profiles. The most reliable customer signals come from people who pay and use consistently; polite compliments (and enthusiastic-but-nonpaying early adopters) mislead founders into believing PMF is achieved.

---

## 3. Retention, usability, and customer support

- **Retention** is measured in cohorts, not averages: cohort retention curves show whether each signup group sticks or decays. Churn is the complement. Notifications, habit loops, and ongoing value delivery are the levers — but a leaky bucket can't be fixed with acquisition (**Corroborated** practitioner consensus).
- **Usability:** the product must be learnable without the founder in the room. A recurring failure: founders assume that because the product makes sense to them it will be intuitive — producing poor onboarding that frustrates and churns users (**Corroborated** via startup-failure analyses).
- **Customer support** is both a cost center and a feedback instrument: support-ticket themes are production evidence (see §13's feedback loop), and support burden scales with user count and product complexity. For AI products specifically, support burden includes *failed tasks users need help rescuing* — a cost category that doesn't exist for deterministic software (§5 below).

---

## 4. Pricing, monetisation, and unit economics

**Model selection (Corroborated** practitioner frameworks):

| Model | Best for | Conversion | Predictability | Watch out |
|---|---|---|---|---|
| Freemium | PLG, viral, high volume | 5–8% free→paid (typical 2–5%) | Low | Free users cost infra + support; needs a natural paywall |
| Tiered subscription | SMB self-serve, sticky workflows | ~31% trial→paid with card required | High | Caps heavy users; churn risk |
| Usage-based | AI/API products, dev tools | Variable | Low | Bill shock; hard to forecast |
| Hybrid (base + overage) | Scale-stage SaaS | Higher ARPU | Medium-high | Complexity |
| Enterprise license | Compliance-heavy, complex deployment | Long cycles | High | Slow to scale |

**The 2026 trend (Corroborated):** usage-based pricing is growing at parity with subscriptions, and AI SaaS is shifting to usage-based specifically to recover inference costs — "if your COGS is per-token or per-compute-unit, usage-based aligns incentives."

**When freemium works vs fails (Corroborated):** works with a large addressable market, low marginal cost per free user, a clear value gap between free and paid, and viral mechanics. Fails with a small market (2–5% of too few users can't sustain the business), high marginal cost (free users eat margin — a free user costs roughly $0.50–$2.00/month in infrastructure in practitioner estimates), no clear upgrade trigger (users satisfied on free forever), or enterprise buyers (decision-maker ≠ user). "Freemium is not a revenue model, it is an acquisition strategy… If your conversion rate is too low, you aren't running a software business, you are running a charity." Free-tier drag is commonly 5–15% of revenue.

**Unit economics (Corroborated** standard definitions): LTV = ARPU × gross margin ÷ churn; CAC = sales+marketing ÷ new customers; LTV:CAC ≥ 3:1 is the floor for continued investment (below that: pause growth spend, fix retention); CAC payback < 12 months; gross margin > 70% for software; net dollar retention > 100% is the expansion signal. The "$500–5,000/year dead zone" — too expensive for pure self-serve, too cheap to justify a sales team — is a recurring practitioner observation (**community observation**, widely echoed).

**Cost-to-serve:** the fully loaded cost of delivering the product to one customer — infrastructure, support, onboarding, maintenance, and (for AI) inference + review + corrections. Pricing that doesn't cover cost-to-serve at the target margin is a slow failure, not a strategy.

---

## 5. AI products: the economics of inference, failure, and human review

**The token paradox (Corroborated** via Forkast/McKinsey/Stanford HAI syntheses): token prices collapsed (roughly $20 → $0.07 per million tokens for equivalent capability per the Stanford HAI 2025 AI Index as cited in McKinsey's July 2026 report), yet enterprise LLM expenditures *tripled* in the 12 months ending 2025 (Menlo Ventures). McKinsey's May 2026 Enterprise AI FinOps survey: **93% of enterprises are exceeding their AI budgets**; a 127-implementation analysis: 73% over budget, some by 2.4×. Cheaper tokens did not mean cheaper AI — the expense moved from the model to the process.

**Where the money actually goes (Corroborated):** agentic tasks consume roughly 1,000× the tokens of a standard query; ~60% of agentic AI spend is *response refinement* — checking, correcting, improving outputs — not the initial inference call (McKinsey QuantumBlack, July 2026, via Forkast). A banking case study: token cost was only 22% of per-loan AI cost; the remaining 78% was tool calls, vector queries, human review, and compliance. **Inferred** rule: the model is the cheapest part of the equation.

**The metric that matters: cost per successful task (Corroborated** practitioner consensus, 2026):

> Cost per successful task = (model spend on *all* attempts + human review and rescue + allocated platform cost) ÷ tasks completed correctly

- **Model spend on all attempts** includes failures and retries, plus secondary models (routing, moderation, validation).
- **Human review and rescue** = share of tasks needing a person × loaded cost of that person's time per task.
- **Allocated platform cost** = hosting, vector storage, observability, and the evaluation runs owed before every prompt/model change, divided by task volume.
- **Tasks completed correctly** is the denominator where reports cheat: a task completed *incorrectly without anyone noticing* is not a success. Without correctness measurement, the number is dishonest — which is itself a readiness signal.

**The success-rate multiplier (Corroborated):** at 90% success, expected attempts per success ≈ 1.11; at 60%, ≈ 1.67 — the same base attempt cost becomes ~50% more expensive before human review enters. Worked comparison: Model A at $1/task and 60% success needs ~167 runs ($167) for 100 successes plus engineering time identifying and rerunning 67 failures plus downstream damage from slips; Model B at $10/task and 95% success costs $1,000 for 95 near-intervention-free successes. Per-token price tells you nothing about which wins — "a model that costs less per attempt is not necessarily cheaper per completed task." Real benchmark: mid-2026 WebVoyager runs — GPT-5.5 at $1.42/run and 66% pass vs Claude Fable 5 at $10.22/run and 92% pass; the "cheap" model's 34% failure rate forced expensive human debugging (**Corroborated** via Towards AI reporting of Test-Lab.ai benchmarks; single benchmark, treat figures as **Corroborated** not universal).

**Guardrail metrics to pair with cost (Corroborated):** task success rate, unsafe/invalid action rate, latency to usable result (including retries and approval waits). "If cost falls while success falls faster, the system did not become more efficient. It became less useful."

**Hidden cost layers (Corroborated):** integration and orchestration; security and compliance; evaluation and observability; human review; production rework (failed outputs, prompt regressions); training and change management; engineering support and incident response; switching/vendor-dependency costs. Pushing multi-agent workflows to production inflates first-year operational expenses 40–80% over initial build estimates (practitioner analysis — **Corroborated** as an observed range, not a law).

**The 95% failure statistic:** MIT's Project NANDA (Aug 2025), covering 300 public AI initiatives, found ~95% of generative-AI pilots showing no return — no revenue increase, no cost reduction ("pilot purgatory"). The attributed cause is a "learning gap": systems that don't retain feedback, adapt to company context, or improve over time; rigid workflows and poor integration. Buying ready-made tools measured ~2× the success rate of building in-house (**Corroborated** via secondary reporting of the MIT study; the study itself is the primary source, accessed second-hand). Consistent with the 2026 observation that AI *feature* replication by competitors now takes weeks, compressing differentiation timelines — feature-based moats are insufficient; iteration speed and workflow integration are the durable advantages.

---

## 6. Technical release vs product that solves a problem

**Plain English:** "the deploy succeeded" and "the product works" are different claims. The first is about the pipeline; the second is about a user's problem, measurably improved, at a cost the business can sustain.

**How teams distinguish them (Inferred synthesis of the evidence):**
1. **Outcome metrics, not output metrics:** deploys/day and story points measure output; activation rate, task success rate, retention, cost per successful task, and support-ticket themes measure outcomes. DORA's own 2025 "vacuum hypothesis" finding is the cautionary tale: individual productivity gains (+7.5% docs, +3.4% code quality) coexisted with *worse* delivery throughput and stability — faster generation without small-batch discipline.
2. **Correctness-gated economics:** for AI products, the denominator is *correct* completions, and silent failures are the most expensive kind (they consume trust, not just tokens).
3. **Willingness-to-pay as the PMF test:** the customer signal that counts is paying, consistent use — not signups, not enthusiastic trials, not polite feedback.
4. **Unit economics as the viability test:** LTV:CAC, gross margin after *full* cost-to-serve (including inference, review, rework), and payback period. Growth at <3:1 LTV:CAC is value destruction with better marketing.
5. **The feedback loop as the ongoing test (§13):** usage → evidence → prioritisation → requirements → implementation → verification → release → measurement. A product that genuinely solves a problem shows it in the loop: retention holds, support burden per user falls, expansion revenue grows, and production findings visibly reshape the roadmap. A product that merely shipped shows motion in the pipeline and decay everywhere else.

**When the loop says redesign or retire (§13 §6, applied):** chronically exhausted error budgets, cost-to-serve above unit economics with no path down, feature replication collapsing differentiation, or a feedback loop that keeps reporting the same unfixable shape. Retirement follows the migration discipline: deprecate, dual-run, communicate, remove.

---

## Key sources consulted (full register in 05-evidence-register.md)

AARRR / pirate metrics (McClure framework via practitioner skills); freemium economics and SaaS benchmarks (2026 practitioner syntheses); LTV:CAC unit economics; MIT Project NANDA (Aug 2025, via dev.to synthesis); McKinsey Enterprise AI FinOps (May 2026) & QuantumBlack (Jul 2026) via Forkast; Stanford HAI 2025 AI Index (via McKinsey); Menlo Ventures (via Forkast); cost-per-successful-task frameworks (MindInventory, OxAgile, Lanexora, aitech365); WebVoyager/Test-Lab.ai 2026 benchmarks (via Towards AI); AI startup failure postmortems (2024–2026); DORA 2025 AI-adoption findings (via Medium synthesis).

## Honest gaps

- SaaS benchmark figures (freemium 2–5%, D30 retention bands, $0.50–$2.00 free-user cost) are practitioner-consensus ranges, not controlled measurements; they vary by segment and source.
- MIT NANDA, McKinsey FinOps, and Stanford HAI figures were accessed via secondary reporting; directions are cross-corroborated, exact numbers are not independently re-verified.
- The WebVoyager cost benchmark is a single 2026 benchmark; model names/pricing will date quickly.
- No peer-reviewed study found directly comparing "technical release success" vs "product success" as defined here — §6 is an **Inferred** synthesis, clearly labeled.
- Long-term maintenance cost data for AI products specifically is sparse; the 40–80% first-year inflation range is practitioner-observed, not researched.
