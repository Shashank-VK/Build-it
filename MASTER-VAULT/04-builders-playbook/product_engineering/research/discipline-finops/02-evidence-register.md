# Evidence Register — FinOps / Cloud Cost Engineering
Atlas research · workstream: discipline-finops · accessed 2026-10-10

One row per finding. Fields: **claim** · source URL · source type · author/org · pub date ·
confidence · corroboration · contradictions · engineering implication.

Verdicts: Verified / Corroborated / Inferred / Proposed / Unknown.
Evidence classes: primary technical / first-hand practitioner / corroborating /
community observations / secondary interpretation / unverified.

---

## Framework and standards

**F01 — FinOps Foundation definition and 6 principles**
- Claim: FinOps is "an evolving cloud financial management discipline and cultural
  practice that enables organizations to get maximum business value by helping
  engineering, finance, technology and business teams to collaborate on
  data-driven spending decisions." Six principles: teams collaborate; everyone
  owns their usage; centralized FinOps function drives best practices; data
  accessible/timely/accurate; business value drives decisions; exploit the
  variable-cost model.
- URL: https://www.finops.org/framework/ (canon); corroborating mirrors:
  https://github.com/brencon/clipsy/blob/HEAD/.claude/skills/cfo/references/finops-framework.md,
  https://github.com/hacrex/cloud-finops-playbook/blob/HEAD/foundations/finops-basics.md
