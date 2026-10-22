# 02 — Project Execution Plan (the personal project OS)

Adapted from the workstream-3 project-OS design handoff (full version, ephemeral scratch — all components below are **Proposed**). Sources adapted: base report §03 (12-stage lifecycle), §11 (9 quality gates), §14 (34 rules), §17 (18 templates), and the 2–8-person small-team OS shrunk to n=1. Same standing assumptions as the README: stack-agnostic, solo, experience unknown.

## 1. The 6 phases + gates

§03's twelve stages collapse into six — Problem→Idea→Validation merge into two phases, because a solo builder running 5–10 story interviews per idea will never ship anything. The evidence ladder's value is preserved in cheaper form (Proposed).

### Phase 1 — Intake
Every idea goes into one capture list within 24h of having it. Write *the problem it solves* in one sentence — an idea without a problem attached gets flagged. No research, no estimates, no guilt.
**Exit gate (2 min):** idea written, problem sentence present, source noted. Done = one list, zero headnoise.

### Phase 2 — Quick validation
Pick the single riskiest assumption (usually "will anyone care" = value risk, §03). Run the cheapest test that could prove you wrong: 2–3 user conversations, a fake-door page, a concierge test, a pricing probe. Timebox: ≤2 days. **Pre-commit the kill criterion *before* the test** (adapted from §17 §3 validation gates).
**Exit gate:** verdict against the pre-committed number: VALIDATED / INVALIDATED (kill with a one-line lesson) / UNCLEAR (one cheaper follow-up, then it dies or proceeds). Two inconclusives = invalidated (adapted from §03 §3, Proposed).

### Phase 3 — Light spec (the one-page bet doc)
Proposed adaptation of §17 template 03-prd.md: press-release paragraph, outcome metric + target + window, non-goals, appetite (timebox), kill/fix/keep evaluation date. Scope by appetite: **fix the time, flex the scope** (§14 R-05). Write the **cut list in the same sitting** — the cut list is the spec's most important section (adapted from §17 §2 decision-criteria gate: any single Fail → reject, not "research more").
**Exit gate — the cold-read test:** can a stranger (or you, 2 weeks later) read the page and know what to build and what to cut? Acceptance criteria are observable outcomes, not implementation (§03 §4).

### Phase 4 — Build
Decompose into tasks that each fit one reviewable change (§14 R-14, ~100 lines as orientation). Trunk-based: integrate daily; hide unfinished work behind flags, not branches (§03 §7). AI-generated code gets *more* scrutiny, not less — you must be able to explain every diff you ship (§14 R-13; the Willison boundary). Agent instructions per repo live in a 20-line AGENTS.md (adapted from §17 template 09).
**Exit gate — the Merge gate:** CI green, no secrets, critical-path tests pass, you re-read the diff and can explain every hunk.

### Phase 5 — Ship
Deploy the tested artefact (§14 R-12). Rehearse rollback once on the first deploy. Watch window 24–72h with a named check (what metric would tell you something broke?). Post-launch evaluation date scheduled *before* launch, copied from the bet doc (adapted from §17 template 16).
**Exit gate — the Ship gate:** rollback path exists, smoke test passed on prod, monitoring covers the new failure modes, post-launch eval is calendared.

### Phase 6 — Iterate
Judge the bet against its pre-committed metric. Verdict per §14 R-34: **keep / fix / kill**. Fix goes back to phase 2 or 3; dead features get *deleted* (§14 R-16), not archived.
**Exit gate:** keep/fix/keep decision dated with the metric number written next to it — no "let's give it more time" without a new test.

**What was cut from §03 and why:** separate Architecture and Foundations phases — a solo builder's architecture *is* the boring default (modular monolith on managed services; §03 §5), and foundations are a one-time setup (day-one ritual, not a recurring phase). Prototype is absorbed into validation (the prototype *is* the test at solo scale). Design merges into the light spec — fat-marker sketches, borrowed components, UX-states checklist on the demoed flow only.

