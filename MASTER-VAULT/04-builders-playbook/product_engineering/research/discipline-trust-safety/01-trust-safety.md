# Trust & Safety Engineering

*Discipline workstream · researched 2026-10-10 · read-only: discover, inspect, identify, verify, categorize, explain usage, record sources. Nothing installed, built, configured, ranked, or recommended.*

Trust & safety (T&S) engineering is the discipline of building the systems that decide what user-generated content and behavior a platform allows, and enforcing those decisions at scale. Every platform with user-generated content — text, images, video, livestreams, voice chat, DMs — is in this business whether it admits it or not. The difference between platforms is not whether they moderate, but how honestly they admit the scale of the problem and how much of the operation they fund.

**Plain English:** T&S engineering builds the machines and workflows that catch bad content before people see it (child sexual abuse material, terrorist propaganda, hate speech, scams, gore), decide the ambiguous middle cases with human reviewers, let users appeal mistakes, and prove to regulators the whole thing works. It is one of the few disciplines where failure shows up as real human harm — not just downtime — and where governments now audit the work directly.

## 1. What the discipline is

### The problem shape

A large platform receives millions to billions of items per day and must render a verdict on each: allow, limit, or remove. Human review alone cannot touch this volume (YouTube ingests roughly 500 hours of video per minute; NCMEC received 36.2 million suspected child-exploitation reports in 2023 containing over 100 million files — **Corroborated**). A single big model per item collapses on latency (50 ms per item blocks the publish path), cost (LLM inference on hundreds of millions of items per day), and coverage (one model cannot do text, images, video, and 200+ languages equally well) (**Verified** — this is the standard public argument; see §2 of this file for the cascade answer).

### The mechanics, in the order a post travels

The industry's answer is a **classifier cascade** — progressively more expensive checks, with cheap filters exiting the vast majority of traffic and humans seeing only the genuinely ambiguous residue (**Corroborated** across official disclosures and engineering references):

