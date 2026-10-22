# 18 — Evidence Register (Report Section)

**Status:** report section; read-only synthesis, not adoption advice. **Source:** all 20 workstreams' evidence registers (`research/<stream>/*-evidence-register.md`). Claim labels preserved exactly as assigned by the research (**Verified / Corroborated / Inferred / Proposed / Unknown**); nothing here is upgraded. The *full merged register* — every finding with per-finding metadata — is being assembled by a sibling agent as `evidence/merged-evidence-register.md`; this section is the report-level reading guide, the load-bearing shortlist, and the honest gaps.

---

## 1. How to read the evidence labels

### The five claim labels

| Label | Definition | What it means for you |
|---|---|---|
| **Verified** | Measured by a controlled or pre-registered design with inspectable methods (e.g. a published RCT), or confirmed by an authoritative primary source (official docs, company RCA, primary legal text) | The strongest claims in this report. Still check the population: "Verified" is always *verified for a population*, not universal. |
| **Corroborated** | Reported by independent sources with consistent direction, but not from a controlled design | Direction is trustworthy; exact magnitudes usually aren't. Two corroborated claims from different *source classes* (academic + vendor + practitioner) beat three from one class. |
| **Inferred** | A reasonable reading of the data, not directly measured by anyone | Plausible, load-bearing only when no one has measured the thing directly. Treat as the best current interpretation, not a fact. |
| **Proposed** | An argument, framework, or synthesis offered by a practitioner, vendor, or this report's researchers — not yet measured | A candidate worth testing, not a finding. §16 (roadmap) is Proposed throughout for exactly this reason. |
| **Unknown** | Nobody has published a measurement | The honest answer. An Unknown is never a pass, never a block — it is a named research debt. §3 lists the 15 that matter most. |

**Preservation rule (project-wide):** claim labels are never upgraded in synthesis. If a finding was Corroborated in the research, it is Corroborated here — even when it appears alongside Verified findings.

### The six evidence classes

| Class | What it is | Typical example in this report |
|---|---|---|
| **Primary technical** | Paper, published report with methodology, official documentation | METR RCT (arXiv 2507.09089); DORA reports; OWASP ASVS; GitHub Docs |
| **First-hand practitioner** | A company describing its own measured work | GitLab's 2017 postmortem; Spotify's fleet-management PR system; Anthropic's agent-building essays |
| **Corroborating** | Independent source consistent with the claim | A second vendor benchmark showing the same review-burden direction |
| **Community observations** | Aggregated practitioner reports without controls | Lean value-stream flow-efficiency figures; HN practitioner consensus on async failure modes |
| **Secondary interpretation** | Press/vendor write-ups of someone else's study | News coverage of DORA percentages; practitioner summaries of Temporal docs |
| **Unverified** | Single-source claims, figures needing primary verification | Faros.ai's 242.7% incident magnitude; single-secondary main-branch success rates |

**Terminology inconsistency (flagged, not fixed):** the automation stream (`research/automation/01-automation-stack.md`) uses a different evidence-class vocabulary — `official-docs`, `eng-blog`, `paper`, `repo`, `practitioner`, `forum`, `standard`, `mirror` — while the economics and rules streams use the six classes above. The mapping is approximately: `paper` ≈ primary technical, `eng-blog` ≈ first-hand practitioner, `repo`/`standard` ≈ primary technical, `practitioner`/`forum` ≈ community observations, `mirror` ≈ secondary interpretation. The per-stream registers keep their original vocabulary; this section and the merged register normalise to the six classes. Also note: streams differ slightly in what "Verified" requires (automation: "read directly in the primary source"; economics: "controlled or pre-registered design"). Where a finding's label depends on the stricter reading, the finding line below names the design explicitly so you can judge.

---

## 2. Load-bearing evidence: the ~40 highest-confidence findings

One line each: the claim, its label, and the primary source. These are the findings the rest of the report stands on.

