# Idea Generation & Prioritisation (§4)

> Research-only deliverable. Claim labels: [Verified] / [Corroborated] / [Inferred] / [Proposed] / [Unknown]. Evidence quality: primary technical · first-hand practitioner · corroborating · community observations · secondary interpretation · unverified. Date of research: 2026-10-10. Full per-finding metadata: `04-evidence-register.md`.

---

## 1. How ideas are generated (eight methods)

Ideas should be generated *against a validated problem* (§3), not in a vacuum. Each method below: plain-English explanation, concrete example, deeper mechanics, and known limits.

### 1.1 Customer-driven ideation

**Plain English:** Ask customers what they've already built for themselves. Users who feel a problem acutely often invent partial solutions — spreadsheets, scripts, Zapier chains, Notion workarounds. Those workarounds are solution sketches drawn by the market.

**Mechanics:** In story-based interviews, the question "what have you tried?" surfaces existing attempts. The team's job is to generalize: which parts of the workaround are essential, which are accidents of the tools at hand? This keeps ideation anchored to evidenced problems rather than brainstormed fantasies.

**Example:** Three separate customers show you near-identical Google Sheets they maintain to track contract renewals because "the CRM can't do reminders properly." The idea — renewal tracking with alerts — is customer-designed before you write a line.

**Limit:** Customers design within the limits of what they know exists; they rarely invent category changes. Use for incremental opportunities, not breakthroughs.

### 1.2 Jobs-to-be-done (JTBD)

**Plain English:** Stop asking what product people want. Ask what *job* they're trying to get done — the progress they're trying to make in a specific situation. People don't want a drill; they want a hole. They don't want analytics; they want to answer "are we on track?" before Monday's meeting.

**Deeper mechanics:** Tony Ulwick's Outcome-Driven Innovation (ODI) operationalizes JTBD: every job has 50–150 *desired outcomes* — the metrics customers use to judge how well the job gets done, written in a strict syntax (direction verb + unit of measure + object + context, e.g., "minimize the time it takes to identify the root cause of a performance issue when multiple services are involved"). Each outcome is rated 1–10 on **importance** and **satisfaction** with current solutions, then ranked by the **opportunity algorithm**: `Opportunity = Importance + max(Importance − Satisfaction, 0)` [Corroborated — Ulwick via marketingjournal.org (primary: Ulwick himself), Wikipedia, and multiple practitioner docs]. Scores >15 mark severely underserved outcomes (highest-priority innovation targets); <10 marks over-served territory where investment won't differentiate [Corroborated].

**Example:** For the job "run a weekly incident review," the outcome "minimize the time it takes to assemble the timeline of what happened" scores Importance 9, Satisfaction 3 → Opportunity 15. The idea space is now precisely bounded: anything that shortens timeline assembly.

**Limit:** Heavyweight when done fully (large outcome inventories, survey panels). The lite version — 10–20 outcome statements rated in interviews — captures most of the value [Inferred — practitioner consensus, not formally studied].

### 1.3 Opportunity-solution trees (OST)

**Plain English:** A one-page map that keeps the team honest: at the top, the *outcome* you want (a business metric); below it, the *opportunities* (customer problems/needs that could move that metric); below each, candidate *solutions*; below each solution, the *experiments* that will test it. If an idea can't be traced up the tree to an outcome, it doesn't belong on the roadmap.

**Deeper mechanics:** Created by Teresa Torres (*Continuous Discovery Habits*, 2021). Key rules: work one outcome at a time; generate *multiple* solutions per opportunity (never evaluate a single solution in isolation — "compare and contrast" beats "should we do this?" because binary framing invites confirmation bias); test assumptions, not ideas, with the smallest experiment that can produce a reliable answer [Corroborated, secondary interpretation]. The tree is a thinking tool, not documentation — it evolves as experiments land.

**Example:** Outcome: "increase trial-to-paid conversion from 8% to 12%." Opportunity: "evaluators can't tell whether the product handles their data volume." Solutions: (a) sample-data import wizard, (b) public load-test report, (c) concierge pilot with their data. Experiments: fake-door test for the wizard, 5 usability sessions on a prototype, 3 paid pilots.

### 1.4 Design thinking (with its critique)

**Plain English:** The empathize → define → ideate → prototype → test loop. Its real contribution is *divergence before convergence*: generate many possibilities before judging any of them, and prototype cheaply before committing.

