# Phase 6 — Autonomous Agent Orchestration Architecture

> Research completed: 2026-08-09
> Decisions locked: 2026-08-10 (all five)
> Phase 8 corrections applied: 2026-08-11
> Status: FINAL — all five questions closed + Phase 8 corrections applied, ready to build
> Sources: Live fetches of cobusgreyling/loop-engineering, Forward-Future/loopy, huangruiteng/loopx READMEs; OpenCode /docs/commands/ and /docs/skills/ pages; loopx CONTRIBUTING.md + docs (user-sourced 2026-08-10); facebook/astryx + @astryxdesign/cli README (direct fetch 2026-08-11); Forward-Future/loopy SKILL.md (direct fetch 2026-08-11)

---

## Decisions Log (Q1-Q4 closed 2026-08-10)

### Q1: loopx vs. walkinglabs overlap — DECISION: SKIP loopx entirely

Source: loopx's own CONTRIBUTING.md and docs (confirmed by user 2026-08-10).

Confirmed facts:
- loopx maintains its own separate state store (.loopx/, .codex/goals/, .local/) with no built-in bridge to feature_list.json or claude-progress.md
- Running both in parallel = two genuinely unsynced sources of truth tracking overlapping things (goals, todos, evidence) — exactly the kind of state-confusion the harness framework exists to prevent
- loopx explicitly requires an external "Turn Loop Controller" to decide when to wake it and call it (its contributing guide: "Do not add a sleep loop, cron implementation, recurring daemon... inside run-once") — that controller doesn't exist in this setup and building it is a whole separate project
- loopx is designed for 200+ wall-clock-hour unattended multi-day runs, not interactive DoD-driven single tasks

Decision: walkinglabs (AGENTS.md + feature_list.json + claude-progress.md) is the sole source of truth.
loopx is removed from this architecture entirely. Revisit loopx specifically if/when real multi-day unattended runs become an actual need — treat it as a distinct future integration project, not a bolt-on.

---

### Q2: Council trigger wording — DECISION: FINALIZED

The following SKILL.md frontmatter is ready to use verbatim:

  ---
  name: two-judge-verification
  description: >
    Auto-triggers before finalizing an architectural decision, choosing
    between competing algorithms/approaches, writing security-sensitive
    code (auth, secrets handling, input validation), or when the primary
    agent's own confidence in an answer is genuinely low. Does NOT
    trigger for routine code edits, small bug fixes, formatting, or
    any change where the correct approach is not actually in question.
    If uncertain whether this qualifies, err toward NOT triggering --
    the cost/latency of a false trigger is not worth it for low-stakes work.
  ---

---

### Q3: Pre-commit hook scope — DECISION: ONLY commits touching feature_list.json

Rationale: Gating all commits blocks legitimate WIP/checkpoint commits that aren't claiming anything is done.
The DoD evidence rule only fires when a feature status actually transitions to "passing".

Hook behavior:
- Diff feature_list.json specifically
- Check whether any feature status is transitioning to "passing"
- If yes: require that feature's evidence[] to be non-empty before allowing commit
- All other commits: pass through untouched

---

### Q4: loopx OpenCode command facade — CONFIRMED, MOOT

Confirmed from loopx docs: installs a static command facade for OpenCode by default (fixed slash commands, not a live poller).
Persistent/recurring goal tracking requires explicit opt-in via --with-goal-bridge flag, not automatic.
Moot since Q1 resolves to skip loopx for now. Recorded here as a confirmed fact for future reference.

---

### Q5: /idea vs /goal naming — DECISION: use /idea, do not adopt goal-engineering

cobusgreyling/goal-engineering is real and pairs with loop-engineering (same author), but its core
mechanism (GOAL.md) is a second persistent state file duplicating feature_list.json/claude-progress.md's
role -- the exact dual-source-of-truth problem Q1 already eliminated by dropping loopx.

Additionally, /goal is not an available name: Grok Build CLI and OpenAI Codex each implement /goal
natively with different, incompatible internal mechanics -- reusing it here would create false
expectations for anyone familiar with either.

Decision: entry command is /idea. goal-engineering is not adopted.

---

## Verification — Confirmed Real Tools (revised after Q1 decision)