**Delivery economics & productivity (§13)**
1. Expert developers on large, familiar codebases took **19% longer** with AI assistance allowed — and believed afterward they had been 20% faster (39-point perception gap). **Verified** · METR RCT, arXiv 2507.09089, pre-registered, n=16, 246 real issues.
2. Three field RCTs (Microsoft, Accenture, Fortune 100, n=4,867) found **+26.08% (SE 10.3%)** more *completed tasks* with Copilot access; juniors gained most. **Verified** (output counts; value Unknown) · Cui et al., MIT Economics draft, postregistered AEARCTR-0014530.
3. Copilot users finished a greenfield HTTP-server task **55% faster** (1h11m vs 2h41m). **Verified for the lab task only** · Peng et al. 2023, ACM — vendor-authored, no maintenance/integration/review phase; does not generalise to delivery.
4. A Google internal RCT (n=96 engineers, complex multi-file enterprise task) found **~21% less time** with AI assistance. **Corroborated** · Paradis et al. 2025 (full methodology not inspected in this pass).
5. Agentic CLI tools raised merged PRs/engineer/day **+24.0%** over four months, dose-dependent. **Verified** (output metric; quality/value Unknown) · Microsoft 2026, arXiv, with placebo-timing robustness check.
6. ~800 developers, Copilot test vs control: **no significant change** in PR cycle time or throughput (delta: 1.7 minutes — "inconsequential"). **Corroborated** (null on throughput) · Uplevel Data Labs 2024 — explicitly correlational per their own analyst.
7. Industry-wide median **+7.7%** PR throughput with AI adoption; "nobody hit 2x, 5x, or 10x." **Corroborated** · DX 2025–26 aggregates, hundreds of companies.
8. DORA 2025: AI adoption's relationship with delivery **throughput flips positive** vs 2024, but the relationship with **stability stays negative** — "speed without stability is accelerated chaos." **Corroborated** (strongest population-level evidence; survey-based) · Google Cloud, ~5,000 professionals + 100h interviews.
9. Code duplication **+81%**, refactoring line-moves **−70%**, genuine-refactoring commit share **21%→<4%** — consistent across three annual cuts. **Corroborated** · GitClear 2024–2026 (211M lines → 623M commits).
10. AI PRs wait **4.6× longer** before first review and are accepted at **32.7% vs 84.4%** for human PRs. **Corroborated** · LinearB benchmark, 8.1M PRs, 4,800 orgs.
11. Where AI adoption was high: **98% more PRs merged, 91% more review time**. **Corroborated** · Faros AI, >10,000 developers.
12. PRs/author **+20% YoY** while incidents/PR **+23.5%** and change failure **+~30%**. **Corroborated** · Cortex 2026 benchmark, 50+ orgs.
13. **45.1%** of merged Claude Code PRs required further human modification. **Verified** (for its population) · Watanabe et al., arXiv 2509.14745, 567 PRs, 157 OSS projects.
14. Agent code pooled across vendors was **less likely** than human code to contain a security smell (OR 0.63); Codex PRs reverted 6.1% vs 11.5% human, Devin 14.5% — quality is **vendor- and task-specific**. **Verified** · Kraishan 2026, arXiv 2609.17598, 37,623 agent PRs, replication data released.
15. **45%** of AI-generated code contains an OWASP Top-10 vulnerability; 2.74× more vulns than human-written code (2025); 56% average security pass rate in the 2026 retest. **Corroborated** (two waves, same direction) · Veracode — lab-generated code, no human review loop.
16. ~40% of Copilot completions vulnerable across CWE scenarios (replication ~27%). **Verified** · Pearce et al.
17. AI-assisted developers wrote **less secure code while believing it more secure**. **Verified** · Perry et al. — the confidence-inflation mechanism behind R-13/R-20.
18. OpenAI retired SWE-bench Verified after **59.4% of audited problems** were found to have flawed test cases; the same model scored 80.9% on SWE-bench Verified vs 45.9% on contamination-resistant SWE-bench Pro. **Verified** · OpenAI, Feb 2026 — benchmark-score productivity arguments are Unverified.

