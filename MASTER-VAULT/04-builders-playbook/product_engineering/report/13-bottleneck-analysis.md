# 13 — Automation Economics & Bottleneck Analysis

**Status:** report section; read-only synthesis, not adoption advice. **Source:** the economics workstream (2026-10-10) — `research/economics/01-delivery-economics.md` (12 measured dimensions), `02-bottleneck-analysis.md` (constraint migration), `03-productivity-evidence-review.md` (20 studies, frameworks). Claim labels preserved exactly as assigned by the research (**Verified / Corroborated / Inferred / Proposed / Unknown**); nothing here is upgraded. Full study-by-study detail lives in `research/economics/03-productivity-evidence-review.md`.

---

## The one-sentence economics

AI has made the cheapest step of software delivery (writing code) cheaper, while making the expensive steps (specifying, verifying, reviewing, securing, integrating, operating) a larger share of total cost — and the two steps the business actually pays for, **cost per verified result** and **user outcomes**, have no public measurements at all (**Unknown**).

## Reading guide for the labels

- **Verified** — measured by a controlled or pre-registered design with inspectable methods (e.g. a published RCT).
- **Corroborated** — reported by independent sources with consistent direction, but not from a controlled design.
- **Inferred** — a reasonable reading of the data, not directly measured by anyone.
- **Proposed** — an argument or framework offered by a practitioner or vendor, not yet measured.
- **Unknown** — nobody has published a measurement.

Global caveat (**Corroborated**): nearly all AI-era evidence measures *output proxies* (PRs merged, tasks completed, lines of code) rather than *business value* (revenue impact, customer outcomes). Do not equate generated code, completed agent tasks, or perceived productivity with actual business value.

---

## 1. The 12 delivery dimensions, condensed

| # | Dimension | What the evidence says | Verdict |
|---|---|---|---|
| 1 | **Active work time** | Mixed by task type: −19% for experts in mature codebases (METR), +55% on a toy greenfield task (Peng 2023), +26% task completion in enterprise (Cui et al.). No study measures it as a share of the full value stream. | Verified (task-level) |
| 2 | **Waiting time** | Baseline flow efficiency ~5–20% of elapsed time is waiting (**Corroborated**, lean literature); AI-era totals unmeasured, but every proxy (review queues, PR wait, CI backlogs) moves the wrong way. | Inferred / Unknown |
| 3 | **Queue lengths** | No published before/after queue-depth series. Proxies: AI users ship ~60% more PRs (DX), review capacity hasn't grown; AI PRs wait 4.6× longer pre-review (LinearB). | Inferred |
| 4 | **Rework** | Up: code churn +~15% (GitClear); AI-PR acceptance 32.7% vs 84.4% (LinearB); 45.1% of merged agent PRs needed human modification (Watanabe). Twist: Codex PRs reverted *less* than human (Kraishan) — vendor-specific, not uniform. | Corroborated |
| 5 | **Review burden** | Up sharply: review time +91% where AI adoption high, PRs +98% merged (Faros AI); 38% say reviewing AI code costs more effort than a colleague's (Sonar); human-review coverage fell 89%→68% in one tracked company. | Corroborated |
| 6 | **First-pass success** | No published industry rate with a pre-AI baseline. Proxies point down: main-branch success ~70.8%, a five-year low (single secondary source, unverified); only 54.9% of Claude Code PRs landed unmodified. | Inferred / Unknown |
| 7 | **Failure & recovery** | Failures up: incidents/PR +23.5% YoY, change failure +~30% (Cortex); DORA: AI adoption's relationship with stability negative two years running. MTTR under AI adoption unmeasured. | Corroborated / Unknown |
| 8 | **Delivery throughput** | Artifact throughput up ~8–26% in field studies (Cui et al. +26.08%; Microsoft CLI study +24.0%). DX: median +7.7% PR throughput — "nobody hit 2x, 5x, or 10x." Value-throughput unmeasured. | Verified (output only) |
| 9 | **Product quality** | Structural decay: duplication +81%, refactoring 21%→<4% of commits (GitClear); defect signals up (CodeRabbit ~1.7× more issues in AI PRs). Security mixed: lab code weak (Veracode 45% OWASP Top-10), reviewed in-the-wild agent code *better* than human on smells (Kraishan, OR 0.63). | Corroborated |
| 10 | **Human intervention** | High and uneven: 45.1% of agent PRs revised post-merge; 39% of agent-presented plans rejected (Anthropic). Approaches zero only for fully standardised maintenance (Spotify: 2.5M PRs auto-merged, dependency/patch work). | Corroborated |
| 11 | **Cost per verified result** | No direct measurement exists anywhere. All public cost discussion covers inputs (seat pricing, token prices), never cost per change that survives 30 days in production without incident. | Unknown |
| 12 | **User outcomes** | No study connects AI coding adoption to customer-facing outcomes (satisfaction, retention, SLA attainment) with any control. Adjacent negatives: stability falls; adjacent positives: self-reported product performance rises. | Unknown |

