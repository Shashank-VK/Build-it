# Evidence Register — Automation Economics & Bottlenecks
Atlas research · workstream: economics · accessed 2026-10-10

One row per finding. Fields: **claim** · source URL · source type · author/org · pub date ·
confidence · corroboration · contradictions · engineering implication.

Verdicts: Verified / Corroborated / Inferred / Proposed / Unknown.
Evidence classes: primary technical / first-hand practitioner / corroborating /
community observations / secondary interpretation / unverified.

---

## Controlled trials

**E01 — METR 2025 RCT: 19% slower with AI (experts, mature codebases)**
- Claim: 16 experienced OSS developers, 246 real issues, randomized AI-allowed vs
  AI-forbidden: AI-allowed tasks took 19% longer; developers forecast +24% beforehand,
  believed +20% afterward (perception gap ~39 pts); <44% suggestions accepted.
- URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ·
  paper arXiv 2507.09089
- Source type: primary technical (pre-registered RCT) · Org: METR (nonprofit) ·
  Pub: Jul 2025 · Accessed: 2026-10-10
- Confidence: **Verified** (for its population) · Corroboration: direction consistent
  with DX perceived-vs-measured gap; perception gap corroborated by New Relic 2026
  (review-time optimism vs incident reality) · Contradictions: Cui et al. (+26% tasks),
  Peng et al. (+55% lab) — resolved by task-type/expertise differences
- Implication: do not roll out AI on expert-maintained mature codebases on vibes;
  measure task completion, not felt speed.

**E02 — METR 2026 follow-up: weak evidence only**
- Claim: follow-up with late-2025 agentic CLI tools compromised by selection effects,
  pay-rate change, unreliable time-tracking; authors call it "weak evidence"; likely
  some speedup vs early 2025, magnitude unknown.
