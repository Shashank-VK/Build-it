# BUILDER-RULES.md — Universal External Product Builder & Socratic Spec Engine
# Tag this file (@BUILDER-RULES.md) in ANY project folder across OpenCode, Claude Code, Antigravity, Cursor, Codex, or Windsurf.

You are connected to **BUILDER-OS** located at:
`BUILDER_OS_ROOT = /mnt/c/Users/Shashank Karamudi/Desktop/BUILDER-OS`

## CRITICAL FOLDER CLEANLINESS RULE
- The user is working inside their **Target Project Folder** (default: the current working directory `pwd`, or the folder path the user specifies).
- **Keep the Target Project Folder root clean**: Only `./specs.md` and actual application files (`src/`, `tests/`, `package.json`, `README.md`, etc.) belong in the project root.
- **All harness state, logs, and OS artifacts MUST live inside `./.builder-os/`** (`./.builder-os/feature_list.json`, `./.builder-os/claude-progress.md`, `./.builder-os/init.sh`, `./.builder-os/build-log.md`, `./.builder-os/grill-notes.md`, etc.).
- **NEVER use or install `caveman`.**

---

## STEP 0: AUTOMATIC STATE DETECTION (RUN THIS FIRST ON EVERY SESSION)

As soon as the user tags or reads `BUILDER-RULES.md`, check the Target Project Folder for `./specs.md`:

1. **CASE 1 — `./specs.md` DOES NOT EXIST YET (or user explicitly asks to plan/grill)**:
   - Go immediately to **STAGE 1 (The 2-Question Intake)**.
2. **CASE 2 — `./specs.md` ALREADY EXISTS IN THE PROJECT FOLDER**:
   - Check if `./.builder-os/feature_list.json` has uncompleted features (`not_started`, `in_progress`, or `blocked`).
   - Do **NOT** re-interview the user! Announce:
     > *"Found locked `specs.md` (and `.builder-os/` state). Entering **STAGE 3 (Autonomous Build & Verification Pipeline)**..."*
   - Jump straight to **STAGE 3** and start/resume building the product immediately!

---

## STAGE 1: THE 2-QUESTION INTAKE (WHEN NO `specs.md` EXISTS)

If the user has not already stated their mode and idea/PRD in their first message, ask **ONLY these two questions** and stop for their reply:

> **1. Choose Your Mode:**
> - **Option A — Grill Mode (Interactive Brainstorm, One Question at a Time)**: You give me your rough idea or PRD, and I will interview you **one question at a time** (with multiple-choice options + my architectural recommendation) so we can brainstorm deeply. At the end, I will generate a complete `specs.md` + `.builder-os/feature_list.json` in your project folder so you can build in a fresh context window.
> - **Option B — Auto Mode (Zero Questions Asked)**: You give me your idea or PRD, and I will make all architectural, stack, UX, and edge-case decisions on my own, write `specs.md` + `.builder-os/`, and build the entire verified product end-to-end without stopping.
>
> **2. Your Idea / PRD & Target Folder:**
> - Share your idea or PRD (paste it or give the file path), and confirm if we are building in the current folder (`pwd`) or a specific folder path.

---

## STAGE 2A: GRILL MODE PROTOCOL (ONE QUESTION AT A TIME -> `specs.md`)

When the user selects **Grill Mode**:
1. Initialize `./.builder-os/` by running:
   `bash "/mnt/c/Users/Shashank Karamudi/Desktop/BUILDER-OS/scripts/init-project-subfolder.sh" "<target-folder>"`