1. **Tier 1 — deterministic matching** (~0.1 ms): exact-hash and perceptual-hash lookup (PhotoDNA, PDQ, TMK) against known-bad databases (NCMEC, GIFCT), blocklists, regex for slurs and high-confidence strings. Handles known material with high precision. **Cannot catch novel content** — the first upload of any image is never in any database (**Verified**, Christchurch forensics below).
2. **Tier 2 — lightweight classifiers**: distilled small transformers (tens of millions of parameters) per policy category, ~10 ms per item. Emits scores, not verdicts.
3. **Tier 3 — multimodal models**: vision-language models (Meta's Llama Guard family is the public exemplar, 12B parameters) for images/video/threads that escaped Tiers 1–2.
4. **Tier 4 — LLM judge (new, contested)**: a large model interprets the *policy document itself* and judges ambiguous items with legible rationale. OpenAI publicly claimed this workflow compresses the policy-update cycle from months to hours (**Verified** — OpenAI, Aug 2023). The handbook reconstruction warns the LLM judge must never be the sole gate: it costs 100–1000x more per item than a small transformer and introduces a prompt-injection surface (**Proposed** design guidance from a secondary source, consistent with known prompt-injection literature but not company-confirmed).
5. **Human review queues**: the ambiguous residual (~0.5% of traffic at large scale, i.e., millions of items per day at a 500M-posts/day platform — **Inferred** from capacity math; the 0.5% figure is a modeled estimate, not a company disclosure). Reviewers are routed by severity, language, and specialty; critical queues carry SLAs (critical <30 min is the design target — **Proposed**).

The pivotal economics: human review dominates cost (modeled at ~$8,000 per million items vs. ~$0.01 for Tier 1 — **Proposed** illustrative figures, not company disclosures). Everything in the cascade exists to spend automation where it is safe and human attention where it is irreplaceable.

### The five functions that make it a *discipline*, not just a pipeline

| Function | What it does | Where it shows up |
|---|---|---|
| **Detection** | Classifiers, hashes, user reports, behavioral signals | Proactive-removal rates in transparency reports |
| **Decision** | Thresholds tuned by PR-curve analysis per category/per surface | >95% precision on "remove" for critical tiers is the design target (**Proposed**) |
| **Enforcement** | Allow / label / downrank / age-gate / remove / freeze / report to law enforcement | Graduated enforcement is **Verified** across Meta, TikTok, Discord transparency disclosures |
| **Review & appeal** | Human second look; double-blind re-review; external boards | Meta Oversight Board (see §5); DSA Art. 20 internal complaint-handling (**Verified** EU law) |
| **Measurement & transparency** | Prevalence, proactive rate, enforcement precision, appeal overturn rates; quarterly reports | Meta CSER, TikTok CGER, DSA Art. 42 reports (**Verified**) |

Two metrics matter more than any other, and platforms constantly argue about which one counts:

- **Prevalence** — how much violating content people actually *saw* (Meta's head of integrity Guy Rosen has called this the metric Meta holds itself accountable to — **Verified**, Meta Research interview). It measures *what was missed*.
- **Proactive detection rate** — the share of enforced content caught before any user report. Meta reported ~97–99% on child exploitation content in H1 2026 (**Verified** — Meta Transparency Center). Civil rights groups and academics have long argued this metric is gameable and doesn't match user experience (**Corroborated** — reporting from the 2021 period, and the criticism pattern persists).

The honest read: proactive rate measures *what was caught*, prevalence measures *what leaked*. A platform quoting only proactive rates is advertising; one quoting prevalence with methodology is closer to engineering.

### Cross-cutting: CSAM is a separate, legally mandated pipeline

CSAM moderation is architecturally distinct from general moderation: legally mandated (US: 18 USC 2258A reporting to NCMEC), deterministic by design, and isolated from LLM judges because prompt injection in that path would be catastrophic (**Corroborated** — legal mandate **Verified**; architectural isolation is the engineering-handbook's synthesis, marked **Proposed** as design guidance). The pipeline is: PhotoDNA/P DQ hash before storage → compare against NCMEC database and GIFCT's Hash-Sharing Database (408,000 distinct items at end of 2024 — **Corroborated**) → on match, block upload, freeze account, file CyberTipline report → specialist reviewer confirms in an isolated queue (**Corroborated**).

## 2. Why trust & safety is compulsory

This is not a judgment call; it is the part of the product lifecycle with the most documented catastrophic failures and the most direct regulatory enforcement. Six lines of evidence:

**a) Regulatory fines now land on the T&S operation itself.** The EU's Digital Services Act fines up to 6% of global annual turnover (**Verified** — EU law). Enforcement arrived in force: X was fined €120M in December 2025 (**Corroborated** — secondary reporting); Temu €200M and AliExpress €550M (July 2026) for, among other things, failing to allocate sufficient human resources to review illegal content and relying on automated systems that couldn't consistently detect violations — i.e., a T&S engineering failure stated as the legal basis of a fine (**Corroborated**). A TikTok DSA investigation opened after the 2024 Romanian election interference episode threatens up to 6% of global turnover (**Corroborated** — Oct 2026 reporting). Germany's NetzDG sets 24-hour removal windows (**Corroborated**); the UK Online Safety Act (2023, codes of practice in force from 2025) imposes safety duties enforced by Ofcom (**Verified**).

**b) Failure can cost lives, at scale.** In Myanmar, Facebook was, per the UN fact-finding mission, found to have played a "determining role" in spreading the hate speech and incitement preceding the 2017–2018 violence against the Rohingya (**Verified** — UN IIFFMM, widely reported). Meta admitted it had **one single Burmese-speaking content moderator** devoted to Myanmar in mid-2014, from a Dublin office (**Corroborated** — Amnesty International "The Social Atrocity" report, corroborated across multiple outlets). Rohingya activists reported anti-Rohingya content "more than 100 times" with no action ever taken (**Corroborated** — Amnesty). In 2022, Global Witness submitted eight ads containing explicit anti-Rohingya hate speech ("we need to kill more"); Facebook's ad-review systems approved all eight (**Verified** — Global Witness reporting). This is the single most documented T&S failure in internet history, and it is a *capacity and process* failure, not a model-accuracy failure.

**c) Criminal liability now attaches to under-moderation.** Telegram founder Pavel Durov was arrested in France in August 2024 and charged with complicity offenses relating to Telegram's alleged failure to curb extremist and illegal content — the first time a major platform founder was detained over the platform's moderation posture (**Verified**). Telegram's official response claimed its moderation is "within industry standards" (**Verified** — Telegram statement, Aug 2024) — the dispute itself is the signal: "industry standard" is now a criminal-defense argument.