- Source type: primary technical (the Foundation's own canon) · Org: FinOps
  Foundation (Linux Foundation) · Pub: ongoing · Accessed: 2026-10-10
- Confidence: **Verified** · Corroboration: repeated consistently across
  practitioner playbooks, AWS/Azure Well-Architected cost pillars ·
  Contradictions: none on the text; tension between "centralized function" and
  "everyone owns" noted in practitioner postmortems
- Implication: the canon is the shared vocabulary; quote it, then watch how
  practice deviates from it.

**F02 — Inform → Optimize → Operate lifecycle; Crawl → Walk → Run maturity**
- Claim: three-phase continuous lifecycle (Inform: visibility/allocation;
  Optimize: rate+usage; Operate: governance/automation); three maturity levels
  Crawl/Walk/Run.
- URL: https://www.finops.org/framework/ · https://github.com/ricmmartins/azure-governance-made-simple/blob/HEAD/guide/part-5-cost-finops/ch18-finops.md
- Source type: primary technical / corroborating · Org: FinOps Foundation ·
  Pub: ongoing · Accessed: 2026-10-10
- Confidence: **Verified** (as the published framework) · Corroboration:
  mirrored in AWS Well-Architected cost pillar (COST 1–5) and Azure guidance
- Implication: lifecycle ordering matters — chargeback-style accountability
  attempted before Inform completes is the canonical failure sequence.

**F03 — FOCUS 1.0: vendor-neutral billing-data standard**
- Claim: FinOps Open Cost and Usage Specification 1.0 standardizes cloud billing
  data (column names, definitions, semantics) so one query/dashboard works across
  providers. AWS (via CUR 2.0), Azure (Cost Management exports), Google Cloud,
  Oracle generate FOCUS-formatted exports and sit on the steering committee.
- URL: https://siliconangle.com/2024/06/20/finops-foundation-debut-focus-specification-unified-cloud-computing-bills/ ·
  https://cloudfinopskit.com/insights/what-is-focus-finops.html ·
  https://brainagents.ai/blog/what-is-focus-finops-standard
- Source type: primary technical (Foundation announcement) / secondary
  interpretation · Pub: Jun 2024 (1.0); support updates through 2026 ·
  Accessed: 2026-10-10
- Confidence: **Verified** (spec exists; hyperscaler support announced) ·
  Corroboration: consistent across explainer sources · Contradictions/limits:
  coverage and data quality vary by provider (GCP native export has lagged);
  SaaS-vendor coverage uneven — validate before migrating downstream consumers
- Implication: multi-cloud FinOps can collapse N ETL pipelines into one — but
  FOCUS normalizes the schema, not the allocation policy or ownership model.

**F04 — Scopes expand beyond public cloud ("Cloud+")**
- Claim: FinOps practice now formally includes SaaS, licensing, private
  cloud/data centre, and AI spend. State of FinOps 2025: 65% of orgs include
  SaaS, 49% licensing, 39% private cloud, 36% data centers.
- URL: https://www.webpronews.com/finops-surge-cloud-costs-hit-27-billion-by-2030-amid-ai-boom/ ·
  https://www.channeldive.com/news/finops-teams-gain-clout-ai-costs-climb/812895/
- Source type: secondary interpretation of Foundation survey · Pub: 2025–2026 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (survey data, vendor-reported) · Limitations:
  percentages are practitioner-survey self-reports, not audited adoption
- Implication: the discipline is broadening exactly as AI spend breaks old
  cloud-only tooling — but standards (e.g. FOCUS for SaaS) lag the ambition.

**F05 — 2026 Framework adds Executive Strategy Alignment**
- Claim: the 2026 FinOps Framework update added Executive Strategy Alignment as
  a formal capability: the most common failure mode is no C-suite sponsor, i.e.
  practitioners can see waste but lack authority to change the decisions behind it.
- URL: https://www.shankuehn.io/post/building-a-finops-program-diagnosis-to-operating-rhythm
- Source type: practitioner (FinOps consultant) · Pub: ~Sep 2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (single practitioner source; consistent with
  State of FinOps findings on org alignment) · Limitations: one source; the
  framework text itself not independently re-verified in this pass
- Implication: diagnose sponsorship first; a FinOps program without an executive
  owner is an observability dashboard with no actuator.

---

## Forensic cases

**F06 — Prime Video: >90% cut, serverless → EC2/ECS (one monitoring tool)**
- Claim: a Prime Video audio/video quality-monitoring service moved from
  Step Functions + Lambda + S3 (per-transition pricing hit scaling limits at
  ~5% of expected load; costly tier-1 S3 calls) to a single-process design on
  EC2/ECS with in-memory frame transfer: infrastructure cost down >90%,
  scaling headroom up, plus EC2 Compute Savings Plan eligibility.
- URL: https://www.webpronews.com/amazons-prime-video-pivots-away-from-aws-microservices-architecture/ ·
  https://www.thestack.technology/amazon-prime-video-microservices-monolith/ ·
  https://www.devclass.com/ci-cd/2023/05/05/reduce-costs-by-90-by-moving-from-microservices-to-monolith-amazon-internal-case-study-raises-eyebrows/1621790?td=rt-3a ·
  https://Dev.To/aws-heroes/is-serverless-overpriced-what-can-we-learn-from-the-primevideo-team-1d9i ·
  https://www.networkworld.com/article/972298/6-lessons-from-the-amazon-prime-video-serverless-vs-monolith-flap.html
- Source type: first-hand practitioner (company engineering blog, via press) /
  corroborating · Org: Amazon Prime Video (Marcin Kolny) · Pub: May 2023 ·
  Accessed: 2026-10-10
- Confidence: **Verified** (the 90% figure and architecture details are the
  company's own published account) · Corroboration: five independent outlets
  report the same facts · Contradictions: none on facts; narrative misreadings
  ("serverless is dead", "cloud exit") corrected by balanced analyses
- Implication: per-invocation pricing × high-frequency workloads = the crossover
  pattern; the lesson is evolutionary architecture, not anti-serverless. Scope:
  ONE tool, ONE team, still on AWS — not a repatriation.

**F07 — 37signals: $3.2M → under $1M/year, full AWS exit**
- Claim: 2022 AWS spend $3.2M ($2.3M on commodity servers); ~$700K Dell hardware
  recouped from H2-2023 savings; monthly spend $180K → $80K pre-exit; S3 exit:
  $1.5M/year bill replaced by $1.5M one-time 18 PB Pure Storage arrays (<$200K/year
  to run), with AWS waiving $250K egress under its free-exit-transfer policy.
  Total: $3.2M/year → "well under a million", same headcount, delete-AWS-account
  planned summer 2025.
- URL: https://www.theregister.com/special-features/2025/05/09/37signals-on-prem-migration-to-save-millions-abandon-aws/691340 ·
  https://www.itpro.com/cloud/cloud-computing/this-software-company-says-ditching-the-cloud-was-worth-usd10-million-in-savings-and-theres-still-more-to-come ·
  https://www.thestack.technology/dhh-aws-egress-s3-pure/ ·
  https://www.itpro.com/cloud/370111/37-signals-save-7m-abandoning-cloud-prices-grotesque
- Source type: first-hand practitioner (CTO's dated, numerically specific posts)
  / press corroboration · Org: 37signals (David Heinemeier Hansson) · Pub:
  2023–2025 · Accessed: 2026-10-10
- Confidence: **Verified** (company's own detailed accounting, consistently
  reported) · Contradictions/limits: savings vs a projected counterfactual bill
  (modelled, not measured); generalisability limited (mature Rails apps, flat
  traffic, experienced ops, ideological CTO); repatriation is single-digit %
  of companies per analyst; egress-waiver policy eased the exit and can change
- Implication: repatriation can pay at this shape of company; it is not a
  general prescription. Vendor figures direction-trusted, magnitude-discounted
  applies to the company's own counterfactual projections too.

**F08 — Dropbox: $74.6M over two years (S-1 documented)**
- Claim: Infrastructure Optimization initiative (S3 → custom colo infra, "Magic
  Pocket"): $92.5M decrease in third-party datacentre expense in 2016 offset by
  $53M in depreciation/facilities/support = $39.5M net 2016 + $35.1M 2017 =
  $74.6M over two years. Cost of revenue down 4% then 6% while revenue grew 31%.
  Metadata was always private-DC; ~10% of data stayed on AWS; dead-user data
  deletion bundled into the same initiative.
- URL: https://www.geekwire.com/2018/dropbox-saved-almost-75-million-two-years-building-tech-infrastructure/?ref=runtime.news ·
  https://www.datacenterknowledge.com/cloud/here-s-how-much-money-dropbox-saved-by-moving-out-of-the-cloud ·
  https://www.techtarget.com/it-infrastructure/blog/AWS-Cloud-Cover/Dropbox-is-likely-an-outlier-with-its-successful-cloud-data-migration-off-AWS
- Source type: primary technical (SEC S-1 filing) via press · Org: Dropbox ·
  Pub: Feb 2018 (S-1) · Accessed: 2026-10-10
- Confidence: **Verified** (SEC filing — strongest evidence class in this file)
  · Corroboration: multiple outlets, same numbers · Contradictions/limits:
  bundled waste deletion inflates the headline; $53M first-year capex; partial
  exit; commentators called it an outlier requiring Dropbox's scale and uniform
  workload
- Implication: the gold-standard documented repatriation; the fine print
  (partial exit, bundled deletion, capex) is what makes it instructive.

**F09 — Segment: >$1M cut via billing forensics, stayed on cloud**
- Claim: AWS bill grew to two-thirds of COGS with no matching employee usage
  growth; two engineers, 2–3 months of forensic work, cut >$1M. Runaway employee
  use was not the cause.
- URL: https://www.informationweek.com/data-management/inscrutable-amazon-bill-behind-it-a-1-million-savings
- Source type: first-hand practitioner (company blog via press) · Org: Segment
  (CTO Calvin Frank-Owen) · Pub: ~2017–18 · Accessed: 2026-10-10
- Confidence: **Verified** (company's own account) · Limitations: single source;
  dollar figure described as "over a million", significance asserted not audited
- Implication: the neglected lesson — understanding the bill, not leaving the
  cloud, was the fix. Standing bill-forensics capability beats fire drills.

**F10 — Spotify: Cost Insights in Backstage, gamified showback**
- Claim: Spotify built Cost Insights into its Backstage developer portal
  (engineer-visible cloud costs + optimization suggestions) plus an internal
  crowdsourced wiki ("Our Cookbook"); developers treated optimization "like a
  game"; a central cost-management org intervened only on anomalous ramps;
  millions in annual savings reported. Anomaly detection was on the roadmap at
  reporting time.
- URL: https://www.infoworld.com/article/2267139/how-5-companies-got-their-developers-to-care-about-cloud-costs.html ·
  https://siliconangle.com/2020/11/20/spotify-scales-infrastructure-thousands-microservices-open-source-fail-faster-approach-kubecon/ ·
  https://dev.to/castai/zoom-spotify-and-others-slashed-their-cloud-costs-by-millions-how-did-they-do-it-38b
- Source type: first-hand practitioner (Spotify engineering, via press/analyst)
  · Org: Spotify · Pub: 2020–2021 · Accessed: 2026-10-10
- Confidence: **Verified** (Spotify's own account of the mechanism) ·
  Limitations: dollar savings company-reported and unspecified —
  direction-trusted, magnitude-discounted; single-source per outlet
- Implication: the reference implementation of showback + social incentives +
  targeted central intervention — notably not chargeback.

**F11 — Uber (2026): AI cost held flat while agent requests grew 9.4×**
- Claim: live model routing (Pareto-optimal picks), defaulting subagents to
  cheaper models, batching multiple tool calls into scripts → total AI spend
  roughly flat Feb–Aug 2026 while weekly agent requests grew 9.4×; cost per
  session down 52% from June peak.
- URL: https://dev.to/topuzas/the-real-cost-curve-of-running-agents-in-production-from-four-different-companies-9jf
- Source type: practitioner case-study write-up · Pub: Oct 2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (detailed write-up; company-original sourcing not
  independently verified — single-source, direction-trusted, magnitude-discounted)
- Implication: sharpest public example of cost-aware model routing as
  engineering architecture rather than a finance exercise.

**F12 — GEICO: enterprise repatriation after 2.5× bill growth**
- Claim: after a decade-long cloud journey, bills up 2.5× with worse
  reliability; repatriating workloads as part of an architectural overhaul.
- URL: https://thenewstack.io/why-companies-are-ditching-the-cloud-the-rise-of-cloud-repatriation/
- Source type: first-hand practitioner (VP Platform & Infrastructure
  Engineering Rebecca Weekly, via press) · Pub: ~2024 · Accessed: 2026-10-10
- Confidence: **Corroborated** (executive quote, single outlet) · Limitations:
  no published dollar figures or architecture detail
- Implication: enterprise-scale repatriation driven by architecture (cost +
  reliability together), not ideology.

---

## Failure evidence (why compulsory)

**F13 — Segment's two-thirds-of-COGS AWS bill**
- See F09. Claim restated for the failure lens: unmetered growth reached
  two-thirds of cost-of-goods-sold before anyone investigated.
- Confidence: **Verified** · Implication: margin collapse from unmetered costs
  is a documented, not hypothetical, failure mode.

**F14 — CloudWatch logging: $2,100/mo → $340/mo in one afternoon**
- Claim: 800-user product, $11,400/mo total AWS; CloudWatch Logs $2,100/mo —
  43 log groups, no retention policies, one ingesting 180 GB/mo of debug-level
  logging left on for eight months. Fix: retention policies, kill debug, delete
  dead groups → $340/mo.
- URL: https://dev.to/vlad_z_16b6320e21f32bee0d/an-11400-aws-bill-and-cloudwatch-logs-was-2100-of-it-37aj
- Source type: first-hand practitioner · Pub: Oct 2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (detailed first-hand account; the debug-logging
  pattern is independently ubiquitous) · Limitations: single account, self-reported
- Implication: observability spend is a shadow second bill; retention and log
  levels belong in cost review, not just engineering hygiene.

**F15 — Lambda/Fargate crossover: $12,400/mo vs $3,200/mo flat**
- Claim: same REST API on Lambda and ECS Fargate for 3 months: Lambda
  $87/mo at low traffic → $12,400/mo at high (30M req/mo; API Gateway and
  CloudWatch the hidden multipliers); Fargate ~$3,200 flat; crossover ~3.2M
  requests/mo; hybrid cut the bill 53–68%.
- URL: https://dev.to/garrett_yan/serverless-vs-containers-a-cost-analysis-with-real-numbers-3dao
- Source type: first-hand practitioner (measured experiment) · Pub: Sep 2026 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (independent second account reports a
  $12,000/mo Lambda bill rebuilt on EC2 for ~$315: https://medium.com/@webdeveloper45/our-serverless-lambda-bill-hit-12-000-we-switched-back-to-ec2-for-400-heres-what-changed-9939039071e8)
  · Limitations: both single-source; your crossover point is your own —
  direction trusted, magnitudes discounted
- Implication: per-request pricing reverses above a crossover point; the
  crossover is measurable and should be.

**F16 — Runaway AI agent: ~$50K in under an hour (Mandiant)**
- Claim: an accounting agent in a runaway loop made 15,000+ high-cost API
  calls in under an hour → ~$50,000 cloud charges, no attacker involved. Root
  causes: no spend ceiling, no owner with a kill switch, cost signals arriving
  hours after spend.
- URL: https://www.shashi.co/2026/10/mandiant-says-one-runaway-ai-agent.html
  (reporting Mandiant/Google AI Risk and Resilience report, Sep 16 2026)
- Source type: primary technical (Mandiant/Google report) via press · Pub:
  Sep–Oct 2026 · Accessed: 2026-10-10
- Confidence: **Verified** (reported from the Mandiant/Google report) ·
  Corroboration: consistent with practitioner analyses of agent cost-failure
  modes (unbounded retries, no token budgets, delayed observability)
- Implication: cost controls must live in the orchestration layer — budgets,
  hard stops, per-run ceilings — because billing-latency detection is too slow
  for agent-speed spend.

**F17 — Agentic token multiplier: 5–30× chatbot consumption, mostly invisible**
- Claim: agentic workflows burn 5–30× more tokens than chatbots (Gartner);
  50–90% of agentic consumption is invisible internal traffic (repeated system
  prompts, reasoning loops, context re-injection). One case: ~€5 → ~€80 per
  operation after uninstrumented agentic automation.
- URL: https://github.com/andresilvalab/ai-ops-sec/blob/HEAD/src/content/posts/en/crise-dos-tokens.md ·
  https://www.techaheadcorp.com/blog/inference-cost-explosion/
- Source type: practitioner synthesis citing Gartner/analyst figures · Pub: 2026 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (multiple sources, same structure) ·
  Limitations: multipliers are analyst/practitioner estimates, not controlled
  measurements — direction-trusted, magnitude-discounted
- Implication: instrument tokens per run and isolate internal agent traffic
  before optimizing; the meter you watch (user tokens) is not the meter that
  bills you.

**F18 — AI cost crisis structure: prices fell, bills multiplied**
- Claim: per-token prices collapsed (Stanford AI Index 2025: inference costs
  down ~280× in two years; GPT-4-class from $30/MTok input 2023 to ~$0.10–0.40
  2026); simultaneously Deloitte Q4 2025: enterprise AI gross margins 40% →
  33%; Gartner: 40% of AI agent projects cancelled by 2027 on cost overruns;
  Uber burned its annual AI budget in ~four months (CTO public admission).
- URL: https://medium.com/@horecny/the-ai-price-collapse-is-real-your-excuse-to-wait-is-not-cc575844497c ·
  https://www.techaheadcorp.com/blog/inference-cost-explosion/ ·
  https://github.com/andresilvalab/ai-ops-sec/blob/HEAD/src/content/posts/en/crise-dos-tokens.md
- Source type: secondary interpretation / analyst citations · Pub: 2025–2026 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** on the paradox structure; the Gartner 40%
  cancellation figure is widely repeated but single-analyst-sourced —
  direction-trusted, magnitude-discounted
- Implication: unit-price trends mislead; product cost is tokens-per-task ×
  tasks, and agentic tasks moved the first factor against the price trend.

---

## Practices

**F19 — Showback vs chargeback consensus: start with showback**
- Claim: practitioner consensus — start with showback (awareness), graduate to
  chargeback (accountability) only when attribution is defensible; chargeback
  on unreliable attribution "turns every invoice into a political dispute";
  never charge teams for spend they cannot influence. FinOps Foundation: neither
  model is inherently more mature.
- URL: https://dev.to/zop_8abedcc7e12/chargeback-vs-showback-building-team-level-cloud-cost-accountability-330h ·
  https://www.finout.io/blog/cloud-cost-allocation-basics-benefits-and-types ·
  https://www.aiplusinfo.com/blog/finops-for-agentic-ai/ ·
  https://www.linkedin.com/pulse/finops-ai-chargeback-actually-works-sowdesh-kumar-sukumar-y7hjc
- Source type: practitioner guidance / community observations · Pub: 2025–2026 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (four+ independent sources, consistent rules) ·
  Limitations: behavior-change rates quoted (10–20% showback, 40–60% chargeback)
  are one practitioner's measured claim, not controlled studies
- Implication: chargeback is a policy decision with data preconditions
  (~95% attribution, published shared-cost rules, controllable levers) — not a
  maturity badge.

**F20 — Only 14% of orgs run active chargeback (State of FinOps 2025)**
- Claim: 14% of organizations implement active chargeback programs; showback-first
  is the norm. Survey: 861 respondents, $69B combined annual cloud spend.
- URL: https://cast.ai/blog/kubernetes-chargeback-showback/ (citing FinOps
  Foundation 2025 State of FinOps)
- Source type: secondary interpretation of Foundation survey · Pub: 2025 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (survey data via a second source) · Limitations:
  self-reported survey; definition of "active chargeback" per respondents
- Implication: chargeback is the exception, not the rule — programs should be
  designed for the showback reality.

**F21 — Top priorities: waste reduction #1, governance rising (State of FinOps 2025)**
- Claim: workload optimization and waste reduction was the #1 practitioner
  priority (50%); allocation and forecasting next; in forward priorities,
  governance-and-policy moved to #1 while waste reduction stayed #2; unit
  economics and managing AI/ML spend rose sharply.
- URL: https://inverodigital.com/insights/2025-state-of-finops-report-highlights/ ·
  https://www.webpronews.com/finops-surge-cloud-costs-hit-27-billion-by-2030-amid-ai-boom/
- Source type: secondary interpretation of Foundation survey · Pub: 2025 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (two independent summaries, same numbers) ·
  Limitations: survey self-report
- Implication: the field is maturing from "find waste" to "govern at scale" —
  exactly the bottleneck sequence in §6 of the main file.

**F22 — Anomaly-detection operating pattern (multi-scope, dollar floors, owner routing)**
- Claim: monitors at multiple scopes (service, account, tag) simultaneously;
  absolute-dollar thresholds alongside percentages; alerts to FinOps AND the
  owning team; monthly false-positive tuning. Aggregate-only monitors miss
  masked anomalies.
- URL: https://github.com/optimnow/cloud-finops-skills (finops-anomaly-management.md;
  URL entry unavailable in search output — text only) · corroborating pattern in
  https://github.com/azibat92/finops-sentinel- (z-score, 30-day window, severity tiers)
- Source type: practitioner guidance / open-source implementations · Pub: 2026 ·
  Accessed: 2026-10-10
- Confidence: **Corroborated** (consistent pattern across guidance + multiple
  OSS implementations) · Limitations: each deployment's effectiveness is
  self-reported; no controlled comparison of methods
- Implication: anomaly detection is table stakes and cheap (native tooling is
  free) — the differentiator is routing and tuning discipline, not the algorithm.

**F23 — Cloud waste estimated at 28–32%; Kubernetes CPU utilization ~8%**
- Claim: ~28–32% of cloud spend estimated wasted (Flexera surveys);
  Cast AI 2026: average production Kubernetes CPU utilization ~8%, CPU
  overprovisioning ~69%, memory overprovisioning ~79%.
- URL: https://www.opentext.com/fr/media/point-of-view/optimize-cloud-spend-and-business-value-with-finops-pov-en.pdf (citing Flexera 2023–2025) ·
  https://tech-insider.org/devzero-vs-kubecost-vs-cast-ai-2026/ (citing Cast AI 2026)
- Source type: vendor surveys/reports · Pub: 2023–2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** as survey/vendor-reported figures · Limitations:
  estimates and vendor-sampled measurements — direction-trusted,
  magnitude-discounted
- Implication: the waste pool is large enough that Inform-phase work pays
  before any architectural bets.

**F24 — Idle vs inefficient: different buckets, different fixes**
- Claim: idle (zero-traffic) workloads and inefficient (low-utilization)
  workloads need different fixes — rightsizing an idle pod improves its
  efficiency dashboard while the correct action is deletion or scale-to-zero;
  rightsizing can hide idle spend.
- URL: https://devtocash.com/blog/2026-09-16-kubernetes-idle-cost-find-zero-traffic-workloads-scale-to-zero
- Source type: first-hand practitioner · Pub: Sep 2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (consistent with waste-class taxonomies across
  sources) · Limitations: single practitioner's cluster experience
- Implication: track idle and inefficient as separate waste classes with
  separate detectors and separate remediation.

**F25 — Waste classes and their mechanical detection rules**
- Claim: unattached EBS (status=available 30+ days, gp3 $0.08/GB-mo), idle
  ALB/NLB (zero requests 14 days, ~$16.43/mo base), orphaned snapshots
  ($0.05/GB-mo), unassociated Elastic IPs (~$3.65/mo), stopped instances still
  paying for volumes, NAT gateways with zero traffic ($32.85/mo).
- URL: https://devtocash.com/blog/2026-09-01-aws-waste-reclamation-ai-agent-unattached-ebs-idle-load-balancers ·
  https://github.com/ellevas/cloudrift ·
  https://github.com/nathanl05/aws-cost-analyzer
- Source type: practitioner / open-source tooling · Pub: 2025–2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (consistent rules across independent tools and
  write-ups; prices are us-east-1 list) · Limitations: list prices, not any
  org's effective rates
- Implication: waste reclamation is mechanical and automatable — the detection
  rules are stable; the gap is enforcement (dry-run → notify → auto-remediate).

**F26 — Commitment purchasing on guesswork (55%)**
- Claim: 55% of developers say cloud purchasing commitments are "ultimately
  based on guesswork"; 55% say it's too hard to understand their cloud spending.
- URL: https://cdn.prod.website-files.com/6222ca42ea87e1bd1aa1d10c/67be20d4204f8f764a4410fa_FinOps%20in%20Focus%20Report.pdf
- Source type: industry survey report · Pub: 2025 · Accessed: 2026-10-10
- Confidence: **Corroborated** (survey data; consistent with practitioner
  complaints) · Limitations: self-reported; vendor-adjacent publication
- Implication: the largest discount lever (30–70% via commitments) is operated
  on vibes — commitment management must be an engineering input (only
  engineering knows what's steady-state), not a finance purchase.

**F27 — Unit-economics denominator discipline**
- Claim: track physical denominators (requests, tokens, orders, GB) for
  engineering targets and commercial denominators (per tenant, % of revenue)
  for margin — keep both; report total spend next to the unit every time;
  the denominator must already be counted and owned by the business, or it will
  be disputed.
- URL: https://www.anystackengineering.com/blog/cloud-unit-economics-cost-per-request-for-engineering-leaders ·
  https://github.com/ankitjha67/product-architect/blob/HEAD/agents/68-finops-cloud-economics.md ·
  https://www.ai-infra-link.com/why-engineering-teams-should-own-cloud-costs-in-2026/
- Source type: practitioner guidance · Pub: 2025–2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (three independent sources, same rules) ·
  Limitations: practitioner consensus, not measured outcomes
- Implication: unit economics is the management signal that separates growth
  from waste; total spend alone cannot do that.

**F28 — OpenCost: CNCF incubating, FinOps-certified K8s allocation**
- Claim: OpenCost is the CNCF vendor-neutral project (incubating since Oct
  2024) for measuring and allocating Kubernetes/cloud costs; joins K8s API +
  Prometheus + cloud billing; allocates by namespace/workload/pod/label; without
  billing wired in, reports public on-demand list prices, not your rates;
  FinOps Foundation certified allocation methodology.
- URL: http://cast.ai/blog/opencost-kubernetes/ ·
  https://horovits.medium.com/open-standards-in-finops-mastering-kubernetes-cost-and-bill-efb00731e99a?responsesOpen=true ·
  https://github.com/lurodrisilva/personal-skills/blob/HEAD/platform-engineering/opencost/SKILL.md
- Source type: primary technical (project/spec) / corroborating · Pub: 2022–2026 ·
  Accessed: 2026-10-10
- Confidence: **Verified** (project status and architecture from primary
  sources) · Limitations: none material
- Implication: the neutral measurement plane for Kubernetes cost; everything
  downstream (chargeback, rightsizing) inherits its pricing-source trust.

**F29 — Kubernetes idle-headroom ownership is where chargeback stalls**
- Claim: pod→namespace allocation mechanics are solved; who owns idle headroom
  is organizational, and most chargeback programs stall on it — unresolved, the
  first dispute kills the program; unallocated cost above ~5% makes reports
  disputable.
- URL: https://cast.ai/blog/kubernetes-chargeback-showback/
- Source type: practitioner (vendor) guide · Pub: Sep 2026 · Accessed: 2026-10-10
- Confidence: **Corroborated** (consistent with consultant postmortems on
  chargeback failure) · Limitations: single detailed source; vendor-authored
- Implication: answer "who owns idle" in policy before going live; treat idle
  as a platform-team line item rather than taxing whoever was scheduled next
  to it.

**F30 — Per-agent AI attribution at the gateway (proposed pattern)**
- Claim: every model call should carry team/use-case/environment metadata
  applied at a gateway choke point; shared costs (gateway, evals, guardrails)
  need an explicit documented allocation policy; metering must be auditable by
  a skeptical engineer; pilots get capped innovation allowances exempt from
  chargeback.
- URL: https://www.linkedin.com/pulse/finops-ai-chargeback-actually-works-sowdesh-kumar-sukumar-y7hjc ·
  https://www.aiplusinfo.com/blog/finops-for-agentic-ai/
- Source type: practitioner proposals · Pub: Oct 2026 · Accessed: 2026-10-10
- Confidence: **Proposed** (reference designs, not measured programs) ·
  Corroboration: consistent with Uber's routing approach (F11) as direction
- Implication: AI spend needs its own attribution architecture — namespace/tag
  models don't fit token flows; build the gateway before the chargeback.