**Net reading:** output goes up (8), everything around verification and stability goes down or is unmeasured (2–7, 9), humans intervene heavily (10), and the two metrics that would settle the business case don't exist (11–12). This is not an argument against AI tooling; it is an argument that the *bottleneck moved*.

---

## 2. The bottleneck shift: coding was ~15% of lead time

**Plain English:** value-stream maps consistently show customer lead time is ~85% waiting and ~15% active work — and of that active work, only a fraction is writing code. AI compressed the one step that was already small and cheap.

### Stage by stage: what AI did to each, and where the queue formed

| Stage | Plain English | Effect of AI | Bottleneck status |
|---|---|---|---|
| **Specification** | Turning a need into a description code can be built against | Barely touched (**Inferred**): DORA 2025 found AI is used least for requirements analysis, planning, architecture. As generation gets cheap, precise specification *rises* in value. | Unchanged or relatively more binding — errors get amplified into code faster (Amazon logistics incident, Mar 2026: an AI change following an outdated wiki corrupted delivery estimates for 6.3M orders in six hours — the code compiled and passed tests). |
| **Implementation** | The typing-and-thinking step | The one step AI directly accelerates: +55% toy task (Peng, Verified w/ caveat); +26% enterprise tasks (Cui, Verified); −19% for experts in mature codebases (METR, Verified); +24% merged PRs with agentic CLIs (Microsoft 2026, Verified). | **Removed** as the binding constraint for most teams. Devaland's 91-day measurement: programming estimates "too high by a factor of tens" — a "two focused days" task took 10 minutes of actual programming; the days were spent on sign-offs, acceptance, verification. |
| **Review** | Human or automated checking before merge | **The best-documented shift** (**Corroborated**): see §3. | **The new binding constraint** for most AI-adopting teams. |
| **Testing & integration** | CI pipelines, merging without conflicts | "AI produces pull requests faster than CI pipelines can process them" — dozens of PRs/day became hundreds, testing backlogs lasting days (**Corroborated**); incidents/PR +23.5% (Cortex); main-branch success 70.8%, a five-year low (single secondary, unverified). | Binding wherever test automation lags generation speed. |
| **Security & compliance** | Vulnerability scanning, security review, policy gates | Mixed: 45% of AI-generated code with an OWASP Top-10 issue (Veracode, Corroborated); but agent PRs in the wild *less* likely to contain security smells than human PRs (Kraishan, OR 0.63, Verified) — lab code and reviewed agent PRs are different populations. | Binding as a *risk* bottleneck even where it isn't a *time* bottleneck — 81% ship with unresolved risks (LaunchDarkly). |
| **Deployment & operation** | Release, monitoring, incident response, maintenance | Incidents per PR rising (+23.5% YoY, Cortex, Corroborated); 78% of leaders saw AI-tied incident spikes (New Relic, Corroborated); 43% of AI changes needed manual production debugging after passing QA (Lightrun, Corroborated). Maintenance compounding: refactoring share 21%→<4% (GitClear, Corroborated). | The *deferred* bottleneck — costs arrive quarters later as incidents and maintenance load. |

### Baseline comparison table (directional, not controlled)

