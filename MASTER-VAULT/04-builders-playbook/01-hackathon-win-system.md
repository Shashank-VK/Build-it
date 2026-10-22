# 01 — The Hackathon Win System

The maxim (from the distillation): *"Know what you're being judged on, cut everything that doesn't serve it, verify what the AI wrote, deploy before you're ready, and never show anything you can't defend as real."*

Evidence labels on every claim: **Verified / Corroborated / Inferred / Proposed / Unknown**. Raw sourcing in `research/hackathon-intel-notes.md` (249 lines) and `research/hackathon-intel-evidence.md` (30 rows). Where a 48h hour number is extrapolated rather than sourced, it's labeled **Proposed/Inferred**.

## The 5 findings this whole file hangs on

1. **The demo video is what judges actually evaluate — treat it as the product.** (Corroborated) In online judging the video is the primary artifact; one team won 1st place with a video-only entry after being locked out of the venue. Record a backup video before the deadline crunch — #1 insurance against dead wifi/rate-limited APIs.
2. **Overscoping is the #1 killer; scope to one hero feature.** (Corroborated) The winner's filter: "can we demo this compellingly in 3 minutes?" Working skeleton by ~25% of the clock, code freeze in the last ~15%, submit 30 min before the hard Devpost cutoff.
3. **Idea selection beats execution speed — spend 25–50% of early time on the idea.** (Corroborated) Problem-first, explainable to a non-technical person in one sentence, clearest problem→solution→impact story. Target less-competitive sponsor/API prize tracks deliberately.
4. **Boring stack, familiar tools; novelty belongs in the idea, not the stack.** (Corroborated) Deploy a hello-world to a live URL in the first hours; mock-data fallbacks for live APIs. 2026 wrinkle: AI coding assistants are dramatically better at mainstream stacks, so obscure tech now also costs AI-effectiveness (Verified analysis).
5. **Read the rubric, then aim at it — most teams don't.** (Verified) Winners balance across ALL criteria rather than spiking one. Documented score-killers: ambiguity + thin GitHub behind a slick video, template resubmission, rehashed ideas, recycling one project across hackathons, backend-only builds with no UI.

## 1. Idea selection — with the evaluator logic

The idea beats the build. An 8-time winner (Verified — LinkedIn post): *"a good idea beats fast execution every time."* At Hack the North he spent **more than half the time** brainstorming/exploring/prototyping and finished the build in under 8 hours — and won. (Corroborated across winner accounts.)

### The evaluator logic (fills `templates/idea-evaluator.md`)

1. **Start with the judges.** Before brainstorming, ask: "what would make a judge stop and lean in during a 3-minute demo?" (Verified — the 8-winner's framework).
2. **Generate widely, 30–60 min.** No filtering yet. Problems you've lived with beat problems you invented — be the domain expert (Corroborated).
3. **Filter with one operational question:** *"can we demo this compellingly in 3 minutes?"* (Corroborated). Anything that fails is too complex — scope it down or kill it.
4. **Pick the clearest story.** Clearest problem→solution→impact narrative beats the cleverest tech (Corroborated). One-sentence test: explainable to a non-technical person in one sentence (Corroborated).
5. **Check prize-track fit.** Less-competitive sponsor/API prize tracks are deliberately targetable (Corroborated): using the sponsor's API genuinely can win a track with fewer entrants. (Proposed caveat: don't shoehorn — Verified score-killer is "fitting a solution to this hackathon.")
6. **Pre-commit the kill rule.** ≤2 hours of validation for a hackathon idea (adapted from project OS phase 2). One falsifiable question, one cheap test (2 hallway conversations, a fake-door, or a judge-proxy read of the rubric: "would a judge care enough to click twice?").

### Score-killer screen (run every idea through this before committing)

