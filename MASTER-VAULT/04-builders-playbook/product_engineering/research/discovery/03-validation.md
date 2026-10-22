# Validation (§5)

> Research-only deliverable. Claim labels: [Verified] / [Corroborated] / [Inferred] / [Proposed] / [Unknown]. Evidence quality: primary technical · first-hand practitioner · corroborating · community observations · secondary interpretation · unverified. Date of research: 2026-10-10. Full per-finding metadata: `04-evidence-register.md`.

---

## 1. Validation methods: what each one is, what it proves, what it costs

**Plain-English definition of validation:** running a cheap test that could prove you wrong *before* you spend serious resources. A validation method is any technique where a real user takes a real action (or refuses to) in response to something resembling your idea. Opinions don't count; behavior does.

| Method | Plain English | Concrete example | What it proves | Cost / time | Watch out for |
|---|---|---|---|---|---|
| **Customer interviews (solution-stage)** | Show a prototype or storyboard; ask what they'd do, watch where they hesitate | Click-through mock of the guided-trial flow (§2 worked example, Idea C); 5 evaluators narrate what they'd click | Usability risk reduced; comprehension gaps found | Days; free–cheap | Still opinions about a fake thing — proves understandability, not demand |
| **Landing page / smoke test** | A page describing the offer with one call to action; measure who acts | Page: "Guided setup: see your workflow in our product in 10 minutes" → CTA "Start guided trial"; track click-through and signup | Message resonance; top-of-funnel interest | An evening; free–$50 | Clicks ≠ demand; traffic source determines everything |
| **Fake door (painted door)** | A button/menu item for a feature that doesn't exist; measure clicks, then explain | "Import sample dataset" button in the real product; clickers get "coming soon — want early access?" | Feature interest *in context*, from real users | An evening; free | Click curiosity inflates numbers; must debrief honestly or burn trust |
| **Concierge MVP** | Deliver the service manually, 1:1, as if the product existed | Team manually builds the sample dataset for 5 trial users over Zoom, watching what they do with it | Whether the *value* lands when the tech is perfect | 1–2 weeks; founder time | Doesn't scale — that's the point; proves value, not scalability |
| **Wizard of Oz** | Looks automated to the user; humans operate it behind the curtain | "AI import" button that actually routes to a team member who builds the import in 10 minutes | Whether users want the outcome enough to wait for / trust it | Days–weeks; labor-intensive | Users may behave differently if they suspect it's manual |
| **Prototype (throwaway)** | A realistic-feeling mock for usability testing; explicitly not production code | Figma prototype of the 3-step guided setup; 5 moderated sessions | Usability risk; first-impression comprehension | Days; design time | Polished prototypes over-test visual design, under-test the value proposition |
| **Pilot (paid or committed)** | A real deployment with a small set of real customers under real conditions | 3 design-partner teams run the guided trial for 2 weeks; success = 2 convert to paid | Value + viability in realistic conditions | Weeks; support load | Design partners are friendlier than the market — discount their enthusiasm |
| **Technical PoC / spike** | Build the hard part only, to answer "can we?" | Spike: can the sample-data generator produce realistic data for 3 schema shapes in <30s? | Feasibility risk only | Days (time-boxed) | Proves nothing about demand — keep market and technical validation separate |
| **Pricing test** | Put a real price in front of real buyers and watch what happens | Pre-order page with refund terms; painted-door pricing ("Pro: $49/mo" button → "join waitlist"); Van Westendorp/Gabor-Granger surveys for range-finding | Willingness to pay (behavioral) or price-perception range (survey) | Days–weeks | Survey WTP overstates real WTP; A/B-testing price needs volume most startups lack (see §3) |
| **Usability research** | Structured observation of users attempting tasks; measures task success, errors, time | 6 evaluators attempt "import your data" unmoderated; 4 fail at the mapping step | Exactly where the design breaks | Days | Small-n is fine for *finding* problems (5 users find most usability issues — a long-standing practitioner heuristic), useless for *measuring* rates |

**Ordering principle:** run the cheapest test that attacks the *riskiest assumption first* [Corroborated across lean-startup sources]. If the riskiest assumption is "anyone wants this," a landing page beats a prototype. If it's "anyone can use this," five usability sessions beat a pilot. If it's "anyone will pay," nothing beats asking for money.

---

## 2. What counts as sufficient evidence

"Sufficient" is always relative to the *next* decision and its cost. Evidence sufficient to justify a $5k prototype is not sufficient to justify a $500k build. The framework:

### 2.1 The commitment hierarchy (strongest commonly available signals)