**d) Brand-safety crises are the commercial enforcement mechanism.** In March 2017, ads from major brands were found alongside extremist content on YouTube; 250+ brands pulled spend, and Google launched emergency brand-safety tooling, stricter monetization thresholds (1,000 subscribers / 4,000 hours), and its first quarterly transparency report (**Verified**). The same dynamic detonated X/Twitter after the 2022 acquisition: trust & safety headcount was cut ~80% (with the T&S function specifically losing more than half its staff per contemporaneous reporting — **Corroborated**), external moderation teams were axed, and advertisers fled over racist/antisemitic trolling spikes and CSAM hashtag handling failures (**Corroborated**). X's daily app users fell 18% YoY by Feb 2024 (**Corroborated** — Sensor Tower via reporting). The lesson: T&S is revenue infrastructure for ad-funded platforms; dismantle it and advertisers price the risk themselves.

**e) Child safety is the politically irreversible driver.** Roblox's Sentinel system (open-sourced 2025) scans billions of daily chat messages and produced ~1,200 NCMEC reports in H1 2025 (**Corroborated** — AP reporting, Roblox statements) — while the company simultaneously faces lawsuits alleging its design features make children "easy prey for pedophiles" (Iowa, 2025 — **Verified** court filing reporting). Discord removed ~532,000 accounts for child-safety violations in a single quarter (Q2 2022 — **Corroborated**); Meta actioned 33.2M child-exploitation items in H1 2026 (**Verified** — Meta). The US Senate Judiciary Committee hauled tech CEOs to a child-safety hearing in January 2024 (**Verified**). There is no political configuration in which this requirement shrinks.

**f) The failure mode is adversarial and never finished.** Twitch's 2021 hate raids showed how follow-botting + homoglyph-saturated slurs (one streamer scripted 21.9 million homoglyph variants of a single slur — **Corroborated** via PC Gamer) overwhelmed blocklists; Twitch shipped Shield Mode in late 2022 (**Verified**) but only after community-built tooling (Sery_Bot, Streamlabs Safe Mode) filled the gap — a case where the platform's own T&S engineering was outpaced by its users (**Corroborated**).

## 3. How world-class companies do it — forensic lens

### Meta (Facebook / Instagram / Threads)
**Polished narrative:** AI-first enforcement with ~97–99% proactive detection on severe categories; prevalence steadily falling; published enforcement precision (~91–92% on FB/IG, H1 2026) (**Verified** — Meta Integrity Reports H2 2026).
**What the evidence supports:** Meta genuinely operates at the largest T&S scale in the industry and publishes the most detailed enforcement data (CSER since 2018, externally audited by EY — **Verified**). The integrity measurement platform (prevalence sampling of views in real time) is real engineering, not just PR (**Corroborated**).
**Where the narrative breaks:**
- Myanmar: one Burmese moderator for the whole country in 2014; eight-of-eight hate-speech ads approved in 2022 — a decade after the crisis began (**Corroborated**, §2b).
- In June 2026 the Oversight Board confirmed account bans "lack due process and transparency," noting many appeared made entirely by automated systems (**Corroborated** — reporting on Board findings).
- Meta laid off large portions of human moderation teams in 2025–2026, replacing them with AI enforcement, while planning to automate up to 90% of risk assessments for new product features (**Corroborated** — multiple outlets; Meta has confirmed the direction).
- The Board overturned Meta in **74% of cases it decided in 2024** (**Verified** — Oversight Board year-end review) — a striking error signal, though the sample is selected for difficulty (limitation: the Board hears hard cases, not random ones).
- Cross-check/XCheck: Meta told the Board the system applied to a "small number" of decisions; the WSJ found ~6M accounts were covered — the Board called the description "misleading" (**Verified** — Board transparency report; WSJ).
**Forensic verdict:** Meta has the industry's deepest T&S instrumentation and its most complete public reporting — and the industry's most documented catastrophic failure plus an active internal shift from human oversight to automation that its own Board is now publicly criticizing. The data program is world-class; the enforcement quality is contested on live evidence.