2. Read the Socratic runbook at `/mnt/c/Users/Shashank Karamudi/Desktop/BUILDER-OS/.harness/skills/36-grill-me-socratic-planner/SKILL.md` and Domain checklists at `/mnt/c/Users/Shashank Karamudi/Desktop/BUILDER-OS/os/domains/`.
3. **STRICT ONE-BY-ONE INTERVIEW RULE**:
   - **Ask strictly ONE question per turn.** Never dump multiple questions at once.
   - For **every single question**, provide:
     1. **Why this matters** (1 short sentence).
     2. **3–4 concrete options (A, B, C, D)** with brief pros/cons.
     3. **My Recommendation** (which option fits best and why, while inviting brainstorming or custom answers).
   - **Incremental Save**: After every user answer, append the Q&A decision to `./.builder-os/grill-notes.md` so zero progress is ever lost if the context window fills up.
   - Dig deep across these 6 areas (skipping anything already answered in their PRD):
     1. Core problem, target user flow, and explicit **Non-Goals (No-Gos)**.
     2. Tech stack (Frontend, Backend/API, Database, Auth).
     3. Data model, core entities, and API/state boundaries.
     4. UI/UX aesthetic style (referencing `BUILDER_OS_ROOT/vault-reference/02-god-research/agy-thirdpass/02-design-styles.md`), animations, and UX states (loading, empty, error, offline).
     5. Edge cases, failure modes, rate limits, and security/privacy constraints.
     6. Verification criteria & deployment target.
4. **Locking `./specs.md` & `./.builder-os/feature_list.json`**:
   - Once all questions are answered (or whenever the user says *"that's enough, generate specs.md"*), synthesize everything into:
     1. **`./specs.md`** (in the Target Project Folder root): Complete Product & Technical Specification (Overview, User Flows, Explicit Non-Goals, Tech Stack, Visual & UX Design Contract, Database Schema, API Contracts, Security & Failure Modes, Ordered Feature Breakdown, and Verification Commands).
     2. **`./.builder-os/feature_list.json`**: Populate all ordered features (with **UPHILL / hardest features first** per `unknown-first-sorter`), `status: "not_started"`, and explicit `verification[]` steps.
     3. **`./.builder-os/pitch.md`, `prfaq.md`, `design-note.md`**: Populate the OS gate artifacts automatically from the locked spec.
   - Stop and tell the user:
     > ✅ **`./specs.md` and `./.builder-os/feature_list.json` are locked and saved on disk!**
     > To build with a 100% fresh context window, open a **new session** in this folder and type:
     > `"Read @BUILDER-RULES.md and build specs.md"` (or tell me `"build now"` to start in this session).

---

## STAGE 2B: AUTO MODE PROTOCOL (ZERO QUESTIONS -> `specs.md` -> IMMEDIATE BUILD)

When the user selects **Auto Mode** (or says *"don't ask me anything"*):
1. Ask **ZERO questions**.
2. Run `bash "/mnt/c/Users/Shashank Karamudi/Desktop/BUILDER-OS/scripts/init-project-subfolder.sh" "<target-folder>"`.
3. Resolve any unstated choices using BUILDER-OS Verified Defaults:
   - **Web**: Next.js 15 (App Router) or Vite + React 19, TypeScript (strict), Tailwind CSS + `shadcn/ui` or Meta `facebook/astryx` (`--dense`).
   - **Backend/API**: Python 3.12 + FastAPI + Pydantic v2 (or Next.js Server Actions / Hono), OpenAPI 3.1 contract-first.
   - **Database**: PostgreSQL or SQLite (local MVP), 3NF normalized.
   - **Mobile**: Kotlin + Jetpack Compose + Room.
   - **UX/Design**: Full UX states (loading skeletons, empty, error, keyboard accessible) + `laws-of-ux-skills` + `taste-skill` + `stop-slop`.
4. Generate `./specs.md` in the project root AND populate `./.builder-os/feature_list.json`, `pitch.md`, `prfaq.md`, `design-note.md`, and `build-log.md`.
5. Proceed **immediately** into **STAGE 3** without stopping.

---

## STAGE 3: AUTONOMOUS BUILD & VERIFICATION PIPELINE (READS `./specs.md`)

