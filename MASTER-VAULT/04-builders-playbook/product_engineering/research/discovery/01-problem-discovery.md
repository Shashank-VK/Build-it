# Problem Discovery & Opportunity Identification (§3)

> Research-only deliverable. Discover, inspect, identify, verify, categorize — no installation, building, ranking, or recommendation.
> **Claim labels used throughout:** [Verified] = directly documented by an authoritative source · [Corroborated] = multiple credible sources agree · [Inferred] = plausible, not directly confirmed · [Proposed] = reference design by this researcher · [Unknown] = insufficient public evidence.
> **Evidence quality tags:** primary technical · first-hand practitioner · corroborating · community observations · secondary interpretation · unverified.
> Date of research: 2026-10-10. Full per-finding metadata lives in `04-evidence-register.md`.

---

## 1. Where meaningful problems come from

Eight channels, each explained in plain English with a concrete example and notes on evidence strength and failure modes.

### 1.1 Customer interviews (story-based, not opinion-based)

**Plain English:** Talk to the people who have the problem, and ask them to tell you what *actually happened* last time they hit it — not what they think of your idea, not what they might do someday. The discipline is: their past behavior is evidence; their opinions about your future product are not.

**Deeper mechanics:** Rob Fitzpatrick's *The Mom Test* (2013) gives the canonical rules, restated consistently across practitioner sources [Corroborated, secondary interpretation]: (1) talk about their life, not your idea; (2) ask for specifics about the past, not hypotheticals about the future; (3) listen more than you talk. Bad data looks like compliments and vague enthusiasm ("that sounds interesting", "I'd definitely use that"). Good data looks like commitments and advancement — the customer spending time, reputation, or money. Teresa Torres's continuous-discovery practice adds cadence: at minimum weekly touchpoints by the team building the product, conducting small research activities in pursuit of a desired outcome [Corroborated, secondary interpretation of *Continuous Discovery Habits*, 2021].

**Concrete example:** Instead of "Would you use a tool that auto-generates release notes?" (hypothetical, everyone says yes), ask "Tell me about the last release you shipped. How did you write the notes? How long did it take? What went wrong?" If they describe a painful 2-hour scramble, you have evidence. If they say "oh, we don't really do release notes," you have evidence too — that the problem isn't real for them.