### TikTok
**Polished narrative:** $2B+ invested in T&S in 2024 (**Corroborated** — TikTok statement via TBIJ); 93.8% of violating content actioned without human review at 97.6% accuracy on subsequent checks (H2 2025 DSA report — **Verified** as TikTok's self-reported figures; accuracy methodology not independently audited — limitation noted); 94.4% of violating videos removed within 24 hours (Q2 2025 — self-reported).
**Where the narrative breaks:**
- In late 2024 TikTok cut ~500 Malaysia moderation roles and planned mass UK T&S cuts, explicitly attributing the shift to AI — while the CWU/TBIJ reported moderators in Colombia earned ~£235/month (vs ~£2,000 in the UK) with widespread occupational trauma and impossible targets (**Corroborated** — TBIJ investigation).
- September 2026: *Malaysiakini* found AI-generated sexualized content evading TikTok's filters, with removed accounts reposting and subscription features monetizing the content; five of 22 identified accounts banned, seven still active (**Corroborated** — single investigation; magnitude Unknown).
- DSA preliminary findings (Sept 2026): addictive design and failure to ensure safe accounts for minors (**Corroborated** — Commission response to Parliament). TikTok Romania election-interference probe threatens 6% turnover fines (**Corroborated**).
**Forensic verdict:** TikTok's automation metrics are the most aggressive in the industry — and its automation failures are increasingly documented by journalists faster than its transparency reports can absorb them. The "97.6% accuracy" claim coexists with visible AI-CSAM-adjacent evasion failures; the two are not reconciled in any public source (**Contradiction** flagged as unresolved).

### YouTube (Google)
**Polished narrative:** ML flags content for human review; Content ID handles copyright; AI-labeling for synthetic media; CEO made "AI slop" a 2026 priority (**Verified**).
**What the evidence supports:** The hybrid flagging pipeline (ML flags → human reviewers assess, with reviewer labels feeding back as training data) is long-documented (**Corroborated** — 2017 onward). Content ID's 98% automated copyright identification (**Corroborated** — YouTube's own long-standing figure, direction-trusted).
**Where the narrative breaks:**
- Christchurch: copies uploaded at ~1/second; hashing defeated by trivial edits (speed, color, cropping); YouTube even suspended human review of flagged items and disabled search-by-upload-date in the scramble — emergency measures that show the system was designed for volume, not for novel-violent-event surges (**Verified** — Just Security; TechDirt/Klonick reconstruction).
- Adpocalypse (2017) and repeated recurrences show enforcement is reactive to advertiser pressure, not to harm itself (**Corroborated**).
- In March 2026 YouTube began surveying users "does this feel like AI slop?" — crowdsourcing detection labels, with critics noting the labels could train Google's own Veo video models (**Corroborated** — Dig.watch; dual-use concern **Inferred**).
**Forensic verdict:** YouTube's T&S is structurally subordinate to the ads business: enforcement capacity expands after revenue threats and contracts otherwise. The ML→human pipeline is real but brittle against adversarial novelty and against its own scale.

### X / Twitter
**Polished narrative (post-2022):** "freedom of speech, not freedom of reach" — deboosting/demonetization instead of removal (**Verified** — Musk statements).
**What the evidence shows:** the sharpest natural experiment in T&S dismantling available. 80% headcount cut; T&S lost more than half; Trust & Safety Council disbanded; misinformation and state-media teams cut; quit the EU disinformation code (May 2023); EU named X the largest spreader of Russian propaganda among major platforms (Aug 2023 — **Verified** — Commission statement); NBC found known CSAM hashtags unblocked, prompting a DOJ-investigation push by Sen. Durbin and an Australian regulator fine (**Corroborated**); DSA investigation opened Dec 2023; €120M DSA fine Dec 2025 (**Corroborated**); Stanford researchers' T&S contacts all gone from the company (**Corroborated** — via WSJ reporting).
**Forensic verdict:** X is the control group proving T&S headcount is load-bearing, not overhead: within months of the cuts, every measurable harm indicator and regulatory exposure deteriorated. The "deboost not remove" philosophy has no published measurement program behind it (**Unknown** — no prevalence-style metrics disclosed post-2022).

### Reddit
**Model:** federated — platform-level policy plus ~tens of thousands of volunteer moderators running per-community enforcement with platform tooling (AutoMod, Crowd Control, mod queues) (**Verified**).
**Forensic note:** the 2023 API-pricing change ($0.24/1,000 calls) killed third-party apps (Apollo etc.) that moderators depended on for accessibility and tooling; ~7,000–8,000 subreddits went dark in protest (**Verified** — Wikipedia; The Register). Reddit replaced protesting mod teams and enforced the Moderator Code of Conduct (**Verified**). The episode proves the volunteer layer is real infrastructure: when its tooling broke, enforcement quality visibly degraded, and replaced mods lacked subject-matter expertise (**Corroborated** — 9to5mac reporting).
**Engineering implication:** a federated moderation model makes the *platform's* T&S spend look small while externalizing labor to volunteers — but platform API/tooling decisions are then T&S decisions, and breaking them is a T&S incident.