| Repo | Status | Role in Architecture |
|---|---|---|
| cobusgreyling/loop-engineering | LIVE | Scaffolding/audit/governance shell — INCLUDED |
| Forward-Future/loopy | LIVE | Skill for designing and running bounded loops (Loop Library catalog) — INCLUDED |
| huangruiteng/loopx | LIVE | State kernel — EXCLUDED (see Q1 decision) |

---

## Architecture: Revised Layer Stack (loopx removed)

ORCHESTRATION LAYER STACK (post-Q1 decision)
=============================================

LAYER: SCAFFOLDING, AUDIT & GOVERNANCE
cobusgreyling/loop-engineering
  loop init      -> scaffold LOOP.md, STATE.md, skills
  loop doctor    -> health check, top-3 next actions
  loop-audit     -> readiness score, governance check
  loop-gate      -> mechanical path denylist enforcement (gate.yaml)
  loop-context   -> circuit breaker for budget/runaway spend
  loop-mcp-server -> exposes patterns + state as MCP tools

     |
     v

LAYER: SKILL FOR DESIGNING AND RUNNING BOUNDED LOOPS
Forward-Future/loopy (as skill — installed via `npx skills add Forward-Future/loopy --skill loopy -g`)
  Find/Craft: selects or designs the right loop for the task type (from live Loop Library catalog or LOOPS.md)
  Run: bounded passes + evidence-backed receipt
  Debrief: receipt -> minimal improvement recommendation
  Save: accepted loops -> LOOPS.md
  NOTE: Run receipts are NOT auto-propagated to feature_list.json evidence[]
  Agent must explicitly record receipt content in evidence[] when loop run serves as DoD verification

     |
     v

LAYER: SESSION STATE (walkinglabs — sole source of truth)
  AGENTS.md          -> startup workflow + working rules + DoD rules + Layer 1/2 boundary
  feature_list.json  -> scope lock (single_active_feature), verification steps, evidence[]
  claude-progress.md -> per-session log: goal, completed, verification, evidence, next step
  init.sh            -> installs deps, runs VERIFY_CMD baseline, confirms starting state is clean

---

## Layer 1 / Layer 2 Boundary (for AGENTS.md)

Proposed text to add to AGENTS.md as a new section:

## Autonomy Boundary -- Required Reading

There are two categories of action in this repository.

### Layer 1: Toolkit Changes (Always Approval-Gated)

The following actions ALWAYS require explicit human approval before proceeding.
Do not attempt them autonomously. Stop and ask.

- Installing any new package, tool, CLI, or MCP server
- Modifying opencode.json
- Modifying AGENTS.md (this file)
- Modifying .git/hooks/
- Modifying gate.yaml or any file that controls what the agent is permitted to do
- Changing model routing, provider configuration, or API credentials
- Adding or removing skills from .opencode/skills/ or ~/.config/opencode/skills/

If any task requires a Layer 1 change to proceed, stop at that step, describe
what is needed and why, and wait for explicit approval. Then resume Layer 2 work.

### Layer 2: Task Execution (Autonomous after /idea or equivalent entry command)

Once a task has been started, the following proceed autonomously without per-step approval:

- Writing, modifying, or deleting code within the active feature scope
- Running the feature verification[] steps from feature_list.json
- Reading and writing claude-progress.md and feature_list.json
- Calling Astryx CLI tools via bash (e.g. `npx @astryxdesign/cli component Button --dense`) as the task requires — NOTE: Astryx has no MCP server; use bash tool calls only
- Calling other registered MCP tools (browser, playwright, etc.) as the task requires
- Loading skills based on context matching
- Triggering the council via the deliberation skill for high-stakes decisions
- Committing code once verification passes and evidence is recorded
- Running loop-engineering CLI tools (loop doctor, loop-audit, loop-context)
- When a loopy Run serves as the DoD §4 verification step: MUST explicitly copy the run receipt content into feature_list.json evidence[] before marking the feature passing — loopy does NOT auto-populate evidence[]

Layer 2 autonomy ends when:
- The feature reaches status "passing" with evidence[] recorded
- A Layer 1 action is required to proceed
- loop-gate or loop-context signals a constraint violation
- /pause is invoked

Do not use Layer 2 autonomy to perform Layer 1 actions via indirect means.

---