From Verified judge interviews (Devpost's "Advice from 5 seasoned judges"): kill the idea if it's a template resubmission (barely changed starter), rehashed/already-in-market, recycled from your last hackathon with a new label (judges check Devpost profile history), or a pre-existing idea shoehorned to fit the contest. All five judges said some version of "we see through it."

## 2. Stack guidance

- **Boring stack, familiar tools.** (Corroborated) The build's novelty belongs in the idea, not the stack.
- **AI-effectiveness is now a stack criterion.** (Verified analysis, 2026) AI coding assistants are dramatically better at mainstream stacks — obscure tech costs you both debugging time *and* AI output quality.
- **Hello-world to a live URL in the first hours.** (Corroborated) Deployment is where "works on my machine" dies; make it die at hour 4, not hour 47 (adapted from §14 R-25: "it deploys from main in one step," Proposed hackathon version: first deploy by hour 2).
- **Mock-data fallbacks for live APIs.** (Corroborated) The 24h blueprint explicitly: "add fallback mock JSON data in case live API rate limits get hit during judging." Tech that dies live (wifi, rate limits, unfamiliar infra) is a Corroborated killer.
- **Secrets never in code.** Public hackathon repo + API keys = leak in hours. (Adapted from §14 R-15 — automatable, 5-min secret scan, zero-cost excuse.)

## 3. The 48-hour battle plan

The **structure** is Corroborated (skeleton by ~25% of clock, code freeze in the last ~15%, submit 30 min before the hard Devpost cutoff). The **hour numbers** are Proposed/Inferred extrapolations — sources skew 24h, so this scales the Corroborated 24h blueprint (LinkedIn "Developer's Guide to Shipping Complete MVPs in 24 Hours": ideation 0–2, hello-world 2–4, core build 4–14, polish + mock fallbacks 14–18, code freeze 18–21, pitch video 21–24) to 48h and preserves the winner timing proportions.

Fill `templates/battle-plan-48h.md` at the pre-hack sit-down (10 min, Proposed — adapted from the project OS: outcome metric = the demo moment; cut list = what the demo will NOT show; roles-for-one: who's coding, who's pitching — both you, timeboxed).

| Phase | Hours (Proposed) | What happens | Gate |
|---|---|---|---|
| **0 — Idea + scope lock** | 0–4 (~10%) | Brainstorm 30–60 min → filter with the 3-minute demo question → napkin spec → **cut list written before coding** (adapted from §14 R-05; the distillation's Proposed 3-row version: who judges, what's scored, kill criterion). No new features after this phase ends. | Idea passes the evaluator (§1). |
| **1 — Skeleton to live URL** | 4–12 (by 25% of clock) | Repo + hello-world deployed to a live URL. The deploy path is the deliverable of this phase. | Live URL exists; rollback = redeploy last good commit. |
| **2 — Hero feature** | 12–34 | One hero feature, end-to-end on the real path. Second feature does not exist. Demo path is a real code path (adapted from §17 §7 — undisclosed fakery is AP-14; anything simulated is *disclosed*). | Demo path works end-to-end on production-shaped data (adapted from §14 R-18/R-19). |
| **3 — Polish + insurance** | 34–41 | UI polish on the demo flow only. **Mock-data fallbacks for every live API.** **Record the backup video now, before the crunch** (finding #1 — #1 insurance against dead wifi/rate-limited APIs). | Backup video file exists. Every visible control on the demo path does something real (adapted from §17 §5.2). |
| **4 — Freeze + submit** | 41–48 (last ~15%) | Code freeze — bug fixes only, no new code. Re-run the demo path E2E on prod. **Submit 30 min before the hard cutoff** (Corroborated — Devpost's own guide warns disqualification for missed baseline requirements is common). | Submitted with 30 min slack. Video + text description complement each other (Corroborated judge advice). |

Mid-hackathon discipline checkpoints — the distillation's 3 gates for 48h (adapted from §11 §5, Tier-3 calibration per §17 §4.2):
1. **Gate 8 — Deployment** (end of phase 1): skeleton is live; rollback path known.
2. **Gate 6 — Testing** (end of phase 2): the *frozen demo path* exercised E2E on production-shaped data.
3. **Gate 5 — Implementation** (continuous): CI green on the exact commit, no secrets in code, every AI-generated diff re-read and explainable (adapted from §14 R-13; Perry finding — AI-assisted devs wrote *less* secure code while *more* confident).

Explicitly parked in 48h (from the distillation): formal discovery (G1), full spec (G2 — napkin spec instead), full design (G3 — loading/error/empty states on the demo flow only), prototype memo (G4 — the pitch script *is* the memo), full security review (G7 — floor only: no secrets, no hand-rolled auth, mark it "not shippable" after), post-launch (G9).

## 4. Demo script framework

Judges evaluate the video like the product — script it like one. (Corroborated judge pattern from Devpost interviews: real filter order is (1) meets requirements, (2) demo/video communicates clearly, (3) balanced across criteria, (4) story/enthusiasm signals effort.)

### The 5 beats (fills `templates/demo-script.md`)

1. **Hook (10s).** The problem, in one line a non-technical person gets. If the judge isn't leaning in here, nothing after matters (Corroborated — 3-minute demo filter).
2. **The demo (90s).** Show the hero feature live. Narrate the *user's* action, not your tech. One dead button costs more than the feature you cut to fix it (adapted from §17 §5 functional completeness — no dead controls on the demo path).
3. **Reality inventory (30s).** Mark every shown capability Real vs Simulated; simulated = disclosed (adapted from §17 §7 — "anything not marked is assumed simulated"). Undisclosed fakery is the #1 demo-killer (§14 AP-14; judges probe one step off-script and are now specifically hunting AI-built fakery).
4. **How it works, briefly (30s).** Enough to show real engineering — thin GitHub behind a slick video is a Verified score-killer (Databricks judge).
5. **Impact close (20s).** Problem→solution→impact, one sentence each. If targeting a sponsor track, land the track's value here (Corroborated — deliberate track targeting).

### The backup-video insurance move (finding #1)

Record a full run-through of the demo video **before the deadline crunch** (end of phase 3, hours 34–41), not at hour 47. Two real failure modes it covers: venue wifi dying mid-judging, and live APIs rate-limiting during judging (both Corroborated). One team won 1st place on video alone after being locked out of the building (Verified — author's LinkedIn post). Keep the video in a tab during live judging (Corroborated — "the recovery playbook across sources").

## 5. Judging psychology — aim at the rubric

- **Requirements first.** (Verified — Databricks judge's first pass is checking requirements; Devpost: "surprising how many submissions did not fulfill the basic requirements.") Read the rubric, write down each criterion, cut every feature that doesn't serve one (adapted from §14 R-01/R-02: judges = your customer segment).
- **Balance across criteria beats spiking one.** (Verified — Square judge: the biggest negative is "over-indexed on one particular criteria at the detriment of the rest" — e.g., extremely backend-heavy with no UI. MLH's standard line corroborates the other side: demo what you built, not the pitch.)
- **Technical depth is format-dependent.** (Corroborated) Technical hackathons (Atlassian's AI-SME screening, CockroachDB×AWS's "production readiness" criterion) reward depth; most others reward clarity + story + working demo. Know which room you're in (Proposed).
- **Storytelling signals effort.** (Verified — judges cited presentation/storytelling as "a huge part of your success"; video is "the first indicator of time invested.")
- **The thin-repo tell.** (Verified) Slick video + light GitHub reads as effort-faked. Commit often from hour 1 (adapted from §14 R-11 — version control from commit 1).

## 6. Anti-patterns that lose — the lethal 6

From the distillation (§07 + §14), hackathon-ranked:

1. **AP-14 — Misleading product demos** (§14). Hardcoded data, demo-only code paths, capabilities that collapse under one judge question. "Anything not marked is assumed simulated" (§17 §7). The one anti-pattern judges are now *specifically* hunting in AI-built projects. (Disclosed Wizard-of-Oz is legitimate — §14 AP-14/§03 §3.)
2. **AP-15 — Missing UX states** (§14; §17 §5.7). Blank screen during load, silent failure, no empty state. In a 3-minute demo, one missing loading state reads as "it's broken."
3. **AP-12 — Broken interactions** (§14). Dead buttons, forms that lose input, flows that dead-end on the demo path.
4. **AP-09 — AI-generated code without verification** (§14). The demo path was "accepted" without being read; fails on real (non-fixture) data. AI-assisted authors are more confident and less secure (Perry et al., §14 R-20 evidence).
5. **AP-02 — Scope creep** (§14). Fixed clock, growing spec. Kill rule: any feature not serving a judging criterion dies.
6. **§07 V-1/V-2/C-1 — the slop tell.** Purple-glow dark mode, three feature cards, "Transform/Elevate/Unlock" copy. Distributional convergence (§07 §1): thin input produces cliché output. (Proposed) In 48h you can't out-polish; make *one* opinionated identity decision (a type voice, a color role, a compositional stance — §07 §2) and be boring everywhere else. Specificity beats polish.

## 7. Team playbook — role splits + solo-hacker notes

### Team patterns (Verified per source; overall pattern Corroborated)

- **Teammates are the #1 factor.** HN 3-time winner: "at least one 10X programmer on each of my winning teams."
- **Size:** solo = fast prototype/small scope/tiny-but-polished; 2 = split frontend/backend or build/pitch; 3–4 = most stable, clear roles + strict sync points; 5+ = only with disciplined leads (Verified — Hackathon-Starter-Pack guide).
- **Role splits (Inferred from multiple accounts):** Builder(s) + pitch/demo owner is the minimal viable 2-person split. For 3–4: frontend, backend/integrations, demo/pitch + Devpost submission. Non-coders own research/testing/data/demo recording/writeup — but with checkable outputs ("prepare five user-error examples by lunchtime," not "help with product") (dev.to Stavleak guide).
- **Winners allocate roles by strength and practice the story.** "Most teams don't allocate roles based on strengths and don't practice their story." (Corroborated)
- **Agree code ownership/reuse rules before major design work** (Verified — Kurzweil Library winner account). Have a backup location with internet (their venue closed 11pm; they moved and merged until 4am).

### Solo-hacker notes (Verified per source)

- **Scope rule: "tiny scope, polished output."** Solo is viable; breadth is what kills you.
- **Be the domain expert:** solve your own immediate problems first (Corroborated). Depth over breadth — "AI can already do everything mediocre" (listsof30).
- **Solo doesn't mean isolated:** talk to teams, attend workshops (hints/starter code drop there) — "solo grinding" is a documented first-timer mistake (Verified — BizThon 101).
- **If teamless at the event:** use team-matching channels, describe skills honestly, don't promise all-nighters to get invited (Verified — dev.to first-hackathon guide).
- **Solo vs team win rates: Unknown.** No data found. Not guessed here.

## Honest gaps (from `research/`)

- Solo vs team win rates: **Unknown.**
- Live demo vs video, systematic comparison: **Unknown**, format-dependent.
- 48h hour-by-hour winner schedule: sources skew 24h — §3's plan is built from the Corroborated structure and labeled where Proposed.
- Measured score weights, most prize amounts, judge watch behavior: **Unknown or single-source.**