1. **Money changing hands** — prepayment, paid pilot, signed contract with a start date. The only signal that proves willingness to pay. Everything below is weaker.
2. **Costly non-monetary commitment** — user gives you their real data, spends an hour on integration, introduces you to their boss, signs an LOI. Costs them something real.
3. **Behavioral change** — they alter a workflow, invite teammates, return unprompted. Observed, not stated.
4. **Stated intent with specifics** — "we would buy this if it did X by March" from a budget holder. Useful directionally; routinely overstated.
5. **Stated interest** — compliments, survey "interest," waitlist signups from untargeted traffic. Level 1 evidence; necessary but never sufficient alone.

The waitlist caveat is worth stating precisely: absolute waitlist size is a vanity metric; *conversion-weighted* size is the signal. Practitioner guidance suggests a good waitlist converts 15–20% to paying, above 30% is excellent — so 53 people at 20% and 1,000 at 1% are the *same* 10 customers with different perceptions [community observations, fabricioctelles/revenue-centric-design skill doc citing @richardrx, 2026]. Until there's a transaction, there's no validated hypothesis.

### 2.2 Named benchmarks (use as reference points, not laws)

- **Sean Ellis / Superhuman PMF test:** "How would you feel if you could no longer use this product?" — ≥40% "very disappointed" marks product-market fit; below marks "still searching." Origin: Sean Ellis benchmarked hundreds of startups; popularized by Rahul Vohra at Superhuman (First Round Review, 2018), who moved Superhuman from 22% → 58% by segmenting on the "very disappointed" users and systematically converting the "somewhat disappointed" [Corroborated — startuparchive.org, TechCrunch 2021, yespress.io]. Vohra's key operational insight: the *segmentation* (who loves you, what they love, what blocks the somewhat-disappointed) matters more than the number. Caveats: needs ≥30 active users who've experienced real value; meaningless for employer-mandated products; the 40% line is a heuristic from venture-backed SaaS, not a law of nature [community observations].
- **Activation/retention floors:** practitioner playbooks cite rules of thumb like 40%+ activation (core action after signup) as healthy — treat as *starting hypotheses for your context*, not targets imported blindly [community observations].
- **Pricing research methods:** **Van Westendorp** (four open questions: too cheap / bargain / expensive / too expensive) establishes *price-perception boundaries* — not genuine willingness to pay [secondary interpretation, surveyking.com]. **Gabor-Granger** (purchase intent at specific shown price points) builds demand/revenue curves and finds revenue-maximizing prices; suited to new or infrequently-purchased products [secondary interpretation, appinio.com]. Both are *survey* methods — they inform pricing, they don't validate it; validation is behavioral (pre-orders, paid pilots).

### 2.3 The sufficiency rule (Proposed)

Evidence is sufficient when **(a)** it comes from the *named segment*, **(b)** it measures *behavior or commitment* rather than opinion, **(c)** it was collected against *pre-committed success/kill criteria* (§4), and **(d)** its strength matches the cost of the next decision (prototype → build → scale). If any of (a)–(c) fails, the evidence is interesting but not decision-grade.

---

## 3. Experiment design: the anatomy of an honest test

Every validation experiment should be specified *before* it runs. The template (synthesized from lean-startup practitioner sources [Corroborated]):

1. **Hypothesis** — one falsifiable sentence: "Trial evaluators who see a guided sample-data setup will reach the 'aha moment' (first report built) at 2x the rate of the control group within 48 hours."
2. **Riskiest assumption** — name which of the four risks (value, usability, feasibility, viability) this attacks, and why it's the riskiest one *right now*.
3. **Method** — the cheapest technique from §1 that can actually test it.
4. **Metric** — one primary metric tied to the hypothesis, plus 1–2 guardrail metrics (things that must not get worse).
5. **Pre-committed success criterion** — "the experiment succeeds if X people do Y by date Z," with specific numbers. Example: "Fake door: 30 sample-data button clicks from ICP trial traffic by week 2."
6. **Pre-committed kill criterion** — symmetric: "we kill or pivot if fewer than 10 clicks by week 2." Both go in writing *before* deployment.
7. **Interpretation plan** — what success means, what failure means, and what "inconclusive" triggers (usually: a cheaper follow-up test, not a bigger one). Writing this upfront prevents **HARKing** — Hypothesizing After the Results are Known, where the team rationalizes whatever happened as support [community observations, quinnhall07/startup-skills].
8. **Time-box and cost cap** — experiments that run forever are just building with extra steps.

