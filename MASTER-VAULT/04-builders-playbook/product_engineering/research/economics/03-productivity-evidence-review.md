# Productivity Evidence Review: Study by Study
**Methodology, what each study actually establishes, and the gaps.**
Atlas research · workstream: economics · 2026-10-10

Labels per study: design class, what it found, what it *actually* establishes, limits/gaps,
and a verdict. Verdicts: **Verified / Corroborated / Inferred / Proposed / Unknown** (defined
in 01-delivery-economics.md). A recurring theme: almost every study measures output proxies
(tasks, PRs, lines), not business value.

---

## Controlled trials (the strongest designs)

### 1. METR — "Early 2025 AI, Experienced Open Source Developer Productivity" (RCT)
- **Design:** randomized controlled trial, pre-registered. n=16 experienced open-source
  developers, 246 real issues on their own repositories (avg >1M lines, ~22k stars), run
  Feb–Jun 2025, published Jul 2025 (arXiv 2507.09089). Tasks randomly assigned to
  AI-allowed (Cursor Pro + Claude 3.5/3.7 Sonnet) vs AI-forbidden. Objective
  time-to-completion.
- **Found:** AI-allowed tasks took **19% longer**. Developers had forecast a 24% speedup
  beforehand and believed afterward they were 20% faster (~39-point perception gap);
  <44% of AI suggestions accepted; 69% said they'd keep using the tools anyway.
- **Actually establishes:** on large, familiar codebases, with expert maintainers, early-2025
  assistant-style AI imposed net verification/integration costs exceeding generation
  savings — and self-report is unreliable as a productivity measure.
- **Limits:** small n (16); expert-only; mature OSS codebases (not greenfield, not
  enterprise); pre-agentic tooling; short tasks. Does not generalize to juniors, new
  projects, or 2026 agentic tools.
- **Verdict: Verified** (for its population). The best-measured negative result in the
  field; also the best-measured demonstration of the perception-reality gap.

### 2. METR 2026 follow-up (redesign with late-2025 agentic tools)
- **Design:** attempted follow-up cohort with agentic CLI tooling.
- **Found:** compromised by selection effects, a pay-rate change, and unreliable
  time-tracking; authors describe it as producing only **"weak evidence"**; point estimate
  ~18% slowdown but not credible. Authors judge developers are *likely* more sped up in
  early 2026 than early 2025, with weak evidence on magnitude.
- **Actually establishes:** how hard this is to measure well — and that no rigorous RCT of
  current agentic tools exists. Absence of evidence is not evidence of absence.
- **Verdict: Verified** — as a statement about the *state of evidence*, not about the effect.

### 3. Cui, Demirer, Jaffe, Musolff, Peng & Salz (2025) — three field RCTs at Microsoft, Accenture, anonymous Fortune 100
- **Design:** three randomized field experiments run by the companies "as part of their
  ordinary course of business," combined n=4,867 developers; treatment = GitHub Copilot
  access (2022–23 era); outcome = completed tasks proxied by PRs, commits, builds.
  Postregistered (AEARCTR-0014530). Draft via MIT Economics, Feb 2025.
- **Found:** **+26.08% (SE 10.3%)** more completed tasks with AI access; less-experienced
  developers had higher adoption and larger gains.
- **Actually establishes:** in real enterprise settings, Copilot access raised *output
  counts* by roughly a quarter, concentrated among juniors. The largest-scale causal
  evidence available.
- **Limits:** outcome is task *counts*, not value, quality, or downstream cost; each
  experiment noisy; 2022–23 tooling (pre-agentic); author team includes Microsoft/GitHub
  affiliates — disclose, don't dismiss. Cannot speak to review burden, rework, or
  stability.
- **Verdict: Verified** (output rose); **Unknown** whether business value rose.

### 4. Peng, Kalliamvakou, Cihon & Demirer (2023) — GitHub's "55% faster" lab study
- **Design:** RCT, n=95 developers, one task: write an HTTP server in JavaScript; Copilot
  group vs control; published via ACM.
- **Found:** Copilot group finished in 1h11m vs 2h41m — **55% faster**; completion 78%
  vs 70%.
- **Actually establishes:** on a small, self-contained, greenfield task maximally
  favorable to autocomplete, Copilot-era AI roughly halved time-to-first-working-code.