- Source type: primary technical (authors' own caveat) · Org: METR · Pub: Feb 2026 ·
  Accessed: 2026-10-10
- Confidence: **Verified** (as a statement about evidence quality)
- Implication: no rigorous RCT of current agentic tools exists; all 2026-era claims
  rest on weaker designs.

**E03 — Cui et al. 2025: +26.08% completed tasks (3 field RCTs, n=4,867)**
- Claim: randomized Copilot access at Microsoft, Accenture, anonymous Fortune 100:
  +26.08% (SE 10.3%) completed tasks (PRs/commits/builds); juniors gained most.
- URL: https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf
- Source type: primary technical (postregistered AEARCTR-0014530) ·
  Org: Princeton/MIT/Microsoft/Wharton authors · Pub: Feb 2025 · Accessed: 2026-10-10
- Confidence: **Verified** (output counts) · Corroboration: Accenture RCT direction,
  Microsoft 2026 CLI study, Paradis 2025 · Contradictions: Uplevel null result;
  METR negative — populations differ
- Implication: largest causal evidence base says enterprise Copilot access raised
  output ~26%; still says nothing about value, quality, or downstream cost.

**E04 — Peng et al. 2023: 55% faster on HTTP-server lab task**
- Claim: 95 developers, RCT, JS HTTP server: Copilot group 1h11m vs 2h41m (55% faster),
  completion 78% vs 70%.
- Source type: primary technical (ACM) · Org: GitHub-affiliated authors · Pub: 2023 ·
  Accessed: 2026-10-10
- Confidence: **Verified** (lab task only) · Corroboration: none at delivery level ·
  Contradictions: superseded in relevance by field studies
- Implication: frequently mis-cited; measures the most AI-favorable slice of work.
  Vendor-authored — disclose when citing.

**E05 — Paradis et al. 2025: ~21% faster (96 Google engineers, complex task)**
- Claim: RCT, Google-internal AI in VS Code, multi-file enterprise task: ~21% time reduction.
- Source type: primary technical (methodology not inspected for this file) ·
  Org: Google · Pub: 2025 · Accessed: 2026-10-10
- Confidence: **Corroborated** · Corroboration: Cui et al. direction
- Implication: supports "AI helps on realistic multi-file tasks" — but no
  downstream quality follow-up found.

**E06 — Microsoft 2026: +24% merged PRs/day with agentic CLI tools**
- Claim: early-2026 Claude Code + Copilot CLI rollout; +24.0% merged PRs/engineer/day
  (range +14.5–33.7%), sustained 4 months; dose-response by usage frequency;
  placebo-timing check passed. Authors: output moved; "whether that output justifies
  its cost is a question of value, not throughput alone."
- URL: https://arxiv.org/html/2607.01418
- Source type: primary technical (observational with robustness check) ·
  Org: Microsoft Research · Pub: 2026 · Accessed: 2026-10-10
- Confidence: **Verified** (output metric) · Corroboration: Cui et al., Accenture ·
  Contradictions: none on output; quality explicitly open
- Implication: best agentic-era output evidence; quote the authors' own value caveat
  whenever citing the +24%.

**E07 — Accenture × GitHub 2024: +8.69% PRs, +15% merge rate, +84% builds**
- Claim: ~450 devs with Copilot vs ~200 without: +8.69% PRs/dev, +15% merge rate,
  +84% successful builds, ~30% suggestion acceptance.
- Source type: secondary interpretation (vendor-reported) · Org: GitHub/Accenture ·
  Pub: 2024 · Accessed: 2026-10-10
- Confidence: **Corroborated** (direction); magnitudes **Unverified**
- Implication: usable as directional corroboration only.

---

## Population surveys & research programs

**E08 — DORA 2024: AI adoption → −1.5% throughput, −7.2% stability**
- Claim: +25% AI adoption associated with −1.5% delivery throughput, −7.2% delivery
  stability; 75% felt more productive; 24% highly trusted AI code.
- Source type: primary technical (survey program); percentages via secondary
  interpretation · Org: Google Cloud DORA · Pub: Oct 2024 · Accessed: 2026-10-10
- Confidence: **Corroborated** · Corroboration: direction confirmed by DORA 2025
  primary source · Contradictions: DORA 2025 reversed the throughput sign
- Implication: origin of the "productivity paradox" framing; shows the throughput
  effect is time-varying (adjustment then adaptation).

**E09 — DORA 2025: throughput up, stability down; AI as amplifier**
- Claim: ~5,000 professionals + 100h interviews (Jun–Jul 2025): 90% use AI; >80%
  believe productivity rose; 30% little/no trust. Positive AI↔throughput and
  AI↔product-performance relationships (reversing 2024); negative AI↔stability
  relationship persists. Seven capabilities moderate outcomes; user-centric focus is
  the strongest moderator.
- URL: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Source type: primary technical · Org: Google Cloud DORA · Pub: Sep 2025 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** · Corroboration: Cortex, Faros, LinearB on the
  stability/throughput trade-off
- Implication: the authoritative population-level finding is a *trade-off*, not a
  win; invest in platforms, small batches, and testing before/while scaling AI.

**E10 — Stack Overflow Survey 2025: trust inversion**
- Claim: ~49k respondents; 84% use/plan AI; trust in AI accuracy 40%→29%; 46%
  actively distrust; ~3% highly trust; top frustration "almost right, but not quite"
  (66%); 45% say debugging AI code takes longer than expected.
- URL: https://survey.stackoverflow.co/2025/
- Source type: primary technical (large survey) · Org: Stack Overflow · Pub: 2025 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** · Corroboration: LaunchDarkly, Sonar trust figures
- Implication: adoption is not endorsement; plan verification capacity for
  low-trust output.

**E11 — DX aggregates 2024–2026: modest measured gains, perception gap**
- Claim: ~3.8 hrs/week saved on code completion; AI users ship 60% more PRs; median
  PR throughput +7.7% (Nov 2024–Feb 2026), mean +13%, top ~70%, "nobody hit 2x/5x/10x";
  perceived delivery rate +4.5%/yr ("modest return given the investment"); deploy
  frequency rose then flattened; juniors use most (41.3% daily), seniors save more
  per use.
- Source type: primary technical (vendor telemetry + surveys) · Org: DX ·
  Pub: 2024–2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** · Corroboration: METR perception gap; DORA
  self-report vs measured divergence
- Implication: industry ceiling looks like single/low-double digits on output;
  senior judgment is the scarce complement to AI generation.

**E12 — Uplevel Data Labs 2024: null on throughput, +41% detected bugs**
- Claim: ~800 developers, Copilot vs control, 3-month windows: no significant change
  in PR cycle time/throughput (Δ=1.7 min); +41% detected-bug rate; no burnout effect.
- URL: https://www.cio.com/article/3540579/devs-gaining-little-if-anything-from-ai-coding-assistants.html
- Source type: primary technical (observational; explicitly correlational) ·
  Org: Uplevel Data Labs · Pub: Sep 2024 · Accessed: 2026-10-10
- Confidence: **Corroborated** (null on throughput); bug finding **Inferred**
  (authors: "obviously not a causal relationship")
- Implication: the key counterevidence to "throughput always rises"; cite the
  authors' own causality caveat.

---

## Code quality, security, rework

**E13 — GitClear longitudinal: structural decay (2024/2025/2026 cuts)**
- Claim: duplication +81% (40→73/1M lines); copy/paste +41%; error-masking +47%;
  churn +15%; cross-file calls −35%; refactoring moves −70%; refactoring share
  21%→<4%; 2024 first year copy/paste > moved lines.
- Source type: primary technical (longitudinal mining) · Org: GitClear ·
  Pub: 2024–2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (three annual cuts, same direction) ·
  Corroboration: CodeRabbit issue density; DORA stability decline ·
  Contradictions: none on structure
- Implication: AI-era code is bigger, more duplicated, less refactored — a
  compounding maintenance liability. Temporal correlation, not proven causation.

**E14 — Veracode 2025/2026: AI code security weakness**
- Claim: 45% of AI-generated code has OWASP Top-10 issue; 2.74× more vulns than
  human code (2025); Summer 2026 retest (11 models × 80 tasks): 56% avg pass rate,
  barely improved.
- Source type: primary technical (lab evaluation) · Org: Veracode · Pub: 2025, 2026 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** · Contradictions: Kraishan 2026 (E17) — resolved:
  lab-generated unreviewed code vs in-the-wild reviewed agent PRs are different
  populations
- Implication: raw model output is not shippable on security grounds; the review
  loop is doing real work (which is why it's overloaded).

**E15 — CodeRabbit: 1.7× issues in AI PRs (470 OSS PRs)**
- Claim: AI PRs 10.83 vs 6.45 issues (1.7×); 1.4× critical; 1.75× logic, 1.64×
  maintainability, 1.57× security, 1.42× performance issues; 80% of PRs get no human
  comments when AI review enabled.
- URL: https://www.theregister.com/software/2025/12/17/ai-authored-code-needs-more-attention-contains-worse-bugs/2576263
- Source type: primary technical (vendor study) · Org: CodeRabbit · Pub: Dec 2025 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (direction); magnitudes vendor-measured ·
  Corroboration: GitClear, Uplevel, DORA stability
- Implication: AI-assisted changes need *more* review attention per change while
  receiving *less* — the core review-burden squeeze.

**E16 — Watanabe et al.: 45.1% of merged Claude Code PRs needed human revision**
- Claim: 567 Claude Code PRs, 157 OSS projects: 83.8% merged; 54.9% merged
  unmodified; 45.1% required human changes (bugs, docs, project standards).
- URL: https://arxiv.org/pdf/2509.14745v3
- Source type: primary technical · Org: NAIST / Queen's University · Pub: 2025 ·
  Accessed: 2026-10-10
- Confidence: **Verified** (for its population)
- Implication: plan on roughly half of agent PRs needing human rework; merge rate
  alone overstates agent autonomy.

**E17 — Kraishan 2026: quality is vendor-specific; agent code fewer security smells**
- Claim: 37,623 agent PRs (Codex, Devin, Copilot, Cursor, Claude Code), 2,807 repos,
  Dec 2024–Jul 2025: Codex reverted 6.1% vs 11.5% human (OR 0.50); Devin 14.5%
  (OR 1.31); pooled agent code less likely to contain security smells (OR 0.63);
  Copilot PRs drew most human review; Claude Code PRs waited longest for first
  human review (median 12.6h). Replication data released.
- URL: https://arxiv.org/abs/2609.17598
- Source type: primary technical · Org: independent researcher · Pub: Sep 2026 ·
  Accessed: 2026-10-10
- Confidence: **Verified** · Contradictions: Veracode/CodeRabbit blanket-negative
  framing — resolved by population difference (reviewed in-the-wild PRs vs raw
  generation)
- Implication: evaluate agents per-vendor and per-task; "AI code is worse" is false
  as a blanket claim; review-effort concentration is measurable and uneven.

---

## Review burden, waiting, incidents (benchmarks & surveys)

**E18 — LinearB benchmark: AI PRs wait 4.6× longer, accepted 32.7% vs 84.4%**
- Claim: 8.1M PRs, 4,800 orgs: AI PRs wait 4.6× longer before review, reviewed 2×
  faster once picked up, acceptance 32.7% vs 84.4% manual.
- URL: https://rocketdevs.com/blog/hidden-cost-ai-generated-code (secondary write-up)
- Source type: secondary interpretation of vendor benchmark · Org: LinearB ·
  Pub: 2025–2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (direction); exact figures **Unverified** (via secondary)
- Implication: the queue signature — work waits longer to *enter* review than review
  itself takes; rejected PRs are pure sunk cost.

**E19 — Faros AI: +98% PRs merged, +91% review time; incidents/PR +242.7%/2yr**
- Claim: >10,000 developers: high AI adoption → 98% more PRs merged, 91% more
  review time; DORA-dataset analysis: incidents per PR +242.7% over two years.
- Source type: secondary interpretation of vendor analysis · Org: Faros AI ·
  Pub: 2025–2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (direction); the 242.7% magnitude **Unverified**
- Implication: the cleanest "pour doubles, backs up at the narrow part" quantification
  available; review is the binding constraint.

**E20 — Cortex 2026: PRs/author +20% YoY, incidents/PR +23.5%, change failure +~30%**
- Claim: 50+ orgs, Q3 2024→Q3 2025: PRs per author +20% YoY; incidents per PR +23.5%;
  change failure rates +~30%.
- Source type: secondary interpretation of vendor benchmark · Org: Cortex ·
  Pub: 2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (direction; consistent with DORA stability finding)
- Implication: throughput and failure moving in opposite directions at org scale.

**E21 — New Relic 2026 / Lightrun 2026: production-reality gap**
- Claim (New Relic, 200 US tech decision-makers): 94% rate AI code higher quality
  *at review time*, yet 78% saw AI-tied incident spikes, 82% had ≥1 major
  AI-attributed production failure/6mo, 74% said ≥25% of AI code needed major
  post-deploy rework. Claim (Lightrun, 200 SRE/DevOps leaders): 43% of AI changes
  needed manual production debugging after passing QA/staging.
- URL: https://mstone.ai/blog/ai-code-post-merge-cost/ (secondary synthesis)
- Source type: secondary interpretation of leader surveys · Orgs: New Relic/Hanover
  Research; Lightrun/Global Surveyz · Pub: 2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (direction across two independent surveys);
  perception-based, not instrumented
- Implication: review-time judgment is a weak proxy for durability; the cost shows
  up post-deploy.

**E22 — Practitioner surveys: Sonar / Harness / LaunchDarkly / AIDev**
- Sonar (1,100+ devs): AI = 42% of committed code; 96% don't fully trust it; 38%
  say reviewing it takes more effort than a colleague's; only 48% always check it.
- Harness: 67% spend more time debugging AI-generated code.
- LaunchDarkly (767 engineers): 94% accelerated coding; 91% low trust shipping AI
  code; 81% ship with unresolved risks.
- AIDev dataset paper: agent PR acceptance 84.0% (chores) → 55.4% (performance);
  task type dominates acceptance.
- Source type: community observations / vendor surveys · Pub: 2025–2026 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (convergent direction across independent samples)
- Implication: low trust + delivery pressure = shipped risk; acceptance rates must
  be segmented by task type to be interpretable.

---

## Cost & value-stream evidence

**E23 — AI coding spend: tiers, break-even, diminishing returns**
- Claim: seat pricing $10–40/mo standard, $40–200+/mo power/enterprise, up to
  $300–1,000+/mo/developer raw API in extremes; token pricing spans 3 orders of
  magnitude; output tokens 5–8× input cost. Break-even trivially favorable on gross
  time saved (e.g. $300/mo tool vs $15k/mo engineer needs ~3 hrs/mo). Larridin 2026:
  diminishing-returns curve — healthy ROI region, inflection point, then
  "tokenmaxxing" (spend rises, output flat). Microsoft Apr 2026 earnings: Copilot
  usage pressured Cloud gross margin; recovered after Jun 2026 usage-based pricing.
- Source type: community observations + vendor framework + earnings calls ·
  Pub: 2025–2026 · Accessed: 2026-10-10
- Confidence: pricing facts **Corroborated**; break-even sketches **Inferred**;
  diminishing-returns curve **Proposed** (vendor framework, data unverified)
- Implication: seat price is not the cost; verification labor is. No public
  cost-per-verified-result exists.

**E24 — Value-stream / wait-time evidence**
- Claim: flow efficiency typically 5–20% (~15% common); canonical illustration 7.5
  days work in 53.5 days elapsed (~14%). AutonomyAI customer (first-hand): 1 hour of
  work, 3-week median request-to-production lead time → 1–2 days after *workflow*
  change, not coding change. Devaland 91-day measurement: programming estimates off
  by "a factor of tens"; delays sat in client material, sign-offs, acceptance,
  verification. DORA 2025 explicitly recommends value-stream mapping.
- URLs: https://dev.to/karim_g/flow-efficiency-why-most-of-your-lead-time-is-just-waiting-3m8e ·
  https://koreatechdesk.com/ai-coding-software-delivery-bottlenecks ·
  https://devaland.com/blog/ai-coding-agents-bottleneck-moved-91-days-measured
- Source type: community observations + first-hand practitioner · Pub: 2025–2026 ·
  Accessed: 2026-10-10
- Confidence: baseline flow efficiency **Corroborated** (lean literature +
  practitioners); AI-era waiting-time totals **Unknown**
- Implication: coding was ~15% of lead time before AI; accelerating it alone cannot
  move customer lead time much. AI-era before/after VSM is the top missing measurement.

**E25 — SWE-bench Verified retired (benchmark validity)**
- Claim: OpenAI retired SWE-bench Verified (Feb 2026): 59.4% of audited problems had
  flawed test cases + training contamination; same model 80.9% → 45.9% on
  SWE-bench Pro.
- Source type: corroborating (reported across secondary sources; OpenAI announcement) ·
  Pub: Feb 2026 · Accessed: 2026-10-10
- Confidence: **Corroborated**
- Implication: capability claims built on benchmark scores are Unverified for
  delivery purposes; require delivery-metric corroboration.

---

## Frameworks (reference, not findings)

**E26 — SPACE (ACM Queue, Feb 2021)** · Forsgren, Storey, Maddila, Zimmermann, Houck,
Butler · https://queue.acm.org/detail.cfm?id=3454124 · Five dimensions
(Satisfaction, Performance, Activity, Communication, Efficiency); non-prescriptive;
still the standard academic lens; AI-era critique: Activity metrics inflated,
review-queue signals missing. Confidence: established framework.

**E27 — DX Core 4 (Aug 2024)** · Abi Noda / DX, advised by Forsgren & Storey ·
Four dimensions (Speed, Effectiveness, Quality, Impact) with counterbalancing metrics;
500+ company benchmarks; source of "median +7.7% PR throughput, nobody hit 10x."
Established framework; benchmarks vendor-sourced.

**E28 — DORA metrics & 2025 AI edition** · Google Cloud · Deployment frequency, lead
time, change fail rate, recovery time (+ rework rate); 2025 replaced performance
ladder with seven team archetypes + AI Capabilities Model (seven capabilities).
Primary source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report ·
Accessed 2026-10-10. Established framework.

---

## Open measurement gaps (Unknown — what would be needed)

1. **Cost per verified result:** (license + inference $/dev/mo) + (human review/rework/
   debug minutes × loaded cost) + (escaped-defect cost), per change surviving 30 days
   in production incident-free. Needs: org-level instrumentation; nobody publishes it.
2. **User outcomes:** CSAT/churn/SLA attainment before/after AI adoption with controls.
   Needs: product analytics joined to engineering adoption data.
3. **AI-era waiting-time decomposition:** per-stage wait vs work time before/after
   adoption. Needs: value-stream mapping studies (DORA 2025 recommends; none published).
4. **First-pass success rate:** pre-registered definition, AI vs human changes, same
   repos. Needs: a standard definition + a multi-org study.
5. **Queue lengths:** review/CI/deploy queue depth time series segmented by change
   provenance. Needs: engineering-intelligence platforms to publish it.
6. **Recovery (MTTR) under AI adoption:** controlled or matched before/after. Needs:
   incident data joined to adoption data.
7. **A rigorous RCT of current agentic tools:** METR's 2026 attempt failed on
   methodology; the field is waiting on a replacement.
