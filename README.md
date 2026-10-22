# BUILDER-OS & MASTER-VAULT — How to Use Efficiently

You never need to work inside the `BUILDER-OS/` or `MASTER-VAULT/` folders.
You build your projects inside **any clean folder you open**, and control everything by tagging **`@BUILDER-RULES.md`**.

---

## 1. Where Everything Lives (Quick Overview)

- **`Desktop/BUILDER-OS/BUILDER-RULES.md`** -> **The ONLY file you tag (`@BUILDER-RULES.md`)** when starting or resuming a project.
- **`Desktop/BUILDER-OS/BOOTSTRAP-ONCE.md`** -> One-time setup prompt if you ever install a new IDE/harness or move to a new PC.
- **`Desktop/BUILDER-OS/`** -> The active engine (25 core skills in `.harness/skills/`, 15 workflows, 4 subagents, `os/` rules, templates, and `scripts/verify.sh`).
- **`Desktop/MASTER-VAULT/`** -> Your read-only backup library (851 files across `01-opencode-research`, `02-god-research`, `03-solo-levelling`, `04-builders-playbook`, `05-superior-os`).
- **`~/.agents/skills/` & `~/.agents/library/`** -> Your global cross-tool skills (`skills/` is active; `library/` holds ~98 extra skills you can activate anytime via `/promote-skill`).

---

## 2. The Best Workflow (2-Session Method to Beat Context Limits)

### Session 1: Brainstorm & Create `specs.md`
1. Open your IDE/harness in **the folder where you want to build your project** (e.g., `Desktop/my-app/`).
2. Tag **`@BUILDER-RULES.md`** (`Desktop/BUILDER-OS/BUILDER-RULES.md`).
3. The agent will ask you two things: **Which Mode?** and **What is your Idea/PRD?**
   - **Pick Grill Mode** if you want to brainstorm:
     - It asks you **one question at a time** (with A/B/C options + its recommendation).
     - Every answer is saved live into `./.builder-os/grill-notes.md`.
     - When finished, it writes **`./specs.md`** in your project root and locks the feature queue in **`./.builder-os/feature_list.json`**.
   - **Pick Auto Mode** ("don't ask me anything") if you want zero questions:
     - It decides the stack, architecture, DB, and UX states on its own, writes `./specs.md`, and starts building immediately.

### Session 2: Build with a 100% Fresh Context Window
1. After Grill Mode finishes creating `./specs.md`, open a **new chat session** in that same project folder.
2. Type:
   > **`Read @BUILDER-RULES.md and build specs.md`**
3. Because `./specs.md` already exists on disk, the agent skips all questions and immediately builds your app feature-by-feature (writing tests first, checking live docs via `context7`, verifying UI in `playwright`, and saving all harness logs cleanly inside `./.builder-os/`).

---

## 3. Useful Commands During a Build
- **`/loop-status`** -> Check which feature in `.builder-os/feature_list.json` is currently being built.
- **`/council <question>`** -> Run the Two-Judge Council (Devil's Advocate vs. Steelman) on any tough decision.
- **`/pause <reason>`** -> Save progress to `.builder-os/claude-progress.md` so you can close the window and resume later in a fresh session.
- **`/promote-skill <name>`** -> Move a specialized skill from `~/.agents/library/` into active `~/.agents/skills/`.

---

## 4. Golden Rules (DOs & DON'Ts)
- **DO** work in your own project folders and tag `@BUILDER-RULES.md`.
- **DO** start a fresh session once `specs.md` is ready so the coding agent gets the full context window.
- **DO NOT** edit or run tests directly inside `MASTER-VAULT/` (keep it as your untouched backup).
- **DO NOT** move all 98 skills from `~/.agents/library/` into `~/.agents/skills/` at once (causes prompt bloat).

---

## 5. Reference

- **`MAP.md`** -> complete file map of every folder and file across `BUILDER-OS/`, `MASTER-VAULT/`, and `~/.agents/`.
- **`ALL-IN-ONE.md`** (on the Desktop) -> every file concatenated into one file, for search, archiving, or sharing offline.
- **`BUILDER-OS/README-OS.md`** -> the engineering documentation for the OS itself (loop rails, gates, evidence contract).
