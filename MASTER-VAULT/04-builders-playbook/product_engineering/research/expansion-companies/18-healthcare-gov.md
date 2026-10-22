# Healthcare.gov rescue (2013–2014) — product engineering case study (instructive failure → rescue)

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
The Healthcare.gov launch (Oct 1, 2013) is the most studied government software failure in history — and its rescue ("the tech surge") is the most studied government software *recovery*. The evidence base is excellent: participant accounts, the 4sight Health case study, and the direct institutional outcome (the founding of the U.S. Digital Service, Aug 2014). This file reconstructs both the failure machine and the rescue machine.

## 1. Forensic reconstruction — how the machine actually worked

### The failure machine: no one in command, unscalable by construction
- Claim: The launch failed structurally before it failed technically: **no single person or team was in command** of the end-to-end build — dozens of contractors owned pieces, with no accountable integrator. Label: **Corroborated** — the 4sight Health case study ("HealthCare.gov's Death-Defying 2013 Launch") documents the command vacuum; widely corroborated in post-launch reporting. Confidence: high.
- Claim: The architecture was unscalable by construction — a monolithic front door with synchronous dependencies, no capacity planning for launch-day load, and inadequate end-to-end testing. Label: **Corroborated** (4sight; fedscoop on the surge team's diagnosis). Plain-English: it was built like an internal enterprise app and launched like a Super Bowl ad.

### The rescue machine: the tech surge
- Claim: The White House assembled a "tech surge" led by **Mikey Dickerson** (Google SRE — the person who ran reliability for google.com) and engineers from Google, Oracle, Red Hat, and others (fedscoop: "Healthcare.gov tech surge calls Google, Oracle, Red Hat"). Label: **Corroborated** — fedscoop (2013); gantnews profile of Dickerson (2017). Confidence: high.
- Claim: The surge's operating method: (1) establish a single accountable team with direct White House air cover; (2) instrument everything and fix by measurement; (3) run **two-minute patch drills** — deploy pipeline so fast and safe that fixes shipped in minutes; (4) ruthless prioritization (a public punch list). Results by Dec 2013: downtime cut from ~57% to ~5%, response times from ~8 seconds to 0.34 seconds, 400+ bug fixes, ~130,000 enrolled by Dec 23. Label: **Corroborated** — 4sight case study; gantnews. Confidence: medium-high (figures from a single case study; directionally corroborated everywhere).
- Claim: The institutional outcome: Dickerson founded the **U.S. Digital Service (Aug 2014)** to make the surge repeatable — small teams of top technologists embedded in agencies, the "tour of duty" model. Label: **Corroborated** (gantnews; widely reported). Engineering implication: the rescue's real product wasn't the fixed website — it was the *organizational pattern*.

## 2. Postmortem record — the failure, dissected
- **What broke (Oct 2013):** launch-day collapse under load; only a trickle of users could enroll; weeks of near-total dysfunction. Root causes per the evidence: no accountable integrator; contractor incentives rewarded billing, not working software; requirements churn from policy changes; testing that never simulated launch conditions; a launch date fixed by statute (the Affordable Care Act), not readiness. Label: **Corroborated**.
- **What the rescue changed technically:** measurement-first triage, continuous deployment discipline (two-minute patch drills), capacity/queueing fixes, bug-burndown transparency. Label: **Corroborated** (4sight).
- **What it changed institutionally:** USDS (2014), 18F's expansion, and the broader "civic tech" movement — the idea that government can hire product engineers directly instead of only contracting. Label: **Corroborated**.

## 3. Narrative audit — dismantling with receipts
- **"Government can't do tech" vs. what actually happened.** The lazy narrative: government projects fail because government. The receipts: the failure was a *procurement and accountability* design — 55+ contractors, no integrator, fixed-price waterfall against churning policy requirements. The rescue succeeded with the *same* civil servants plus a small empowered team and sane engineering practices. The variable wasn't public-vs-private talent; it was org design and deployment discipline. Label: **Inferred** (audit synthesis) on **Corroborated** facts.
- **The hero narrative vs. the unglamorous truth.** Dickerson-as-savior makes a good story; the receipts show the rescue was instrumentation, queueing, bug triage, and deploy-pipeline work — SRE fundamentals, not genius. The transferable lesson is boring on purpose: measure, prioritize, ship small fixes fast, repeat. Anyone selling the rescue as a leadership parable without the two-minute patch drills is selling the poster, not the practice. Label: **Inferred**.
- **"Tech surge" as a pattern — and its limits.** The surge model (parachute elite team, fix, institutionalize) worked once and was institutionalized as USDS. But the audit note: surges are *expensive, unrepeatable-by-default* interventions that succeed by suspending normal rules (direct White House authority, no procurement friction). If your org needs a surge, the prior system already failed; building the standing capability (what USDS was for) is the actual lesson. Also note honestly: USDS itself was later gutted/restructured in political transitions — the institutional lesson has its own postmortem, out of scope here. Label: **Inferred**; the USDS-later-history caveat is **Corroborated** by public reporting but not deep-dived this pass.
- **Negative evidence:** no evidence was found that the underlying policy (the ACA's enrollment mechanism) was the technical problem — the failure was implementation and integration, not requirements impossibility. The site worked after the rescue without policy changes.

## Transferable lessons
1. **Name one accountable integrator.** "No one in command" is the root cause; every multi-vendor program needs a single throat to choke with authority over all pieces.
2. **Two-minute patch drills.** If you can't ship a fix in minutes, you don't have a deployment pipeline — you have a release ceremony. The rescue's signature practice is worth copying literally.
3. **Instrument before you optimize.** The surge's first move was measurement; the punch list was ordered by data, not by who shouted loudest.
4. **Fixed dates need flexible scope.** The launch date was statutory; the failure was pretending scope was fixed too. When the date can't move, cut scope early and publicly.
5. **Institutionalize the rescue.** A surge that doesn't leave behind a standing capability (USDS) is just heroics. Build the team before you need it.

## Sources
| ID | Claim | URL (verbatim) | Type | Author/Org | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| H1 | Death-defying launch case study: command vacuum, surge mechanics, metrics (57%→5% downtime, 8s→0.34s, 400+ fixes) | https://www.4sighthealth.com/wp-content/uploads/2016/11/HealthCare.Gov’s-Death-Defying-2013-Launch-Final.pdf | Secondary case study | 4sight Health | 2016 | 2026-10-10 | Medium-high |
| H2 | Dickerson profile: Google SRE → surge lead → USDS founder | https://gantnews.com/2017/01/17/mikey-dickerson-fixed-healthcare-gov-that-was-just-the-beginning/ | Secondary profile | gantnews | Jan 2017 | 2026-10-10 | Medium-high |
| H3 | Tech surge called in Google, Oracle, Red Hat engineers | https://fedscoop.com/healthcare-gov-tech-surge-calls-google-oracle-red-hat-help/955 | Contemporary reporting | FedScoop | 2013 | 2026-10-10 | High |

**Gaps:** Internal surge comms/docs (not public); 18F's parallel role (not deep-dived); post-2016 USDS history (noted, not covered); contractor-side accounts (not found).