## Auto-Triggering: Skills and Council (confirmed from OpenCode docs)

From opencode.ai/docs/skills/ (live fetch 2026-08-09):
- Skills are SKILL.md files in .opencode/skills/<name>/SKILL.md
- The agent loads a skill automatically when the task context matches the SKILL.md description field
- No manual /skill-name invocation required

Council auto-trigger: The finalized two-judge-verification SKILL.md description (from Q2 above) encodes
exactly the conditions that cause the agent to load and run the council without user invocation.

MCP tools: registered in opencode.json (playwright, browsermcp, etc.), called by the agent at any time based on its own judgment. No user-trigger required once registered.

Astryx CLI tools: NOT an MCP server. The agent calls `npx @astryxdesign/cli <command> --dense` as bash tool calls when building UI components. No opencode.json MCP entry needed or valid for Astryx. Run `npx @astryxdesign/cli init` once per project to generate AGENTS.md with component inventory.

---

## Slash Command Suite

From opencode.ai/docs/commands/ (live fetch 2026-08-09):
- Custom commands: .opencode/commands/<name>.md
- Frontmatter: description (shown in TUI), subtask (boolean), template (prompt template)
- Template supports: $ARGUMENTS, $1, $2, etc.
- subtask type: runs without adding to primary conversation thread
- Custom commands can override built-in commands by using the same name

Proposed suite:

.opencode/commands/
  idea.md       -> /idea <task description>
  loop-status.md   -> /loop-status
  loop-doctor.md   -> /loop-doctor
  pause.md         -> /pause
  council.md       -> /council <question>

/[ENTRY COMMAND] <task description>
  Purpose: Entry point for all new task execution. Routes through full DoD pipeline.
  Template:
    New task: $ARGUMENTS
    1. Read claude-progress.md -- confirm current verified state and next best step
    2. Read feature_list.json -- confirm no other feature is in_progress
    3. Run ./init.sh -- confirm baseline is passing before any feature work begins
    4. Use Loopy to find or craft the most appropriate bounded loop for this task
    5. Execute the loop; apply the DoD template as the completion gate
    6. Do not mark the task complete until evidence[] is recorded and verification passes

/loop-status
  Purpose: Non-destructive status check without interrupting execution.
  Template: Read loopy status + feature_list.json in_progress feature + claude-progress.md last entry.

/loop-doctor
  Purpose: Interrupt and audit a running or completed loop.
  Template: npx @cobusgreyling/loop doctor . -- report top-3 issues, flag any runaway signals.

/pause
  Purpose: Gracefully pause autonomous execution, request human review.
  Template: Write pause marker to claude-progress.md, set in_progress feature to "blocked"
  with reason "manual pause". Does not kill work -- suspends and saves state for resumption.

/council <question or context>
  Purpose: Force Two-Judge council review outside its automatic triggers.
  Template: Explicitly invoke two-judge-verification skill with $ARGUMENTS as the question.

---

## Bounded Autonomy Mechanisms (updated after Q1, Q3, and Phase 8 decisions)

| Mechanism | Enforceable? | Implementation |
|---|---|---|
| Path denylist | HARD (already mechanical) | loop-gate gate.yaml |
| Budget/runaway detection | HARD (already mechanical) | loop-context circuit breaker |
| Loop readiness | ADVISORY -> optional CI gate | loop-audit --suggest |
| Single active feature | ADVISORY (AGENTS.md rule) | Agent reads on startup; could be reinforced by hook |
| Evidence before passing | HARD (dual gate: git pre-commit + OpenCode plugin hook) | Git hook blocks ANY commit when active feature is in_progress/blocked; OpenCode plugin hook warns agent before it tries to commit; both required — plugin hook misses out-of-session commits |
| DoD completion | ADVISORY (agent reads AGENTS.md) | Reinforced by dual pre-commit gate |
| loopy receipt propagation | ADVISORY (AGENTS.md rule) | Agent must explicitly copy run receipt to feature_list.json evidence[] — not automatic |

---

## Full Architecture Diagram (loopx removed)

USER                    OPENCODE AGENT                TOOLS & SERVICES
----                    --------------                ----------------

/idea <task>
     |
     v
Read claude-progress.md -----------------------> Current verified state + next best step
Read feature_list.json ------------------------> Scope: one feature at a time
     |
     v