| Stage metric | Pre-AI baseline | AI-era reading | Source class |
|---|---|---|---|
| Code review time | Baseline | +91% where AI adoption high | Vendor benchmark (Faros AI) |
| PR size | Baseline | +154% | Secondary reporting |
| PR acceptance (AI vs human) | 84.4% human | 32.7% AI-generated | Vendor benchmark (LinearB) |
| Time to first review (AI PRs) | — | 4.6× longer wait; 12.6h median (Claude Code) | Vendor / academic |
| Change failure rate | Baseline | +~30% YoY | Vendor benchmark (Cortex) |
| Incidents per PR | Baseline | +23.5% YoY | Vendor benchmark (Cortex) |
| Delivery stability (DORA) | Baseline | Negative relationship with AI adoption, 2 yrs running | Primary technical (DORA) |
| Delivery throughput (DORA) | Baseline | Negative (2024) → positive (2025) | Primary technical (DORA) |
| Refactoring share of changes | ~21% (2022) | <4% (2026) | Primary technical (GitClear) |
| Code duplication | 40/1M lines | 73/1M lines (+81%) | Primary technical (GitClear) |
| Human review coverage of AI PRs | 89% | 68% (one tracked company) | Secondary |
| Main-branch success rate | ~90% benchmark | 70.8% (five-year low) | Single secondary — unverified |

**Reading note:** baselines are rarely from the same population as the AI-era reading. Treat the table as directionally consistent evidence, not a controlled before/after.

---

## 3. Review is the binding constraint

**The finding (Corroborated):** review is the single best-documented bottleneck shift in the AI era.

- **Volume without capacity:** where AI adoption was high, developers merged 98% more PRs while review time rose 91% (Faros AI).
- **The wait:** AI PRs wait **4.6× longer** before first review (LinearB, 8.1M PRs); Claude Code PRs wait a median **12.6h** for first human review (Kraishan).
- **The difficulty:** PRs are 154% larger; 38% of developers say reviewing AI code takes *more* effort than a colleague's (Sonar); 45% say debugging AI code takes more time than expected (Stack Overflow 2025).
- **The coverage slide:** human-review coverage of AI PRs fell 89%→68% in one tracked company; ~90% of large changes ship with no formal review (CodePulse/BigQuery analysis).
- **The judgment asymmetry:** users reject 3% of individual agent commands but **39% of presented plans** (Anthropic) — humans are bad at step-checking, decent at direction-judging.
- **The counterweight:** Microsoft's AI code-review assistant touches >90% of PRs with 10–20% faster completion — AI review tooling shifts some burden off humans, with the caveat that 80% of PRs get no human comments when AI review is enabled (CodeRabbit).

**Structural reason (Inferred):** verification scales with *output volume × output unfamiliarity*. AI increases both simultaneously — more code, written by no one, in styles the reviewer didn't choose. Review is cognitively harder than writing for the same change, and AI widened the gap between the two.

---

## 4. The productivity-evidence critique, condensed

Seven studies, highest signal first. Full methodology notes in `research/economics/03-productivity-evidence-review.md`.

| Study | Design | Found | Verdict | The caveat |
|---|---|---|---|---|
| **METR RCT (2025)** | Pre-registered RCT, n=16 experienced OSS developers, 246 real issues on >1M-line repos | AI-allowed tasks took **19% longer**; developers *believed* they were 20% faster (39-point perception gap) | Verified (for its population) | Pre-agentic tooling; experts + mature codebases — does not generalise to juniors or greenfield |
| **DORA 2025** | Survey ~5,000 professionals + 100h interviews | Throughput sign flips positive vs 2024, but AI adoption's relationship with **stability stays negative** — "speed without stability is accelerated chaos" | Corroborated (strongest population-level evidence) | Cross-sectional survey; self-reported performance |
| **Cui et al. (2025)** | 3 field RCTs (Microsoft, Accenture, Fortune 100), n=4,867, postregistered | **+26.08% (SE 10.3%)** more completed tasks with Copilot; juniors gained most | Verified (output rose) | Task *counts*, not value; 2022–23-era tooling; Microsoft/GitHub-affiliated authors |
| **Uplevel (2024)** | ~800 developers, test vs control, 3-month windows | **No significant change** in cycle time or throughput (delta: 1.7 minutes — "inconsequential"); +41% *detected*-bug rate | Corroborated (null on throughput); bug finding Inferred | Explicitly correlational — their own analyst: "it's obviously not a causal relationship" |
| **GitClear (2024–2026 cuts)** | Longitudinal mining (211M lines → 623M commits) | Duplication +81%, refactoring line-moves −70%, genuine-refactor commits 21%→<4% | Corroborated (three consistent cuts) | Correlational with AI adoption; vendor = code-review tooling |
| **DX aggregates (2025–26)** | Telemetry + surveys across hundreds of companies | Median **+7.7%** PR throughput; "nobody hit 2x, 5x, or 10x"; perceived delivery +4.5% over a year ("modest return given the investment") | Corroborated | Vendor customer base; cross-sectional elements |
| **Peng et al. (2023)** | RCT, n=95, one task: write a JS HTTP server from scratch | **55% faster** with Copilot (1h11m vs 2h41m) | Verified *for the lab task only* | **The toy-task caveat:** vendor-authored (GitHub employees); no maintenance, integration, review, or legacy-context phase — it measures exactly the slice of work AI helps most and excludes every slice where the costs moved. The most-cited number in enterprise AI is also the least representative of enterprise work. |