**Rules, incidents & canonical practice (§14)**
19. Knight Capital: a manual partial deploy plus a repurposed dead-code flag executed ~4M bad trades in 45 minutes; no kill switch, no effective risk limit. **Verified** · SEC findings/company disclosures.
20. CrowdStrike: a missing non-wildcard test for the 21st field let a content bug past "multiple layers" of testing; staged deployment listed as a required fix. **Verified** · company RCA.
21. GitLab 2017: 300GB deleted; silent pg_dump failures; backup-failure alerts eaten by DMARC; 18-hour restore from a lucky snapshot. **Verified** · public postmortem.
22. DORA elite performers: on-demand deploys, <1-day lead time, ~5% change-fail, <1-hour recovery — speed and stability rising together. **Verified** · DORA/Accelerate.
23. The four golden signals (latency, traffic, errors, saturation); alert on symptoms, page only on actionable; error budgets mediate feature-vs-reliability work. **Verified** · Google SRE book.
24. Build, release, and run as distinct stages with immutable artefacts; config in the environment; logs as event streams. **Verified** · Twelve-Factor App.
25. Source control, one-step build, daily builds (modernised to CI); hallway usability testing. **Verified** · Joel Test (Spolsky).
26. ASVS: three cumulative security levels; Level 1 is the automatable baseline designed so there is no cost excuse. **Verified** · OWASP ASVS v4.0.3/v5.0.0.
27. Companies that "live and die by outputs" ship features to schedules rather than customer needs — the build trap. **Verified** · Perri, *Escaping the Build Trap*.
28. Progress is validated learning against metrics, not lines shipped; metrics defined after launch get chosen to flatter the launch. **Corroborated** · Ries, Lean Startup (innovation accounting, pivot/persevere).
29. Fixed appetite, flexible scope; overrun work dies via circuit breaker rather than borrowing next cycle's budget. **Verified** · Shape Up (Basecamp).
30. Writing the launch artefact (PR/FAQ) before design forces customer language, pricing, and tradeoffs to be confronted early. **Verified for mechanics, Corroborated for efficacy** · Amazon Working Backwards (Bezos 2004 email).
31. Five users find most usability issues per iteration. **Corroborated** · Nielsen (long-standing practitioner finding, industry-wide).
32. Weekly customer contact by the team building the product beats quarterly research projects; value/usability/feasibility/viability risks retired explicitly. **Corroborated** · Torres (*Continuous Discovery Habits*); Cagan (four risks), SVPG.
33. ~42% of startup postmortems cite "no market need" as the top cause of failure. **Corroborated** · CB Insights (self-reported postmortem data; founders may misattribute).
34. ≥40% "very disappointed" on the Sean Ellis question marks product-market fit. **Corroborated** · Sean Ellis benchmark via Superhuman (First Round Review, 2018) — a heuristic from venture-backed SaaS, not a law.