**What goes wrong without this:** the Devver postmortem is the canonical warning — the team assumed they'd found their MVP, went "heads down" building, and minimized customer contact; the founder's retrospective question was "is there an even simpler version of this product that we can deliver sooner to learn more about pricing, market size, and technical challenges?" [first-hand practitioner, Ben Brinckerhoff via readwrite.com]. And the 50-MVP review found the modal failure was building "the wrong thing, the right way" — clean code, deadlines hit, polished product nobody needed — with teams building for imaginary users and confusing "MVP" with "smaller final product" [unverified single source, Medium, Jul 2026 — directionally consistent with CB Insights data but treat the "41 of 50" figure skeptically].

---

## 4. Avoiding misleading conclusions

### 4.1 Small samples and underpowered tests

**Plain English:** A test with too few users can't tell signal from noise — but it will *look* like it can, because it always produces a number.

**Mechanics:** Before running any quantitative test, compute the minimum sample size for the effect size you care about (free calculators exist). If you can't reach that floor in reasonable time, don't run the test — decide qualitatively instead: "five good interviews beat an underpowered A/B test" [community observations, citing @richardrx, 2026]. Never stop a test early because the number "looked pretty mid-way" (peeking inflates false positives). Test *big* changes (headline, offer, pricing structure, onboarding) since large effects need less sample to detect. And specifically: don't A/B test price as an early startup — you'll never have the volume or context for it to mean anything [community observations, citing ProfitWell].

### 4.2 Vanity metrics vs. actionable metrics

**Plain English:** A vanity metric makes you feel good and changes no decision. An actionable metric tells you what to do next.

| Vanity metric | Why it misleads | Actionable counterpart |
|---|---|---|
| Page views, signups (raw) | Traffic without intent | Signup → activation rate, by source |
| Waitlist size (raw) | Interest without commitment | Conversion-weighted waitlist; % who complete the next costly step |
| Social followers, press mentions | Audience without buying | Referral → purchase conversion |
| Total users / downloads | Includes the churned and inactive | Cohort retention; DAU/MAU for the core action |
| Feature shipped count | Output, not outcome | Outcome metric the feature was supposed to move |
| NPS collected once | Score without diagnosis | NPS trend + verbatim themes tied to behavior |

The TechCrunch "banish vanity metrics" piece gives the canonical illustration: a chatbot with a viral coefficient above 2 (users invited 2+ friends each) — spectacular on a slide — while almost nobody *accepted* the invitations; the real number was conversions, which they never cracked [first-hand practitioner, TechCrunch, Dec 2022].

### 4.3 The bias checklist for interpreting results

- **Confirmation bias:** the team finds what it wanted. Countermeasures: pre-committed kill criteria (§3), adversarial review ("what would convince us we're wrong?"), Torres's compare-and-contrast framing (evaluate 3+ options side by side, never one idea up-or-down).
- **HARKing:** rewriting the hypothesis after seeing the data. Countermeasure: written interpretation plan before deployment.
- **Selection bias:** design partners, friendly users, and incentivized testers are not the market. Countermeasure: label the sample honestly; discount enthusiasm from non-representative sources.
- **Survivorship in interviews:** you hear from users who stayed, not the ones who churned silently. Countermeasure: deliberately recruit churned users and non-converters.
- **Novelty effects:** new features get a curiosity bump that decays. Countermeasure: measure retention of the behavior over weeks, not the launch spike.
- **Politeness data:** compliments filed as validation. Countermeasure: the Mom Test rules — only commitments count.

---

## 5. When AI is genuinely necessary vs. when conventional software is better

This is the feasibility/viability judgment that must precede any AI validation work. The decision framework below is synthesized from multiple practitioner sources [Corroborated]:

**Use conventional software (rules, heuristics, lookup tables) when:**
- The rules are simple and well-defined — if the logic fits in a few if-statements, a model adds complexity for no benefit (tax calculation, sorting, unit conversion, form validation).
- You have little or no data — ML needs examples; with dozens of data points you cannot train anything meaningful. Collect data first.
- The cost of being wrong is catastrophic and correctness must be guaranteed — ML models are probabilistic and *will* sometimes be wrong (dosage calculation, access control, financial ledger entries).
- A threshold or lookup table already covers ~99% of cases — ML increases maintenance cost without meaningful improvement.
- Explainability is required — regulated decisions (lending, hiring, insurance) where every decision must be fully explainable; most models are not interpretable.
- The problem changes faster than you can retrain — the model is always stale.

**Use machine learning when:**
- No easily definable rule solves the task — the patterns are too complex or numerous to hand-code (fraud detection, churn prediction).
- Conditions change faster than rules can be rewritten — the system must adapt to new data continuously.
- Personalization at scale is the product — recommendations, ranking, dynamic pricing.
- Language, images, or other unstructured data are the input — document understanding, visual inspection.