**Deeper mechanics / critique:** Design thinking's documented failure mode is becoming a workshop ritual disconnected from evidence — "innovation theater": sticky notes and journey maps that never change a decision [community observations]. The research-validated core (talk to users, prototype cheaply, test) is sound; the cargo-cult version (a two-day offsite, then back to the same roadmap) is not. Treat it as a *generative* method inside a discovery system (like OST), never as the discovery system itself [Inferred — synthesis of practitioner critiques].

### 1.5 Product analytics (behavioral ideation)

**Plain English:** Let user behavior suggest the ideas: where do people get stuck, what do power users do that others don't, which features are adopted and which are ignored?

**Mechanics:** Cohort analysis shows *who* succeeds; session replays and funnel drop-offs show *where* they struggle; feature-adoption data shows what's actually valued versus what's merely shipped. Ideas generated here start with quantified reach (you know exactly how many users hit the friction), which makes later prioritization more honest.

**Example:** Analytics shows users who connect the Slack integration retain 2x better, but only 12% ever connect it. Idea: move integration setup into onboarding. The reach is measurable (88% of signups), and the value hypothesis is grounded (2x retention correlation — causation still to be tested).

**Limit:** Analytics tells you *what*, never *why*. Every analytics-generated idea needs a qualitative "why" check before it earns resources.

### 1.6 Competitive analysis

**Plain English:** Systematically study competitors' products, pricing, reviews, and changelogs — to find gaps, not to copy features.