**Framework note (research, not ranking):** the three lenses most useful for AI-era measurement are **SPACE** (productivity is five dimensions — Satisfaction, Performance, Activity, Communication, Efficiency — so Activity gains can't mask Performance losses), **DX Core 4** (Speed/Effectiveness/Quality/Impact as counterbalanced dimensions; source of the "median +7.7%" figures), and **value-stream mapping** (work-time vs wait-time per stage — the recommended diagnostic, and DORA 2025's explicit recommendation for AI-adopting teams).

---

## 5. When the bottleneck does NOT shift: the amplifier finding

DORA 2025's most important result is a **moderator**, not a main effect (**Corroborated**): AI amplifies the system it lands in — "strong teams get faster, struggling teams get faster at producing mess." The seven capabilities that flip AI from harm to help are all *pre-existing engineering disciplines*: clear AI stance, healthy data ecosystem, AI-accessible internal data, strong version control, small batches, user-centric focus, quality internal platforms.

- Small batches + fast feedback + strong tests → the extra volume flows through without destabilising (Microsoft's internal AI code review).
- Standardised, low-judgment work → near-zero human intervention is achievable (Spotify: 2.5M maintenance PRs auto-merged over 18 months, humans on exceptions only).
- Mature codebases + expert developers → AI can slow the work down (METR); gains concentrate in greenfield, boilerplate, and less-experienced developers.

**The honest summary:** AI removes the implementation bottleneck and promotes the verification bottleneck. Teams that had already industrialised verification (tests, review discipline, platforms, small batches) capture the gain. Teams that had not get faster at generating the rework, incidents, and technical debt they were already producing — "accelerated chaos."

---

## 6. What the evidence does NOT support

1. **"AI makes developers 2×/10× more productive."** The controlled range is −19% to +56% (the +56% being a toy task); industry aggregates top out around +7–26% on output *counts*.
2. **"Throughput gains = business value."** No study connects AI adoption to customer outcomes, revenue, or cost per verified result — the Microsoft 2026 authors say this explicitly.
3. **"AI code is uniformly worse (or better)."** Kraishan 2026 shows vendor- and task-specific quality; Veracode shows lab security weakness; both can be true of different populations.
4. **"Faster coding = faster delivery."** DORA (2 years), Cortex, Faros, LinearB, and the branch-throughput divergence all say the constraint moved downstream.
5. **Any vendor ROI claim.** Break-even sketches ignore verification labor; treat all as Unverified unless independently corroborated with inspectable methodology.
6. **Self-reported productivity as evidence.** METR's 39-point perception gap, DX's perceived-vs-measured divergence, and New Relic's review-time-vs-incidents gap all show felt speed is not measured speed.
7. **Benchmark scores as delivery evidence.** SWE-bench Verified was retired by OpenAI (Feb 2026) after 59.4% of audited problems were found to have flawed test cases; any "agents can do X% of engineering work" claim built on benchmark scores is **Unverified**.

## The unmeasured unknowns (the empirical debt)

- **Cost per verified result** (Unknown) — fully loaded inference + license + human spec/review/test/debug/fix cost per change that survives 30 days in production. Nobody publishes it.
- **User outcomes** (Unknown) — customer satisfaction, retention, SLA attainment connected to AI adoption with any control.
- **Aggregate waiting time** (Unknown) — no published AI-era value-stream map with a before/after waiting-time decomposition.
- **First-pass success** (Inferred/Unknown) — no pre-registered industry rate for AI-assisted changes with a pre-AI baseline.
- **Spec quality under AI adoption** (Unknown) — the stage whose importance *rises* as generation gets cheaper has no published measurement.
- **Recovery time (MTTR)** (Unknown) — no controlled study of recovery under AI adoption.

---

**Sources:** `research/economics/01-delivery-economics.md` · `research/economics/02-bottleneck-analysis.md` · `research/economics/03-productivity-evidence-review.md` · `research/economics/04-evidence-register.md`
