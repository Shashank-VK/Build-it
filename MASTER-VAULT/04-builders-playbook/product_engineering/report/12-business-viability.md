# 12 — Business Viability: Adoption, Economics & the Cautionary Cases

*Adoption and business viability: distribution through unit economics, the AI-product cost structure, false product-market-fit signals, and two worked cautionary cases. Synthesised from the build-ship stream (§14) and domain-C economics research. Claim labels — **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown** — are preserved; nothing upgraded.*

---

## 1. The adoption funnel: AARRR

**Plain English:** "Pirate metrics" (Dave McClure's AARRR) organize the user lifecycle into five stages, each with a leading metric and an owner. Used as a *diagnostic* funnel: the lowest-converting stage is the current bottleneck, and growth investment goes there first.

| Stage | Question | Leading metrics | Typical owner |
|---|---|---|---|
| **Acquisition** | How do users find the product? | Visits, sign-ups, cost per visitor, channel attribution | Marketing |
| **Activation** | Do they experience the first value ("aha moment")? | Activation rate, time-to-value, % reaching the activation event within 7 days | Product + onboarding |
| **Retention** | Do they come back? | W1/W4/W12 retention, DAU/MAU stickiness, cohort curves | Product |
| **Revenue** | Do they pay and expand? | Free→paid conversion, ARPU, expansion MRR | Product + sales |
| **Referral** | Do they invite others? | K-factor (invites × conversion), NPS promoter share | Growth |

**Worked intuition (Corroborated** practitioner example): 1,000 visitors → 200 signups (20%) → 80 activated (40%) → 32 retained at D30 (40%) → 10 paid (31%) → 3 referrals. A 40% improvement at a 2% activation rate is worth more than a 40% improvement at a 20% paid-conversion rate — fix the bottleneck stage first.

## 2. Onboarding, activation, retention

**Plain English:** onboarding exists to shorten *time-to-value* — the gap between signup and the moment the user first gets real value. Everything before that moment is friction the user hasn't yet been paid for enduring.

**Practices (Corroborated):** shorten onboarding (fewer steps); show value immediately (skip empty states — e.g., a seeded example project instead of a blank dashboard); progressive onboarding (don't teach everything at once); define the activation event precisely per product (Slack: first message sent; Dropbox: first file uploaded; Figma: first design created).

**Benchmarks that circulate (Corroborated** as practitioner consensus; exact numbers vary by source and segment — treat as *orientation*, not targets): B2C SaaS D1 40–60%, D7 20–40%, D30 10–20%; activation goal >60% of signups reaching the event in the first session; D30 retention >20% consumer / >40% B2B SaaS; freemium conversion 2–5% average, 5–8% excellent, 8%+ best-in-class. The diagnostic use matters more than the number.

**Retention is measured in cohorts, not averages** (**Corroborated** practitioner consensus): cohort retention curves show whether each signup group sticks or decays; a leaky bucket can't be fixed with acquisition. And the product must be learnable without the founder in the room — founders assuming intuitiveness produces poor onboarding that frustrates and churns users (**Corroborated** via startup-failure analyses).

## 3. Pricing, monetisation, unit economics

**Model selection (Corroborated** practitioner frameworks):

| Model | Best for | Predictability | Watch out |
|---|---|---|---|
| **Freemium** | PLG, viral, high volume | Low | Free users cost infra + support (~$0.50–$2.00/month each, practitioner estimates); needs a natural paywall. "Freemium is not a revenue model, it is an acquisition strategy." Free-tier drag is commonly 5–15% of revenue |
| **Tiered subscription** | SMB self-serve, sticky workflows | High | Caps heavy users; churn risk |
| **Usage-based** | AI/API products, dev tools | Low | Bill shock; hard to forecast. **The 2026 trend:** usage-based pricing is growing at parity with subscriptions, and AI SaaS is shifting to usage-based specifically to recover inference costs — "if your COGS is per-token, usage-based aligns incentives" |
| **Hybrid** (base + overage) | Scale-stage SaaS | Medium-high | Complexity |
| **Enterprise license** | Compliance-heavy, complex deployment | High | Long cycles; slow to scale |

**Unit economics (Corroborated** standard definitions): LTV = ARPU × gross margin ÷ churn; CAC = sales+marketing ÷ new customers; **LTV:CAC ≥ 3:1** is the floor for continued investment (below that: pause growth spend, fix retention); CAC payback < 12 months; gross margin > 70% for software; net dollar retention > 100% is the expansion signal. The "$500–5,000/year dead zone" — too expensive for pure self-serve, too cheap to justify a sales team — is a recurring practitioner observation (community observation, widely echoed).

**Cost-to-serve:** the fully loaded cost of delivering the product to one customer — infrastructure, support, onboarding, maintenance, and (for AI) inference + review + corrections. **Pricing that doesn't cover cost-to-serve at the target margin is a slow failure, not a strategy.** Cost-to-serve data reprices tiers — it is an input to the §11 feedback loop, not a finance afterthought.

## 4. AI products: the economics of inference, failure, and human review

**The token paradox (Corroborated** via Forkast/McKinsey/Stanford HAI syntheses): token prices collapsed (roughly $20 → $0.07 per million tokens for equivalent capability, per the Stanford HAI 2025 AI Index as cited in McKinsey's July 2026 report), yet enterprise LLM expenditures *tripled* in the 12 months ending 2025 (Menlo Ventures). McKinsey's May 2026 Enterprise AI FinOps survey: **93% of enterprises are exceeding their AI budgets**; a 127-implementation analysis: 73% over budget, some by 2.4×. Cheaper tokens did not mean cheaper AI — the expense moved from the model to the process.

**Where the money actually goes (Corroborated):** agentic tasks consume roughly 1,000× the tokens of a standard query; ~60% of agentic AI spend is *response refinement* — checking, correcting, improving outputs — not the initial inference call (McKinsey QuantumBlack, July 2026, via Forkast). A banking case study: token cost was only 22% of per-loan AI cost; the remaining 78% was tool calls, vector queries, human review, and compliance. **Inferred** rule: the model is the cheapest part of the equation.

**The metric that matters: cost per successful task (Corroborated** practitioner consensus, 2026):

> Cost per successful task = (model spend on *all* attempts + human review and rescue + allocated platform cost) ÷ tasks completed correctly

- **Model spend on all attempts** includes failures and retries, plus secondary models (routing, moderation, validation).
- **Human review and rescue** = share of tasks needing a person × loaded cost of that person's time per task.
- **Allocated platform cost** = hosting, vector storage, observability, and the evaluation runs owed before every prompt/model change, divided by task volume.
- **Tasks completed correctly** is the denominator where reports cheat: a task completed *incorrectly without anyone noticing* is not a success. Without correctness measurement, the number is dishonest — which is itself a readiness signal.

**The success-rate multiplier (Corroborated):** at 90% success, expected attempts per success ≈ 1.11; at 60%, ≈ 1.67 — the same base attempt cost becomes ~50% more expensive before human review enters. Worked comparison: Model A at $1/task and 60% success needs ~167 runs ($167) for 100 successes plus engineering time identifying and rerunning 67 failures plus downstream damage from slips; Model B at $10/task and 95% success costs $1,000 for 95 near-intervention-free successes. **Per-token price tells you nothing about which wins** — "a model that costs less per attempt is not necessarily cheaper per completed task." Real benchmark: mid-2026 WebVoyager runs — GPT-5.5 at $1.42/run and 66% pass vs Claude Fable 5 at $10.22/run and 92% pass; the "cheap" model's 34% failure rate forced expensive human debugging (**Corroborated** via Towards AI reporting of Test-Lab.ai benchmarks; single benchmark — treat figures as **Corroborated**, not universal).

**Guardrail metrics to pair with cost (Corroborated):** task success rate, unsafe/invalid action rate, latency to usable result (including retries and approval waits). "If cost falls while success falls faster, the system did not become more efficient. It became less useful."

**Hidden cost layers (Corroborated):** integration and orchestration; security and compliance; evaluation and observability; human review; production rework (failed outputs, prompt regressions); training and change management; engineering support and incident response; switching/vendor-dependency costs. Pushing multi-agent workflows to production inflates first-year operational expenses **40–80%** over initial build estimates (practitioner analysis — **Corroborated** as an observed range, not a law).

**The 95% statistic:** MIT's Project NANDA (Aug 2025), covering 300 public AI initiatives, found ~95% of generative-AI pilots showing no return — no revenue increase, no cost reduction ("pilot purgatory"). The attributed cause is a "learning gap": systems that don't retain feedback, adapt to company context, or improve over time; rigid workflows and poor integration. Buying ready-made tools measured ~2× the success rate of building in-house (**Corroborated** via secondary reporting; the MIT study is the primary source, accessed second-hand). Consistent with the 2026 observation that AI *feature* replication by competitors now takes weeks, compressing differentiation timelines — feature-based moats are insufficient; iteration speed and workflow integration are the durable advantages.

## 5. False-PMF signals

**Plain English:** the gap between "people are using the demo enthusiastically" and "a sustainable business exists."

**The AI-era failure mode (Corroborated** via 2026 startup postmortem analysis): the AI-curious early adopter — tries every new AI product, engages enthusiastically, generates usage metrics that look like product-market fit — is a meaningfully different person from the mainstream customer required for a sustainable business. AI products fall into this gap at high rates because their early-adopter profiles are unusually distinct from mainstream profiles. The most reliable customer signals come from people who **pay and use consistently**; polite compliments — and enthusiastic-but-nonpaying early adopters — mislead founders into believing PMF is achieved.

**How teams distinguish a technical release from a product that solves a problem (Inferred synthesis, clearly labeled — no peer-reviewed study directly compares these as defined):**

1. **Outcome metrics, not output metrics:** deploys/day and story points measure output; activation rate, task success rate, retention, cost per successful task, and support-ticket themes measure outcomes. DORA's 2025 "vacuum hypothesis" finding is the cautionary tale: individual productivity gains coexisted with *worse* delivery throughput and stability — faster generation without small-batch discipline.
2. **Correctness-gated economics:** for AI products, the denominator is *correct* completions, and silent failures are the most expensive kind — they consume trust, not just tokens.
3. **Willingness-to-pay as the PMF test:** the customer signal that counts is paying, consistent use — not signups, not enthusiastic trials, not polite feedback.
4. **Unit economics as the viability test:** LTV:CAC, gross margin after *full* cost-to-serve (including inference, review, rework), and payback period. Growth at <3:1 LTV:CAC is value destruction with better marketing.
5. **The feedback loop as the ongoing test (§11):** a product that genuinely solves a problem shows it in the loop — retention holds, support burden per user falls, expansion revenue grows, and production findings visibly reshape the roadmap. A product that merely shipped shows motion in the pipeline and decay everywhere else.

## 6. Worked case: Klarna's two acts — the automation arc stated once, fully

*This is the canonical case for this report; it is stated here in full. Cross-references elsewhere point here rather than restating it.*

**Act I — the automation.** Feb 2024: Klarna's AI assistant doing the work of ~700 customer-service agents; 2.3M conversations in the first month; resolution times 11 minutes → under 2 minutes; ~$40M claimed annual savings; ~700 customer-service roles cut; hiring frozen. (Core facts **Verified** — CEO on-the-record via Bloomberg; partnership and volume figures via company announcement. The headline performance figures — ~82% faster response, 25% fewer repeat inquiries, two-thirds of inquiries handled by AI — are company-reported metrics with no independent audit: **Unverified**, not load-bearing.)

**Act II — the reversal.** May 2025: CEO Sebastian Siemiatkowski on the record — the company "went too far," cost "seems to have been a too predominant evaluation factor," producing "lower quality." Rehire under an "Uber-style" flexible remote model; workforce 5,500 → ~3,000; 2025 IPO; stock down >50% since (press reporting). The endpoint is hybrid, not abandoned — the AI remains active; human service reframed as "a VIP thing." The reversal itself is **Verified** (CEO on-the-record, May 2025); the "$60M lesson" framing and NPS-recovery claims in practitioner retellings are unverified single-source assertions, excluded from the load-bearing claims.

**The two distinct engineering lessons** (the gaps research flags Klarna in both an incentive-design and a workforce-architecture context):

1. **The incentive lesson.** Cost as "the too predominant evaluation factor" (the CEO's own words) converted a support-quality decision into a brand crisis — the incentive selected the wrong optimisation.
2. **The workforce-architecture lesson.** The failure wasn't the AI's task performance (routine inquiries it handled well). It was the *system* the tasks belonged to: cutting agents removed the escalation layer without building escalation logic, leaving the AI↔human boundary undefined and unmanaged. Complex cases — disputes, hardship, angry customers — had nowhere to go. The rehire was more expensive than the cut (retraining, brand repair). The durable design emerging across sources: **tiered autonomy** — AI owns high-volume/low-complexity, humans own high-stakes/ambiguous, with the boundary instrumented (escalation rate, resolution quality by tier) and reversible.

**The spreading thesis (context):** Salesforce's parallel move (~9,000 → ~5,000 support staff, AI handling ~half of conversations — via 2026 practitioner reporting, single source) shows the workforce-automation thesis is spreading; Klarna shows the failure mode is too. A Gartner prediction via a Feb 2026 vendor blog (citing Gartner): **by 2027, half of the companies that cut customer-service staff because of AI will rehire people to do similar work** (analyst prediction — **Corroborated** as reported, not as fact).

**Cross-references:** §10 (the escalation capacity that AI-agent approval controls assume is the same capacity this staffing decision removed — the D5 human-approval control needs humans to exist); §11 (error-budget-style discipline applies to support automation: instrument the boundary before cutting the capacity).

## 7. Worked case: Moffatt v. Air Canada — the liability precedent

*Stated here in full; §10 cross-references this section for the legal treatment.*

**What happened (Verified — 2024 BCCRT 149, *Moffatt v. Air Canada*; covered by the Guardian, BBC, ABA):** the chatbot invented a bereavement-fare policy (book full fare, claim a retroactive discount within 90 days) that did not exist. The customer relied on it; the airline refused the refund and argued the chatbot was "a separate legal entity responsible for its own actions." The tribunal called this "a remarkable submission," ruled the airline liable for negligent misrepresentation, and awarded CA$812.02.

**Implication:** a support bot's statements carry the company's legal authority. No disclaimer about "AI" separates the two. The pattern repeats: a clinic's chatbot falsely claimed its doctors held specialist plastic-surgery qualifications — the Higher Regional Court of Hamm held the company responsible (Corroborated — Lexology via secondary press); Cursor's front-line support bot "Sam" invented a single-device-per-subscription policy, and users announced cancellations on Reddit/HN before the correction arrived (Corroborated — Ars Technica April 2025; co-founder confirmed). The practitioner root-cause pattern: policy-shaped hallucinations usually trace to *content architecture* (multiple sources of truth, "helpful snippets" never packaged as machine-checkable statements), not model quality. The prevention sits in constrained answering — answer only from approved content; "I'm not sure, let me connect you" instead of guessing; never let the bot promise refunds, discounts, or dates it can't verify — plus a visible human exit, confidence-threshold handoffs, and post-resolution human sampling of AI-resolved tickets.

## 8. The vendor-ROI-claim skepticism framework

**The standing rule from the economics research:** every public ROI claim is either a vendor claim (**Unverified**) or a break-even sketch that ignores verification labor. Treat all of them as **Unverified** until independently reproduced.

**What to ask of any vendor performance claim** (synthesised from the evals and customer-support research):

| Question | Why it matters | What the research shows |
|---|---|---|
| **Who measured it?** | Vendor-run benchmarks are company-run; independent reproduction is the bar | Domain-B eval guidance: vendor benchmarks (e.g., Fin Apex's 73.1%) are *corroborating*, not *verified*, until independently reproduced |
| **What does the headline metric actually count?** | "Resolution" ≠ "deflection" | An independent 2026 benchmark synthesising 40+ sources found vendor headline rates of 67–90% come from high-structure case studies, while independent cross-program aggregates put the tier-1 automation median near **41%**, top quartile **59%**. **Resolution ≠ deflection:** counting any conversation that never reached a human — including customers who gave up — inflates reported performance by **20–40 points** versus counting issues genuinely solved end-to-end (vendor claims **Unverified**; the benchmark is secondary interpretation) |
| **Is the denominator honest?** | Silent failures excluded from "success" flatter the number | Cost-per-successful-task (§4): a task completed *incorrectly without anyone noticing* is not a success; without correctness measurement the number is dishonest |
| **Does the public benchmark predict *my* task?** | Generic benchmarks often don't correlate with production performance | Evals research: build the domain-specific benchmark (50–200 questions with ground truth) for the actual task, users, and risk profile; never judge-alone |
| **What gaming does the metric invite?** | Optimizing a vendor-defined metric produces Goodhart failures | Metric gaming: Klarna — great efficiency metrics, eroding trust; uncalibrated LLM judges *create* false confidence (position/verbosity/self-preference bias) |
| **What does the claim exclude?** | Verification labor, review, rework, and evaluation runs are real costs | Break-even sketches that ignore verification labor are the standard failure mode of ROI claims |
| **Is the number stable over time?** | Eval rot: datasets fossilize while traffic shifts | Silent regressions are the norm without evals — the documented cases include a 15% regression found weeks later with $200K+ impact |

**The evals discipline that answers the skepticism (Corroborated):** golden datasets, holdouts, regression gates, calibrated judges, the production-to-eval loop (production traffic feeds the eval set), and the minimum pipeline — golden → offline → gate → online at 10% → feedback loop. No vendor publishes its full golden dataset or judge prompts (all proprietary) — which is itself the reason to treat vendor claims as corroborating, not verified.

## Sources

- Full evidence: `research/build-ship/04-adoption-viability.md`, `research/domain-c/01-customer-support.md` (Klarna, Moffatt, resolution-rate reality check, vendor claims), `research/economics/01-delivery-economics.md` (ROI-claim standing rule), `research/domain-b/08-evals.md` (vendor-benchmark skepticism; eval discipline), `research/domain-b/11-domain-boundaries.md` (B/C domain placement of support automation), `research/gaps/01-missing-topics.md` (T3 incentive-design and T4 workforce-architecture framings of Klarna), plus evidence registers in each stream.
- Legal spine: *Moffatt v. Air Canada*, 2024 BCCRT 149.
- Related report sections: §08 (demo-authenticity checklist — category 5 social proof; category 7 AI honesty), §10 (AI-agent approval controls D5; the AI-statements liability cross-ref; EU AI Act duties), §11 (the feedback loop — §5 of this section's "ongoing test"; experimentation pitfalls; cost-to-serve as a loop input).