**Mechanics:** Useful outputs: a feature-comparison matrix (where you are genuinely behind on table stakes), review-mining of rival 1-star reviews (their weaknesses are your opportunity list), and pricing/packaging analysis (where the market's willingness-to-pay clusters). The discipline from §3.5 applies: a competitor shipping something proves buildability, not desirability.

### 1.7 Technical experimentation (spikes)

**Plain English:** Small, time-boxed engineering investigations that answer "can we build this?" before anyone promises it. A spike produces knowledge, not shippable code.

**Mechanics:** Spikes de-risk the **feasibility** risk in Cagan's four-risks framework. Time-box strictly (days, not weeks); define the question narrowly ("can we render 10k rows at 60fps with this library?"); end with a written answer, not a demo that quietly becomes the implementation. Spikes are for feasibility only — they must not be confused with market validation (§5 keeps the two separate deliberately).

### 1.8 AI-assisted ideation and research

**Plain English:** Use AI to widen the idea pool (generate 30 candidate solutions for an opportunity, summarize 500 reviews, draft experiment plans) — then apply human judgment and customer evidence to narrow it.

**Mechanics and guardrails:** Same rules as §3.6: AI generates, humans (and customers) decide. Particularly useful for: divergent brainstorming against a well-defined opportunity, first-pass synthesis of large qualitative corpora, and adversarial review ("attack this idea"). Particularly dangerous for: treating AI-generated market sizing as fact, letting AI "interview" synthetic users as a substitute for real ones, and allowing AI summaries to launder away the uncertainty in the source material. Every AI-generated idea enters the evaluation below with its evidence level marked honestly — usually Level 0–1 until tested.

---

## 2. Evaluation dimensions

Score or judge every surviving idea on all nine. A strong idea can be weak on one dimension; a fatal weakness on *value*, *feasibility*, or *commercial viability* kills it regardless of other strengths.

| Dimension | Question it answers | How to assess (cheaply) |
|---|---|---|
| **User value** | Does this solve a real, priced pain for a named segment? | Evidence ladder level (§3.3); Ulwick opportunity score of the underlying outcome |
| **Reach** | How many users/customers does it touch per time period? | Analytics (behavioral), ticket volumes, segment sizing |
| **Differentiation** | Why would someone choose us because of this? | §3.5 test: 10x on what they care about, or unserved job |
| **Feasibility** | Can we build it with our time, skills, and technology? | Technical spike; engineer's read (effort must come from engineering, never a PM guess [community observations, practitioner skill doc]) |
| **Cost** | What does it cost to build *and* run? | Build estimate + ongoing infra/support/ops cost |
| **Uncertainty** | How much of the above is guesswork? | Confidence rating per estimate; count of untested assumptions |
| **Business value** | Does it move a business metric (revenue, retention, acquisition, cost)? | Trace up the OST to the outcome; sanity-check the math |
| **Maintenance burden** | What does owning this cost forever? | Support surface, edge cases, data pipelines, model retraining, compliance — the "total cost of ownership," not just build cost |
| **Risk** | What are the downside scenarios? | Cagan's four risks; legal/security/brand review for sensitive ideas |

**Two dimensions teams most often skip:** *maintenance burden* (the demo is cheap; the 3-year ownership is the real price — especially for AI features with ongoing inference costs and eval upkeep) and *uncertainty itself* (an idea with modest expected value and low uncertainty often beats a high-expected-value idea that's pure guesswork — this is what confidence adjustments in scoring frameworks try to capture).

---

## 3. The idea lifecycle: reject, combine, refine, defer

Ideas don't just get "prioritized" — they move through dispositions, and each disposition should be explicit and dated:

- **Reject:** fails a decision criterion (§3.7) or scores fatally on value/feasibility/viability. Record *why* with evidence, so the idea doesn't resurrect every quarter. Rejection is a decision, not a failure — most ideas should be rejected; a funnel that rejects nothing is a funnel with no filter.
- **Combine:** two ideas attack the same opportunity from different angles — merge them into one stronger solution, or sequence them (idea B becomes the fast-follow to idea A). OST makes this visible: sibling solutions under one opportunity are combine candidates.
- **Refine:** the opportunity is real but the solution is wrong-shaped. Send it back through ideation with the new constraint written down ("users want the outcome, but reject anything requiring a second login"). Refinement is not failure — it's the normal path; Torres's cadence expects solutions to evolve as assumption tests land.
- **Defer:** valid idea, wrong time. Record the *trigger* that would un-defer it ("revisit when we have 500+ mobile actives" / "revisit after the platform API ships"). A deferred idea without a trigger is a rejected idea lying to itself.

---

## 4. Scoring systems: when they help vs. when they create false precision

### 4.1 The frameworks in brief

- **RICE** (Intercom): `Score = (Reach × Impact × Confidence) / Effort`. Reach = people affected per period; Impact = 3/2/1/0.5/0.25 multiplier; Confidence = 100/80/50%; Effort = person-time [Corroborated, secondary interpretation]. Strength: forces all four considerations onto the table; comparable across unrelated ideas. Weakness: see §4.2.
- **ICE** (simpler cousin): `Impact × Confidence × Ease`, each 1–10. Faster, even less grounded — best for rough triage only.
- **Ulwick opportunity scoring** (for *opportunities*, not solutions): `Importance + max(Importance − Satisfaction, 0)` on 1–10 scales; >15 = severely underserved [Corroborated]. Strength: built on customer-rated outcomes rather than internal guesses. Weakness: needs real survey/interview data; garbage in, gospel out.
- **Kano model:** classifies features into basics (expected; absence angers), performance (more is better), and delighters (unexpected; presence delights) — via structured customer surveys. Strength: stops teams from gold-plating basics while starving delighters. Weakness: survey-heavy; customers often can't evaluate features they haven't experienced.
- **MoSCoW:** Must/Should/Could/Won't — a negotiation tool for scope, not a ranking algorithm. Strength: forces explicit trade-offs with stakeholders. Weakness: everything becomes "Must" without a strong facilitator.
- **Cost of Delay / WSJF** (Weighted Shortest Job First): prioritizes by economic cost of waiting divided by job size. Strength: correct for time-sensitive opportunities. Weakness: requires credible delay-cost estimates, which are usually the hardest numbers to get.

### 4.2 The false-precision problem (negative evidence)

Three independent practitioner critiques converge [first-hand practitioner ×2, community skill doc]:

1. **The output looks like math; the inputs are gut feel.** Comparing a feature scoring 1.7 against one scoring 1.9 is "comparing two guesses, dressed up with a decimal point" (Kirsty Kearney-Greig, Medium, Jun 2026). Planning-fallacy research (Kahneman & Tversky, 1979) shows systematic underestimation of effort and cost; on the impact side, "at best, only one in three product ideas creates a measurable positive result" — and scoring frameworks rarely model ideas that make things *worse*.
2. **The number short-circuits the strategic conversation.** Once a score exists, "why are we doing this? who is it for? what are we trying to learn?" get flattened into "this scored higher." The framework that was supposed to help you think becomes an excuse not to (same source).
3. **Scores drift toward the loudest voice.** People unconsciously inflate the inputs that justify what they already wanted; the score looks objective but the inputs came from whoever pushed hardest in the room (same source). A separate practitioner account describes running RICE on eight backlog items for two hours — and the ranked output was "identical to what our lead developer had suggested informally before we started" (Instameal case, Medium, Jun 2026).

Torres herself reportedly rejects quantified scoring formulas for opportunity selection: "these are messy, subjective decisions and that's okay," treating them as reversible two-way-door decisions where speed beats false precision [secondary interpretation via tannerbroberts/ost-agent docs; consistent with the critiques above].

### 4.3 When scoring helps vs. when it hurts (Proposed synthesis)

**Scoring helps when:** inputs are data-rich (real reach numbers, prior impact measurements); the team needs a *defensible, comparable* record of why X beat Y (stakeholder alignment, regulated environments needing a decision trail); it's used to *structure the conversation* ("our confidence is 50% — what would raise it?") rather than to end it.

**Scoring hurts when:** inputs are pure guesses (then the formula launders guesses into "data"); the score is treated as the decision rather than an input to judgment; scores aren't revisited when context shifts; or the exercise consumes more rigor than the decision warrants (a lone obvious next step doesn't need a RICE writeup — one practitioner skill doc explicitly says so [community observations]).

**Practical rule:** Score to *compare and discuss*, never to *decide*. Record the scores *and* the overrides with reasons. Treat low confidence as a discovery task ("confidence 50% → run the assumption test first"), not just a discount factor.

---

## 5. DELIVERABLE — Worked example: evaluating 3 competing ideas

> **Method note:** This is an *illustrative* worked example with invented-but-plausible numbers, constructed to demonstrate the evaluation method. It is not data from a real company. Every evidence statement is labeled with its (illustrative) evidence level per §3.3 so the reader can see how evidence quality — not just scores — drives the decision.

### Scenario

A B2B project-management SaaS (2,000 paying teams, ~18,000 weekly active users) has one outcome for the quarter: **raise trial-to-paid conversion from 8% to 11%**. Discovery surfaced one target opportunity: *"Evaluators can't tell whether the product will handle their team's real workflow before the trial ends."* Three candidate solutions compete for one team's quarter:

| | Idea A: AI meeting-notes importer | Idea B: Native offline mobile app | Idea C: Self-serve guided trial with sample data |
|---|---|---|---|
| **Origin** | Emerging-tech-driven (§1.8): "we should do something with AI" | Customer-driven (§1.1): enterprise prospects keep asking in sales calls | Analytics-driven (§1.5): 64% of trials never invite a teammate; 71% never import real data |
| **Sketch** | Auto-generate project plans from meeting transcripts via LLM | Full offline-capable iOS/Android apps | One-click sample dataset + 3-step guided setup inside the trial |

### Step 1 — Evidence audit (before any scoring)

| Idea | Strongest evidence (illustrative) | Evidence level | Riskiest untested assumption |
|---|---|---|---|
| A | 2 prospects mentioned "AI" positively on sales calls | L1 (compliments) | That meeting-notes → project plans is a *priced* pain vs. a novelty; ongoing inference + eval costs |
| B | 11 enterprise prospects asked for mobile in 6 months; 3 cited it in lost-deal notes | L2–3 (repeated, some priced: deals lost) | That mobile unblocks *trial conversion* (askers are enterprise buyers, not trial evaluators — segment mismatch) |
| C | Behavioral: 71% of trials never import data; interviews (n=9): "I couldn't tell if it fits our process with the empty workspace" | L4 + L2 (behavioral + story-based) | That sample data + guidance converts better than empty workspace (testable cheaply) |

Note what the audit already reveals: Idea A starts from technology, not from the opportunity — it doesn't obviously serve "evaluators can't tell if it handles their workflow." Idea B has real demand but from the *wrong segment* for this quarter's outcome. Idea C is the only one whose evidence connects directly to the target opportunity.

### Step 2 — Nine-dimension evaluation

| Dimension | A: AI importer | B: Mobile app | C: Guided trial |
|---|---|---|---|
| User value | Low–Medium: novelty interest, no priced pain found | Medium: real pain for *field teams*, not evaluators | High: directly attacks the target opportunity |
| Reach | ~15% of trials (those with meeting-heavy workflows) — guess | ~8% of user base are mobile-primary — measured | 100% of new trials — measured |
| Differentiation | Low: every competitor is shipping AI summaries; parity race | Medium: few competitors have true offline | Medium: execution quality differentiator, not a moat |
| Feasibility | Medium: LLM integration known; eval harness needed | Low: two native apps or RN rewrite; 2+ quarters | High: sample-data generator + onboarding flow; weeks |
| Cost | High: inference costs scale with usage; ongoing eval | Very high: two platforms to maintain forever | Low: one-time content + flow work |
| Uncertainty | Very high: value, cost, and differentiation all guesses | Medium: demand evidenced, conversion link untested | Low–Medium: mechanism directly testable |
| Business value | Unclear link to trial conversion | Serves retention/expansion, not this quarter's outcome | Direct: attacks the #1 trial drop-off cause |
| Maintenance burden | High: model drift, prompt upkeep, cost monitoring | Very high: OS updates, device matrix, offline sync conflicts | Low: content refresh occasionally |
| Risk (4 risks) | Value ✗ unproven; Viability ✗ cost model unknown | Value ~ (wrong segment); Viability ✓ enterprise upsell later | All four risks testable cheaply |

### Step 3 — Scoring (used as a discussion tool, with honesty about inputs)

Ulwick opportunity scores for the underlying outcomes (illustrative ratings from the n=9 interviews + behavioral data):

| Outcome (job: "evaluate whether this tool fits our workflow") | Imp. | Sat. | Opportunity |
|---|---|---|---|
| Minimize time to see the product working with realistic data | 9 | 2 | 9 + 7 = **16** (severely underserved) |
| Minimize effort to get meeting notes into a project plan | 5 | 4 | 5 + 1 = **6** (served) |
| Increase ability to use the product offline on mobile | 6 | 5 | 6 + 1 = **7** (served) |

RICE-style comparison (labeled honestly — Reach for B and C is measured; for A it's a guess, so Confidence is set to 50% and the score is flagged):

| Idea | Reach/quarter | Impact | Confidence | Effort (person-weeks, eng read) | RICE-ish | Verdict on the number |
|---|---|---|---|---|---|---|
| A | 700 trials (guess) | 1 (medium) | 50% | 10 | 35 | **Do not trust** — two of four inputs are guesses |
| B | 1,440 users (measured) | 1 (medium) | 50% (segment mismatch) | 26 | 28 | Real reach, wrong outcome |
| C | 4,600 trials (measured) | 2 (high) | 80% (behavioral + interviews) | 4 | 1,840 | Highest *and* best-evidenced |

### Step 4 — Decision (judgment, informed by — not dictated by — scores)

- **Idea C → PROCEED to validation.** Best evidence-to-opportunity fit, directly serves the quarterly outcome, all four risks testable cheaply (fake-door test on the "try sample data" button; 5 usability sessions on a prototype; see §5). First validation: does the sample-data experience actually change evaluator comprehension?
- **Idea B → DEFER with trigger.** Real demand, wrong segment for this outcome. Trigger to revisit: "when enterprise expansion (not trial conversion) is the quarterly outcome, or when mobile-primary signups exceed 20%." Record the lost-deal notes as evidence for that future review.
- **Idea A → REJECT (this framing) with a refine path.** It fails the §3.7 differentiation test (parity race) and the evidence audit (L1 only, technology-first). Refine path, not a full reject of the *technology*: "revisit only with Level 2+ evidence that meeting-notes→plan is a priced pain for a named segment." The two positive sales-call mentions are filed as what they are — compliments, not demand.

### What the example demonstrates

1. **Evidence audit before scoring** — the audit alone nearly decides it; scoring then confirms rather than discovers.
2. **Segment-outcome fit beats raw score** — Idea B's demand is real but belongs to a different outcome; without the outcome frame, its "11 lost-deal mentions" would have bullied the decision.
3. **Honest confidence labels** — Idea A's RICE number exists but is explicitly distrusted; the framework structured the conversation ("what would raise confidence to 80%?") instead of ending it.
4. **Every disposition is explicit** — proceed / defer-with-trigger / reject-with-refine-path, each with the evidence pointer that would reopen it.

---

*Sources and per-finding metadata: `04-evidence-register.md`. Next: `03-validation.md`.*
