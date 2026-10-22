# PRD: [Project Name]

> **Execution Mode** (uncomment one):
> - `MODE: INTERACTIVE` (Default — Grill me once with 5-7 batched questions if anything is missing)
> - `MODE: FULL_AUTO` (Don't ask me anything — decide on your own using BUILDER-OS defaults and build end-to-end)

## 1. What We Are Building (Problem & Core Value)
- **Target User**: 
- **Core Problem**: 
- **One-Sentence Solution**: 

## 2. Key Features (Must-Haves)
1. 
2. 
3. 

## 3. Explicit Non-Goals (No-Gos — Min 2)
- Does NOT include: 
- Does NOT include: 

## 4. Tech Stack & Design Preferences (Leave blank to let BUILDER-OS decide)
- **Frontend / UI**: 
- **Backend / API**: 
- **Database**: 
- **Appetite (Time/Complexity Budget)**: 

---

## How to use this template

1. Fill in sections 1-4. Section 4 may be left blank in `INTERACTIVE` mode —
   `BUILDER-OS` applies its Default Stack & Design Contract for anything
   unspecified, and asks you once about anything genuinely ambiguous.
2. Set `MODE:` explicitly. In `FULL_AUTO` mode the agent asks **zero**
   questions and builds the entire product end to end using the defaults.
3. Sections 1 and 3 are the two the OS enforces hardest: no appetite and
   fewer than 2 explicit No-Gos means Gate 3 cannot pass.
4. After the PRD is accepted, the pipeline is:
   PRD -> PR/FAQ -> Pitch -> Design Note -> FCAR -> Scope Lock -> TDD Loop
   -> Launch Checklist. See `AGENTS.md` for the full 5-phase contract.

## What happens next

`BUILDER-OS` will:

- **Phase 1** — Survey the codebase and scaffold `projects/<name>/`.
- **Phase 2** — Draft the PR/FAQ and Pitch, write the Design Note with at
  least 2 alternatives, and run the Two-Judge council review (`bos-*` skills).
- **Phase 3** — Lock scope into `feature_list.json` with uncertain work first,
  and configure `init.sh` with real install/verify/start commands.
- **Phase 4** — Work one feature at a time, test-first, recording evidence for
  every feature marked `passing`.
- **Phase 5** — Security scan, launch checklist, and final verification.