- **Limits (methodology critique):** vendor-authored (GitHub employees); toy task with no
  maintenance, integration, review, or legacy-context phase — i.e., it measures the one
  slice of work AI helps most and excludes every slice where the evidence says costs
  moved; freelancers, not a team; single session. The most-cited number in enterprise AI
  is also the least representative of enterprise work.
- **Verdict: Verified** (for the lab task); **does not generalize** to delivery productivity.

### 5. Paradis et al. (2025) — Google internal RCT, 96 engineers
- **Design:** randomized trial with 96 full-time Google engineers on a complex,
  enterprise-grade coding task (reported as 10 files / 474 lines), Google-internal AI
  in VS Code.
- **Found:** ~**21% less time** with AI assistance.
- **Actually establishes:** directionally, AI can speed up a realistic multi-file
  enterprise task. Full methodology not inspected for this file.
- **Limits:** single task; internal tooling; no downstream quality/stability follow-up
  reported in secondary coverage.
- **Verdict: Corroborated** (consistent with Cui et al.; methodology not independently
  verified here).

### 6. Microsoft — "Adoption and Impact of Command-Line AI Coding Agents" (arXiv, 2026)
- **Design:** observational study of Microsoft's early-2026 rollout of Claude Code and
  GitHub Copilot CLI; adopters vs non-adopters, four-month window, with a placebo-timing
  robustness check (pretending the rollout started earlier showed no jump).
- **Found:** **+24.0%** merged PRs/engineer/day (likely range +14.5% to +33.7%),
  sustained over four months; gains concentrated in regular users (5+ days/week: >50%
  lift vs ~15% at 3 days/week); Copilot CLI showed ~2.2× the PR lift of Claude Code in
  comparable weeks (authors warn against generalizing — Microsoft owns GitHub).
- **Actually establishes:** agentic CLI tools moved a concrete output metric at scale,
  with a dose-response relationship (more use → more PRs). The authors' own conclusion
  is the responsible one: the lift is "direct evidence that agentic command line tools
  can move a concrete output metric — though whether that output justifies its cost is a
  question of value, not throughput alone. The pressing open question is now about
  quality."
