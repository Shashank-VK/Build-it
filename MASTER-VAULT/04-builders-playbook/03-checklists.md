# 03 — Checklists

Solo-sized, print-friendly. Each item carries its source — a base-report section, or **Proposed** where it's a solo adaptation. Hackathon claims keep their evidence labels (see README for the label key).

## A. Pre-hackathon prep (the week/day before)

Run this before the clock starts. Most hackathon losses are decided here.

- [ ] **Rubric captured:** every judging criterion written down, with your aim for each. (Finding #5 — Verified; adapted from §14 R-01/R-02)
- [ ] **Track picked deliberately:** main track or a less-competitive sponsor/API track chosen on purpose. (Corroborated)
- [ ] **Idea run through the evaluator** (`templates/idea-evaluator.md`): passes the 3-minute demo filter + score-killer screen. (Corroborated)
- [ ] **Boring stack confirmed:** the stack you already know; deploy target decided. (Finding #4 — Corroborated)
- [ ] **Repo initialized, CI green** on a placeholder commit; secret scan added (5 min). (Adapted from §14 R-11/R-15; Proposed for pre-hack timing)
- [ ] **Deploy path tested:** hello-world deploys to a live URL from main in one step — verified *before* the clock starts. (Adapted from §14 R-12/R-25 — Proposed hackathon version: "it deploys from main in one step")
- [ ] **Mock-data plan:** for every live API you'll touch, a fallback mock JSON path is sketched. (Corroborated)
- [ ] **Backup video plan:** camera/screen-recording setup tested, backup location noted (venue wifi is a Corroborated killer).
- [ ] **No secrets in code — from commit 1.** Env-based config only; secret scan runs on every push. (Adapted from §14 R-15)
- [ ] **Pre-hack sit-down done (10 min):** outcome metric (the demo moment), cut list, roles-for-one — in `templates/battle-plan-48h.md`. (Proposed — adapted from project OS §6)
- [ ] **Sleep plan:** "never ship after midnight" applies here too — the phase-4 freeze exists so you're not debugging at 4am. (Proposed — adapted from the Ship gate rules)

## B. During-hackathon — the 3 gates

The distillation's 3 gates for 48h (adapted from §11 §5, Tier-3 calibration per §17 §4.2). Run them at the phase boundaries in `01` §3.

**Gate 8 — Deployment** (end of phase 1, by hour ~12 — Proposed/Inferred boundary):
- [ ] Live URL serves the skeleton. (Corroborated structure)
- [ ] Rollback path known: which commit is the last good one, what command redeploys it. (Adapted from §14 R-25)
- [ ] Repo public-ready: no secrets in history, README exists. (Adapted from §14 R-11/R-15)

**Gate 6 — Testing** (end of phase 2, by hour ~34 — Proposed/Inferred boundary):
- [ ] Demo path exercised end-to-end on production-shaped data, repeatedly — not fixture-perfect data. (Adapted from §14 R-18/R-19)
- [ ] Mock-data fallbacks verified for every live API (rate-limit the API yourself once and watch it fall over gracefully). (Corroborated)
- [ ] Loading/empty/error states present on the demo flow — no blank screens, no silent failures. (Adapted from §14 AP-15, §17 §5.7)

**Gate 5 — Implementation** (continuous):
- [ ] CI green on the exact commit you're demoing. (Adapted from §14 R-13)
- [ ] No secrets in code — scan ran on the current diff. (Adapted from §14 R-15)
- [ ] Every AI-generated diff re-read and explainable by you. Never merge what you can't explain — Perry finding: AI-assisted authors are more confident and less secure (adapted from §14 R-13, AP-09).

## C. Demo-day checklist

- [ ] **Backup video recorded** before the crunch (phase 3) — one team won 1st place on video alone. (Corroborated — finding #1)
- [ ] **Demo script written** (`templates/demo-script.md`): hook → demo → reality inventory → how-it-works → impact close. (Proposed — finding #1 framework)
- [ ] **Reality inventory done:** every shown capability marked Real vs Simulated; simulated = disclosed. Anything not marked is assumed simulated (§17 §7). Undisclosed fakery is §14 AP-14. (Adapted from §17 §7)
- [ ] **No dead controls** on the demo path — every visible button/input does something real. (Adapted from §17 §5.2; §14 AP-12)
- [ ] **No placeholder copy** on the demoed path — no lorem ipsum, no "coming soon" buttons. (Adapted from §17 §5.5)
- [ ] **Video + text description complement each other.** (Corroborated — judge advice)
- [ ] **GitHub is effort-visible:** commits from hour 1, thin repo behind a slick video is a Verified score-killer. (Verified — Databricks judge; adapted from §14 R-11)
- [ ] **Submitted 30 min before the hard cutoff.** Devpost: missed baseline requirements disqualifies more people than you'd think. (Corroborated)
- [ ] **5-minute personal debrief** after: what broke, what do I change. (Proposed — distillation: the 48h ceiling on §14 R-30)

## D. Project launch readiness (for real projects, weeks-long)

The distillation's §17 §6 adapted — steal what matters; full checklist lives in the base report. Items marked Proposed are solo adaptations.

**Technical half:**
- [ ] Tested artefact = shipped artefact (what you tested is what's live). (Adapted from §14 R-12)
- [ ] Rollback rehearsed at least once on the first deploy; rollback command known. (Adapted from §14 R-25, §11 §6)
- [ ] Smoke test passed on production, on the money path, through the real path. (Adapted from §14 R-19, §11 §6)
- [ ] Secrets audit clean; dependency scan run; no hand-rolled auth/crypto. (Adapted from §14 R-15, R-22 floor)
- [ ] ASVS L1 gap register: known gaps listed with dates, not full pass — but gaps are *written down*. (Proposed — adapted from §17 template 13)
- [ ] AI-generated code on critical paths re-read and explainable. (Adapted from §14 R-13)
- [ ] Post-launch evaluation date calendared *before* launch. (Adapted from §17 template 16)

**Real-UX half (run by fresh eyes — you after a break, or a friend on a clean account):**
- [ ] Stranger can complete the core flow on a phone. (Proposed — adapted from §17 §5 acceptance criterion, §14 R-20's inapplicability)
- [ ] All UX states on the core flow: loading, empty, error, destructive-confirm. (Adapted from §17 §5.7)
- [ ] Zero placeholder copy on the core flow. (Adapted from §17 §5.5)
- [ ] Demo authenticity kept: validation demos vs commitment demos distinguished; nothing shown that can't be defended as real. (Adapted from §17 §7)

**Day-two test (Proposed — distillation):** you know within an hour if it's on fire (named check from the Ship gate), and the kill/fix/keep date is in the calendar. If nobody's watching, it isn't launched — it's abandoned at higher resolution.