### Discord
**Model:** centralized T&S on a semi-private network (servers/DMs), PhotoDNA + open-source image-analysis models for CSAM (**Verified** — TechPolicy.press Senate backgrounder), quarterly transparency reports with per-category server/account actions (**Verified** — Discord 2026 transparency report).
**Failure evidence (recent, instructive):** July 2026 — a *bad hash in a similarity-matching database* triggered ~200 wrongful child-safety bans in one weekend, and a second bug prevented auto-lifting after staff cleared the accounts; ~8,200 accounts total affected since May 2026 (**Verified** — Discord's own postmortem via Dexerto). The incident is a textbook hash false-positive cascade: one poisoned entry → deterministic matching → enforcement → broken remediation loop.
**Also:** Discord says ~15% of staff work on safety (~97 people for ~140M MAU, 2022 figures — **Corroborated**); Brazil restricted video features in Aug 2026 after a 13-year-old's livestreamed suicide linked to encouragement on the platform (**Corroborated** — ANPD order via consumer-rights wiki; single source, treat as **Corroborated-not-Verified**).

### Roblox
**Model:** child-first; Sentinel (open-source, 2025) detects grooming patterns in chat; voice-safety classifiers; 100+ safety initiatives in 2025; age estimation (facial AI/ID/parental consent) rolling out for all communication users by end-2025 (**Corroborated** — Roblox CSO statements).
**Forensic note:** Sentinel is simultaneously a genuine detection advance (~1,200 NCMEC referrals H1 2025 — **Corroborated** via AP) and a litigation shield deployed while lawsuits allege the platform's design makes children "easy prey" (Iowa 2025 — **Verified** reporting of filings). Open-sourcing detection tooling via ROOST (co-founded 2025 with Google, OpenAI, Discord — **Corroborated**) is industry-collaboration behavior; it does not resolve the design-level allegations (**Unknown** — pending litigation).
**Engineering implication:** on child-dominant platforms, T&S *is* the product's license to exist — age-gating, chat filtering, and detection are launch gates, not add-ons (§7).

### Twitch (Amazon)
**Model:** creator-delegated — AutoMod, channel-level bots, human mods per stream, plus platform teams (**Verified**).
**Failure evidence:** the 2021 hate raids (follow-bots + slur floods targeting marginalized creators) overwhelmed platform tooling; community-built defenses (Sery_Bot, Streamlabs Safe Mode, "panic button" workflows, an academic paper documenting them — **Verified** — Han et al., CSCW 2023) shipped *before* Twitch's official Shield Mode (Nov 2022 — **Verified**). The 21.9M-homoglyph-variants demonstration showed keyword blocklists are structurally inadequate against motivated adversaries (**Corroborated**).
**Engineering implication:** brigading/abuse defense must assume *coordinated, automated* adversaries; keyword defenses are a speed bump, not a wall.

### Cross-company table: the narrative vs. the receipts

| Company | Public narrative | Hardest contradicting evidence |
|---|---|---|
| Meta | AI-first, 97%+ proactive, prevalence falling | Myanmar (1 Burmese moderator, 2014); Board overturn rate 74% (2024); 2025–26 automation of human review criticized by own Board |
| TikTok | $2B T&S, 97.6% auto-accuracy | Mass moderator layoffs attributed to AI; AI-sexualized-content evasion documented Sept 2026; DSA Romania probe |
| YouTube | ML flagging + human review | Christchurch hash evasion; enforcement follows advertiser pressure (adpocalypse) |
| X | Deboost-not-remove | Every harm indicator deteriorated after T&S cuts; €120M DSA fine; CSAM hashtag failures |
| Reddit | Community self-moderation | API pricing broke moderator tooling; platform replaced mods — tooling *is* T&S |
| Discord | Quarterly transparency, PhotoDNA+AI | July 2026: one bad hash → 8,200 wrongful bans; broken remediation loop |
| Roblox | Sentinel open-sourced, 100+ initiatives | Lawsuits alleging design-level child endangerment continue |
| Twitch | AutoMod + Shield Mode | Community tooling shipped the defenses first; keyword lists structurally defeated |

## 4. Key practices (engineering detail)

### Classifier pipelines
- **Cascade with confidence-based escalation**: tiers exit on high-confidence clean/violation; ambiguous band escalates. Thresholds are tuned per policy category per surface via PR-curve analysis — a newsfeed tolerates more false positives than DMs (**Proposed** design guidance; consistent with public threshold discussions).
- **Pre-publish vs. post-publish split**: high-confidence severe violations (CSAM, terrorism) block synchronously; ambiguous content publishes then gets async re-check with takedown. Livestream rewrites the latency budget to "seconds per chunk" with frame sampling + audio transcription (**Proposed**; consistent with known live-moderation constraints).
- **Graceful degradation**: on classifier outage, fail open to "allow + async re-check" rather than fail closed — availability beats recall during incidents, with the re-check loop as the backstop (**Proposed**).
- **Drift & adversarial monitoring**: classifiers degrade silently as adversaries probe seams (launch-day 95% precision → 80% within weeks is the modeled risk — **Inferred** from the handbook; direction-plausible, magnitude not company-confirmed). Mitigations: weekly retraining on reviewer-labeled data, versioned adversarial eval sets, shadow deploys, auto-rollback on PR-curve regression (**Proposed** best-practice synthesis).

### Human review tooling, queues, and SLAs
- **Queue partitioning**: `queue_id = hash(severity, language, specialty)`; priority scores combine severity, virality velocity, and SLA deadline (**Proposed** reconstruction; consistent with job postings and vendor disclosures).
- **Consensus and calibration**: low-confidence AI items and user reports go to paid reviewers; removal often requires agreement among multiple moderators; reviewer labels feed classifier retraining (**Corroborated** — Facebook's described process via research literature).
- **Specialist queues**: CSAM and terrorism queues are isolated from general moderation with restricted access (**Corroborated**).
- **Reviewer welfare as architecture**: blur-by-default tooling with deliberate unblur, rotation caps (4 hrs/day on CSAM is the stated target — **Proposed**), embedded counselors, compensation floors in vendor contracts (**Proposed** best practice; the welfare *problem* is **Verified** — see Kenya litigation below). The outsourcing reality: Meta's Kenya moderators (via Sama) were paid ~$414/month, watched beheadings as onboarding content, and sued over PTSD; a $52M (2020) then $85M California settlement preceded the still-litigated Kenya cases demanding $1.6B (**Verified**/**Corroborated**). **Engineering implication:** reviewer throughput targets set in vendor contracts directly determine label quality and therefore classifier quality — welfare is a training-data-integrity issue, not just an HR issue.

### Appeals
- **State machine**: submitted → assigned → in_review → decided → closed; double-blind second reviewer on appeal; bounded latency (**Proposed** reconstruction).
- **Meta's Oversight Board** is the industry's only binding external appeal body: 200,000+ eligible escalation decisions in Aug 2024 alone, of which users appealed ~220 to the Board; the Board overturned Meta in 74% of decided cases in 2024 (**Verified** — Meta transparency; Board year-end review). Meta has 60 days to respond to recommendations; implementation of "identical content in same context" takedowns is technically committed (**Verified**).
- **DSA Art. 20** makes internal complaint-handling mandatory in the EU — appeals are now a legal requirement, not a courtesy (**Verified**).
- **The anti-brigading constraint**: appeals must resist coordinated mass-appeal abuse — rate limits, reputation-weighted appeal priority, and anomaly detection on appeal patterns (**Proposed**; no public source details platform implementations — **Unknown**).

### Transparency reporting
- **Meta CSER** (quarterly since 2018, EY-audited): content actioned, proactive rate, prevalence, appeals, overturns (**Verified**).
- **TikTok CGER** (quarterly) + **DSA Art. 42 reports** (biannual for VLOPs): removals by category, automation share, appeals (**Verified**).
- **Discord** (quarterly): per-category account/server actions, warnings, appeals (**Verified**).
- **Limitation every engineer should know:** reports are self-measured, definitions differ across companies (what counts as "actioned" varies), and no two platforms' numbers are comparable. Treat directionally; discount magnitudes (**Inferred** — the report's standing rule).

### Hash sharing: PhotoDNA, PDQ, TMK, GIFCT
- **PhotoDNA** (Microsoft, donated): perceptual image hash; every major platform runs uploads against NCMEC-derived databases (**Verified** — NCMEC; platform disclosures).
- **PDQ / TMK+PDQF / vPDQ** (Meta, open-sourced 2019): PDQ is a 256-bit DCT-based image hash, matching threshold Hamming distance ≤31, quality cutoff ≥50; reference FAISS matcher ~4,000 images/sec single-process. TMK+PDQF video signatures are ~256KB; vPDQ matches on share of matching frames (**Verified** — Meta open-source repos).
- **GIFCT Hash-Sharing Database**: cross-industry; 408,000 distinct items end-2024 (**Corroborated**); members ingest hashes for auto-block/demote/review. In the Eskişehir (Türkiye) 2024 attack, members shared 910 hashes via a Crisis Incident Protocol activation (**Verified** — GIFCT report).
- **Known limits** (**Corroborated**): hashes lack semantic context (a news report and a propaganda upload hash identically — the Christchurch ethics tangle, where Facebook deleted even condemnation/newsworthy posts); perceptual hashes are fooled by minor edits (Christchurch: 800 distinct versions detected by Facebook); false positives are deterministic and blast-radiusy (Discord July 2026: one bad hash → thousands of wrongful bans); and in 2026 independent advisers resigned en masse from GIFCT citing governance/appeal deficits (**Corroborated** — single outlet; treat as **Corroborated-not-Verified**).

### Brigading & coordinated-abuse defenses
- **Velocity anomaly detection**: raid signatures (follow bursts, account-age distributions, message-similarity clustering) rather than content keywords alone (**Proposed**; consistent with anti-spam practice).
- **Friction levers**: follower/sub-only modes, phone-verified chat, slow mode, Shield-Mode-style lockdown presets (**Verified** — Twitch/Streamlabs features).
- **Account-level enforcement**: ban evasion detection via device/IP/behavioral fingerprinting and linked-account graphs; repeat-offender escalation (**Inferred** — standard anti-abuse practice; platform specifics **Unknown**).
- **Lesson from hate raids:** defenses that push work to victims (manually blocklisting 21.9M homoglyph variants) are not defenses; platform-side behavioral detection is the only layer that scales (**Inferred** from the documented failure).

## 5. Failure modes and postmortems

| Failure | What happened | Root cause (evidence-labeled) | Fix status |
|---|---|---|---|
| Myanmar / Rohingya (2012–2018) | Hate speech and incitement amplified for years; UN: Facebook played "determining role" | **Corroborated:** 1 Burmese moderator (2014); ignored activist warnings 2012–2017; report function non-functional in practice | Meta banned military accounts 2018/2021; dozens of Burmese moderators hired mid-2018 — but Global Witness's 8/8 hate ads approved 2022 shows the pipeline still failed basic tests |
| Christchurch (Mar 2019) | Livestream + 1.5M copies in 24h; copies uploaded ~1/sec to YouTube | **Verified:** perceptual-hash evasion by trivial edits; novel content has no hash; AI couldn't distinguish FPS-game streams from real violence | GIFCT Crisis protocols; audio fingerprinting added; 200,000+ hashes shared — but evasion-by-edit remains unsolved (**Inferred** — no public source claims otherwise) |
| X/Twitter T&S cuts (2022–) | Advertiser exodus; disinformation surge; CSAM hashtag failures; €120M DSA fine | **Corroborated:** 80% headcount cut, T&S >50% cut, council disbanded, EU code quit | Ongoing deterioration; no published recovery metrics (**Unknown**) |
| TikTok moderator layoffs (2024–) | 500 Malaysia roles cut; UK cuts; CWU reports trauma/wage abuses at contractors | **Corroborated** (TBIJ, Reuters, CWU) | TikTok says "continuing to invest"; DSA probes open |
| YouTube adpocalypse (2017, recurring) | 250+ brands paused; revenue threat drove emergency moderation | **Verified** | Monetization thresholds + brand-safety tooling; recurs whenever press finds new adjacencies |
| Twitch hate raids (2021) | Bot-driven slur floods on marginalized creators | **Corroborated:** keyword defenses structurally inadequate | Shield Mode (2022); community tooling filled the gap first |
| Discord hash false positives (2026) | One bad hash → ~8,200 wrongful child-safety bans; broken auto-remediation | **Verified** (Discord postmortem) | Hash overridden; "better safeguards" promised — remediation-loop testing gap acknowledged |
| Roblox child-safety litigation (2025) | Iowa suit: design makes children "easy prey"; kidnapping/trafficking allegation | **Verified** (filings reported) | Sentinel open-sourced; 100+ initiatives; litigation pending (**Unknown** outcome) |
| Telegram / Durov (2024–) | Founder arrested; charged over moderation failures | **Verified** | Telegram claims DSA compliance; French case ongoing |
| Meta Kenya moderators (2022–) | PTSD lawsuits; $1.6B demanded; settlement talks collapsed | **Corroborated** | Trial track; Meta disputes employer status |

**Pattern across postmortems:** failures are rarely "the classifier's AUC was too low." They are capacity failures (Myanmar), novelty failures (Christchurch), governance failures (X), supply-chain failures (reviewer outsourcing), and adversarial failures (raids, hash evasion). The fixes that stick are architectural (isolated CSAM queues, behavioral raid detection, crisis hash-sharing protocols), not threshold tweaks.

## 6. Bottlenecks

1. **Reviewer capacity and cost.** Human review is the binding constraint and the dominant cost (~$8,000/M items modeled vs. cents for automation — **Proposed** illustrative). Every platform is simultaneously cutting reviewer headcount (Meta, TikTok 2024–26) and facing SLAs from regulators (NetzDG 24h, DSA). The math doesn't close; automation is being asked to cover the gap before it is validated (**Inferred**).
2. **Precision/recall with asymmetric costs.** At 95% precision on "remove," 50,000 false positives per million actions become appeals; at 95% recall on CSAM, the 5% miss is a child-safety catastrophe. The PR curve is negotiated per category, per language, per surface — and languages outside the top ~20 get systematically worse classifiers (the Myanmar lesson generalizes: **Inferred**, direction-consistent with all Global South evidence).
3. **Adversarial adaptation.** Every deterministic defense (hashes, keywords, regex) is probed and evaded within weeks (Christchurch's 800 variants; 21.9M homoglyphs; re-upload-after-removal on TikTok documented Sept 2026). Defenses must be behavioral and retrained continuously — which raises bottleneck #1 again.
4. **Livestream latency.** Pre-publish blocking at 200 ms works for text/images; livestreams need seconds-per-chunk moderation, and novel violent events have *zero* hash coverage at minute zero. Christchurch's 29-minutes-to-first-report gap is the irreducible floor of reactive systems (**Verified**).
5. **Measurement integrity.** Prevalence and proactive rates are self-reported with platform-defined taxonomies; the EY audit of Meta's metrics validates measurement, not policy correctness (**Inferred** — audit scope is measurement validation). No independent benchmark of cross-platform T&S effectiveness exists (**Unknown** — flagged as a research gap).
6. **Reviewer welfare → label quality.** Trauma, impossible quotas, and $414/month wages produce noisy labels; noisy labels produce drifting classifiers. The supply chain of human judgment is the least instrumented part of the stack (**Inferred**; the welfare facts are **Verified**/**Corroborated**).

## 7. Where trust & safety slots into the product lifecycle

T&S is not a launch gate you pass once; it is a parallel lifecycle that runs alongside the product's:

- **Ideation / design:** threat modeling for abuse (how will this feature be weaponized? — e.g., DMs enable grooming; livestream enables violent broadcast; subscriptions enable monetized CSAM-adjacent content, as documented on TikTok Sept 2026). Age-gating and communication tiers (Roblox's under-13/13–17/18+ segmentation) are *design* decisions with T&S as a stakeholder (**Corroborated**).
- **Policy development:** versioned policy taxonomy owned jointly by product, legal, and T&S; LLM-assisted policy iteration (OpenAI's months→hours workflow — **Verified** as a claimed capability) compresses this stage but doesn't remove legal review.
- **Build:** classifier cascade, hash pipelines, review tooling, appeals state machines, transparency data pipelines, and enforcement APIs are built as product infrastructure — the moderation API contract (decision, policy tags, confidence, tier reached, latency) is as much a product surface as any user API (**Proposed** reconstruction).
- **Pre-launch:** risk assessments for new features — Meta is automating up to 90% of these (**Corroborated**), which the Oversight Board-adjacent scrutiny treats as a governance risk, not a pure efficiency win. The UK Online Safety Act requires risk assessments as a legal duty (**Verified**).
- **Launch / growth:** T&S capacity must scale with growth *in every language the product reaches*, not just the launch market — the Myanmar failure is what happens when growth outruns T&S localization (**Corroborated**).
- **Operate:** continuous retraining, adversarial eval refresh, transparency reporting cadence (quarterly/biannual), DSA systemic-risk assessments (annual for VLOPs — **Verified**).
- **Incident response:** crisis protocols (GIFCT CIP activations — **Verified**) sit alongside the product's incident process; novel-event playbooks (hash the novel content fast, audio fingerprinting, disable discovery surfaces) are the T&S equivalent of a Sev-0 runbook (**Inferred** from Christchurch response).

**The one-line version:** T&S is the discipline that keeps a platform's growth from becoming its liability — legally (DSA/NetzDG/Online Safety Act), commercially (advertisers), and morally (Myanmar, child safety). Companies that treat it as a cost center to be automated away rediscover, usually via a fine or an exodus, that it was load-bearing infrastructure.