**Use generative AI when:**
- The system must *create or transform* text, images, audio, video, or code — summarization, drafting, translation, generation.
- **And** you add grounding, evaluation, and human review proportional to the harm of wrong output. "You cannot put a disclaimer on your storefront" — refund info, pricing, and policy answers must be factually correct [community observations, Medium, 2026].

**The common reality is hybrid:** deterministic rules handle the routine and the high-stakes; models handle the nuance. Example: support workflow where rules answer FAQs instantly, and ML-driven triage escalates ambiguous or emotional messages to humans [secondary interpretation, Medium, 2026]. The implementation checkpoint: explicitly mark what stays deterministic, what comes from a learned model, and where humans must review — that boundary drives all later architecture and evaluation decisions [secondary interpretation, designveloper.com, 2026].

**Validation implication:** if the "AI" version of your idea can be validated with a **Wizard of Oz** test (humans behind the curtain) or a **concierge** test, do that *before* any model work — it tests the value risk, which is where AI ideas usually die, without paying the feasibility cost. Only after value is evidenced should you validate feasibility (can we get the quality/latency/cost we need?) with a technical PoC.

---

## 6. DELIVERABLE — Proceed / Revise / Research-more / Stop criteria

Apply per experiment *and* per idea (aggregating experiments). Thresholds below are illustrative defaults — **each team must pre-commit its own numbers** before running the test; the structure, not the specific values, is the deliverable.

### 6.1 Per-experiment verdicts

| Verdict | Condition | Next action |
|---|---|---|
| **Validated** | Pre-committed success criterion met, on a representative sample, with the primary metric moving and guardrails intact | Promote the assumption to "holds for now"; attack the next-riskiest assumption |
| **Invalidated** | Pre-committed kill criterion triggered, or success criterion missed by a wide margin with no sampling excuse | Kill the solution framing; return to the opportunity (§4 refine/combine) or pivot the problem (§3) |
| **Inconclusive** | Result lands between success and kill lines, or a sampling/method flaw is discovered | Run *one* cheaper follow-up test targeting the ambiguity — not a bigger version of the same test. Two consecutive inconclusives = treat as invalidated (the market is telling you it doesn't care enough to give a clear signal) |

### 6.2 Per-idea stage gates

| Gate | Proceed | Revise | Research more | Stop |
|---|---|---|---|---|
| **Problem → Ideation** (§3→§4) | Problem gate passed (§3.7): priced pain, named segment, demand signal | Opportunity real but solution space mis-shaped; re-ideate with new constraints | ≥2 conditional criteria; time-boxed ≤2-week sprint with kill criteria | Kill criterion hit: no priced pain, unworkable economics, cosmetic differentiation |
| **Idea → Prototype** (§4→§5) | Riskiest assumption identified; cheapest test designed; success/kill criteria pre-committed | Assumption test shows the *mechanism* is wrong but adjacent mechanism plausible | Key dimension is Unknown and testable cheaply (spike, 5 interviews) | Feasibility spike fails with no alternative path; or value test shows nobody cares |
| **Prototype → Build** | Value + usability evidenced (behavioral/commitment, not opinion); feasibility spike passed; viability math works on verified numbers | Usability fails but value holds → redesign, re-test usability only | Viability input (WTP, CAC) still estimated → pricing/pilot test first | Paid-pilot or prepayment test fails; Sean Ellis <25% with no segment story; unit economics fail on measured costs |
| **Build → Scale** | Retention/expansion in cohort; repeatable acquisition motion; economics improve with scale | Works for one segment, not the next → segment deliberately, don't generalize | Scale unknowns (support load, infra cost curve) → instrumented limited rollout | Retention flatlines; acquisition costs rise faster than value; the "growth" is bought, not earned |

### 6.3 The stop discipline

Stopping is a skill, not a failure. Three rules:

1. **Stop on evidence, not on feelings.** The kill criteria were pre-committed precisely so that sunk cost ("but we've already spent two months") can't vote. Sunk cost is not a reason to continue; it's the reason the criteria were written down beforehand.
2. **Distinguish "stop the solution" from "stop the problem."** Most stops should be solution-stops: the opportunity survives, the approach doesn't. Only stop the problem when the §3.7 gate fails.
3. **Write the postmortem while it's fresh.** What was believed, what was tested, what was learned, what would change the decision. Future ideas will rhyme with this one; the record is the asset. (The CB Insights finding — ~42% of startup postmortems cite no market need [Corroborated] — is, at root, a finding about teams that never built this stopping discipline.)

---

*Sources and per-finding metadata: `04-evidence-register.md`. Previous: `02-ideation-prioritisation.md`.*