- **Limits:** not randomized (adopters self-select; "agents amplify productive
  developers"); PRs merged, not quality, customer impact, security, or maintainability;
  single company.
- **Verdict: Verified** (output metric moved); quality/value **Unknown**.

### 7. Accenture × GitHub enterprise RCT (2024)
- **Design:** randomized trial, ~450 developers with Copilot vs ~200 without.
- **Found (vendor-reported):** +8.69% PRs/developer, +15% PR merge rate, +84% successful
  builds; ~30% suggestion acceptance; 88% of generated characters retained in editor;
  95% enjoyed coding more.
- **Actually establishes:** direction — enterprise Copilot rollout raised output counts
  and build success off whatever baseline Accenture had.
- **Limits:** methodology not independently inspectable; reported by the vendor;
  the +84% builds figure likely reflects a low baseline and says little about value.
- **Verdict: Corroborated** (direction consistent with Cui et al.); magnitudes
  **Unverified** as independent measurements.

---

## Large-scale observational and benchmark studies

### 8. Uplevel Data Labs (Sept 2024) — ~800 developers, Copilot, test vs control
- **Design:** ~800 developers on large engineering teams; Copilot-access group vs
  control, matched on role/working days/coding volume; 3-month pre/post windows;
  metrics: PR cycle time, PR throughput, bug rate, extended hours.
- **Found:** **no significant change** in efficiency metrics (cycle-time delta: 1.7
  minutes — "inconsequential"); **+41% detected-bug rate** in the Copilot group.
- **Actually establishes:** in this population and era, Copilot did not move throughput
  or cycle time; the bug-rate correlation is the notable signal.
- **Limits:** explicitly correlational — Uplevel's own analyst: "It's obviously not a
  causal relationship… We just don't understand the why just yet." Bugs are *detected*
  bugs (detection effort may differ between groups). Vendor = engineering-metrics
  company.
- **Verdict: Corroborated** as counterevidence (null on throughput); the bug finding is
  **Inferred**, not causal.

### 9. DX — aggregate customer benchmarks and AI reports (2024–2026)
- **Design:** telemetry + surveys across DX's customer base (hundreds of companies).
- **Found:** AI code completion saves ~3.8 hrs/week; AI users ship **60% more PRs**;
  median PR throughput **+7.7%** (Nov 2024–Feb 2026), mean +13%, top performers ~70% —
  "nobody hit 2x, 5x, or 10x"; perceived rate of delivery +4.5% over a year ("modest
  return given the investment, and the new spend on AI"); deployment frequency rose then
  flattened; juniors use AI most (41.3% daily vs 32.7% staff) but seniors save more time
  per use; regional split (North America up, Europe pulled back).
- **Actually establishes:** the industry-wide *ceiling* looks like single-digit to
  low-double-digit throughput gains, with high variance — and perceived gains run ahead
  of measured ones.
- **Limits:** vendor customer base (selection); "AI users ship 60% more PRs" is
  cross-sectional (users differ from non-users).
- **Verdict: Corroborated.**

### 10. DORA 2024 (Google Cloud; ~39,000 professionals cited in secondary coverage)
- **Design:** annual survey-based research program; 2024 edition focused on AI.
- **Found:** every 25% increase in AI adoption associated with **−1.5% delivery
  throughput** and **−7.2% delivery stability**; 75% of developers *felt* more
  productive; only 24% had high trust in AI code.
- **Actually establishes:** the first large-scale signal that AI adoption and delivery
  performance could move in opposite directions — the origin of the "productivity
  paradox" framing.
- **Limits:** cross-sectional survey; effect sizes are modeled estimates, not
  experiments; "throughput −1.5%" is small and could reflect adjustment costs.
- **Verdict: Corroborated** (percentages via secondary sources citing the report;
  direction confirmed by the 2025 primary source).

### 11. DORA 2025 — "State of AI-assisted Software Development" (Google Cloud)
- **Design:** survey of ~5,000 technology professionals (Jun 13–Jul 21, 2025) + 100+
  hours of interviews; cluster analysis yielding seven team archetypes; new "DORA AI
  Capabilities Model" (seven capabilities).
- **Found (primary source, Google Cloud blog):** 90% use AI at work; >80% believe it
  raised their productivity; 30% have little/no trust in AI code. "Unlike last year, we
  observe a positive relationship between AI adoption on both software delivery
  throughput and product performance… However, AI adoption does continue to have a
  negative relationship with software delivery stability." Central theory: "AI
  accelerates software development, but that acceleration can expose weaknesses
  downstream… an increase in change volume leads to instability." Strongest moderator:
  user-centric focus amplifies AI's positive influence; without it, AI can hurt
  performance.
- **Actually establishes:** the throughput/stability *trade-off* as the central
  empirical regularity of the AI era, and that outcomes are conditional on pre-existing
  engineering discipline (platform quality, small batches, version control, fast
  feedback).
- **Limits:** still survey-based and cross-sectional; self-reported productivity and
  product performance; Google Cloud is a vendor with an interest in platform investment.
- **Verdict: Corroborated** (strongest available population-level evidence; not causal).

### 12. GitClear — longitudinal code-quality analyses (2024, 2025, 2026 cuts)
- **Design:** mining of code-change metrics across customer + OSS data (211M lines in
  the 2024 cut; 623M commits in the 2026 cut), tracking duplication, churn, refactoring,
  copy/paste over 2020–2026.
- **Found:** duplicated blocks +81%; within-commit copy/paste +41%; error-masking
  constructs +47%; 2-week churn +15%; cross-file function calls −35%; refactoring
  line-moves −70%; genuine-refactoring commit share 21%→<4%; 2024 first year
  copy/pasted lines exceeded moved lines; code volume up ~40%.
- **Actually establishes:** the *structural* signature of AI-era code: more code, more
  duplicated, less refactored, less maintained. Consistent across three annual cuts.
- **Limits:** correlational with AI adoption (temporal coincidence, not proof AI caused
  it); vendor = code-review tooling company; "moved lines" is a proxy for refactoring.
- **Verdict: Corroborated** (direction consistent across cuts and with independent
  quality studies).

### 13. Stack Overflow Developer Survey 2025 (~49,000 respondents)
- **Found:** 84% use or plan to use AI tools; trust in AI accuracy fell 40%→29%;
  46% actively distrust output; ~3% highly trust; top frustration "almost right, but
  not quite" (66%); 45% say debugging AI code takes more time than expected.
- **Actually establishes:** the trust inversion — adoption rising while trust falls —
  at the largest available sample size.
- **Limits:** self-reported; no productivity measurement.
- **Verdict: Corroborated.**

### 14. Engineering-intelligence benchmarks (LinearB, Faros AI, Cortex — vendor data via secondary reporting)
- **LinearB** (8.1M PRs, 4,800 orgs): AI PRs wait **4.6× longer** before review, are
  reviewed 2× faster once picked up, and are accepted at **32.7% vs 84.4%**.
- **Faros AI** (>10,000 developers): high AI adoption → **98% more PRs merged**,
  **91% more review time**; DORA-dataset analysis: incidents/PR **+242.7%** over two
  years (magnitude needs primary verification).
- **Cortex 2026** (50+ orgs, Q3 2024→Q3 2025): PRs/author +20% YoY, incidents/PR
  **+23.5%**, change failure **+~30%**.
- **Actually establish:** the review-burden and incident-cost side of the ledger, at
  scales no academic study reaches.
- **Limits:** vendor benchmarks via secondary reporting; methodologies not inspected;
  populations are vendor customers.
- **Verdict: Corroborated** (three independent vendors, same direction); exact
  magnitudes **Unverified**.

### 15. Leader/perception surveys (New Relic 2026, Lightrun 2026, Sonar, Harness, LaunchDarkly)
- **New Relic** (200 US tech decision-makers): 94% rate AI code higher quality *at
  review time*, yet 78% saw AI-tied incident spikes, 82% had ≥1 major AI-attributed
  production failure in six months, 74% said ≥25% of AI code needed significant
  post-deploy rework.
- **Lightrun** (200 SRE/DevOps leaders): 43% of AI changes needed manual production
  debugging after passing QA/staging; zero respondents could verify an AI fix in one
  redeploy cycle.
- **Sonar** (1,100+ devs): AI = 42% of committed code; 96% don't fully trust it;
  38% say reviewing it takes more effort than a colleague's.
- **Harness:** 67% spend more time debugging AI code. **LaunchDarkly** (767 engineers):
  94% accelerated coding, 91% low trust shipping it, 81% ship with unresolved risks.
- **Actually establish:** the review-time vs production-reality gap, and that delivery
  pressure is converting review queues into shipped risk.
- **Limits:** perception/recollection, not instrumentation; decision-maker samples skew
  toward larger orgs.
- **Verdict: Corroborated** (direction consistent across five independent surveys).

---

## Code-quality and security studies

### 16. Veracode GenAI Code Security Reports (2025; Summer 2026 retest)
- **Design:** 100+ LLMs across Java/JS/Python/C# (2025); 11 frontier models × 80
  coding tasks (Summer 2026).
- **Found:** 45% of AI-generated code contains an OWASP Top-10 vulnerability; 2.74×
  more vulns than human-written code (2025); average security pass rate only 56% in
  the 2026 retest — "barely improved" year over year.
- **Limits:** lab-generated code (no human review loop); vendor = security company.
- **Verdict: Corroborated** (two waves, same direction).

### 17. CodeRabbit — "State of AI vs Human Code Generation" (470 OSS PRs)
- **Found:** AI PRs ~10.83 issues vs 6.45 human (~1.7×); 1.4× more critical issues;
  1.75× logic/correctness, 1.64× maintainability, 1.57× security, 1.42× performance
  issues. Also: 80% of PRs get no human comments when AI review is enabled.
- **Limits:** vendor = AI code-review company (direct commercial interest in finding
  issues for its tool to catch); OSS PRs only.
- **Verdict: Corroborated** (direction matches GitClear, Uplevel, DORA stability
  findings); magnitudes vendor-measured.

### 18. Watanabe et al. — "On the Use of Agentic Coding" (arXiv 2509.14745; 567 Claude Code PRs, 157 OSS projects)
- **Found:** 83.8% of agent PRs eventually merged; only **54.9%** merged without
  further modification; 45.1% needed human revision (especially bug fixes, docs,
  project-specific standards). Agents used mostly for refactoring, docs, testing.
- **Actually establishes:** a measured human-intervention rate for agentic PRs in the
  wild: roughly half need a human touch after the agent is "done."
- **Limits:** OSS only; Claude Code only; merge ≠ value.
- **Verdict: Verified** (for its population).

### 19. Kraishan (2026) — "Not All Agents Are Equal" (arXiv 2609.17598; 37,623 agent PRs, 5 agents, 2,807 repos)
- **Design:** AIDev dataset + 58,792 cached GitHub API responses, Dec 2024–Jul 2025;
  security smells, maintainability, post-merge churn, revert rates, review behavior;
  matched human baseline; full replication data released.
- **Found:** quality is **vendor-specific**: Codex reverted 6.1% vs 11.5% human
  (OR 0.50); Devin reverted 14.5% (OR 1.31). Agent code pooled *less* likely to contain
  security smells than human code (OR 0.63). Review effort concentrates unevenly:
  Copilot PRs drew most human reviews/change requests; Claude Code PRs waited longest
  for first human review (median 12.6h).
- **Actually establishes:** the important counterevidence — "AI code is worse" is
  false as a blanket claim; it depends on the agent, the task, and whether a human
  reviewed it. Also the best measurement of review-effort concentration.
- **Limits:** observational; provenance labeling imperfect; OSS only.
- **Verdict: Verified** (strongest post-merge evidence available).

---

## Benchmark-validity note

### 20. SWE-bench Verified retired (OpenAI, Feb 2026)
- OpenAI retired SWE-bench Verified after finding **59.4% of audited problems had
  flawed test cases** plus pervasive training contamination; the same model scored
  80.9% on SWE-bench Verified but 45.9% on contamination-resistant SWE-bench Pro.
- **Implication for this workstream:** benchmark scores that underpin "agents can do
  X% of engineering work" claims overstated real-world capability by a wide margin.
  Any productivity argument built on benchmark scores rather than delivery metrics is
  **Unverified**.

---

## Frameworks: current state

### SPACE (Forsgren, Storey, Maddila, Zimmermann, Houck, Butler; ACM Queue, Feb 2021)
- **Plain English:** productivity is not one number. Measure five dimensions together —
  **S**atisfaction & well-being (do people have what they need, are they burning out?),
  **P**erformance (are outcomes reliable and high-quality?), **A**ctivity (counts: commits,
  PRs — useful context, dangerous alone), **C**ommunication & collaboration (does knowledge
  move?), **E**fficiency & flow (can people work uninterrupted?).
- **Concrete example:** a team merges 2× more PRs (Activity up) but reviewers burn out
  (Satisfaction down) and incidents rise (Performance down) — SPACE says productivity did
  *not* improve.
- **Deeper mechanics:** SPACE is deliberately non-prescriptive; its power is forcing
  multi-dimensional measurement so Goodhart's law doesn't eat you. The AI-era critique
  (e.g. Larridin 2026): Activity metrics are now inflated by generation volume while the
  quality signals SPACE doesn't natively track (churn, durability, review-queue depth)
  move the wrong way — teams need review throughput/queue time as first-class efficiency
  signals.
- **Current state:** still the standard academic lens; a 2025 arXiv systematization
  ("The Fast and Spurious") uses it to show GenAI studies cluster on Satisfaction/
  Performance/Efficiency while Communication and human-AI collaboration are underexplored.
  A 2025 systematic review (Mohamed) found ~64% of LLM-productivity studies exploratory,
  92% covering >1 SPACE dimension but only 14% covering >3.

### DX Core 4 (DX; Abi Noda; launched Aug 2024)
- **Plain English:** unifies DORA + SPACE + DevEx into four boardroom-legible dimensions:
  **Speed** (diffs/engineer, perceived delivery rate), **Effectiveness** (Developer
  Experience Index — 14-item friction survey), **Quality** (change failure rate),
  **Impact** (% time on new capabilities). Each dimension counterbalances the others so
  you can't "win" speed by sacrificing quality.
- **Concrete example:** diffs/engineer rises (Speed up) but change failure rises too
  (Quality down) and DXI falls (Effectiveness down) — the framework flags the trade,
  exactly the AI-era pattern.
- **Deeper mechanics:** built with the creators of DORA (Nicole Forsgren) and SPACE
  (Margaret-Anne Storey) advising; benchmark data across 500+ companies (e.g. top-quartile
  smaller tech orgs ~4.3 merged diffs/engineer/week).
- **Current state:** the most deployment-ready synthesis; its benchmarks are the source
  of the "median +7.7%, nobody hit 10x" figures.

### DORA (DevOps Research and Assessment; Google Cloud)
- **Plain English:** measures *delivery system* health with four (now five) system
  metrics: deployment frequency, lead time for changes, change fail rate, failed-deployment
  recovery time (+ deployment rework rate). It asks "how good is the machine?" not "how
  good is the engineer?"
- **Concrete example:** elite performers deploy on demand with <1hr lead time and <15%
  change failure; the 2025 AI edition replaced the elite-to-low ladder with seven team
  archetypes because "fast and fragile" teams were being flattened into the same bucket
  as "fast and durable" ones.
- **Current state:** the 2025 "State of AI-assisted Software Development" edition is the
  authoritative population-level source on AI's delivery impact (see study 11).

### Value-stream mapping (VSM)
- **Plain English:** draw every step from customer request to customer value, and for
  each step record *work time* and *wait time*. The ratio (flow efficiency) tells you
  where the delay lives.
- **Concrete example:** Idea →(wait 12d)→ Analysis 2d →(wait 5d)→ Development 4d
  →(wait 6d)→ Review 0.5d →(wait 9d)→ Test 1d →(wait 14d)→ Production. Work = 7.5 days,
  elapsed = 53.5 days, flow efficiency ≈ 14%. Hiring developers shortens the 4-day box;
  removing queues shortens everything else — which is where the delay lives.
- **Deeper mechanics:** VSM converts waste into cost (excess lead time × team cost/day)
  and links directly to DORA metrics (lead time, deployment frequency, change failure).
  DORA 2025 explicitly recommends it for AI-adopting teams.
- **Current state:** the recommended diagnostic, but no published AI-era VSM with
  before/after waiting-time decomposition was found — the central measurement gap.

### Cost per verified result
- **Plain English:** the fully loaded cost of one unit of output that actually works in
  production — inference + licenses + human spec/review/test/debug/fix time + the
  amortized cost of defects that escape.
- **Concrete example:** a $20/month seat that "saves" 4 coding hours but adds 6 hours
  of review, rework, and incident response has a *negative* return at any engineer
  salary — the seat price is irrelevant next to the verification labor.
- **Current state:** **Unknown.** Nobody publishes it. The Larridin 2026 spend report
  proposes the right shape (diminishing-returns curve: healthy ROI → inflection point →
  "tokenmaxxing" where spend rises and output stays flat), but it is a vendor framework,
  not a measurement.

---

## What the evidence does NOT support

1. **"AI makes developers 2×/10× more productive."** The controlled range is −19% to
   +56%, and the +56% is a toy task. Industry aggregates top out around +7–26% on
   *output counts*. Nobody credible has measured 2× on delivery.
2. **"Throughput gains = business value."** No study connects AI adoption to customer
   outcomes, revenue, or even cost-per-verified-result. The Microsoft 2026 authors say
   this explicitly.
3. **"AI code is uniformly worse (or better)."** Kraishan 2026 shows vendor- and
   task-specific quality; Veracode shows lab security weakness; both can be true.
4. **"Faster coding = faster delivery."** DORA (2 years), Cortex, Faros, LinearB, and
   the branch-throughput divergence all say the constraint moved downstream.
5. **Any vendor ROI claim.** Break-even sketches ignore verification labor; treat all
   as Unverified unless independently corroborated with inspectable methodology.
6. **Self-reported productivity as evidence.** METR's 39-point perception gap, DX's
   perceived-vs-measured divergence, and New Relic's review-time-vs-incidents gap all
   show felt speed is not measured speed.

## The honest bottom line

The evidence supports three statements with confidence: (a) AI raises *artifact*
throughput in most settings, roughly +8–26% in field studies; (b) it shifts the
bottleneck downstream into review, testing, integration, and operations, with stability
falling as throughput rises; (c) nobody can currently tell you what it does to business
value, because the two metrics that would answer — cost per verified result and user
outcomes — have no public measurements. Everything else is directionally consistent but
causally thin.
