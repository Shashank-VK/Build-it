# Delivery Economics of AI-Assisted Software Development
**What is measured (and what is not) across twelve delivery dimensions**
Atlas research · workstream: economics · 2026-10-10

This file walks through the twelve dimensions the brief asked for — active work time, waiting
time, queue lengths, rework, review burden, first-pass success, failure and recovery rates,
delivery throughput, product quality, human intervention, cost per verified result, user outcomes —
and records what public evidence exists for each, with honest verdict labels.

## How to read the verdict labels

- **Verified** — measured by a controlled or pre-registered design whose methods you can inspect
  (e.g. a published RCT with an available paper).
- **Corroborated** — reported by independent sources with consistent direction (e.g. a vendor
  survey plus an academic study pointing the same way), but not from a controlled design.
- **Inferred** — a reasonable reading of the data, not directly measured by anyone.
- **Proposed** — an argument or framework offered by a practitioner or vendor, not yet measured.
- **Unknown** — nobody has published a measurement; the file says what *would* be needed.

Evidence classes used: **primary technical** (paper, published report with methodology),
**first-hand practitioner** (company engineering blog describing its own measured work),
**corroborating** (independent source consistent with the claim), **community observations**
(aggregated practitioner reports without controls), **secondary interpretation** (press/vendor
write-ups of someone else's study), **unverified** (single-source claims).

**Global caveat (Corroborated):** nearly all AI-era evidence measures *output proxies*
(PRs merged, tasks completed, lines of code) rather than *business value* (revenue impact,
customer outcomes). The task brief's rule stands throughout: do not equate generated code,
completed agent tasks, or perceived productivity with actual business value.

---

## 1. Active work time

**Plain English:** the hours a person actually spends *doing* the work — typing, debugging,
reading, deciding — as opposed to waiting for something else. In value-stream mapping this is
often called "touch time."
**Concrete example:** a feature takes 3 weeks elapsed but only ~25 hours of hands-on work;
the rest is waiting.

**What the evidence says:**

- **METR RCT (Verified, primary technical):** In the most methodologically rigorous study
  available (randomized controlled trial, pre-registered, n=16 experienced open-source
  developers, 246 real issues on repos averaging >1M lines, Feb–Jun 2025), developers took
  **19% longer** to complete tasks when AI assistance was allowed (Cursor Pro + Claude 3.5/3.7
  Sonnet). They had forecast a 24% speedup beforehand and still believed afterward they had
  been 20% faster — a ~39-point perception-reality gap. Authors attribute the drag to expert
  developers on large, familiar codebases where integrating and verifying suggestions costs
  more than writing from scratch. (arXiv 2507.09089, publ. Jul 2025)
- **METR 2026 follow-up (Verified — as "weak evidence"):** a follow-up cohort using late-2025
  agentic CLI tools produced, by the authors' own description, only weak/unreliable signal due
  to selection effects, a pay-rate change, and unreliable time-tracking; authors said developers
  are *likely* more sped up in early 2026 than early 2025 but the size of the gain is weakly
  evidenced. This is the honest state of the art: the best RCT is a year old and tested
  pre-agentic tooling.
- **Paradis et al. 2025 (Corroborated, primary technical):** a randomized trial with 96
  full-time Google engineers found AI assistance reduced time on a complex, enterprise-grade
  coding task by ~21%. Full methodology not inspected for this file; the direction contrasts
  with METR, consistent with the "task type matters" reading.
- **DX aggregate data (Corroborated, primary technical/vendor):** code-completion AI saves
  developers ~3.8 hours/week on average; perceived rate of delivery rose only ~4.5% over a
  full year across their customer base ("a modest return given the investment, and the new
  spend on AI," per DX deputy CTO Justin Reock, 2026 reporting). Notably, most developers
  spend only a minority of their time writing code, so shaving coding time moves a small
  slice of the day.

**Implication:** active work time can fall for some task types (boilerplate, greenfield) and
rise for others (expert work in mature codebases). No study measures "active work time" as a
share of the full value stream under AI adoption — see §2.

---

## 2. Waiting time

**Plain English:** everything between the moments of active work — a ticket sitting unassigned,
a PR waiting for review, a build queue, waiting for a deploy window, waiting on another team.
Value-stream maps consistently show this dwarfs active work.

**What the evidence says:**

- **Baseline (Corroborated, community observations + lean literature):** practitioner
  value-stream exercises consistently land at **5–20% flow efficiency** (active work ÷ elapsed
  time), with ~15% a commonly reported figure; a canonical lean illustration shows 7.5 days of
  work inside 53.5 days elapsed (~14%). In other words, ~85% of customer lead time is waiting.
- **AI-era direction (Inferred, corroborated pieces):** faster code generation *adds* work
  items into the same downstream queues. Direct AI-era measurements of total waiting time are
  missing (Unknown at the aggregate level), but every component proxy moves the wrong way:
  review queues grow (LinearB: AI PRs wait **4.6× longer** before first review; Faros AI:
  review time up **91%** where AI adoption is high), PRs get larger and harder to review
  (154% larger per Faros-derived reporting; PR volume +98%), and Claude Code PRs wait a
  median **12.6h** for first human review (Kraishan 2026). The one published before/after of a
  *full* stream (AutonomyAI customer, via KoreaTechDesk, first-hand practitioner): 1 hour of
  work with a 3-week median request-to-production lead time, cut to 1–2 days by changing the
  *workflow*, not the coding speed — "the queue was the product being measured."
- **DORA 2025 (Corroborated, primary technical):** "AI accelerates software development, but
  that acceleration can expose weaknesses downstream… an increase in change volume leads to
  instability" without robust control systems (testing, version control, fast feedback).

**Implication:** waiting time is the dominant term in delivery economics and the least
measured AI-era term. Any claim that AI "halved delivery time" without a waiting-time
decomposition is a claim about coding speed, not delivery.

---

## 3. Queue lengths

**Plain English:** how many work items are piled up in front of each stage — review queues,
CI queues, deploy queues. Longer queues mean longer waits and more context-switching.

**What the evidence says:**

- **(Inferred, corroborating proxies):** no published study reports raw queue lengths
  (tickets awaiting review, CI queue depth) before and after AI adoption — **Unknown** at the
  aggregate level. The inference that queues lengthen rests on converging proxies:
  - PR volume is up sharply where AI is used (DX: AI users ship 60% more PRs; Microsoft CLI
    study: +24% merged PRs/engineer/day sustained over 4 months; GitHub platform data: >500M
    PRs merged in the year to Oct 2025, ~1 in 3 involving an agent by Jul 2026).
  - Review capacity has *not* grown to match (review time per PR up; share of AI PRs getting
    at least one human review fell from 89% to 68% in one tracked mid-size company, with
    automated AI-review coverage rising 19%→84%).
  - LinearB's benchmark (8.1M PRs, 4,800 orgs): AI PRs wait 4.6× longer before review — the
    signature of a lengthened queue.
- **What would be needed:** per-stage queue-depth time series from engineering-intelligence
  platforms (review queue, CI queue, deploy queue) segmented by AI-authored vs human-authored
  changes. Nobody publishes this.

---

## 4. Rework

**Plain English:** work that has to be redone — rejected PRs, post-merge fixes, rollbacks,
code rewritten or deleted shortly after being written.

**What the evidence says:**

- **Churn (Corroborated, primary technical):** GitClear's longitudinal analyses find
  two-week code churn (rewritten/deleted shortly after writing) **up ~15%** in the AI era
  (2026 study, 623M commits), and earlier work showed churn nearly doubling 2020→2025.
- **Rejection (Corroborated, vendor benchmark via secondary):** LinearB's 8.1M-PR benchmark:
  AI-generated PRs had a **32.7% acceptance rate vs 84.4%** for manually written PRs — a
  rejected PR consumes author and reviewer time while shipping nothing.
- **Post-merge rework (Corroborated, academic + surveys):** Watanabe et al. (567 Claude Code
  PRs, 157 OSS projects): **45.1%** of merged agent PRs required further human modification.
  New Relic's 2026 survey (200 US tech decision-makers): 74% said ≥25% of AI-generated code
  needed significant rework *after deployment*; Lightrun's 2026 survey (200 SRE/DevOps
  leaders): 43% of AI-generated changes needed manual debugging in production after passing
  QA/staging.
- **Reverts (Verified, primary technical — with a twist):** Kraishan 2026 (37,623 agent PRs,
  5 commercial agents, 2,807 repos, Dec 2024–Jul 2025, full replication data released):
  Codex-authored PRs were reverted about *half* as often as human PRs (6.1% vs 11.5%); Devin
  PRs reverted *more* often (14.5%). Revert risk is vendor- and task-specific, not uniformly
  worse — genuine counterevidence to blanket "AI code is worse" claims.

**Implication:** rework is the hidden tax that converts coding-speed gains into flat or
negative delivery gains. It is also where measurement is thinnest — nobody publishes
"hours of rework per AI-assisted PR" as a standard metric.

---

## 5. Review burden

**Plain English:** the human effort spent checking code before it ships — reviewer hours,
review rounds, time-to-first-review, and the cognitive load of verifying work you didn't
write.

**What the evidence says:**

- **Volume up, capacity flat (Corroborated):** Faros AI (>10,000 developers): where AI
  adoption was high, developers merged **98% more PRs** while **review time rose 91%**.
  Secondary reporting (attribution uncertain — see evidence register) describes the DORA
  2025-era data as: +9% bug rate, **+91% code-review time, +154% PR size** with rising AI
  adoption.
- **Review is harder, not just longer (Corroborated, surveys):** Sonar (1,100+ developers):
  42% of committed code is AI-generated, but 96% don't fully trust it functionally correct,
  only 48% always check it before committing, and 38% say reviewing AI code takes *more
  effort* than a colleague's. Stack Overflow 2025 (~49,000 respondents): 45% say debugging
  AI code is more time-consuming than expected; "almost right, but not quite" is the top
  frustration (66%). Harness survey: 67% report spending *more* time debugging AI-generated
  code.
- **Coverage is slipping (Corroborated):** in one tracked company, human-review coverage of
  AI PRs fell 89%→68% as volume doubled; a CodePulse/BigQuery analysis (262k repos, 191k
  developers) found ~90% of large changes shipping with no formal review (zero approvals,
  comments, or change requests).
- **The judgment asymmetry (Corroborated):** Anthropic's data (via secondary): users reject
  only 3% of individual agent commands but **39% of presented plans** — humans are bad at
  step-checking, decent at direction-judging. Review effort concentrates unevenly by tool:
  Kraishan 2026 found Copilot PRs drew the most human reviews/change requests.
- **A counterweight (First-hand practitioner):** Microsoft's internal AI code-review
  assistant touches >90% of PRs (>600k/month); PR completion times improved 10–20%. AI
  review tooling is itself shifting some review burden off humans — with the caveat from
  CodeRabbit's own study that 80% of PRs get no human comments when AI review is enabled,
  i.e. automation can hollow out human involvement.

**Implication:** review is the clearest documented bottleneck shift. Generation got cheaper;
verification got more expensive and is increasingly skipped.

---

## 6. First-pass success

**Plain English:** the share of changes that go from submission through testing, review, and
deployment without being kicked back or fixed along the way.

**What the evidence says:**

- **(Unknown, with weak proxies):** no published source reports an industry "first-pass
  success rate" for AI-assisted changes with a pre-AI baseline. Closest proxies, all
  pointing down:
  - "2026 State of Software Delivery" reporting (single secondary source, **unverified**):
    main-branch success rates at **70.8%**, a five-year low vs a 90% recommended benchmark —
    ~3 in 10 merges failing.
  - LinearB: 32.7% AI-PR acceptance vs 84.4% manual.
  - Watanabe: only 54.9% of merged Claude Code PRs landed without modification.
  - AIDev dataset paper: agent PR acceptance ranged 84.0% (chores) to 55.4% (performance
    work) — task type dominates.
- **What would be needed:** a pre-registered definition (e.g. merged without a change
  request, passing CI first try, no hotfix within 7 days), measured on AI vs human changes
  in the same repos.

---

## 7. Failure and recovery rates

**Plain English:** how often changes break things in production (change failure rate,
incidents per change) and how long it takes to recover (MTTR).

**What the evidence says:**

- **Failures up (Corroborated):** Cortex's 2026 benchmark (50+ orgs, Q3 2024→Q3 2025):
  PRs/author +20% YoY while **incidents per PR rose 23.5%** and **change failure rates
  climbed ~30%**. Faros.ai's analysis of the DORA dataset: incidents per PR up **242.7%**
  over two years (secondary reporting; magnitude needs primary verification).
- **DORA 2025 (Corroborated, primary technical):** AI adoption continues to have a
  **negative relationship with delivery stability** even as throughput rises — "speed without
  stability is accelerated chaos." DORA 2024 had shown −1.5% throughput and −7.2% stability
  with rising adoption; 2025 reversed the throughput sign but not the stability sign.
- **Recovery (Weak/Unverified):** the "2026 State of Software Delivery" secondary reporting
  claims mean recovery time of 72 minutes, up 13% YoY — single-source, treat as unverified.
  No controlled study of MTTR under AI adoption was found.
- **Production incident attribution (Corroborated, leader surveys):** New Relic 2026: 78%
  of decision-makers saw measurable production-incident spikes tied to AI code; 82% had ≥1
  major AI-attributed production failure in six months.

---

## 8. Delivery throughput

**Plain English:** how much working software reaches users per unit of time — merged PRs,
deploys, completed tasks. The metric most often cited, and the most easily gamed by volume.

**What the evidence says:**

- **Controlled field evidence, positive (Verified, primary technical):** Cui et al. (Feb
  2025; Princeton/MIT/Microsoft/Wharton; postregistered AEARCTR-0014530): three randomized
  field experiments at Microsoft, Accenture, and an anonymous Fortune 100 company
  (n=4,867 developers total) found a **+26.08% (SE 10.3%)** increase in *completed tasks*
  (PRs, commits, builds as proxies) among developers with Copilot access; less-experienced
  developers gained most. Caveats: task *counts*, not value; each experiment noisy; 2022–23
  era tooling.
- **Controlled field evidence, positive but output-only (Verified, primary technical):**
  Microsoft's early-2026 CLI-agents study (arXiv; Claude Code + Copilot CLI): **+24.0%**
  merged PRs/engineer/day (likely range +14.5% to +33.7%), sustained over four months, with
  a placebo-timing check. The authors' own conclusion is the key sentence: the lift is
  "direct evidence that agentic command line tools can move a concrete output metric —
  though whether that output justifies its cost is a question of value, not throughput
  alone. The pressing open question is now about quality."
- **Enterprise RCT, positive (Corroborated, vendor-reported):** Accenture × GitHub (450
  devs with Copilot, 200 without): **+8.69%** PRs/developer, **+15%** PR merge rate, **+84%**
  successful builds, ~30% suggestion acceptance. Reported by the vendor; methodology not
  independently inspectable — treat direction as corroborated, magnitudes as vendor-claimed.
- **Lab evidence, positive but narrow (Verified, primary technical — with methodology
  critique):** Peng et al. 2023 (GitHub-affiliated authors, ACM): 95 developers writing a
  JavaScript HTTP server from scratch finished **55% faster** with Copilot (1h11m vs 2h41m).
  Critique: toy task maximally favorable to autocomplete, vendor-authored, no maintenance or
  integration phase — measures the one slice of work where AI helps most.
- **Observational, null (Corroborated):** Uplevel Data Labs (Sept 2024; ~800 developers,
  test vs control, 3-month windows): **no significant change** in PR cycle time or
  throughput; cycle-time delta was 1.7 minutes ("inconsequential"). The one significant
  move: **+41% detected-bug rate** — but Uplevel's own analyst stressed "it's obviously not
  a causal relationship" (correlational design). Strong counterevidence to "throughput
  always rises."
- **Observational, modest (Corroborated):** DX 2025–26 aggregates: median **+7.7%** PR
  throughput (Nov 2024–Feb 2026), average +13%, top performers ~70%; "nobody hit 2x, 5x, or
  10x." Deployment frequency rose then flattened.
- **The branch-throughput divergence (Inferred):** feature-branch throughput +7.7% YoY
  while main-branch throughput stayed flat (KoreaTechDesk, citing delivery benchmarks) —
  work is being *started* faster than it is being *finished*, the signature of a
  downstream bottleneck.

**Implication:** throughput of *artifacts* rises in most settings; whether throughput of
*value* rises is unmeasured everywhere.

---

## 9. Product quality

**Plain English:** does the software work correctly, securely, and stay maintainable —
defect density, security vulnerabilities, code-structure health.

**What the evidence says:**

- **Structural decay (Corroborated, primary technical):** GitClear's longitudinal studies
  (2024: 211M lines; 2026: 623M commits): duplicated blocks **+81%** (40→73 per million
  changed lines), within-commit copy/paste **+41%**, error-masking constructs **+47%**,
  refactoring line-moves **−70%**, genuine-refactoring commit share **21%→<4%**,
  cross-file function calls **−35%**. Copy-pasted lines exceeded moved (refactored) lines
  for the first time in 2024. Direction is consistent across three annual cuts.
- **Defect density up (Corroborated):** CodeRabbit (470 OSS PRs): AI PRs carry ~1.7× more
  total issues (10.83 vs 6.45), 1.4× more critical, 1.75× more logic/correctness errors.
  (Vendor = AI review company: direction consistent with independent data, magnitude
  vendor-measured.) Uplevel: +41% detected bugs (correlational). DORA-era analyses: +9% bug
  rate with rising adoption.
- **Security (Mixed — genuine disagreement):** Veracode (100+ LLMs, Java/JS/Python/C#):
  **45% of AI-generated code contains an OWASP Top-10 vulnerability**, 2.74× more vulns
  than human-written code (2025); Summer 2026 retest of 11 frontier models on 80 tasks:
  average security pass rate only **56%**. **Counterevidence:** Kraishan 2026 (37,623 agent
  PRs in the wild): agent code pooled across vendors was *less* likely than human code to
  contain a security smell (odds ratio 0.63), driven by fewer hardcoded credentials and
  eval-style constructs. Resolution: lab-generated code vs in-the-wild agent PRs that
  passed human review are different populations — both findings can be true.
- **Perceived vs measured quality (Corroborated):** DORA 2025: 59% say quality improved
  with AI, yet stability fell; New Relic 2026: 94% of leaders rate AI code *higher quality
  at review time*, while 78% simultaneously saw production-incident spikes tied to it —
  review-time judgment is a weak proxy for durability.
- **Trust (Corroborated, large surveys):** Stack Overflow 2025: trust in AI accuracy fell
  40%→29%; 46% actively distrust output; only ~3% highly trust. LaunchDarkly (767
  engineers): 94% report accelerated coding, but 91% have low trust shipping AI code to
  production and 81% ship with unresolved risks.

---

## 10. Human intervention

**Plain English:** how much human judgment, correction, and supervision each AI-assisted
change requires — plan rejections, revision rates, escalations, the "human in the loop" tax.

**What the evidence says:**

- **Revision is the norm (Corroborated):** Watanabe: 45.1% of merged Claude Code PRs needed
  human modification. Anthropic: users reject 39% of agent-presented plans (vs 3% of
  individual commands). GitHub's own 2022 telemetry: only 26% of Copilot suggestions
  accepted (~3 in 4 rejected); Accenture: ~30% acceptance, though 88% of generated
  characters stayed in the editor (i.e., accepted-then-edited).
- **Review effort concentrates unevenly (Verified, primary technical):** Kraishan 2026:
  Copilot PRs drew the most human reviews and change requests; Claude Code PRs waited
  longest for first human review (median 12.6h).
- **Intervention at scale (First-hand practitioner):** Spotify's fleet-management system
  (Claude-based): 2.5M PRs auto-merged over 18 months, "vast majority" with zero manual
  edits — but confined to standardized maintenance (dependency updates, patches), with
  humans handling exceptions. Human intervention approaches zero only where the task is
  fully standardized.
- **(Unknown):** no published "human minutes per AI task" or escalation-rate metric with a
  pre-AI baseline exists.

---

## 11. Cost per verified result

**Plain English:** the fully loaded cost of one unit of *actually working, shipped, correct*
output — inference + licenses + the human time spent specifying, reviewing, testing,
debugging, and fixing it. This is the metric the whole debate needs and nobody publishes.

**What the evidence says:**

- **(Unknown — no direct measurement found.)** All public cost discussion covers *inputs*,
  not cost per verified result:
  - Seat pricing: $10–$40/month standard tiers; $40–$200+/month power/enterprise tiers;
    extreme usage $300–$1,000+/month/developer in raw API terms.
  - Break-even arithmetic is trivially favorable *if* you count gross time saved: a
    $15k/month loaded engineer needs ~3 hours/month saved at $300/month tooling.
  - Microsoft's April 2026 earnings: rising Copilot usage was pushing down Cloud gross
    margin; margins recovered after the June 2026 shift to usage-based pricing — the
    subsidy era is ending and true costs are being passed through.
  - Token pricing spans three orders of magnitude ($0.06–$168 per million tokens by
    tier), and output tokens cost 5–8× input tokens; a heavy agentic day can burn
    0.5–1M+ tokens.
  - Larridin's 2026 spend report documents a **diminishing-returns curve**: spend and
    productivity rise together through a "healthy ROI" region, then costs spike past an
    inflection point into "tokenmaxxing" — more spend, flat output. (Vendor framework;
    the shape is Proposed, the underlying customer data unverified.)
- **What would be needed:** (a) fully loaded inference + license cost per developer per
  month; (b) human minutes spent on review/rework/debugging per AI-assisted change;
  (c) defect-escape cost; combined into cost per change that survives, say, 30 days in
  production without incident. No organization publishes this.

**Implication:** every public ROI claim is either a vendor claim (Unverified) or a
break-even sketch that ignores verification labor. Treat all of them as Unverified.

---

## 12. User outcomes

**Plain English:** did the customer get a better product, faster, more reliably — the only
measure that ultimately matters.

**What the evidence says:**

- **(Unknown — essentially unmeasured.)** No study in this review connects AI coding
  adoption to customer-facing outcomes (satisfaction, retention, time-to-value, SLA
  attainment) with any control or baseline. What exists is adjacent:
  - **Corroborated, negative adjacent:** delivery *stability* falls as AI adoption rises
    (DORA 2024, DORA 2025, Cortex 2026, Faros.ai) — users experience this as incidents.
  - **Corroborated, positive adjacent:** DORA 2025 finds AI adoption positively related to
    *product performance* (self-reported) alongside throughput; >80% of respondents believe
    productivity rose. Self-reported, vendor-adjacent (Google Cloud), direction consistent
    with throughput evidence.
  - **Inferred:** DORA 2025's strongest moderator finding — "when teams adopt a
    user-centric focus, the positive influence of AI on their performance is amplified;
    without it, AI adoption can have a negative impact" — implies user outcomes depend on
    *what the freed capacity is pointed at*, which nobody measures.
- **What would be needed:** org-level before/after on customer metrics (CSAT, churn,
  incident-affecting-users, lead time from request to customer value) with AI adoption as
  the treatment. This is the central empirical hole in the entire field.

---

## Cross-dimension summary

| Dimension | Direction of evidence | Strongest source | Label |
|---|---|---|---|
| Active work time | Mixed by task type (−19% to +55%) | METR RCT; Cui et al. | Verified |
| Waiting time | Dominates lead time; AI-era total unmeasured | VSM literature; proxies | Inferred / Unknown |
| Queue lengths | Lengthening (inferred from wait proxies) | LinearB; Faros AI | Inferred |
| Rework | Up (churn, rejections, post-merge fixes) | GitClear; Watanabe; Kraishan | Corroborated |
| Review burden | Up sharply; coverage slipping | Faros AI; Sonar; Stack Overflow | Corroborated |
| First-pass success | Down (proxies only) | LinearB; branch data | Inferred / Unknown |
| Failure & recovery | Failures up; recovery unmeasured | Cortex; DORA 2025 | Corroborated / Unknown |
| Delivery throughput | Artifact throughput up ~8–26% | Cui et al.; Microsoft 2026 | Verified (output only) |
| Product quality | Structural + defect signals down; security mixed | GitClear; Kraishan | Corroborated |
| Human intervention | High and uneven; ~45% of agent PRs revised | Watanabe; Kraishan | Corroborated |
| Cost per verified result | No measurement exists | — | Unknown |
| User outcomes | No measurement exists | — | Unknown |

**The one-sentence economics:** AI has made the cheapest step of software delivery
(writing code) cheaper, while making the expensive steps (specifying, verifying, reviewing,
securing, integrating, operating) a larger share of total cost — and the two steps the
business actually pays for, *cost per verified result* and *user outcomes*, have no public
measurements at all.