When `./specs.md` exists (either in a fresh Session 2 or continuing from Auto Mode):
1. **Load State & Skills**:
   - Read `./specs.md`, `./.builder-os/feature_list.json`, and `./.builder-os/claude-progress.md`.
   - Consult `/mnt/c/Users/Shashank Karamudi/Desktop/BUILDER-OS/.harness/skills/index.json` and load relevant `SKILL.md` runbooks from `/mnt/c/Users/Shashank Karamudi/Desktop/BUILDER-OS/.harness/skills/` (`07-api-contract-first`, `08-database-schema-architect`, `21-tdd-red-green-refactor`, `22-playwright-e2e-matrix`, `23-pytest-fixture-factory`, `31-owasp-top10-vuln-scanner`, `35-cryptography-safe-patterns`, `two-judge-verification`).
2. **Configure `./.builder-os/init.sh`**:
   - Set `INSTALL_CMD`, `VERIFY_CMD`, and `START_CMD` in `./.builder-os/init.sh` to match the stack in `./specs.md`.
   - **Command paths are relative to the PROJECT ROOT, not to `.builder-os/`.** `init.sh` runs its commands from the project root automatically (it detects that it lives in `.builder-os/` and uses the parent directory). You can still override with the `PROJECT_ROOT` env var if the project root is somewhere else.
3. **Execute One Feature at a Time (`single_active_feature` Rule)**:
   - Pick the highest-priority `not_started` (or `in_progress`) feature in `./.builder-os/feature_list.json` and mark it `"in_progress"`.
   - Use `context7` MCP to pull live documentation for libraries in `./specs.md`.
   - **TDD Loop (`21-tdd-red-green-refactor`)**:
     1. **Red**: Write the failing unit/integration/E2E test first.
     2. **Green**: Write minimal, strictly-typed code to pass the test.
     3. **Refactor**: Clean up code, run linters/typechecks, and check OWASP rules (`31-owasp-top10-vuln-scanner`).
   - **UI Browser Verification (for Frontend Features)**:
     - Start the dev server in the background and use `playwright` MCP (`22-playwright-e2e-matrix`) to inspect the live DOM, layout, accessibility, and console errors.
   - **Evidence & Commit Gate**:
     - Run `./.builder-os/init.sh` and confirm exit code `0`.
     - Record the test receipt and SHA in `./.builder-os/feature_list.json` (`evidence[]`) and `./.builder-os/build-log.md` (`## Evidence`).
     - Mark the feature `"passing"`, update `./.builder-os/claude-progress.md`, and `git commit` (enforced by `.git/hooks/pre-commit`).
   - Repeat for the next feature until every feature in `./.builder-os/feature_list.json` is `"passing"`.
   - **Context Window Guard**: If context exceeds ~70% (28k tokens) mid-build, run `03-context-compaction-pruner`, save state to `./.builder-os/claude-progress.md`, and let the user know they can open a fresh session and tag `@BUILDER-RULES.md` to seamlessly resume the remaining features.
4. **Final Gate 6 Verification**:
   - Run `/mnt/c/Users/Shashank Karamudi/Desktop/BUILDER-OS/scripts/secret-scan.sh .` and `./.builder-os/init.sh`.
   - Only declare the project complete when all features are `"passing"` and all tests/linters exit with code `0` (Evidence-Carrying Termination).

---

## SKILL PRECEDENCE RULE

When working inside a BUILDER-OS project, ALWAYS prefer the `bos-*` skills in
`BUILDER_OS_ROOT/.harness/skills/` over any similarly named global skill. The
`bos-*` skills carry this OS's exact completion gates and verification
assertions; the global equivalents do not. If a global skill and a `bos-*`
skill both match your trigger, load the `bos-*` one.

Global skills that overlap with the OS are stored inertly in
`~/.agents/library/` and are NOT auto-loaded. If you need one, promote it with
the `/promote-skill` command.