./init.sh --------------------------------------> Install deps, run VERIFY_CMD baseline
     |
     v
Loopy: Find/Craft loop ------------------------> Loop Library catalog + LOOPS.md (project)
     |
     v
loopy: Run (bounded passes)
     |
     +-- Per pass:
     |   [Auto-load skills] -----------------> SKILL.md description matching
     |   [MCP tools] -----------------------> browser, playwright, etc. (opencode.json)
     |   [Astryx CLI] ----------------------> bash: npx @astryxdesign/cli <cmd> --dense (NO MCP)
     |   [High-stakes decision?]
     |       two-judge-verification loads --> deliberation/council-review skill (auto)
     |   Write code / run tests
     |   Check DoD gate:
     |       feature verification[] passed?
     |       evidence[] populated?
     |       pre-commit hook validates -----> Blocks status->passing if evidence[] empty
     |
     +-- Stopping conditions (Loopy enforces):
         Success (DoD gate passes, evidence recorded)
         Clean no-op (no measurable progress)
         Blocker -> write to claude-progress.md, set status "blocked", wait
         loop-context budget exceeded ------> Circuit breaker fires
         loop-gate violation ----------------> Path denylist triggered
         Layer 1 action needed --------------> STOP, describe to user, wait for approval
         /pause invoked
                 |
                 v
       Update claude-progress.md (completed, verification run, evidence, next best step)
       Update feature_list.json (status -> "passing")
       Commit with descriptive message
       Repo clean for next ./init.sh

---

## Summary Table (revised — Phase 8 corrections applied)

| Component | Role | Tool | Trigger |
|---|---|---|---|
| Loop scaffolding | Scaffold LOOP.md, STATE.md, budget, skills | loop init | Manual, one-time setup |
| Readiness check | Scores loop health, top-3 gaps | loop-audit | Auto (on loop start) or /loop-doctor |
| Health audit | Top-3 issues, interrupt | loop doctor | Manual (/loop-doctor) |
| Path denylist | Prevents scope creep to forbidden files | loop-gate gate.yaml | Hard (mechanical) |
| Budget/runaway | Kills runaway long-runs | loop-context circuit breaker | Hard (mechanical) |
| Loop selection/design | Finds or designs the right bounded loop | loopy (skill) Find/Craft | Auto (agent calls) |
| Loop execution | Bounded passes with receipts | loopy (skill) Run | Auto |
| loopy receipt → evidence | Propagate run receipt into feature_list.json evidence[] | Agent manual step (AGENTS.md rule) | After any loopy Run used as DoD verification |
| Session state | Progress log, feature tracker, DoD | walkinglabs templates | Auto (agent reads/writes) |
| Skill loading | Context-appropriate skills | OpenCode SKILL.md | Auto (description matching) |
| Astryx UI components | Design system component docs + search | @astryxdesign/cli bash calls (NOT MCP) | Auto (agent uses bash tool) |
| MCP tool calls | browser, playwright, etc. | opencode.json MCP | Auto (agent judgment) |
| Council review | Two-judge verification | two-judge-verification SKILL.md | Auto (description match) + /council manual |
| DoD gate (hard) | Blocks any commit when feature not passing | git .git/hooks/pre-commit | Hard (fires on ALL commits, any tool) |
| DoD gate (early warning) | Warns agent before commit attempt in-session | OpenCode tool.execute.before plugin | Auto in-session only |
| Status check | Non-destructive status report | loopy + feature_list.json | Manual (/loop-status) |
| Graceful pause | Suspend + save state | custom command | Manual (/pause) |
| Layer 1 gate | Blocks toolkit changes | AGENTS.md rule + human approval | Always manual |

---

## Open Questions

None. All five questions (Q1-Q5) are closed. Architecture is final.

| Q | Decision |
|---|---|
| Q1 | Skip loopx; walkinglabs is sole source of truth |
| Q2 | Council SKILL.md description finalized (verbatim in Decisions Log) |
| Q3 | Pre-commit hook gates only on feature_list.json status -> "passing" transitions |
| Q4 | loopx static command facade confirmed; moot (Q1 skips loopx) |
| Q5 | Entry command is /idea; goal-engineering not adopted |