## 2. The 4 solo gates (9 report gates → 4)

Constraint: **a gate that needs a second human must become automatable or become a ritual you can run against yourself in minutes** (Proposed). Verdicts kept: GO / NO-GO / NOT ASSESSED — unknowns never pass (§17 §4.1).

| Report gate | Solo verdict | What survived |
|---|---|---|
| G1 Discovery | MERGED → **Bet gate** | Kill criterion pre-committed before the test; one commitment signal (time, data, money) for bets >2 weeks of appetite; dated proceed/kill. Cut: 12-row checklist → 3 rows; 5–10 interviews → 2–3 conversations or one behavioral test (cut because the evidence ladder is right at team scale but paralyzing solo — the *commitment hierarchy* survives, the *sample size* doesn't). |
| G2 Spec | MERGED → **Bet gate** | One-page bet doc; observable, testable acceptance criteria; explicit non-goals. Cut: EARS formalization → plain "when/then" sentences; versioned spec → versioned file in the repo. |
| G3 Design | MERGED → **Bet gate** | UX states (loading, empty, error, destructive-confirm) sketched for the demoed flow; borrowed component library (§14 R-07). Cut: contrast records, keyboard specs → "a stranger can use the core flow on a phone." |
| G4 Prototype | MERGED → **Bet gate** | Riskiest assumption named, cheapest test designed, learnings memo = 3 lines in the build log. Cut: formal memo, named decider. |
| G5 Implementation | SURVIVES → **Merge gate** | CI green on the exact commit, secrets scan clean, you re-read the full diff and can explain every hunk (§14 R-13/R-20 adapted: the "second pair of eyes" becomes cold-read + checklist — AI pre-review is triage, never the only reviewer, per §17 template 11). Cut: formal approval, axe report → "no new obvious a11y breakage on the demoed flow." |
| G6 Testing | MERGED → **Release gate** | Critical paths tested through the real path (§14 R-18/R-19); flaky tests are defects, not passes (§03 §8). Cut: full test plan → test cases live in the build task itself. |
| G7 Security review | MERGED → **Release gate** | 10-minute threat model on trust boundaries (auth, payments, user data) — kept, because retrofitted security is architecture-shaped (§03 §5; §14 R-09's own exception allows the 10-min version). Secrets audit, dependency scan, ASVS L1 *gap register* (not full pass) before internet-facing launch. Cut: signed review → dated log line. |
| G8 Deployment | SURVIVES → **Ship gate** | Staged deploy (or at minimum: deploy ≠ big-bang on a Tier-1 surface), rollback path rehearsed once, smoke test on prod, deploy log with commit hash. Cut: required reviewers, wait timers → the personal rules: **never ship after midnight, never ship without a rollback you've actually run once.** |
| G9 Post-launch | SURVIVES → **Watch gate** | Watch window with a named symptom metric (golden signals, §14 R-28), incident notes in the log, blameless retro for anything significant — blameless *toward yourself* is the point; self-blame with no action items is the failure mode (§14 R-30). Kill/fix/keep date calendared before launch (adapted from §17 template 16). Cut: on-call rotation, SLOs → one alert you'll actually receive and act on (§14 R-29: an alert you ignore is decoration). |

**Net: Bet, Merge, Release, Ship, Watch.** Every gate keeps the evidence principle (§17 §4.1): a green build, a pretty screenshot, or an agent's "done" never counts as proof — the artifact is the dated line in the build log.

## 3. The weekly planning ritual (~30 min, same slot weekly)

1. **Review (10 min):** read last week's build-log entries. Mark each active bet: on track / stuck / dead.
2. **Close the loop (5 min):** anything past its kill/fix/keep date gets the verdict *now* — keep, fix (new bet), or kill (delete + one-line lesson). No "let's see" without a new pre-committed test.
3. **Place bets (10 min):** 1–3 bets for the week, each with a fixed appetite (days, not scope — §14 R-05). Each bet: one-line outcome + cut list. **Everything not bet on is explicitly not being done this week** — write the "not this week" list; that's the anti-backlog.
4. **Schedule the first action (5 min):** each bet's next concrete step is calendared. A bet with no first action is a wish, not a plan.

### The pre-build sit-down (~45 min, before any new project)

1. **Write the one-page bet doc** (phase 3).
2. **Set the appetite as a date, not an estimate** (§14 R-05). "Two weeks" beats "about 60 hours" — the date forces the cut list.
3. **Write the cut list.** If you can't name three things you're *not* building, the scope isn't real — you're holding a wish list (adapted from §17 template 03's non-goals, made mandatory and celebrated: the solo failure mode is scope creep with no one to say no).
4. **Name the kill criterion.** What number, by what date, ends this? (Adapted from §17 §2.)
5. **Record the boring defaults** (§03 §5): modular monolith, managed Postgres-or-equivalent, managed hosting, one repo. Any deviation gets a one-line ADR: *context / decision / why / what would reverse it* — 5 minutes, `docs/adr/NNNN-title.md` (adapted from §17 template 05, Proposed scope-down).

## 4. The build log habit (<5 min/day)

One file per project, plain markdown, append-only. **Write it before you close the laptop.** If it takes more than 5 minutes you're writing a blog post, not a log.

```markdown
## 2026-10-10
- **Status:** one line — where the build stands tonight.
- **Changed:** what actually changed (commits / files / deploys). Link, don't describe.
- **Decisions:** what you decided + one line of why. (The solo ADR — §14 R-06 shrunk to a bullet.)
- **Blockers:** what's stuck, and the next concrete step to unstick it.
- **Gates:** any gate run today and its verdict (GO / NO-GO / NOT ASSESSED).
```

Five bullets. The log is the evidence artifact for every gate (§17 §4.1). Fill `templates/build-log.md` — same format, ready to copy.

## 5. Retrospective format (15 min, within 48h of the verdict)

Timer on. Three sections, bullets only (fill `templates/project-retrospective.md`):

```markdown
## Retro — <project> — <date>
**Verdict:** keep / fix / kill + the metric number that decided it.

**Repeat (what worked — do this again):**
- ...

**Kill (what to stop doing — the system fix):**
- ... → each "kill" gets one concrete change to the OS above (a gate tweak, a ritual change, a default). A retro with no system change is a diary entry.

**Lessons for future ideas (what would change the decision):**
- ... (one-liners; they feed the parking lot — "future ideas will rhyme with this one; the record is the asset," adapted from §17 §3.3.)
```

Blameless by construction (§14 R-30): "human error" — yours included — is the start of the investigation, never the conclusion. Always ask *what in the system allowed this*, hence the mandatory "kill" section producing an OS change. (Adapted from §17 templates 15 + 16, merged and shrunk: the report separates incident retros from bet evaluations; at solo scale the project retro *is* both, run once at the verdict.)

## 6. Hackathon mode vs project mode

Under 48h pressure the OS compresses by phase. The principle (adapted from §03 §13's risk tiers): **gates scale, never vanish** — Tier-3 posture, lightweight but present.

| OS element | Project mode | Hackathon mode (48h) |
|---|---|---|
| Validation (phase 2) | ≤2 days, commitment signal for big bets | ≤2 hours. One falsifiable question, one cheap test. Kill criterion = "would a judge/user care enough to click twice." What dies: statistical seriousness. |
| Light spec (phase 3) | One-page bet doc | Napkin spec — outcome metric (usually: *demo moment lands*), demo-path scope, cut list (becomes the *demo scope list* — what the demo will NOT show). The cut list is sacred even here: the #1 hackathon failure is a half-built second feature eating the first. |
| Build (phase 4) | Small tasks, CI, tests on critical paths | One repo, commit often, CI = "it builds." Tests: demo path only, through the real path. **Dropped:** ADRs (one-liners in the log), test plans, code-review ritual beyond the cold read. |
| Ship (phase 5) | Staged deploy, rehearsed rollback | Deploy the tested artefact, smoke-test the demo path on prod, know the rollback command. **Dropped:** staged rollout, wait timers. **Stays sacred:** the deployed thing = the thing you tested (§14 R-12). |
| Gates | Bet → Merge → Release → Ship → Watch | **Bet → Merge → Ship.** Release merges into Merge (one checklist: real path works, no secrets, demo path solid). Watch becomes "demo watch": who restarts it if it dies mid-demo. |
| Build log | 5 bullets/day | Decisions + blockers only, 2 minutes. Still matters — it's your demo narrative and your post-hack writeup. |
| Retro | 15 min, system fix | 5 min, same three questions, asked over food after. **Not dropped** — the hackathon is where your OS learns fastest, and it's the cheapest lesson you'll ever buy. |
| Weekly ritual | 30 min | **Dropped entirely** — replaced by the 10-minute pre-hack sit-down: outcome metric (the demo moment), cut list, roles-for-one. |

**What stays sacred in hackathon mode (non-negotiable even at 48h):**
1. **Git from the first commit** (§14 R-11).
2. **No secrets in code** (§14 R-15 — automatable, costs nothing, leak is forever).
3. **The demo path is a real code path** (§17 §7): reality inventory done honestly; anything simulated is *disclosed*. Undisclosed fakery in a judged demo is §14 AP-14 — and it breaks on stage.
4. **Every visible control does something real** on the demo path (adapted from §17 §5 functional completeness) — one dead button in front of judges costs more than the feature you cut to fix it.
5. **The cut list exists before coding starts.** In project mode it protects the calendar; in hackathon mode it protects the demo.

**What gets dropped without guilt:** architecture deliberation (boring defaults, decide on pain — §03 §5), the full template set (§17's 18 collapse to: napkin spec + build log + retro), security beyond the 10-min threat model and secrets scan, monitoring beyond "does the demo path work right now," and any process whose maintenance cost exceeds its 48h value.

## 7. The "idea → started → abandoned" syndrome

The solo builder's modal failure (§03's evidence ladder: Level 0–1 evidence committing build-scale resources is the modal postmortem failure). Treat it as a system problem, with three mechanisms (all Proposed):

1. **Cap WIP at 2 active builds.** Starting #3 requires killing or parking one first — in writing, with the reason. (Adapted from the Shape Up "bets, not backlogs" insight.)
2. **Parked ≠ abandoned.** Parking an idea requires a *revisit trigger* ("revisit when X"), dated — a deferred idea without a trigger is a rejected idea lying to itself (§03 §2). No trigger → it's killed, lesson logged, guilt discarded.
3. **The abandonment retro (5 min, when you stop something):** what was believed, what was tested, what was learned, what would change the decision (adapted from §17 §3.3's stop discipline). The pattern across three abandonments is data: if you always abandon at week 3 when integration gets hard, that's not an ideas problem, it's an appetite/scope problem — the fix is smaller appetites, not more willpower.

## Open caveats (kept honestly — don't work around these, know them)

- **The "second pair of eyes" problem is unsolved, not solved.** The Merge gate substitutes a cold read + checklist for §14 R-20's independent reviewer. The report's evidence (Perry et al.) says AI-assisted authors are *more* confident and *less* secure — a solo builder re-reading their own AI-assisted diff is the weakest link in this OS. Honest options: AI pre-review as adversarial triage + a "sleep on it" rule for auth/money/migration diffs, or a buddy-review exchange with another builder.
- **Evidence levels are deliberately lowered** (2–3 conversations vs 5–10 interviews). This trades false negatives (killing good ideas) against the solo builder's actual constraint (time). The commitment hierarchy (§03 §3) is the load-bearing part that survives.