**Automation, agents & architecture (§15, automation stream)**
35. Start with the simplest pattern; workflows (LLM steps on predefined paths) where the path is known, agents only where it isn't; a well-designed single agent beats premature multi-agent. **Verified** · Anthropic, "Building Effective Agents," Dec 2024.
36. Multi-agent research cut research time up to 90% at **~15× the token cost** of chat; ~20K tokens overhead per subagent invocation. **Corroborated** (vendor-published; independent replication not found) · Anthropic multi-agent research system.
37. Parallel subagents make implicit, conflicting choices about style, edge cases, and code patterns; "multiple agents contribute intelligence to a task while writes stay single-threaded." **Verified** · Cognition (Devin team), Jun 2025.
38. Prompt injection (OWASP LLM01) has **no reliable fix**; it topped the LLM Top 10 in both 2023 and 2025. **Corroborated** · OWASP Top 10 for LLM Applications 2025. (The 2026 edition, released 3 Aug 2026, supersedes 2025 with renumbered entries — see §10 for current authoritative versions.)
39. Durable execution via event-history replay; dedup keys stop *resubmission*, idempotent code stops *double side effects*. **Verified** · Temporal docs.
40. GitHub Actions environments: required reviewers (prevent self-review), wait timers, deployment branch rules, environment-scoped secrets. **Verified** · GitHub Docs.
41. Teams that split mid-size SaaS apps into microservices and reverted report feature time 1–3 days → 5–12 days, deploys/week 12 → 3, costs up 10–20×; "extract on pain, not fashion." **Corroborated** (first-hand practitioner accounts) · spec-arch stream — the 73%-failure statistic sometimes cited is Unverified.
42. Organisations spend **55–80%** of IT budgets maintaining existing systems (Gartner); **60–80%** of total lifecycle cost is maintenance (IEEE). **Corroborated** (decades-convergent, secondary) · gaps stream — AI-era maintenance cost itself is Unknown.
43. Workers 22–25 in the most AI-exposed occupations saw **~16% relative employment decline**; software developers 22–25 ~20% below the late-2022 peak — adjustment through headcount, not pay. **Corroborated** (ADP payroll records via six outlets; AI causation is the authors' interpretation) · Stanford "Canaries in the Coal Mine" via gaps stream.
44. The FTC's Consumer Reviews and Testimonials Rule (16 CFR Part 465, effective Oct 2024) bans fake reviews/testimonials *whether generated by humans or AI*, at up to ~$53,088 per violation. **Verified** (rule and penalty figure) · FTC via gaps stream; 2026 first-actions reporting Corroborated (no FTC primary fetched).

---

## 3. Unresolved questions: the top 15 (deduped across all streams)

These are the honest gaps — each appears in at least one workstream's gaps section. No claim here is promoted above what the research supports.

1. **Cost per verified result** — the fully loaded cost of one change that survives 30 days in production without incident. No organisation publishes it. (economics — Unknown)
2. **User outcomes** — no study connects AI coding adoption to customer-facing outcomes (satisfaction, retention, SLA attainment) with any control. (economics — Unknown)
3. **AI-era aggregate waiting time** — no published value-stream map with a before/after waiting-time decomposition. (economics — Unknown)
4. **Spec quality and spec time under AI adoption** — the stage whose importance *rises* as generation gets cheap has no published measurement. (economics — Unknown)
5. **Recovery time (MTTR) under AI adoption** — no controlled study found. (economics — Unknown)
6. **First-pass success rate** — no pre-registered industry rate for AI-assisted changes with a pre-AI baseline. (economics — Inferred/Unknown)
7. **Internal defect and security rates of AI-generated code at the hyperscalers** — "the most important unanswered question in the set"; unknown at all five companies studied. (cases-hyperscale — Unknown)
8. **Whether AI-adoption mandates produce outcomes or gaming** — the Meta tokenmaxxing arc suggests gaming; formally Unknown. (gaps T3 — Unknown)
9. **Whether Anthropic's multi-agent figures (90.2% lift, ~15× token cost) replicate** outside their internal eval — vendor-published, uncorroborated by independent replication. (automation — Corroborated-low)
10. **AI-era maintenance cost as a measured number** — the classic 55–80% figures are Corroborated, but the AI-era tail is Inferred from structural code metrics (GitClear, correlational) and Unknown as a measured cost. (gaps T9)
11. **The causal effect of any single test-type mix on escaped defects** — no controlled experiment; the test-pyramid critiques are principled practitioner arguments, not trials. (build-ship — Unknown)
12. **The precise team-size threshold where microservices pay off** — accounts vary (11-engineer team regretted it; 18-engineer startup succeeded with 2 services); team size is a proxy for deploy contention, scaling-profile divergence, and operational maturity. (spec-arch — Unknown)
13. **Assistant-vendor internals** — no vendor publishes per-feature inference costs, full golden datasets, judge prompts, or training-data composition; no AI-quality SLO published (only uptime SLAs). (domain-b — Unknown)
14. **No public third-party safety audit of a commercial assistant's injection defenses.** (domain-b — Unknown)
15. **Review-tax magnitudes** — AI-authored PRs running 2–3× human size, collapsing approval times, rubber-stamp comment density: illustrative vendor analyses (Keypup, Cursor), not independently audited. Direction Corroborated; magnitudes Unverified. (gaps T2)

*Also noted as verification debt (kept out of the top 15 for space, recorded here so they aren't lost):* Faros.ai's **242.7%** incidents-per-PR figure needs primary verification (economics); Google's internal CL-size study is widely cited but not publicly inspectable (build-ship); the arXiv mutation/LLM-test study (2607.22880) was accessed via practitioner notes, not the paper (build-ship); Langfuse/LangSmith/Braintrust features and OpenTelemetry GenAI conventions were not verified this pass (automation); the Gurley "open source as strategy" essay was chased through four consistent secondaries but the primary wasn't fetched (gaps T5).

---

## 4. Pointers

- **The full merged register:** `evidence/merged-evidence-register.md` — every finding across all 20 workstreams with per-finding metadata (source, evidence class, claim label, population/limits). Assembled by a sibling agent; this section is the report-level summary, not a duplicate.
- **Per-stream registers** (the authoritative detail behind this section):
  - `research/economics/04-evidence-register.md`
  - `research/rules/05-evidence-register.md`
  - `research/spec-arch/04-evidence-register.md`
  - `research/automation/03-evidence-register.md`
  - `research/discovery/04-evidence-register.md`
  - `research/quality/04-evidence-register.md`
  - `research/build-ship/05-evidence-register.md`
  - `research/security/07-evidence-register.md`
  - `research/authenticity/04-evidence-register.md`
  - `research/ux-states/04-evidence-register.md`
  - `research/domain-a/12-evidence-register.md`
  - `research/domain-b/12-evidence-register.md`
  - `research/domain-c/10-evidence-register.md`
  - `research/cases-hyperscale/07-evidence-register.md`
  - `research/cases-product/14-evidence-register.md`
  - `research/gaps/02-evidence-register.md`
  - `research/expansion-companies/evidence-register.md`
  - `research/expansion-tools/evidence-register.md`
  - `research/expansion-practices/evidence-register.md`
  - `research/forensics/evidence-register.md`
- **Study-by-study methodology notes:** `research/economics/03-productivity-evidence-review.md`.
- **The gap analysis itself:** `report/19-missing-topics.md` (the evidence-grounded gap analysis the user commissioned).