**Strengths:** Cheapest way to find problems that matter; reveals workarounds (people's improvised fixes are the clearest signal a problem is real).
**Failure modes:** "Interviews" that are actually sales pitches; interviewing only friendly users; treating politeness as validation ("interesting" is not a signal — one practitioner postmortem put it bluntly: they treated "interesting" as a signal to build, "it was politeness") [first-hand practitioner, mindtheproduct.com, 2026].

### 1.2 Workflow observation ("get out of the building")

**Plain English:** Watch people do their actual job in their actual environment. People misremember and oversimplify in interviews; observation catches what they skip.

**Deeper mechanics:** This is the ethnographic strand of customer development. Steve Blank's core injunction — "get out of the building" — is the founding gesture of the whole customer-development movement [Corroborated, secondary interpretation of *The Four Steps to the Epiphany*, 2005]. Observation is what lets you see *workarounds*: the spreadsheet somebody maintains by hand, the Slack channel where people paste error logs, the sticky notes on a monitor. A workaround is evidence that the pain is strong enough that the user already pays a cost to relieve it — the strongest early signal that they'd pay for a real solution.

**Concrete example:** A team building deployment tooling sits with an on-call engineer during an incident and watches them copy-paste log lines into three different tools to correlate an error. The pain isn't "logging" — it's correlation across tools, and the workaround (manual copy-paste) proves urgency.

**Strengths:** Surfaces problems users can't articulate; bypasses recall bias.
**Failure modes:** Hawthorne effect (people behave differently when watched); observing too few contexts and generalizing; expensive per-insight compared to interviews.

### 1.3 Support tickets, reviews, and complaint streams

**Plain English:** Your existing users are already filing problem reports for free. Tickets, app-store reviews, NPS verbatims, and churn-exit surveys are a continuous stream of stated pains — the question is whether you mine them systematically or let them rot in a queue.

**Deeper mechanics:** Ticket data is *stated* pain with volume attached, which makes it good for the "reach" side of prioritization. Clustering ticket tags over time shows whether a problem is growing, stable, or one-off. The trap: tickets describe symptoms ("the export button is slow") more often than root causes, and the loudest customers are not always the most representative — support streams over-represent frustrated power users and under-represent users who silently churned. Triangulation with interviews is required [Inferred — widely practiced, but no single primary source verified this specific claim in this research pass].

**Concrete example:** 40 tickets in a quarter tagged "CSV export" with users describing multi-hour waits. Interviews reveal the root cause isn't export speed — it's that the data model forces them to export at all (they need scheduled reports, not faster exports). The ticket stream found the symptom; interviews found the opportunity.

### 1.4 Product analytics and behavioral data

**Plain English:** Watch what users *do* in the product — where they drop off, what they repeat, what they never touch. Behavior is evidence that doesn't depend on anyone's memory or honesty.

**Deeper mechanics:** Funnel analysis, cohort retention curves, feature-adoption rates, and session replays answer "what is happening" with precision. They are weak at "why." A flattening retention curve is a problem signal; the *reason* still requires qualitative work. Analytics is also the home of the **Sean Ellis test**: ask users "how would you feel if you could no longer use this product?" — companies where ≥40% answer "very disappointed" almost always had product-market fit; those below struggled [Corroborated — Sean Ellis's benchmark, popularized by Rahul Vohra / Superhuman, First Round Review 2018; see §5 for detail].

**Concrete example:** Analytics shows 70% of new workspaces never invite a second teammate. That is a discovered problem (collaboration never starts) — but only interviews reveal whether the cause is "didn't know they could," "tried and it was confusing," or "solo use is actually the job."

**Strengths:** Scales; unbiased by politeness; detects problems nobody reports.
**Failure modes:** Optimizing what is measurable rather than what matters (see "AI discovery pitfalls," §3.6); mistaking correlation for cause; analytics on a tiny user base producing noise treated as signal.

### 1.5 Competitive research

**Plain English:** Study what competitors and adjacent products do — not to copy them, but to find the gaps they leave and the mistakes you can avoid making.

**Deeper mechanics:** Competitor teardowns, review-mining of rival products (their 1-star reviews are your opportunity list), and tracking competitor changelogs reveal where the market is converging and where it is stuck. The critical discipline: distinguish **genuine differentiation** from **superficial imitation** (see §2.4). A competitor shipping a feature proves the feature is buildable, not that users want it — competitors also build things nobody uses. "Sales says we need a mobile app because competitors have one" is the canonical example of solution-first thinking that opportunity-solution-tree practice explicitly rejects [Corroborated, community skill docs summarizing Torres].

**Concrete example:** Mining a rival's G2 reviews surfaces repeated complaints: "reporting is powerful but takes a consultant to set up." The opportunity is not "build reporting too" — it's "reporting a non-expert can set up in an afternoon."

### 1.6 Market and technology changes

**Plain English:** Shifts in the outside world create new problems and dissolve old ones: regulation, platform changes, economic pressure, and new technical capabilities. A problem that wasn't worth solving last year can become urgent overnight.

**Deeper mechanics:** "Why now?" is a required field in a good problem statement. Regulatory change (e.g., data-residency rules), platform shifts (e.g., a new OS capability), or cost curves (e.g., cheaper inference) reframe which problems are solvable and which are urgent. The risk is technology-in-search-of-a-problem: Marty Cagan's 2026 observation is relevant here — AI is collapsing the cost of *delivery*, which shifts the bottleneck to *discovery*, "which is exactly what most orgs are worst at" [secondary interpretation of Cagan, svpg.com 2026, via frameworks-as-skills research doc].

**Concrete example:** A change in EU data regulation suddenly makes "where is my customer data stored, provably" a board-level question for mid-market SaaS buyers. Teams that were tracking the regulation have a problem statement ready; teams that weren't start from zero.

### 1.7 Internal inefficiencies and dogfooding

**Plain English:** Use your own product the way a customer would, and instrument your own operations. The problems your own team hits daily are problems your customers likely hit too — and they're the cheapest to observe.

**Deeper mechanics:** Dogfooding finds usability and reliability problems fast, but it has a known bias: your team is expert, forgiving, and unrepresentative. Internal-inefficiency discovery (e.g., "our own onboarding takes 3 days of manual setup") is legitimate problem sourcing as long as the problem generalizes beyond your company's quirks. Validate externally before investing.

### 1.8 Emerging technology (handled with suspicion)

**Plain English:** New capabilities (yesterday: mobile, cloud; today: generative AI) make previously-impossible solutions possible. The correct direction is: *technology unlocks a new way to solve an already-evidenced problem* — not *technology looking for a problem to justify itself*.

**Deeper mechanics:** The failure mode is well documented: teams start from "we should do something with AI" and retrofit a problem. The discipline is to keep the problem statement technology-free ("users can't find the right document when they need it") and treat the new technology as one candidate solution among several, tested against the same evidence bar as the non-AI alternatives. See §5.6 for when AI is genuinely necessary versus when conventional software is better.

---

## 2. Five distinctions that separate real problems from mirages

### 2.1 Real problem vs. interesting idea

A **real problem** has all three: (a) someone experiences it repeatedly, (b) it costs them something measurable (time, money, risk, emotion), and (c) they already do something costly to cope with it (a workaround, a budget line, a hired person). An **interesting idea** has none of these — it has enthusiasm, usually the founder's.

**Test:** Ask "what do they do today instead?" If the answer is "nothing — they'd just start using us," be suspicious: no current coping behavior usually means no current pain. If the answer is "they pay a contractor $2k/month to do this manually," you have a priced pain.

**Plain-English example:** "An app that reminds you to water your plants" is an interesting idea. "Property managers pay staff 6 hours/week walking units to check for leaks" is a real problem — the workaround (paid staff time) prices the pain.

### 2.2 Root cause vs. symptom

**Plain English:** A symptom is what the user complains about; a root cause is why it keeps happening. Solving symptoms produces features that feel productive and change nothing.

**Deeper mechanics:** The "5 Whys" technique (ask "why?" iteratively) is the classic tool, but it is only as good as the evidence at each step — each "why" should be answered with observed data, not speculation. Ticket clusters (§1.3) are symptom-rich and cause-poor; interviews and observation (§1.1–1.2) are where causes surface.

**Concrete example:** Symptom: "users say onboarding is confusing." Why? "They don't understand the workspace model." Why? "The mental model assumes a company hierarchy, but 60% of signups are freelancers." Root cause: the product's core metaphor doesn't match the actual user base — a tutorial won't fix it; rethinking the model might.

### 2.3 User demand vs. internal assumption

**Plain English:** "Users want X" is a claim. "Here are 12 recorded instances of users doing Y, which X would replace" is evidence. Most roadmaps are built on the first and defended as if they were the second.

**Deeper mechanics:** Steve Blank's formulation: inside the building there are no facts, only opinions — "no business plan survives first contact with customers" [Corroborated, secondary interpretation]. The Mom Test rules exist specifically to stop founders from collecting compliments and filing them as demand. The operational test is **commitment**: has anyone spent time, reputation, or money on this? A signed pilot, a prepayment, a user who built a spreadsheet workaround — these are demand. A survey saying "72% would be interested" is not.

### 2.4 Genuine differentiation vs. superficial imitation

**Plain English:** Differentiation means solving the customer's job *better in a way they can feel* — faster, cheaper, simpler, or solving a part nobody else touches. Imitation means matching a competitor's feature list. Users don't switch for parity; they switch for a 10x improvement on the thing they care about most, or for something entirely new.

**Test questions:** (1) If we removed our branding, would a user notice the difference in the first 5 minutes? (2) Does our advantage compound (data network effects, workflow lock-in through genuine value) or is it a feature any competent team ships in a quarter? (3) Are we differentiating on the *outcome* (what the user achieves) or on *surface* (how the UI looks)?

### 2.5 Technically possible vs. commercially worthwhile

**Plain English:** "We could build it" answers the feasibility risk. "Enough people would pay enough, and we can reach them cheaply enough, for the math to work" answers the viability risk. Most failed products cleared the first bar and never examined the second.

**Deeper mechanics:** This is Cagan's **business viability** risk — whether the solution works for the business across legal, finance, sales, marketing, and brand — which his research notes is one of the two risks weakest teams most under-attend (the other being value) [Corroborated, secondary interpretation of SVPG]. Commercial worthwhileness decomposes into: willingness to pay (do they pay, and how much?), cost to serve (can we deliver it profitably?), and cost to acquire (can we reach these users for less than they're worth?). A technically elegant solution to a problem held by 200 companies worldwide, each reachable only through 6-month enterprise sales cycles, can be a bad business even if every one of them loves it.

---

## 3. Evidence required before committing resources

### The evidence ladder (weakest → strongest)

| Level | Evidence | What it proves | What it doesn't prove |
|---|---|---|---|
| 0 | Founder conviction / internal opinion | Nothing (it's a hypothesis) | Anything |
| 1 | Compliments, "interesting," survey interest | Politeness | Demand |
| 2 | Story-based interviews describing past pain (n≥5–10 in a segment) | Problem exists and recurs | That they'll pay or switch |
| 3 | Observed workarounds with real cost | Pain is priced; urgency exists | That your solution fits |
| 4 | Behavioral data (drop-off, churn reasons, ticket clusters) | Problem occurs at scale | Why it occurs |
| 5 | Commitment: time, reputation, data shared, LOI, paid pilot | Serious intent | Repeatable sales motion |
| 6 | Money: prepayment, paid concierge, purchase | Willingness to pay | Retention / unit economics |
| 7 | Retention & expansion in a cohort | Value delivered over time | That it scales to new segments |

**Reading the ladder:** Level 0–1 is where most ideas die or should die. Level 2–3 justifies *discovery* investment (more research, prototypes). Level 5–6 justifies *build* investment. Level 7 justifies *scale* investment. The most common failure in the postmortem literature is committing build-scale resources on Level 0–1 evidence: CB Insights' analyses of startup postmortems consistently find ~42% cite "no market need" — building something the market didn't sufficiently want — as the top cause of failure, ahead of running out of cash [Corroborated — widely cited; caveat: self-reported postmortem data, founders may misattribute]. One 2026 practitioner postmortem trilogy put the mechanism plainly: "We proved we could build it. We never proved anyone needed it" [first-hand practitioner, mindtheproduct.com, 2026].

### Questions that must be answered before continuing

1. **Who exactly** has this problem? (a named segment, not "users")
2. **How do they cope today**, and what does the coping cost them?
3. **How often** does it occur, and is the frequency growing, stable, or shrinking?
4. **What is the root cause**, and what evidence — not opinion — supports that diagnosis?
5. **Why now?** What changed to make this solvable or urgent?
6. **How will we know** we're wrong? (the pre-committed kill criterion — see §5)
7. **What would have to be true** for this to be a good business? (willingness to pay, reachable channel, viable unit economics)

---

## 4. When to reject an idea (kill criteria)

Reject — don't defer, don't "keep on the backlog" — when any of these hold:

- **No priced pain:** after 10+ story-based interviews in the target segment, nobody describes a costly workaround or a budget they'd redirect. The problem is hypothetical.
- **Problem evaporates on inspection:** what looked like a problem was a symptom of a different cause that has a cheaper fix (or the cause is outside your control).
- **No reachable buyer:** the people with the pain can't buy (no budget authority) and the people with budget don't feel the pain — and no evidence of a path between them.
- **Unit economics can't work:** willingness-to-pay evidence caps below cost-to-serve-plus-acquire, with no credible path to move either number.
- **Differentiation is cosmetic:** the honest answer to "why would someone switch?" is "ours looks nicer" — and incumbents can copy the surface in a quarter.
- **Founder-only conviction:** the team cannot produce Level 2+ evidence after a genuine, time-boxed discovery effort. (Time-box matters: "problem-interview infinity loops" — endless interviewing without a decision — are themselves an anti-pattern [community observations, startup curriculum skill docs].)
- **Ethical/legal dead end:** the problem can only be solved by violating regulation, platform policy, or user trust. Kill early; don't "figure out compliance later."

**The pivot alternative:** Steve Blank's framework distinguishes *iterate* (correct the hypothesis inside the loop) from *pivot* (the hypothesis itself is wrong — change problem, solution, customer, or price point) [Corroborated, secondary interpretation]. Pivoting is not failure; it is the productive output of the search. Consider pivoting when customer conversations consistently invalidate hypotheses, customers lack the assumed pain, won't pay enough, or early sales efforts consistently fail [Corroborated across multiple skill docs summarizing Blank].

---

## 5. How AI can help analyze evidence — without fabricating facts or manufacturing confirmation bias

### Where AI genuinely helps in discovery

- **Clustering and triage at scale:** grouping thousands of support tickets, reviews, or interview transcripts into candidate themes. This is pattern detection over *your own collected evidence* — the raw material is real.
- **Retrieval over your evidence base:** "show me every interview quote about onboarding confusion" across a transcript corpus.
- **Competitor and market scanning:** summarizing public changelogs, reviews, and pricing pages (with links, so claims stay checkable).
- **Counter-argument generation:** explicitly asking the model to steelman the case *against* your hypothesis — the single cheapest confirmation-bias countermeasure.
- **Drafting research instruments:** interview guides, survey questions, experiment plans — drafts a human then edits.

### Where AI actively harms discovery (evidence-backed failure modes)

- **Mistaking synthesis for insight:** AI-generated theme clusters are patterns in data, not insights. A cluster about "checkout confusion" is a pattern; the insight is the specific mental-model mismatch causing it, which requires human interpretation of context [secondary interpretation, Suhail Khan, Medium, Apr 2026].
- **Over-indexing on the measurable:** AI excels at processing behavioral and textual volume but is poor at surfacing the qualitative context — the workaround, the emotional response, the unspoken job-to-be-done. Teams that let AI signals crowd out qualitative research gradually lose contact with lived user experience [same source].
- **Confirmation loops:** AI systems trained on historical data surface patterns consistent with what already occurred; they are less reliable at identifying emerging needs or challenging assumptions embedded in the team's prior research [same source].
- **Synthetic certainty:** synthetic users/personas produce clean charts and large numbers with no grounding. Cited risks include invalid insights that *appear* statistically strong, misalignment between teams and real consumers, and reinforcement of representational gaps in the training data [community observations, Danny Knox, Medium, Nov 2025 — citing Pew Research Center, The Markup, Oxford Internet Institute findings on algorithmic bias].
- **Fabrication in summaries:** documented cases of AI turning "interested in improving warehouse efficiency" into "requires warehouse automation" — upgrading interest to requirement — or inventing savings figures unsupported by source material [secondary interpretation, Paul Layton, LinkedIn, Jul 2026]. In discovery, this is not a minor error: it manufactures the exact evidence the team wanted to find.

### Guardrails for AI-assisted discovery (Proposed — reference design synthesized from the above)

1. **Ground every output in cited source material.** AI summarizes *your* transcripts, *your* tickets, *linked* public pages. Any claim without a source pointer is draft, not evidence.
2. **Separate generation from judgment.** Use AI to generate candidate themes, counter-arguments, and experiment designs; use humans (and customers) to decide what's true.
3. **Always run the adversarial pass.** For every AI-supported conclusion, prompt explicitly: "What evidence in the source material contradicts this? What would a skeptic say?" If the model can't find contradiction, that's a limitation of the prompt or the data — not proof of consensus.
4. **Never let AI interview on your behalf as a substitute for human contact.** AI can draft the guide; the conversation — and the noticing of what *isn't* said — stays human.
5. **Treat AI-clustered themes as hypotheses at Level 1–2 of the evidence ladder**, never as findings. A theme becomes evidence when a human verifies it against raw quotes and when customers confirm it unprompted.
6. **Log AI's contribution.** In the evidence register, note which analyses were AI-assisted so future reviewers can discount appropriately.

---

## 6. DELIVERABLE — Problem-Discovery Checklist

Use as a gate review before any solution work begins. Every row must be satisfiable with a pointer to actual evidence.

| # | Checkpoint | Evidence required | Kill/continue rule |
|---|---|---|---|
| 1 | Segment named | Written description of *who* (role, context, budget authority) | Can't name them → stop, do 5 more interviews |
| 2 | Problem stated in their words | 5–10 story-based interview notes with specific past incidents | Only opinions collected → stop, re-run as story interviews |
| 3 | Priced pain | Workaround described with time/money cost, or budget line identified | No priced pain after 10 interviews → reject |
| 4 | Root cause diagnosed | Each "why" in the chain backed by observed data | Cause is speculation → research more before solutioning |
| 5 | Frequency & trend | Behavioral data or repeated interview reports; direction (growing/stable/shrinking) | Rare and shrinking → defer |
| 6 | "Why now" answered | Named market/tech/regulatory change, or evidence it's newly solvable | No "why now" → flag as high timing risk |
| 7 | Demand vs. assumption separated | At least one commitment signal (time, reputation, data, money) beyond compliments | Only compliments → stop; run a commitment test (§5) |
| 8 | Differentiation hypothesis | Written answer to "why would someone switch to us" that isn't cosmetic | Cosmetic only → reject or reframe the problem |
| 9 | Commercial viability sketched | Rough WTP range, reachable channel, cost-to-serve estimate | Math can't work → reject |
| 10 | Kill criterion pre-committed | Written statement of what evidence would kill this problem framing | No kill criterion → do not proceed (bias protection) |
| 11 | Four risks triaged | Value, usability, feasibility, viability each rated high/med/low uncertainty with owner | Value or viability risk unexamined → research more |
| 12 | Decision: proceed / pivot / reject | Dated decision with evidence pointers, signed by the product trio | No decision → discovery theater (see below) |

**Discovery theater** — the failure mode where interviews happen but never change a decision, so the team correctly concludes the activity has no return and quietly abandons it [community observations, buildbetter.ai, 2026]. The checklist's row 12 exists specifically to prevent it: discovery that cannot produce a *no* is not discovery.

**Why lightweight discovery collapses** (same source, corroborating the checklist's emphasis): recruitment friction kills cadence in the first 2–3 weeks; synthesis debt piles up (transcribe/tag/map takes longer than the interview); discovery is cut first under sprint pressure because skipping it breaks nothing visible; without durable notes, decisions overweight the most recent or most emotional conversation (recency bias).

---

## 7. DELIVERABLE — Explicit Decision Criteria (problem gate)

Apply after the checklist. Score each criterion; the decision follows the lowest score, not the average.

| Criterion | Pass | Conditional (research more) | Fail (reject/pivot) |
|---|---|---|---|
| **Problem reality** | ≥5 independent story-based accounts of specific past pain in the named segment | 2–4 accounts, or accounts outside the named segment | <2 accounts after genuine effort, or pain described only hypothetically |
| **Pain priced** | Workaround cost or budget quantified by the customer | Cost implied but not quantified | No cost anyone will name |
| **Root-cause confidence** | Cause confirmed by observation or behavioral data, not just self-report | Plausible cause, single evidence type | Competing causes, no way to distinguish cheaply |
| **Demand signal** | Commitment observed (time, reputation, data, money) | Interest expressed by credible buyers without commitment | Politeness only; "interesting" with no follow-through |
| **Differentiation** | 10x on the thing they care about, or an unserved job | Parity with a credible wedge (distribution, price, focus) | Cosmetic; incumbent copies in a quarter |
| **Commercial viability** | WTP × reachable buyers > cost-to-serve + cost-to-acquire with margin | One variable unproven but testable cheaply | Math fails on verified numbers |
| **Timing** | Named "why now" with evidence | Timing neutral | Headwind: regulation, platform, or market moving against |

**Decision rule (Proposed):** Any single **Fail** → reject the problem framing or pivot to an adjacent one; do not "research more" around a failed criterion unless you can name the specific cheaper test that would change it. Two or more **Conditional** → time-boxed research sprint (≤2 weeks) with pre-committed kill criteria, then re-gate. All **Pass/Conditional** → proceed to ideation (§4) with the conditionals recorded as the riskiest assumptions to test first in validation (§5).

---

*Sources and per-finding metadata: `04-evidence-register.md`. Next: `02-ideation-prioritisation.md`.*
