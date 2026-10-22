===== ADDENDUM — Part 12 extension: builders-playbook overlap rows (preserve-both, mirrors output/12-diffs-adjudication.md tail) =====
| # | Overlap | Existing claim (Parts 00-13) | Builders-playbook note (Parts 14-17) | Kept as |
| B1 | METR/Cui productivity dispute | Cui +26% less-experienced vs METR −19% experts (population/task, no unifying study) | Same RCTs cited (METR n=16 −19%, Cui n=4,867 +26%, Peng +55% lab-only); aggregates +7–26% throughput, nobody credible 2× delivery (01 F1) | BOTH kept — convergent |
| B2 | Lab-45%-vs-field finding | Lab ~45% OWASP vs Kraishan OR 0.63 reviewed PRs (different populations) | Veracode 45% stable 2025→150+ models Spring 2026 + Cobalt 55.8% Z3 vs Kraishan OR 0.63 (01 F7 counter-evidence) | BOTH kept — population difference confirmed both sides |
| B3 | Klarna boundary | $40M savings vs May-2025 reversal (Verified facts / Inferred mechanism) | 2.3M convos, 11min→<2min, ~700 roles, CEO admission; Gartner 2027 rehire prediction (02/F15) | BOTH kept — convergent |
| B4 | RAG decay 94%→38% | Silent decay green dashboards (faithfully summarized wrong docs) | Healthcare 40k docs 94% demo→38% prod; fix retrieval not model (02 RAG) | BOTH kept — convergent |
| B5 | Review-tax magnitude | 2–3x larger AI PRs, seniors overloaded, no dashboard | Cursor p75 126→345 lines, unreviewed 7%→38.5%; coverage 89%→68% one company (01 F4) | BOTH kept — direction firm, magnitudes illustrative |
| B6 | Microservices aggregates | 73% fail / 42% consolidating flagged marketing-adjacent | Same flag: named reversals real, aggregates fabricated (final-research-audit §5) | BOTH kept — direction only |
| B7 | AGENTS.md 20K/60K precision | Industry claims Unverified, convention Corroborated | Same flag (unresolved F5) | BOTH kept — convention only |
| B8 | Spotify squads | Copied-doc warning | Abandoned-model single-source analyst (final-research-audit §5) | BOTH kept — single-source flagged |
| B9 | Tokenmaxxing reversal | Meta docs unverifiable vs Sep-2026 reversal press | 65% creation-org, >75% AI code, Sep-2026 reversal dropped guidance (01 F21) | BOTH kept — press-reported |
| B10 | Multi-agent 90.2%/15x | Uncorroborated, matched-budget critique | Anthropic orchestrator-worker −90% time, ~15x tokens; Cognition single-threaded-writes counterpoint (coverage-matrix §6) | BOTH kept — different workloads |
# BUILD-PROMPT-UNIVERSAL.md
# The Universal Autonomous Agent Toolkit — Build Phases

> Generated: 2026-08-13
> Target location: C:\Users\Shashank Karamudi\Desktop\RULES\
> Hard rules in effect throughout: containment (all files in RULES), audit-before-copy,
> no installs without explicit approval, ARCHITECTURE.md kept current.

---

## HOW TO USE THIS FILE

**What this file is.** A phase-gated build prompt that constructs an autonomous-but-bounded AI coding harness (DoD-driven task execution, loop-engineering, a Two-Judge verification council, dual commit gates) inside a target project folder — designed to work in WHATEVER coding agent tool is running it (OpenCode, Claude Code, Codex, or an untested one), by having the tool discover its own conventions rather than assuming any one tool's syntax.

**Hard rules — non-negotiable, apply throughout every phase:**
1. CONTAINMENT — everything real lives inside the target project folder; any tool-required global path is a symlink/junction back into it, never a standalone copy.
2. NEVER assume one tool's convention applies to another — this is why Part 1A's Tool Discovery Protocol exists and must run first, every time, even in a tool that's been used before (conventions drift between versions).
3. AUDIT BEFORE COPY, always, for anything pulled from GitHub — clone to temp, actually read it, write a structure audit, get explicit approval, then copy only what's essential.
4. VERIFY BEFORE TRUSTING ANY INSTALL COMMAND — this file has already had two real bugs caught this way (a wrong npm package name for loop-engineering, a fabricated MCP server for Astryx that doesn't exist). A command looking plausible is not the same as it being confirmed against the tool's real, current documentation. When in doubt, fetch the source and check.
5. NOTHING installs, writes outside the project folder, or activates without explicit human approval — every phase must stop and report before proceeding to the next, never auto-chain.
6. Anything the Layer 1/Layer 2 boundary marks as approval-gated (installs, config changes, AGENTS.md edits, promoting a library skill to active) stays gated permanently — this does not relax once the harness is "done," it's a permanent operating rule for the harness itself once built.

**How to use this file, step by step:**
- Paste ONE phase at a time into a fresh session of your actual coding agent tool. Do not paste the whole file at once and let it run unattended.
- Every phase begins with a GATE CHECK — confirm it passes before proceeding; if it doesn't, stop and resolve the blocker first.
- Phase 1, Part 1A (Tool Discovery Protocol) must run first in EVERY session, even if you've used this exact tool before — it's cheap to re-confirm and expensive to assume wrong.
- After each phase reports its completion checklist, STOP. Review what it built. Only then send the next phase.
- If a phase reports something UNCONFIRMED or asks a question, answer it directly — do not tell it to "proceed anyway" or invent an approval that wasn't actually given (this exact mistake already happened once in this file's history and had to be reverted).

**How NOT to use this file:**
- Do not skip the Tool Discovery Protocol because "it's probably the same as last time."
- Do not run Phase 5's library population and then blanket-promote everything — promotion is one item at a time, audited, with an explicit collision check, by design.
- Do not treat the "known-good fallback tables" (OpenCode/Claude Code/Codex specifics) as authoritative for a tool that hasn't actually confirmed its own conventions in this session — they're a cross-check reference, not a shortcut past Part 1A.
- Do not fill init.sh's INSTALL_CMD/VERIFY_CMD/START_CMD with generic guesses (npm install, npm test) just to make Phase 4 "complete" — leave them templated until there's a real project with real commands.
- Do not let any phase proceed past a stop-and-report point without an actual human response in between.

**Structure map — what's in each phase, and dependencies:**
- Phase 1 (Foundation): Tool Discovery Protocol -> copy walkinglabs state templates -> append Layer 1/2 boundary to AGENTS.md -> dual commit gate (hard git hook + soft in-session warning, tool-branched per Part 1A's findings). Nothing else can start until this passes.
- Phase 2 (Loop Engineering): depends on Phase 1's state files existing. Installs loop-engineering (scaffold/audit) + loopy (bounded loop execution skill). Watch for conflicts with walkinglabs files — must stop, not overwrite, if one occurs.
- Phase 3 (Council + Design + Testing + Discipline): depends on Phase 1's boundary rules being in place (specifically for gating Superpowers as Layer-1-only). Installs the Two-Judge council skill, Astryx CLI + UX/design skills, Playwright + browser testing tools, and discipline skill packs.
- Phase 4 (Context, Commands, Ecosystem): depends on Phases 1-3 being functional, since its slash commands (/idea, /loop-status, etc.) reference tools installed in earlier phases. Adds context management, the full command suite, and situational security/guardrail tools.
- Phase 5 (Library System): independent of Phases 2-4's specific tool choices, but depends on Phase 1's Tool Discovery findings for safe library-folder naming. Builds the two-tier skill system — a large inert library plus a one-at-a-time, fully-audited promotion path to active use.

**What this file CAN do:**
- Build a consistent, working harness across multiple different coding agent tools without needing this whole research effort repeated per tool, because Part 1A makes the agent confirm its own environment rather than relying on pre-researched, potentially stale specifics.
- Catch and avoid the specific bugs already found and fixed during development of this harness (the pre-commit hook's transition logic, Astryx's real CLI-not-MCP integration, the loop-engineering package name).
- Give a large, safely-inert library of candidate skills without forcing every one of them to be live and context-matchable at once.

**What this file CANNOT do:**
- Guarantee a completely untested tool's Tool Discovery answers are correct on the first try — the first real run in any new tool is itself a test; expect to fix something.
- Resolve genuine ambiguity on its own (e.g. multiple different projects sharing a name, like the earlier "Hermes" case) — that needs a direct human answer, not a guess presented as fact.
- Replace your review of Phase 5 promotions — the promotion step stops and reports specifically so a human looks at it, not so it can be approved reflexively.
- Function correctly with placeholder init.sh values — the DoD gate and loop-engineering audit both depend on real, project-specific install/verify/start commands eventually being filled in.

---

## PRE-BUILD GATE CHECK

Before pasting Phase 1, confirm these are true:
- [ ] C:\Users\Shashank Karamudi\Desktop\RULES\ is the active workspace
- [ ] RULES\ contains only: audits\ (the STRUCTURE-AUDIT file)
- [ ] opencode-research\harness-templates\ exists and contains: AGENTS.md, feature_list.json, claude-progress.md, init.sh
- [ ] Node.js is installed and `node --version` works in the RULES terminal
- [ ] `npx --version` works in the RULES terminal

If any check fails, resolve it before starting Phase 1.

---

## PHASE 1 — Session Foundation
### Tool Discovery Protocol, Copy templates, AGENTS.md, and Dual pre-commit gate

PHASE 1 GATE: All pre-build checks pass. RULES\ contains only audits\.

---

You are starting Phase 1 of the build. This phase has four parts, done in order.
Follow all hard rules: files go to RULES, no installs, no copies outside RULES.
All actions are Layer 1 changes (toolkit setup) — report each step before doing it.

### PART 1A — Step 0: Tool Discovery Protocol

Before writing any files, determine your own environment by actually checking, not assuming:
1. What is your own name/identity? (check your own documentation, --help output, or config file conventions if unsure)
2. Where do you discover skills from? Check for existing conventions: try .agents/skills/ first (confirmed as a cross-tool open standard across OpenCode, Claude Code, Codex, and others) — if your tool doesn't read that path, find your tool's actual documented skill discovery path via your own --help or docs.
3. Where do you read custom slash/quick commands from? Check your own docs/help output for the real answer — do not assume a path from another tool's convention.
4. What format and file does your MCP (or equivalent external-tool) configuration use? Check your own docs for the real schema (JSON, TOML, YAML, or otherwise) rather than assuming.
5. Do you support a plugin/hook system that can intercept a tool call before it executes (equivalent to OpenCode's tool.execute.before)? If yes, note the mechanism. If no, or unsure, report that the git pre-commit hook (already tool-agnostic) will be the sole hard gate — do not fabricate a soft-gate mechanism that doesn't exist.

Report your findings for all 5 points BEFORE writing any files. If any point can't be confirmed from your own real documentation, mark it UNCONFIRMED and stop to ask for guidance rather than guessing or borrowing another tool's syntax.

**Fallback Reference (Known-Good Baselines):**
Use these only to cross-check your own findings, not to blindly apply if you cannot confirm your own environment.
| Component | OpenCode | Claude Code | Codex |
| :--- | :--- | :--- | :--- |
| **Cross-Tool Skills** | `.agents/skills/` | `.agents/skills/` | `.agents/skills/` |
| **Commands Path** | `.opencode/commands/` | `.claude/commands/` | `.codex/prompts/` |
| **Command Format** | Markdown + Frontmatter | Markdown + Frontmatter | Markdown (`$ARGUMENTS`) |
| **MCP Config File** | `opencode.json` | `.mcp.json` | `config.toml` |
| **MCP Schema** | `mcp: { command: [] }` | `mcpServers: { command: "", args: [] }` | `[mcp_servers.name]` |
| **Intercept Hook** | `dod-gate.ts` | `.claude/settings.json` | (Use hard git gate) |
| **Playwright Loop Flag**| `--loop=opencode` | `--loop=claude` | (Skip Playwright Agents) |

### PART 1B — Copy walkinglabs template files into RULES root

The audit file at RULES\audits\STRUCTURE-AUDIT-walkinglabs-templates.md has already been approved. Execute the copy now.

Source: C:\Users\Shashank Karamudi\Desktop\opencode-research\harness-templates\
Target: C:\Users\Shashank Karamudi\Desktop\RULES\

Copy these four files ONLY (not README.md):
  AGENTS.md
  feature_list.json
  claude-progress.md
  init.sh

After copying, verify all four files exist in RULES\ by listing the directory. Do NOT modify any file yet. Copy only.

### PART 1C — Extend AGENTS.md with Layer 1/Layer 2 boundary section

AGENTS.md is now in RULES\. Open it and append the following section verbatim at the end. Do NOT modify any existing walkinglabs content — append only.

--- BEGIN APPEND ---

## Autonomy Boundary -- Required Reading

There are two categories of action in this repository.

### Layer 1: Toolkit Changes (Always Approval-Gated)

The following actions ALWAYS require explicit human approval before proceeding.
Do not attempt them autonomously. Stop and ask.

- Installing any new package, tool, CLI, or MCP server
- Modifying your agent's configuration file (e.g., opencode.json, .mcp.json, config.toml)
- Modifying AGENTS.md (this file)
- Modifying .git/hooks/
- Modifying gate.yaml or any file that controls what the agent is permitted to do
- Changing model routing, provider configuration, or API credentials
- Adding or removing skills from `<ACTIVE_SKILLS_PATH>`
- Promoting a skill from the library into the active skill path
- Triggering obra/superpowers' interactive workflow

If any task requires a Layer 1 change to proceed, stop at that step, describe
what is needed and why, and wait for explicit approval. Then resume Layer 2 work.

### Layer 2: Task Execution (Autonomous after entry command)

Once a task has been started via your entry command, the following proceed autonomously:

- Writing, modifying, or deleting code within the active feature scope
- Running the feature verification[] steps from feature_list.json
- Reading and writing claude-progress.md and feature_list.json
- Calling Astryx CLI tools via bash (e.g. npx @astryxdesign/cli component Button --dense)
- Calling other registered MCP tools (browser, playwright, etc.) as the task requires
- Loading skills based on context matching
- Triggering the council via the deliberation skill for high-stakes decisions
- Committing code once verification passes and evidence is recorded
- Running loop-engineering CLI tools
- When a loopy Run serves as the verification step: MUST explicitly copy the run receipt
  into feature_list.json evidence[] before marking the feature passing -- loopy does NOT
  auto-populate evidence[]

Layer 2 autonomy ends when:
- The feature reaches status "passing" with evidence[] recorded
- A Layer 1 action is required to proceed
- loop-gate or loop-context signals a constraint violation
- /pause is invoked

Do not use Layer 2 autonomy to perform Layer 1 actions via indirect means.

--- END APPEND ---

### PART 1D — Install dual pre-commit gate

This creates two enforcement mechanisms for the DoD evidence rule:
  (A) git pre-commit hook -- hard gate, universal across all tools
  (B) Plugin hook -- early warning, fires in-session before the agent commits (Tool specific)

**Step 1: Initialize a git repo in RULES (if not already a git repo)**
Run: git init

**Step 2: Create .git/hooks/pre-commit (hard gate - UNIVERSAL)**
Create the file C:\Users\Shashank Karamudi\Desktop\RULES\.git\hooks\pre-commit with this exact content:

--- FILE CONTENT ---
#!/usr/bin/env bash
set -euo pipefail

FEATURE_LIST="feature_list.json"
if [ ! -f "$FEATURE_LIST" ]; then
  exit 0
fi

# Check for any feature transitioning to "passing" with empty evidence[]
BLOCK_REASON=$(node -e "
  const { execSync } = require('child_process');
  let prevData;
  try {
    const prevRaw = execSync('git show HEAD:feature_list.json', { encoding: 'utf8', stdio: ['pipe', 'pipe', 'ignore'] });
    prevData = JSON.parse(prevRaw);
  } catch { prevData = { features: [] }; }

  const fs = require('fs');
  const raw = fs.readFileSync('feature_list.json', 'utf8');
  const data = JSON.parse(raw);
  
  for (const f of data.features) {
    const prev = prevData.features.find(p => p.id === f.id);
    const wasPassing = prev?.status === 'passing';
    const nowPassing = f.status === 'passing';
    if (nowPassing && !wasPassing && (!f.evidence || f.evidence.length === 0)) {
      process.stdout.write('Feature ' + f.id + ' is transitioning to passing with no evidence recorded.');
      break;
    }
  }
" 2>/dev/null || echo "")

if [ -n "$BLOCK_REASON" ]; then
  echo ""
  echo "COMMIT BLOCKED: $BLOCK_REASON"
  echo "Record evidence in feature_list.json before committing."
  echo "To override intentionally: git commit --no-verify"
  echo ""
  exit 1
fi

exit 0
--- END FILE CONTENT ---

On Windows set it as executable via git config: `git config core.hooksPath .git/hooks`

**Step 3: Create Soft-Gate Hook (Tool-Specific early warning)**

Use the findings from your Tool Discovery Protocol to configure the soft-gate. If your tool does not support an intercept hook natively, skip the soft-gate step entirely. The git pre-commit hook will serve as the sole hard gate.

**IF YOU ARE USING OPENCODE:**
Create the hook file in your tool's specific plugin directory (as discovered in Part 1A):

--- FILE CONTENT ---
import { Plugin } from "@opencode-ai/plugin";
import { readFileSync, existsSync } from "fs";
import { execSync } from "child_process";

export default {
  tool: {
    execute: {
      before: async ({ tool, args }: { tool: string; args: Record<string, unknown> }) => {
        if (tool !== "bash") return;
        const cmd = String(args?.command ?? "");
        if (!cmd.includes("git commit")) return;
        if (!existsSync("feature_list.json")) return;
        try {
          let prevData = { features: [] };
          try {
            const prevRaw = execSync('git show HEAD:feature_list.json', { encoding: 'utf8', stdio: ['pipe', 'pipe', 'ignore'] });
            prevData = JSON.parse(prevRaw);
          } catch { /* no prior commit */ }
          
          const data = JSON.parse(readFileSync("feature_list.json", "utf8"));
          const active = (data.features ?? []).find(
            (f: any) => {
              const prev = prevData.features.find((p: any) => p.id === f.id);
              const wasPassing = prev?.status === 'passing';
              const nowPassing = f.status === 'passing';
              return nowPassing && !wasPassing && (!f.evidence || f.evidence.length === 0);
            }
          );
          if (active) {
            return {
              abort: true,
              message: `DoD gate: feature '${active.id}' is transitioning to passing without evidence. Record evidence before committing.`,
            };
          }
        } catch { /* Parse error -- let git hook handle it */ }
      },
    },
  },
} satisfies Plugin;
--- END FILE CONTENT ---

**IF YOU ARE USING CLAUDE CODE:**
Add a `PreToolUse` hook to your `.claude/settings.json` that intercepts `Bash` tool calls containing `git commit` and exits with code 2 if evidence[] is empty in feature_list.json.

**Step 4: Verify**
List the RULES directory recursively and confirm all files exist. Phase 1 is complete when confirmed.

---

## PHASE 2 — Loop Engineering + Loopy
### Scaffold, audit tools, and loop-execution skill installation

PHASE 2 GATE: Phase 1 complete. AGENTS.md, templates, and pre-commit hook are confirmed.

---

### PART 2A — loop-engineering scaffold

**Step 1: Check what loop-engineering actually is**
Run: `npx @cobusgreyling/loop --help`

**Step 2: Initialize a loop scaffold in RULES**
Run: `npx @cobusgreyling/loop init . --pattern daily-triage --tool [YOUR_TOOL]`
(Use the closest tool flag based on your Tool Discovery Protocol: `opencode`, `claude`, `codex`, or `generic`).

CRITICAL: `loop init` will overwrite the existing `AGENTS.md`. You MUST restore the original custom `AGENTS.md` from `opencode-research/harness-templates/AGENTS.md` and re-append the Autonomy Boundary to it immediately after this step.

### PART 2B — Loopy skill installation

**Step 1: Run the interactive installer**
Run: `npx skills add Forward-Future/loopy --skill loopy -g`
When the installer prompts for which agent to install for, select the one closest to your tool.

**Step 2: Resolve Containment Violation**
The global installation places `loopy` outside the `RULES` boundary. You MUST move this entire directory into the project cross-tool standard directory at `RULES/.agents/skills/loopy`. Then, create a Directory Junction (Windows) or symlink at the old global path pointing to the new local path inside `RULES`.

**Step 3: Create LOOPS.md placeholder**
Create `RULES\LOOPS.md` with:

--- FILE CONTENT ---
# LOOPS.md
# Project-specific saved loops (managed by loopy skill)
# Agent: add entries here when asked to save a loop via loopy Save path

(empty -- no saved loops yet)
--- END FILE CONTENT ---

---

## PHASE 3 — Two-Judge Council + Astryx CLI + Testing Tools

PHASE 3 GATE: Phase 2 complete. Loopy installed and junctioned into .agents/skills/.

---

### PART 3A — Two-Judge Council (deliberation skill)

**Step 1: Create the two-judge-verification SKILL.md**
Create the file using the cross-tool open standard directory:
  `RULES\.agents\skills\two-judge-verification\SKILL.md`

with this exact content:

--- FILE CONTENT ---
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

# Two-Judge Verification

When this skill loads, convene a Two-Judge verification panel. 
You MUST explicitly route the models for this process as follows:

1. **Judge 1 (Devil's Advocate):** Use the free 'Big Pickle' model. This judge takes the strongest possible case AGAINST the proposed approach. Identifies failure modes, edge cases, and hidden assumptions.

2. **Judge 2 (Steelman):** Use your standard reasoning model (e.g., Claude 3.5 Sonnet). This judge takes the strongest possible case FOR the approach, responding specifically to Judge 1's objections.

3. **Verdict:** Use your standard reasoning model. After both judges have argued their case, summarize:
   - The core tradeoff
   - Which judge's argument was stronger and why
   - The recommended decision with explicit reasoning
   - Any conditions under which the opposite decision would be correct

Do NOT produce a wishy-washy "both sides have merit" verdict. Make a specific
recommendation. If the evidence genuinely does not favor either side, say that
explicitly and explain what additional information would break the tie.
--- END FILE CONTENT ---

### PART 3B — UI/UX Design System & Skills Setup

**Step 1: Generate AGENTS.md component inventory**
If the project uses Astryx, run: `npx @astryxdesign/cli init --features agents`
(Astryx has NO MCP server, use bash calls).

**Step 2: Supplemental UI/UX Tools**
Run `npx skills add keysjoao/laws-of-ux-skills` (Ensure it lands in `.agents/skills/`).

### PART 3C — Testing Tools Setup (MCP Branching)

**Step 1: Install playwright-mcp**
Use your Tool Discovery Protocol findings to modify your tool's specific config file:
- **For OpenCode** (`opencode.json`): Add to `mcp`:
  `"playwright": { "type": "local", "command": ["npx", "@playwright/mcp@latest"], "enabled": true }`
- **For Claude Code** (`.mcp.json`): Add to `mcpServers`:
  `"playwright": { "type": "stdio", "command": "npx", "args": ["-y", "@playwright/mcp@latest"] }`
- **For Codex** (`config.toml`): Add table `[mcp_servers.playwright]` with `command="npx"` and `args=["-y", "@playwright/mcp@latest"]`.

**Step 2: Install Playwright test agents**
Run: `npx playwright init-agents --loop=[YOUR_TOOL]` (e.g. `--loop=claude`). If you are using a tool that does not support a Playwright agent loop flag yet (e.g. Codex), skip this step.

**Step 3: Create seed.spec.ts**
Create `RULES\seed.spec.ts` with this placeholder:

--- FILE CONTENT ---
// seed.spec.ts
// Seed test for Playwright agents (Planner, Generator, Healer)
// This file provides initialization logic and app fixtures for the agents to reference.
// Replace the placeholder content below with your actual app setup before running agents.

import { test, expect } from '@playwright/test';

test('seed: app loads', async ({ page }) => {
  // Replace localhost:3000 with your actual dev server URL
  await page.goto('http://localhost:3000');
  // Add basic smoke assertions for your app here
  await expect(page).toHaveTitle(/.+/);
});
--- END FILE CONTENT ---

**Step 4: Verify MCP Config**
Confirm your tool's MCP file has Playwright configured.

### PART 3D — Discipline & Workflow Skills

1. **mattpocock/skills (Dev Workflows):**
   Run `npx skills add mattpocock/skills`. Ensure it lands in `.agents/skills/`.

2. **obra/superpowers (Methodology framework) — ⚠️ LAYER-1 / MANUAL USE ONLY ⚠️:**
   Install per your tool's instructions. Ensure it lands in `.agents/skills/`.

---

## PHASE 4 — Context Management, Commands, and Ecosystem

PHASE 4 GATE: Phase 3 complete. Council installed. Testing tools configured in native MCP schema.

---

### PART 4A — Context Management

**Priority 1: context7 (upstash/context7) — ALWAYS install**
Add the remote endpoint `https://mcp.context7.com/mcp` to your tool's MCP config. Follow your tool's schema for remote/HTTP servers based on the Tool Discovery Protocol findings.

### PART 4B — Slash Command Suite

Use the path and format found during the Tool Discovery Protocol to create the following five command files:

**1. idea.md**
--- FILE CONTENT ---
---
description: Start a new task. Routes through the full DoD pipeline.
---

New task: $ARGUMENTS

1. Read claude-progress.md -- confirm current verified state and the next best step
2. Read feature_list.json -- confirm no other feature is in_progress (single_active_feature rule)
3. Run ./init.sh -- confirm baseline is passing before any feature work begins
4. Use Loopy to find or craft the most appropriate bounded loop for this task
5. Execute the loop autonomously; apply the DoD template as the completion gate
6. Do not mark the task complete until evidence[] is recorded in feature_list.json
   and verification passes per the feature's verification[] steps
7. Run the retrospective mechanism to learn from this iteration
8. Update claude-progress.md with the session summary before ending
--- END FILE CONTENT ---

**2. loop-status.md**
--- FILE CONTENT ---
---
description: Non-destructive status check. Does not interrupt execution.
---

Report current status without making any changes:
1. Read feature_list.json -- show the active feature (in_progress), its status, and evidence[]
2. Read the last entry in claude-progress.md -- show the most recent session summary
3. If loopy is active: show current loop pass count and last receipt summary
4. Report any blockers or unresolved risks noted in claude-progress.md
--- END FILE CONTENT ---

**3. loop-doctor.md**
--- FILE CONTENT ---
---
description: Audit a running or completed loop. Reports top-3 issues.
---

Run: npx @cobusgreyling/loop doctor .
Report the top-3 issues found.
Flag any runaway signals (cost, time, pass count).
Recommend specific next actions.
--- END FILE CONTENT ---

**4. pause.md**
--- FILE CONTENT ---
---
description: Gracefully pause autonomous execution. Suspends and saves state.
---

1. Write a pause marker to claude-progress.md: add an entry with today's date,
   Goal: PAUSED BY USER, Known risk/unresolved issue: $ARGUMENTS
2. Set the in_progress feature's status to "blocked" in feature_list.json,
   with notes: "Manual pause. Reason: $ARGUMENTS"
3. Do NOT commit or push. Do NOT continue any active work.
4. Report the current state clearly so resumption is unambiguous.
--- END FILE CONTENT ---

**5. council.md**
--- FILE CONTENT ---
---
description: Force Two-Judge council review outside its automatic triggers.
---

Explicitly invoke the two-judge-verification skill with the following question:

$ARGUMENTS

Run the full two-judge process (Devil's Advocate, Steelman, Verdict).
Make a specific recommendation. Do not hedge.
--- END FILE CONTENT ---

### PART 4C — Final State Verification

Run a complete audit:
1. List RULES\ recursively -- confirm all expected files and directories exist
2. Show your tool's MCP config file content -- confirm playwright and context7 present
3. Run ./init.sh -- confirm it completes without errors (it will fail if INSTALL_CMD / VERIFY_CMD haven't been customized yet -- report the error if so, do not fix blindly)
4. Run: `npx @cobusgreyling/loop audit --suggest`
5. Attempt: `git status`

### PART 4D — Customize init.sh for this project

For each project, update the three variables in init.sh:
  INSTALL_CMD -- the command that installs dependencies for THIS project
  VERIFY_CMD  -- the command that runs the baseline verification for THIS project
  START_CMD   -- the command that starts the dev server for THIS project

Example for a Playwright + Next.js project:
  INSTALL_CMD: "npm install"
  VERIFY_CMD: "npx playwright test --reporter=line"
  START_CMD: "npm run dev"

---

## POST-BUILD VERIFICATION

Phase 4 is complete when all of the following are true:
- [ ] RULES\AGENTS.md has walkinglabs content + Layer 1/2 boundary section appended
- [ ] RULES\feature_list.json -- real project features replacing the placeholder examples
- [ ] RULES\claude-progress.md -- first session entry started
- [ ] RULES\init.sh -- INSTALL_CMD, VERIFY_CMD, START_CMD set for this project
- [ ] RULES\.git\hooks\pre-commit -- hard gate installed
- [ ] Cross-tool `.agents\skills\two-judge-verification\SKILL.md` -- council trigger
- [ ] Agent definition directory has Playwright agents (if supported by tool)
- [ ] Tool Commands Directory has all five slash commands
- [ ] Tool MCP config has playwright and context7 configured
- [ ] RULES\LOOPS.md -- placeholder file present
- [ ] Loopy SKILL.md -- junctioned into `<ACTIVE_SKILLS_PATH>`
- [ ] loop-engineering -- initialized
- [ ] Inert library folder created and populated with INDEX.md
- [ ] promote-skill command installed

---

## FIRST REAL TASK

Once post-build verification passes, test the full pipeline with a real task:

  `/idea [write your actual first feature description here]`

The agent should:
1. Read claude-progress.md and feature_list.json
2. Run ./init.sh
3. Ask loopy to find or craft a loop
4. Execute the loop autonomously
5. At completion: update feature_list.json (status -> passing, evidence[] populated)
6. Trigger the pre-commit gate to confirm it passes
7. Commit with a descriptive message
8. Update claude-progress.md

---

## ARCHITECTURE REFERENCE (LOCKED)

| Decision | Choice |
|---|---|
| Session state source of truth | walkinglabs only (feature_list.json + claude-progress.md) |
| Loop execution | loopy skill (Forward-Future/loopy), installed locally via .agents/skills/ junction |
| Loop governance | loop-engineering (cobusgreyling/loop-engineering) |
| Council trigger | two-judge-verification SKILL.md in .agents/skills/, auto-loads by description match |
| Pre-commit gate (hard) | git .git/hooks/pre-commit, fires on all commits (UNIVERSAL) |
| Pre-commit gate (warning) | Native Plugin hook depending on tool |
| Astryx integration | CLI bash calls ONLY -- no MCP server exists |
| Entry command | /idea (Tool agnostic format) |
| Mega-harness | NONE -- composed from small focused plugins |
| loopy state | LOOPS.md only (distinct from feature_list.json) |
| loopy receipt propagation | MANUAL -- agent must copy to feature_list.json evidence[] |


## PHASE 5 — Two-Tier Library System
### Inert Library Population and Audited Promotion

PHASE 5 GATE: Phase 4 is complete. 

---

### PART 5A — Construct the Inert Library

1. Identify a safe library folder name that will NOT be automatically parsed or executed by your tool. Use your Tool Discovery Protocol findings (e.g., if your active path is `.agents/skills/`, use `.agents/library/`).
2. Fetch the candidate skills catalog (provided below, do NOT install them).

<CATALOG_DATA>
# TOOL CATALOG

You have access to the following 160+ tools, skills, and MCP servers. Search this file when you need a capability.

### obra/superpowers
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/obra/superpowers
- **How it works**: 211,860 stars, actively maintained — Complete agentic skills framework & software development methodology built on 14 composable skills (brainstorming, TDD, systematic-debugging, code review, git-worktrees, subagent-driven-development, etc.). — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/INSTALL.md` and `docs/README.opencode.md`; explicit install command provided.

### anthropics/skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/anthropics/skills
- **How it works**: 151,088 stars, actively maintained — Anthropic's official public agent skills repository. Contains the Agent Skills specification, skill template, and 15+ example skills (docx, pdf, pptx, xlsx, algorithmic art, canvas design, MCP builder, webapp testing, brand guidelines, etc.). — OpenCode support: **Open standard** — Agent Skills spec (agentskills.io) is the open standard OpenCode natively implements; OpenCode discovers `.agents/skills/` and `SKILL.md` files directly.

### mattpocock/skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/mattpocock/skills
- **How it works**: 130,016 stars, actively maintained — "Skills for Real Engineers." 17+ dev workflow skills including `/grill-me`, `/tdd`, `/diagnosing-bugs`, `/code-review`, `/triage`, `/wayfinder`, `/improve-codebase-architecture`. Installable via `npx skills` or Claude Code plugin. — OpenCode support: **Open standard** — pure SKILL.md format installable via `npx skills add mattpocock/skills` which writes to `.agents/skills/`; no proprietary lock-in.

### addyosmani/agent-skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/addyosmani/agent-skills
- **How it works**: 60,265 stars, actively maintained — Production-grade engineering skills covering the full SDLC: 24 skills across DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP. Includes anti-rationalization tables, verification gates, and Google engineering culture patterns. — OpenCode support: **Documented port/adapter exists** — explicit `docs/opencode-setup.md` describes AGENTS.md + `skill` tool integration.

### [REDACTED-caveman]
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/[REDACTED-caveman]
- **How it works**: ~92,000 stars, actively maintained — Token-compression skill that cuts 65% of output tokens by making agents talk in terse [REDACTED]-speak. Six compression levels, [REDACTED]-commit, [REDACTED]-review, [REDACTED]-stats. Supports 30+ agents. — OpenCode support: **Documented port/adapter exists** — explicit OpenCode install instructions in README; curl/pipe installer detects OpenCode and drops skill into `~/.config/opencode/skills/`.

### hardikpandya/stop-slop
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/hardikpandya/stop-slop
- **How it works**: 13,400 stars, maintained — Skill for removing AI tells and "slop" from prose. Banned phrases, structural clichés, sentence-level rules, and 1-10 scoring rubric. — OpenCode support: **Open standard** — plain SKILL.md + references/ directory; copy to `.agents/skills/` or `~/.config/opencode/skills/`.

### Gentleman-Programming/Gentleman-Skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/Gentleman-Programming/Gentleman-Skills
- **How it works**: actively maintained, community-driven — Curated + community skills for Angular, React 19, Next.js 15, TypeScript, Tailwind, Zod, Zustand, AI SDK, Django, Playwright, pytest, Jira, and more. Democratic voting for community contributions. — OpenCode support: **Native** — explicitly documents OpenCode's native skill directory (`~/.config/opencode/skills/`) in README.

### VoltAgent/awesome-agent-skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/VoltAgent/awesome-agent-skills
- **How it works**: actively maintained — Curated awesome-list of 1000+ agent skills from official dev teams (Anthropic, Google, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, Figma, etc.) and community. Hand-picked, not AI-generated. — OpenCode support: **Open standard** — catalog of SKILL.md repos; explicitly lists OpenCode in compatibility matrix and provides `~/.config/opencode/skills/` path.

### cloudflare/skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/cloudflare/skills
- **How it works**: actively maintained, official — Skills for teaching agents how to build on Cloudflare: Workers, Agents SDK, Durable Objects, Wrangler, web-perf, MCP servers (cloudflare-api, cloudflare-docs, cloudflare-bindings). — OpenCode support: **Native** — explicitly documents OpenCode install path (`~/.config/opencode/skills/`) and `npx skills add` support.

### composiohq/skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/composiohq/skills
- **How it works**: (composio-community/skills) — actively maintained — Distributable agent skills for Composio developers. Tool Router best practices, Triggers & Events, production patterns. Uses AGENTS.md + SKILL.md dual format. — OpenCode support: **Open standard** — AGENTS.md consolidated file format that OpenCode natively reads; also standard SKILL.md directories.

### waybarrios/opencode-power-pack
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/waybarrios/opencode-power-pack
- **How it works**: ~460 stars, actively maintained — 55 rigorous skills ported from Claude Code workflows to Codex, OpenCode, and Pi. Code review, security audit, feature development, frontend design, MCP tools, Hugging Face ML/training. — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/plugins/opencode-power-pack.js` plugin; explicit `opencode plugin --global` install docs; registers skills as slash commands automatically.

### hqhq1025/skill-optimizer
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/hqhq1025/skill-optimizer
- **How it works**: ~125 stars, actively maintained — Agent Skills lifecycle toolkit: `skill-miner` (mine repeated workflows from session history), `skill-personalizer` (audit and tune skills to your habits), `skill-generalizer` (turn personal skills into publishable ones). — OpenCode support: **Native** — explicitly documents OpenCode path (`~/.config/opencode/skills/`) and `npx skills add` compatibility.

### glebis/claude-skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/glebis/claude-skills
- **How it works**: actively maintained — ~100 skills for Claude Code covering meetings & transcripts, research & knowledge, writing & publishing, image/audio generation, TDD, app release, personal analytics, and Claude Code ops. — OpenCode support: **Open standard** — installable via `npx skills add glebis/claude-skills` which writes standard SKILL.md files to `.agents/skills/`.

### agentskills/agentskills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/agentskills/agentskills
- **How it works**: actively maintained — The official Agent Skills specification repository. Defines the open SKILL.md format, progressive disclosure model, and directory structure. — OpenCode support: **Open standard** — this IS the specification that OpenCode natively implements.

### alirezarezvani/claude-skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/alirezarezvani/claude-skills
- **How it works**: maintained — Multi-category skill pack: system architecture (Clean Architecture, SOLID, ADR), automated code review, iOS dev, Go with LLM subagents, strategic decision-making, brand voice, SEO. — OpenCode support: **Open standard** — plain SKILL.md format; copy to `.agents/skills/`.

### steipete/agent-rules
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/steipete/agent-rules
- **How it works**: maintained — Rules and knowledge to work better with agents. Archived Cursor rules adapted for cross-agent use. Static prompt templates with no runtime code. — OpenCode support: **Open standard** — static markdown; install script writes to `~/.claude/CLAUDE.md` but content is portable to OpenCode's AGENTS.md.

### FrancyJGLisboa/agent-skill-creator
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/FrancyJGLisboa/agent-skill-creator
- **How it works**: maintained — Meta-skill that teaches agents to create complete agents autonomously. Cross-platform generator for 14+ AI tools. Writes to `~/.agents/skills/` and `~/.claude/skills/`. — OpenCode support: **Open standard** — writes to `.agents/skills/` which OpenCode discovers natively.

### tripleyak/SkillForge
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/tripleyak/SkillForge
- **How it works**: maintained — Ultimate meta-skill for generating best-in-class Claude Code skills. 4-phase architecture with Python validation scripts. — OpenCode support: **Open standard** — SKILL.md output format.

### alirezarezvani/claude-code-skill-factory
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/alirezarezvani/claude-code-skill-factory
- **How it works**: maintained — Toolkit for building production-ready skills, agents, and slash commands at scale. 10 slash commands and 5 agents for generating skills. — OpenCode support: **Open standard** — writes output to `~/.claude/skills/` in portable SKILL.md format.

### NeoLabHQ skills
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/NeoLabHQ
- **How it works**: (code-review, reflexion, sdd, ddd, sadd, kaizen) — maintained — Engineering methodology skills: spec-driven dev, domain-driven dev, self-refinement loops, continuous improvement. — OpenCode support: **Open standard** — SKILL.md format.

### shanraisshan/claude-code-best-practice
- **Category**: 1: Skills (SKILL.md repos / collections)
- **URL**: https://github.com/shanraisshan/claude-code-best-practice
- **How it works**: maintained — Comprehensive best practices guide covering agents, commands, skills, hooks, workflows, and orchestration patterns. — OpenCode support: **Claimed but unverified** — repo exists and discusses cross-tool patterns but no explicit OpenCode install docs found.

### OpenCode Built-in Permission System
- **Category**: 2: Permission Modes (configs / presets)
- **URL**: https://opencode.ai/docs/permissions/
- **How it works**: Core feature of OpenCode, actively maintained — Granular permission framework with `allow` / `ask` / `deny` rules per tool (bash, edit, write, webfetch, etc.). Supports wildcard `*` patterns, per-agent overrides, and `--auto` CLI flag for auto-approve mode. — OpenCode support: **Native**

### joelhooks/opencode-config
- **Category**: 2: Permission Modes (configs / presets)
- **URL**: https://github.com/joelhooks/opencode-config
- **How it works**: actively maintained — Personal OpenCode configuration repository demonstrating production permission patterns: global `webfetch: deny`, per-agent permission boundaries (plan=read-only, build=full, explore=filesystem-only), and `.env` read protections. — OpenCode support: **Native** — pure `opencode.json` config.

### kdcokenny/opencode-workspace
- **Category**: 2: Permission Modes (configs / presets)
- **URL**: https://github.com/kdcokenny/opencode-workspace
- **How it works**: 555 stars, actively maintained — Bundled multi-agent orchestration harness with pre-configured permission boundaries: global `webfetch: deny`, plan/build agents as read-only orchestrators delegating via `task` tool, researcher with MCP-only access, coder with full file+bash, scribe with write-only no-bash, reviewer with read-only+git. — OpenCode support: **Native** — ships as OCX profile with permission presets.

### boxpositron/envsitter-guard
- **Category**: 2: Permission Modes (configs / presets)
- **URL**: https://github.com/boxpositron/envsitter-guard
- **How it works**: actively maintained — OpenCode plugin that blocks agents/tools from reading or editing sensitive `.env*` files while providing safe EnvSitter-backed alternatives (keys, fingerprints, scans, mutations without exposing values). Hooks into OpenCode's tool system to intercept `read`/`edit`/`write`/`patch` on `.env*` paths. — OpenCode support: **Native** — OpenCode plugin using tool hooks.

### OpenCode Native /undo
- **Category**: 3: Checkpoints / Rewind Tools
- **URL**: https://opencode.ai/docs/
- **How it works**: Core feature, actively maintained — Built-in session rewind via `/undo` command. Restores file state and conversation to previous turn. Git-based snapshotting under the hood. Survives restarts. — OpenCode support: **Native**

### @arkfactory/opencode-checkpoint
- **Category**: 3: Checkpoints / Rewind Tools
- **URL**: https://www.npmjs.com/package/@arkfactory/opencode-checkpoint
- **How it works**: actively maintained — Automatic checkpoint plugin for OpenCode. Creates shadow git repository in `.opencode/checkpoints/`, auto-checkpoints on file edits (5s debounce), session end, and errors. Interactive TUI (`/checkpoint-review`) for visual diff review with accept/reject per file. — OpenCode support: **Native** — OpenCode plugin.

### witlox/opencode-checkpoint
- **Category**: 3: Checkpoints / Rewind Tools
- **URL**: https://github.com/witlox/opencode-checkpoint
- **How it works**: actively maintained — Named checkpoint plugin for OpenCode with SQLite storage. `checkpoint_create`, `checkpoint_list`, `checkpoint_restore`, `checkpoint_delete` tools. Fork-based restore using OpenCode's `session.fork()` API. Optional git commit tracking. 100% test coverage. — OpenCode support: **Native** — OpenCode plugin using official session APIs.

### Opencode-DCP/opencode-dynamic-context-pruning
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/Opencode-DCP/opencode-dynamic-context-pruning
- **How it works**: 3,894 stars, actively maintained — Intelligent context compression plugin for OpenCode. Replaces stale conversation content with high-fidelity summaries before LLM requests. Two modes: `range` (contiguous spans) and `message` (individual messages). Deduplication of repeated tool calls, purge of errored tool inputs after N turns. Session history never modified — only pruned content sent to LLM. — OpenCode support: **Native** — OpenCode plugin.

### tickernelz/opencode-mem
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/tickernelz/opencode-mem
- **How it works**: 1,300+ stars, actively maintained — Persistent memory plugin for OpenCode using local vector database. Auto-capture extracts technical context on idle, injects relevant memories into chat. Manual `memory` tool for add/search/list/forget. Web UI at `127.0.0.1:4747`. Public subpath exports for third-party plugins. — OpenCode support: **Native** — OpenCode plugin with auto-capture and web UI.

### 0xranx/OpenContext
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/0xranx/OpenContext
- **How it works**: 715 stars, actively maintained — Personal context/knowledge store for AI agents. Reuses existing coding agent CLI (Codex/Claude/OpenCode). `oc` CLI for global `contexts/` library, MCP server for agent integration, desktop GUI, web UI. Skills + slash commands for Cursor/Claude Code/Codex. — OpenCode support: **Native** — explicit OpenCode config path (`~/.config/opencode/`) documented; MCP server works with OpenCode.

### upstash/context7
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/upstash/context7
- **How it works**: 7,072 stars, actively maintained — Context7 MCP server: up-to-date code documentation for LLMs. Fetches version-specific docs and code examples straight from source. `resolve-library-id` and `get-library-docs` tools. Supports OpenCode via MCP config. — OpenCode support: **Open standard** — MCP server; OpenCode natively discovers MCP servers.

### code-yeongyu/oh-my-openagent
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/code-yeongyu/oh-my-openagent
- **How it works**: 67.2k stars, actively maintained — Multi-model agent orchestration harness for OpenCode. Context injection (auto-inject AGENTS.md, README.md, conditional rules), hash-anchored edit tool, session recovery, LSP/AST tools, built-in MCPs (Exa websearch, Context7 docs, Grep.app). 54+ lifecycle hooks, background agents, Team Mode with parallel agents. — OpenCode support: **Native** — OpenCode plugin with deep context management.

### alvinunreal/oh-my-opencode-slim
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/alvinunreal/oh-my-opencode-slim
- **How it works**: 7.8k stars, actively maintained — Lightweight multi-agent orchestration for OpenCode. Seven specialized agents (Orchestrator, Explorer, Oracle, Council, Librarian, Designer, Fixer). Background orchestration, bundled skills, Council for parallel model consensus, preset switching (`/preset`), LSP/AST tools, built-in MCPs. — OpenCode support: **Native** — OpenCode plugin.

### kdcokenny/opencode-background-agents
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/kdcokenny/opencode-background-agents
- **How it works**: actively maintained — Async background delegation for OpenCode. Delegate research tasks, continue working, retrieve results later. Results persisted to `~/.local/share/opencode/delegations/` as markdown. Survives context compaction. Three tools: `delegate`, `delegation_read`, `delegation_list`. — OpenCode support: **Native** — OpenCode plugin.

### derekbar90/opencode-conductor
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/derekbar90/opencode-conductor
- **How it works**: 121 stars, actively maintained — Protocol-driven workflow plugin for OpenCode. Context → Spec → Plan → Implement lifecycle. `/conductor:setup`, `/conductor:newTrack`, `/conductor:implement`, `/conductor:status`, `/conductor:revert` commands. Persistent planning state. — OpenCode support: **Native** — OpenCode plugin.

### IgorWarzocha/Opencode-Context-Analysis-Plugin
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/IgorWarzocha/Opencode-Context-Analysis-Plugin
- **How it works**: maintained — Token usage analysis plugin for OpenCode. Visual breakdown of token distribution across tools (read, bash, webfetch, etc.). Bar charts showing percentages and counts. `/context` command. — OpenCode support: **Native** — OpenCode plugin.

### oc-mnemoria
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Persistent shared memory (hive mind) for OpenCode agents across sessions. Rust engine with hybrid BM25 + semantic search, CRC32 checksum chains, append-only binary format. 7 tools and `/mn-*` slash commands. — OpenCode support: **Native** — OpenCode plugin.

### supamem
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Project-agnostic dual-memory MCP CLI for OpenCode. Semantic memory (Qdrant tuned hybrid retrieval: dense MiniLM + sparse BM25) and structural memory hooks. Installer wires `qdrant-find` / `qdrant-store` tools. — OpenCode support: **Native** — MCP server + OpenCode plugin installer.

### Hipocampo
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Dual memory system (PostgreSQL + pgvector + Gemini Embeddings) for AI coding agents. BIRE algorithm (unified semantic + lexical search, auto-tagging, hybrid scoring, GIN trigram indexes). Ships as opencode skill with SKILL.md. — OpenCode support: **Native** — OpenCode skill.

### opencode-short-term-memory
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Automatically summarizes conversation context into structured session memory and injects it back into the system prompt every few turns. Preserves user instructions, project context, decisions, active references across long chats and compactions. — OpenCode support: **Native** — OpenCode plugin.

### MrDoe/OpenCodeRAG
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/MrDoe/OpenCodeRAG
- **How it works**: maintained — Local-first RAG plugin for OpenCode. Semantic code search with tree-sitter chunking (19 languages), LanceDB, incremental indexing, file-change detection, watch mode. Ollama or OpenAI embeddings. CLI + OpenCode plugin with chunk retrieval tool. — OpenCode support: **Native** — OpenCode plugin.

### opencode-skillful
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Allow OpenCode agents to lazy-load prompts on demand with skill discovery and injection. Reduces upfront context size by only loading skills when needed. — OpenCode support: **Native** — OpenCode plugin.

### code-yeongyu/oh-my-openagent
- **Category**: 5: Hooks (collections / frameworks)
- **URL**: https://github.com/code-yeongyu/oh-my-openagent
- **How it works**: 67.2k stars, actively maintained — Multi-model agent orchestration harness with 54+ lifecycle hooks (61 with Team Mode), all configurable via `disabled_hooks`. Hooks cover session lifecycle, tool calls, agent transitions, background task events, and more. Full Claude Code compatibility layer with hook parity. — OpenCode support: **Native** — OpenCode plugin with extensive hook system.

### alvinunreal/oh-my-opencode-slim
- **Category**: 5: Hooks (collections / frameworks)
- **URL**: https://github.com/alvinunreal/oh-my-opencode-slim
- **How it works**: 7.8k stars, actively maintained — Lightweight multi-agent orchestration plugin with deep system hooks for agent lifecycle, task delegation, and context monitoring. Hooks integrate with tmux/Zellij/kitty multiplexers for live agent visibility. — OpenCode support: **Native** — OpenCode plugin.

### smartfrog/opencode-froggy
- **Category**: 5: Hooks (collections / frameworks)
- **URL**: https://github.com/smartfrog/opencode-froggy
- **How it works**: 102 stars, maintained — OpenCode plugin providing Claude Code-style hooks, specialized agents, and tools like gitingest. Hooks for session events, file operations, and agent transitions. — OpenCode support: **Native** — OpenCode plugin.

### Opencode Hooks Plugin
- **Category**: 5: Hooks (collections / frameworks)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Use Claude Code hooks definition and hook them to opencode hooks. Bridges Claude Code's hook format to OpenCode's plugin event system. — OpenCode support: **Documented port/adapter exists** — explicit adapter from Claude Code hooks to OpenCode hooks.

### hcom
- **Category**: 5: Hooks (collections / frameworks)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Let AI agents message, watch, and spawn each other across terminals. Claude Code, Gemini CLI, Codex CLI, and OpenCode agents in separate terminals can message each other, detect file edit collisions, read transcripts, view terminal screens, subscribe to activity, and spawn/fork/resume agents. First-class OpenCode support with native plugin. TUI dashboard, cross-device relay, Python API. — OpenCode support: **Native** — OpenCode plugin with cross-agent hook integration.

### FlowDeck
- **Category**: 5: Hooks (collections / frameworks)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — AI-powered multi-agent workflow orchestration with deep system hooks: context monitoring, session idle summaries, shell environment injection. 25 specialist agents, 24 workflow skills, 17 workflow commands, persistent state via `.planning/STATE.md`. — OpenCode support: **Native** — OpenCode plugin with deep hooks.

### upstash/context7
- **Category**: 6: MCP Servers
- **URL**: https://github.com/upstash/context7
- **How it works**: 7,072 stars, actively maintained — Context7 MCP server: up-to-date code documentation for LLMs. `resolve-library-id` and `get-library-docs` tools fetch version-specific docs and code examples. Community-contributed library index. Works with any MCP client including OpenCode. — OpenCode support: **Open standard** — MCP server; OpenCode natively discovers and connects MCP servers via `opencode.json`.

### AlaeddineMessadi/opencode-mcp
- **Category**: 6: MCP Servers
- **URL**: https://github.com/AlaeddineMessadi/opencode-mcp
- **How it works**: actively maintained — MCP server that bridges any MCP client (Claude, Cursor, Windsurf, VS Code, Cline, Zed, Amazon Q) to OpenCode's headless API. 80 tools, 10 resources, 6 prompts. Auto-starts OpenCode HTTP server in-process. Multi-project support. — OpenCode support: **Open standard** — MCP server exposing OpenCode's capabilities to any MCP client; OpenCode itself can also consume MCP servers.

### ajhcs/Better-OpenCodeMCP
- **Category**: 6: MCP Servers
- **URL**: https://github.com/ajhcs/Better-OpenCodeMCP
- **How it works**: actively maintained — Enhanced MCP server for OpenCode CLI. Async task execution, process pooling, crash recovery, 293 tests. Bridges Claude to Gemini, DeepSeek, and other models via OpenCode's multi-model capabilities. Interactive setup wizard. — OpenCode support: **Open standard** — MCP server.

### Ejentum
- **Category**: 6: MCP Servers
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — MCP server with four tools (`harness_reasoning`, `harness_code`, `harness_anti_deception`, `harness_memory`) that AI agents call on demand. Each returns a structured prompt the calling agent ingests before generating. — OpenCode support: **Open standard** — MCP server.

### SwarmVault
- **Category**: 6: MCP Servers
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Local-first RAG knowledge base compiler with bundled skill and MCP server. Turns raw docs, research, and code into persistent markdown wiki, knowledge graph, and hybrid SQLite FTS + embeddings search. Works with OpenCode, Claude Code, and Codex. — OpenCode support: **Open standard** — MCP server + OpenCode skill.

### supamem
- **Category**: 6: MCP Servers
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Project-agnostic dual-memory MCP CLI for OpenCode. Semantic memory (Qdrant hybrid retrieval: dense MiniLM + sparse BM25) and structural memory hooks. Installer wires `qdrant-find` / `qdrant-store` tools. — OpenCode support: **Open standard** — MCP server.

### OpenCode Chromium Browser Plugin
- **Category**: 6: MCP Servers
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Browser automation MCP for Chromium-based browsers (Chrome, Edge, Brave). Manifest V3 extension + Node.js native messaging host. Screenshots, CDP commands, DOM actions, downloads, console/network inspection. — OpenCode support: **Native** — OpenCode plugin with MCP-style browser tools.

### Dodo Payments MCP
- **Category**: 6: MCP Servers
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Official Dodo Payments plugin bundles two MCP servers: live API server with browser OAuth, and documentation search server. Checkout, subscriptions, webhooks, usage-based billing, credits, license keys. — OpenCode support: **Native** — OpenCode plugin with embedded MCP servers.

### OpenCode Claude Memory
- **Category**: 6: MCP Servers
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Share persistent Markdown memory between OpenCode and Claude Code using Claude Code-compatible paths and file formats. Cross-tool memory bridge. — OpenCode support: **Open standard** — uses shared file format readable by both tools.

### fabianlema/opencode-sandbox
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/fabianlema/opencode-sandbox
- **How it works**: 21 stars, actively maintained — Docker sandbox environment for running OpenCode AI agents with all necessary dev tools pre-installed (git, gh, python3, jq, node). Multi-architecture (AMD64 + ARM64/Apple Silicon). Runs as non-root user (`node`). GHCR-hosted with `opencode_here.sh` helper alias (`oh`). Config persisted to `~/.config/opencode-sandbox/`. — OpenCode support: **Native** — Docker container purpose-built for OpenCode; official OpenCode docs recommend Docker/VM for true isolation.

### athal7/opencode-devcontainers
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/athal7/opencode-devcontainers
- **How it works**: actively maintained — OpenCode plugin for isolated branch workspaces using devcontainers or git worktrees. Auto-assigned ports (13000–13099), session state management, automatic copying of gitignored secrets (.env, credentials), unified workspace cleanup. Supports both full container isolation (devcontainers) and lightweight filesystem isolation (worktrees). — OpenCode support: **Native** — OpenCode plugin.

### jailoc
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Sandboxed Docker environments for OpenCode agents. Provides containerized execution contexts for agent operations. — OpenCode support: **Native** — OpenCode plugin.

### ankitmundada/awesome-opencode-subagents
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/ankitmundada/awesome-opencode-subagents
- **How it works**: actively maintained — Definitive curated collection of specialized AI assistants for OpenCode CLI. Categories cover full-stack development tasks. Interactive installer script (`install-agents.sh`) with browse/select/install/uninstall flow. Agents install to `~/.config/opencode/agents/` (global) or `.opencode/agents/` (project). — OpenCode support: **Native** — drops into OpenCode's native agent discovery paths.

### code-yeongyu/oh-my-openagent
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/code-yeongyu/oh-my-openagent
- **How it works**: 67.2k stars, actively maintained — Multi-model orchestration harness bundling 10+ specialized subagents (Explorer, Oracle, Librarian, Designer, Fixer, etc.) with background task management, LSP/AST tools, MCP servers, and 54+ lifecycle hooks. Team Mode with parallel agent execution. — OpenCode support: **Native** — OpenCode plugin.

### alvinunreal/oh-my-opencode-slim
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/alvinunreal/oh-my-opencode-slim
- **How it works**: 7.8k stars, actively maintained — Lightweight multi-agent orchestration with 7 specialized subagents (Orchestrator, Explorer, Oracle, Council, Librarian, Designer, Fixer). Background task management, LSP/AST tools, tmux integration for live agent visibility, MCP servers. — OpenCode support: **Native** — OpenCode plugin.

### kdcokenny/opencode-workspace
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/kdcokenny/opencode-workspace
- **How it works**: 555 stars, actively maintained — Bundled multi-agent harness with 4 specialist subagents: researcher (MCP-only, read-only), coder (full file+bash), scribe (write-only, no bash), reviewer (read-only+git). Pre-configured permission boundaries and planning protocols. — OpenCode support: **Native** — OpenCode plugin + OCX profile.

### NERV
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Invisible engineering infrastructure for AI agents. Spec-Driven Development pipeline, A2A task delegation hub, persistent semantic memory (MAGI), and 9 specialized subagents for OpenCode. Scaffolds 45+ files via `nerv init` including SDD skills, slash commands, MCP servers, and lifecycle plugins. — OpenCode support: **Native** — OpenCode plugin + scaffolding CLI.

### hiai-opencode
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Canonical 12-agent model with bundled skills, MCP servers, LSP integration, and ralph-loop. 10 visible agents (Bob, Coder, Strategist, Critic, Guard, Researcher, Designer, Manager, Brainstormer, Vision) plus hidden Sub and Agent Skills. — OpenCode support: **Native** — OpenCode plugin.

### Open Conclave
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Multi-agent debates moderated by a captain agent until consensus. Each agent has a different system prompt (logical, creative, research-focused). Configurable provider/model per agent. — OpenCode support: **Native** — OpenCode plugin.

### CrewBee
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Task-specific Agent Teams for OpenCode. Define reusable task/project-specific agent teams, project them into OpenCode agents, switch between single-agent and multi-agent collaboration. Built-in Coding Team template with review flow and completion criteria. — OpenCode support: **Native** — OpenCode plugin.

### OpenCode Ensemble
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Parallel agent teams for OpenCode. Coordinate parallel agents with peer messaging, shared task board, git worktree isolation, and live dashboard. — OpenCode support: **Native** — OpenCode plugin.

### Pocket Universe
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Subagent-driven pocket universe for primary agent. Extends native OpenCode subagent paradigm to provide closed-loop, resilient, async agents that block main thread execution. Three tools for parallel subagent communication and coordination. — OpenCode support: **Native** — OpenCode plugin.

### Gem Team
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Self-learning multi-agent orchestration harness for spec-driven development and automated verification. — OpenCode support: **Native** — OpenCode plugin.

### deliberation
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Ask GPT, Gemini, Grok, or OpenRouter for a second opinion or fix as expert subagents over MCP. Seven expert subagents (Architect, Plan Reviewer, Scope Analyst, Code Reviewer, Security Analyst, Researcher, Debugger). `ask-all` asks every model at once; `consensus` runs an arbiter loop. — OpenCode support: **Open standard** — MCP server + OpenCode plugin.

### Python Expert Agent for OpenCode
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Custom configurable agent toolkit with 1 primary custom agent (`python-expert`) plus predefined specialized subagents for code generation, review, testing, and exploration. On-demand skills and context files for standards/patterns/security. — OpenCode support: **Native** — OpenCode plugin.

### OpenCode Agents
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — A set of opencode configurations, prompts, agents, and plugins for enhanced development workflows. — OpenCode support: **Native** — OpenCode plugin/configs.

### Agentic
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Modular AI agents and commands for structured software development with OpenCode. — OpenCode support: **Native** — OpenCode plugin.

### awesome-opencode/awesome-opencode
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: actively maintained, community-driven — The de facto curated marketplace/discovery hub for the OpenCode ecosystem. Organized into plugins, themes, agents, and projects. Each entry links to its repository with description and install instructions. The closest thing to an "app store" for OpenCode. — OpenCode support: **Native** — discovery list of native OpenCode plugins.

### CKGrafico/opencode-market
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/CKGrafico/opencode-market
- **How it works**: actively maintained — CLI to discover, install, and manage OpenCode agent plugins from GitHub marketplaces. Registers marketplaces from GitHub repos (searches `marketplace.json` in `.github/plugin/`, `.claude-plugin/`, or root). `npx opencode-market install <plugin>@<marketplace> [--local|--opencode]`. Supports both OpenCode and Claude Code marketplace formats. — OpenCode support: **Native** — CLI tool purpose-built for OpenCode plugin discovery/installation.

### NikiforovAll/opencode-marketplace
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/NikiforovAll/opencode-marketplace
- **How it works**: actively maintained — CLI marketplace for OpenCode plugins. Install from local directories or GitHub URLs. Zero-config convention-based discovery (`.opencode/`, `.claude/`, `./command/`, `./commands/`). Content-hash based change detection. Supports commands, agents, and skills. User-global or project-local scope. `bunx opencode-marketplace install <url>`. — OpenCode support: **Native** — CLI tool purpose-built for OpenCode.

### kdcokenny/ocx
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/kdcokenny/ocx
- **How it works**: (OCX Ecosystem) — actively maintained — Registry-based plugin manager for OpenCode. `ocx add kdco/workspace --from https://registry.kdco.dev`. Bundles plugins, skills, agents, and MCP servers into profiles. Dependency management and automatic updates. — OpenCode support: **Native** — purpose-built registry and package manager for OpenCode.

### OpenCode Manager
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/chriswritescode-dev/opencode-manager
- **How it works**: actively maintained — Mobile-first web interface for OpenCode AI agents. Repository management, chat/session control, Git/file tools, schedules, AI configuration, MCP server management, plugin management, push notifications, PWA support. Runs as Bun/Hono backend + React/Vite frontend with supervised OpenCode server. — OpenCode support: **Native** — web UI that manages OpenCode plugins and MCP servers.

### opencode-agent-for-cowork
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Cowork (Claude desktop) plugin that bridges natural language conversations with OpenCode. Handles agent routing, stall detection, result validation, per-project operational memory, provider fallback chain, MCP composability. Ships 8 orchestration skills, 3 scheduled-task recipes, 1 custom agent template. — OpenCode support: **Native** — bridges Cowork to OpenCode.

### ajaxdude/opencode-ai-poimandres-theme
- **Category**: 10: Output Styles
- **URL**: https://github.com/ajaxdude/opencode-ai-poimandres-theme
- **How it works**: actively maintained — Minimal, frameless dark theme for OpenCode inspired by the poimandres VS Code theme. Semantic color coding, optimized for truecolor terminals. Three variants: original (100% aesthetic), turquoise-expanded, and accessible (WCAG AA compliant — 100% contrast ratio pass for all 24 critical color pairs). Install via `/theme` command or `opencode.json`. — OpenCode support: **Native** — OpenCode theme format (`~/.config/opencode/themes/`).

### VS Code Themes for OpenCode
- **Category**: 10: Output Styles
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Ports of all built-in VS Code themes from the vscode.theme-defaults extension: vscode-modern, vscode-plus, vscode-vs, vscode-hc. Automatic dark/light variant selection. One-line install script. — OpenCode support: **Native** — OpenCode theme format.

### OpenCode Light Themes
- **Category**: 10: Output Styles
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Largest collection of light themes for OpenCode. 21 carefully crafted light themes converted from popular VS Code themes: scaefy-light, Solarized Light, Vivid Light, Coffee Cream, GitHub Light, Quiet Light, Bluloco Light, Brackets Light Pro, NetBeans Light, Ysgrifennwr, Hop Light, GitHub Plus, Classic Light, HC Flurry, all Milkshake variants. Bilingual EN/TR docs, one-command install. — OpenCode support: **Native** — OpenCode theme format.

### Ayu Dark Theme for OpenCode
- **Category**: 10: Output Styles
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Port of the popular Ayu Dark color scheme with golden yellow accent. — OpenCode support: **Native** — OpenCode theme format.

### Charcoal Theme for OpenCode
- **Category**: 10: Output Styles
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Deep-black grayscale theme for OpenCode — no hues, all shades of gray. Near-black (#0d0d0d) background. All 56 theme color keys use shades of gray. Also available for bat and Ghostty. — OpenCode support: **Native** — OpenCode theme format.

### Lavi Theme for OpenCode
- **Category**: 10: Output Styles
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Soft, sweet dark theme with rich purple tones. Part of the Lavi colorscheme family (Neovim, Alacritty, Ghostty, Kitty, Wezterm, Zellij, etc.). Nix flake and home-manager support. — OpenCode support: **Native** — OpenCode theme format.

### Moonlight Theme for OpenCode
- **Category**: 10: Output Styles
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Moonlight color theme based on the popular moonlight-vscode-theme by atomiks. Dark, cool-toned palette inspired by moonlight aesthetics. — OpenCode support: **Native** — OpenCode theme format.

### @franlol/opencode-md-table-formatter
- **Category**: 10: Output Styles
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode / kdcokenny workspace) — maintained — Markdown table formatting plugin for OpenCode. Part of the OCX workspace bundle. — OpenCode support: **Native** — OpenCode plugin.

### kdcokenny/opencode-background-agents
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/kdcokenny/opencode-background-agents
- **How it works**: actively maintained — Claude Code-style async background delegation for OpenCode. Fire off research tasks, continue working, retrieve results later. Three tools: `delegate(prompt, agent)`, `delegation_read(id)`, `delegation_list()`. Results persisted to `~/.local/share/opencode/delegations/` as markdown — survive context compaction, session restarts, and crashes. Read-only subagents only (write-capable agents must use native `task` tool). 15-minute timeout. Lifecycle parity with Claude Code background agents. — OpenCode support: **Native** — OpenCode plugin.

### zenobi-us/opencode-background
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/zenobi-us/opencode-background
- **How it works**: actively maintained — Background process management plugin for OpenCode. `createBackgroundProcess` (shell command, name, tags, global/session scope), `listBackgroundProcesses` (filter by session/status/tags), `killProcesses` (by ID/session/status/tags). Tracks in-memory with singleton manager. Captures last 100 lines of output. States: pending, running, completed, failed, cancelled. ALL processes killed when OpenCode closes. — OpenCode support: **Native** — OpenCode plugin.

### server-manager
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Non-blocking background server management for OpenCode. Start, track, and stop local dev servers without blocking the AI session. Supports Node.js, Python, Go, .NET, Java, Rust, PHP, and any framework with a dev server. JSON state persistence, per-project log files, HTTP health checks, log tail/grep for debugging. — OpenCode support: **Native** — OpenCode plugin.

### opencode-scheduler
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list / docs ecosystem) — actively maintained — Schedule recurring jobs using launchd (Mac) or systemd (Linux) with cron syntax. Integrates with OpenCode's task system. — OpenCode support: **Native** — OpenCode plugin.

### opencode-notify
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list / docs ecosystem) — actively maintained — Native OS notifications for OpenCode. Know when background tasks complete, error, need approval, or wait for input. dbus (Linux) and osascript (macOS). Shows project name, elapsed time, message preview. — OpenCode support: **Native** — OpenCode plugin.

### Pilot
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Automation daemon that polls for work from GitHub issues and Linear tickets. Runs as a background process, dispatches tasks to OpenCode agents. — OpenCode support: **Native** — OpenCode plugin.

### opencode-background-agents
- **Category**: 11: Background Task Tools
- **URL**: https://opencode.ai/docs/ecosystem/
- **How it works**: (from official docs ecosystem list) — actively maintained — Same as kdcokenny's background agents — listed in official OpenCode ecosystem documentation. — OpenCode support: **Native** — OpenCode plugin.

### alibaba/open-code-review
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/alibaba/open-code-review
- **How it works**: actively maintained, official Alibaba project — Fast, efficient, battle-tested code review tool with hybrid architecture: deterministic pipelines + LLM Agent. Precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection). OpenAI & Anthropic compatible. Delegation mode lets coding agents run the review. — OpenCode support: **Documented port/adapter exists** — explicit "OpenCode" integration in docs: install native review tools and slash commands; also supports Delegation Mode where OpenCode runs the review.

### waybarrios/opencode-power-pack
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/waybarrios/opencode-power-pack
- **How it works**: ~460 stars, actively maintained — Bundles `/security-review` as a first-class slash command. 45 rigorous skills including security audit, code review, feature development. Security-review skill is a licensed adaptation from Anthropic's `claude-code-security-review`. — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/plugins/opencode-power-pack.js` plugin; explicit OpenCode install docs.

### opencode-review
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Automatic structured code review plugin for OpenCode CLI. Reviews staged changes when session goes idle, with configurable cooldown, multi-dimension analysis (code quality, security, performance, testing, documentation), severity levels, and auto-fix chain support. — OpenCode support: **Native** — OpenCode plugin.

### OpenCode Swarm
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Verification-gated swarm with architect planning, independent review, test engineering, security checks, and resumable evidence. Multi-agent security review pipeline. — OpenCode support: **Native** — OpenCode plugin.

### boxpositron/envsitter-guard
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/boxpositron/envsitter-guard
- **How it works**: actively maintained — Prevents agents/tools from reading or editing sensitive `.env*` files, while allowing safe inspection via EnvSitter (keys + deterministic fingerprints; never values). Hooks into OpenCode's tool system. — OpenCode support: **Native** — OpenCode plugin.

### OpenAgentsControl
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/darrenhinde/OpenAgentsControl
- **How it works**: 4.6k stars, actively maintained — Plan-first development framework with built-in security analysis subagent (`CodeReviewer`). Approval gates, pattern-based security validation, context-aware security standards. — OpenCode support: **Native** — OpenCode agent framework with security subagent.

### OpenCode Native Headless Mode
- **Category**: 13: Headless / CI Setups
- **URL**: https://opencode.ai/docs/
- **How it works**: Core feature, actively maintained — Three headless interfaces built into OpenCode: (1) `opencode run "<prompt>"` for one-shot prompts with `--auto`, `--format json`, `--continue`, `--session`, `--fork`, `--mini` flags; (2) `opencode serve --port 4096` for headless HTTP API; (3) `opencode web --port 4096` for web UI. GitHub agent via `opencode github install`. Session export/import, stats tracking. — OpenCode support: **Native**

### wesammustafa/opencode-primer
- **Category**: 13: Headless / CI Setups
- **URL**: https://github.com/wesammustafa/opencode-primer
- **How it works**: actively maintained — Comprehensive community guide covering headless CI setup: `opencode run` for scripts/CI jobs, `opencode serve` for headless API, GitHub Actions workflows, GitLab CI recipes. `--auto` flag for CI-only auto-approve. `--mini` lightweight mode (v1.17.10+). — OpenCode support: **Native** — documentation/guide for native OpenCode headless features.

### OpenCode Manager
- **Category**: 13: Headless / CI Setups
- **URL**: https://github.com/chriswritescode-dev/opencode-manager
- **How it works**: actively maintained — Mobile-first web interface for OpenCode AI agents. Runs as supervised OpenCode server with Bun/Hono backend + React/Vite frontend. Repository management, chat/session control, Git/file tools, schedules, AI configuration, MCP server management. PWA support. — OpenCode support: **Native** — wraps OpenCode's headless server in a web UI.

### AlaeddineMessadi/opencode-mcp
- **Category**: 13: Headless / CI Setups
- **URL**: https://github.com/AlaeddineMessadi/opencode-mcp
- **How it works**: actively maintained — MCP server bridging any MCP client to OpenCode's headless API. 80 tools, 10 resources, 6 prompts. Auto-starts OpenCode HTTP server in-process. Multi-project support. Enables CI systems to delegate coding work to OpenCode via MCP. — OpenCode support: **Open standard** — MCP server exposing OpenCode headless API.

### Subagent Reporter
- **Category**: 13: Headless / CI Setups
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Pipes subagent actions/events directly to stdout during `opencode run` sessions, prefixes them with subagent names, enumerates parallel subagents. Essential for CI visibility when subagents are involved. — OpenCode support: **Native** — OpenCode plugin.

### opencode-plugin-otel
- **Category**: 13: Headless / CI Setups
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — OpenTelemetry telemetry exporter for OpenCode sessions. Exports metrics, logs, traces via OTLP/gRPC to any OTel backend (Datadog, Honeycomb, Grafana Cloud). Instruments session lifecycle, token usage, cost, tool durations, git commits. CI observability. — OpenCode support: **Native** — OpenCode plugin.

### eserete/opencode-token-tracker
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/eserete/opencode-token-tracker
- **How it works**: 3 stars, actively maintained — Real-time token usage, cost, and latency tracking for every AI request in OpenCode. TUI sidebar footer display: `⏳ last: in: 70.0k · out: 1.2k · 1 req · $0.04` / `📊 total: in: 1.2m · out: 0.3m · 42 reqs · $1.23`. Updates every 2 seconds during execution. Install via curl to `~/.config/opencode/plugins/token-tracker.tsx` + `tui.json` registration. — OpenCode support: **Native** — OpenCode TUI plugin.

### opgginc/opencode-bar
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/opgginc/opencode-bar
- **How it works**: actively maintained — macOS menu-bar token usage tracker for OpenCode. Auto-detects providers from `auth.json`. Multi-path support. Color-coded progress (green→yellow→orange→red). Daily tracking, EOM prediction, add-on cost tracking. Per-provider subscription settings. Launch at login. Sparkle auto-updates. — OpenCode support: **Native** — reads OpenCode's `auth.json` directly.

### ramtinJ95/opencode-tokenscope
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/ramtinJ95/opencode-tokenscope
- **How it works**: actively maintained — Comprehensive token usage analysis and cost tracking for OpenCode sessions. Turns telemetry into readable reports. npm installable (`@ramtinj95/opencode-tokenscope`). `/tokenscope` slash command. Session-scoped analysis. — OpenCode support: **Native** — OpenCode plugin.

### Token Monitor
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Token analysis & cost tracking with budgets, trends, and per-project analytics. Tracks input/output/reasoning/cache tokens, estimates costs, daily trends with ASCII charts, budget alerts, export data. Per-agent breakdown, agent×model cross-analysis, project-scoped analytics. — OpenCode support: **Native** — OpenCode plugin.

### OpenCode Throughput
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Real-time LLM performance monitoring. Tracks TTFT, TPS, latency, token usage, and cost per model. Toast notifications + TUI sidebar display. — OpenCode support: **Native** — OpenCode plugin.

### Opencode Quota
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Quota toasts and token tracking across providers. Automatic toasts and slash commands. — OpenCode support: **Native** — OpenCode plugin.

### Opencode Usage Monitor
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — OpenCode sidebar plugin displaying API usage quotas for OpenAI and Z.AI providers. Per-model breakdown, spend tracking, configurable refresh controls. — OpenCode support: **Native** — OpenCode plugin.

### Opencode Telemetry
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Passive cross-session telemetry to local SQLite. Logs every session automatically — tokens, tool calls, skills, per-turn cost. Aggregates costs across orchestration chains (conductor + child sessions). Turn-by-turn forensic inspection. `octm` CLI for reports without spending model tokens. Zero cloud, zero network. — OpenCode support: **Native** — OpenCode plugin.

### opencode-mystatus
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Check all AI subscription quotas in one command. Supports OpenAI (Plus/Pro/Codex), Zhipu AI, Google Antigravity, and more. — OpenCode support: **Native** — OpenCode plugin/slash command.

### Langfuse OpenCode Observability
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://langfuse.com/integrations/developer-tools/opencode
- **How it works**: actively maintained — OpenTelemetry-based observability for OpenCode. Traces user turns, assistant generations, tool calls, retries, reasoning output, compaction, failed steps. Sent to Langfuse for monitoring, debugging, cost analysis. — OpenCode support: **Native** — OpenCode plugin (`@langfuse/opencode-observability-plugin`).

### pai4451/opencode-telemetry-plugin
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/pai4451/opencode-telemetry-plugin
- **How it works**: actively maintained — OpenTelemetry metrics exporter for OpenCode. Exports session telemetry via OTLP/gRPC. Built with `@opentelemetry/sdk-metrics` and `@opencode-ai/plugin`. — OpenCode support: **Native** — OpenCode plugin.

### code-yeongyu/oh-my-openagent
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/code-yeongyu/oh-my-openagent
- **How it works**: 67.2k stars, actively maintained — Multi-model agent orchestration harness for OpenCode. 10+ specialized subagents (Explorer, Oracle, Librarian, Designer, Fixer, etc.), background task management, LSP/AST tools, MCP servers, 54+ lifecycle hooks. Team Mode with parallel agent execution and consensus. — OpenCode support: **Native** — OpenCode plugin.

### alvinunreal/oh-my-opencode-slim
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/alvinunreal/oh-my-opencode-slim
- **How it works**: 7.8k stars, actively maintained — Lightweight multi-agent orchestration. 7 specialized subagents (Orchestrator, Explorer, Oracle, Council, Librarian, Designer, Fixer). Background tasks, LSP/AST tools, tmux integration for live agent visibility, MCP servers. — OpenCode support: **Native** — OpenCode plugin.

### kdcokenny/opencode-workspace
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/kdcokenny/opencode-workspace
- **How it works**: 555 stars, actively maintained — Bundled multi-agent orchestration harness with 16 components. 4 specialist subagents (researcher, coder, scribe, reviewer) with pre-configured permission boundaries. OCX profile system. — OpenCode support: **Native** — OpenCode plugin + OCX profile.

### darrenhinde/OpenAgentsControl
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/darrenhinde/OpenAgentsControl
- **How it works**: 4.6k stars, actively maintained — Plan-first development framework with approval-based execution. 3 main agents (OpenAgent, OpenCoder, SystemBuilder) + 8+ specialized subagents (ContextScout, TaskManager, CoderAgent, TestEngineer, CodeReviewer, BuildAgent, DocWriter, ExternalScout). MVI context system (80% token reduction). Multi-language support (TypeScript, Python, Go, Rust, C#/.NET). — OpenCode support: **Native** — OpenCode agent framework.

### agnusdei1207/opencode-orchestrator
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/agnusdei1207/opencode-orchestrator
- **How it works**: actively maintained — Multi-agent orchestrator plugin for OpenCode. Parallel sessions (up to 50), agent distribution (Commander → Planner → Workers → Reviewer), background tasks, auto-retry, loop-until-done. Shared state coordination. — OpenCode support: **Native** — OpenCode plugin.

### NERV
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Invisible engineering infrastructure. Spec-Driven Development pipeline, A2A task delegation hub, persistent semantic memory (MAGI), 9 specialized subagents. Scaffolds 45+ files via `nerv init`. — OpenCode support: **Native** — OpenCode plugin + scaffolding CLI.

### hiai-opencode
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Canonical 12-agent model. 10 visible agents (Bob, Coder, Strategist, Critic, Guard, Researcher, Designer, Manager, Brainstormer, Vision) + hidden Sub and Agent Skills. Bundled skills, MCP servers, LSP integration, ralph-loop. — OpenCode support: **Native** — OpenCode plugin.

### CrewBee
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Task-specific Agent Teams for OpenCode. Define reusable task/project-specific agent teams, project them into OpenCode agents, switch between single-agent and multi-agent collaboration. Built-in Coding Team template with review flow and completion criteria. — OpenCode support: **Native** — OpenCode plugin.

### OpenCode Ensemble
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Parallel agent teams for OpenCode. Coordinate parallel agents with peer messaging, shared task board, git worktree isolation, live dashboard. — OpenCode support: **Native** — OpenCode plugin.

### Open Conclave
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Multi-agent debates moderated by captain agent until consensus. Each agent has different system prompt (logical, creative, research-focused). Configurable provider/model per agent. — OpenCode support: **Native** — OpenCode plugin.

### OpenCode Swarm
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Verification-gated swarm with architect planning, independent review, test engineering, security checks, resumable evidence. Multi-agent team with quality gates. — OpenCode support: **Native** — OpenCode plugin.

### FlowDeck
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — AI-powered multi-agent workflow orchestration. 25 specialist agents (architect, planner, coder, reviewer, tester, debugger, risk-analyst, policy-enforcer, etc.). 24 workflow skills, 17 workflow commands, 15 pre-built orchestration flows. Persistent state via `.planning/STATE.md`. Wave-based parallel execution. AI Safety layer. — OpenCode support: **Native** — OpenCode plugin.

### Open Dynamic Workflows
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Dynamic multi-agent workflows for OpenCode. Local daemon runs generated orchestration script with concurrent agents, adversarial verification, crash-resume. OpenCode plugin adds workflow triggers and planning UI. Bring your own model. — OpenCode support: **Native** — OpenCode plugin + local daemon.

### Gem Team
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Self-learning multi-agent orchestration harness for spec-driven development and automated verification. — OpenCode support: **Native** — OpenCode plugin.

### Pocket Universe
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Subagent-driven pocket universe for primary agent. Closed-loop, resilient, async agents that block main thread. Three tools for parallel subagent communication. — OpenCode support: **Native** — OpenCode plugin.

### deliberation
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Ask GPT, Gemini, Grok, or OpenRouter for second opinion as expert subagents over MCP. 7 expert subagents (Architect, Plan Reviewer, Scope Analyst, Code Reviewer, Security Analyst, Researcher, Debugger). `ask-all` and `consensus` modes. — OpenCode support: **Open standard** — MCP server + OpenCode plugin.

### Claude Squad
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/smtg-ai/claude-squad
- **How it works**: actively maintained — TUI for parallel agents with git worktree isolation. Supports OpenCode via `-p "opencode"`. tmux sessions, vim-style navigation. AGPL-3.0. — OpenCode support: **Documented port/adapter exists** — explicitly lists OpenCode in agent support; launches OpenCode in tmux worktree sessions.

### Baton (mraza007)
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/topics/agent-orchestration
- **How it works**: maintained — Poll-dispatch-reconcile orchestration for git worktrees. Supports Claude Code, Codex, Gemini, OpenCode. — OpenCode support: **Claimed but unverified** — listed in orchestration roundups as supporting OpenCode but no explicit docs found.

### mark-hingston/opencode-workflows
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/mark-hingston/opencode-workflows
- **How it works**: actively maintained — Workflow automation plugin for OpenCode using the Mastra engine. Deterministic, auditable, resumable, composable agent orchestration. Patterns: Sequential Chain, Parallel Experts, Tool-Augmented, Human-in-the-Loop (`suspend` steps), Conditional Routing. Each step's output captured and reviewable. Workflows persist to disk and survive restarts. — OpenCode support: **Native** — OpenCode plugin.

### derekbar90/opencode-conductor
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/derekbar90/opencode-conductor
- **How it works**: 121 stars, actively maintained — Protocol-driven workflow plugin for OpenCode. Context → Spec → Plan → Implement lifecycle. `/conductor:setup`, `/conductor:newTrack`, `/conductor:implement`, `/conductor:status`, `/conductor:revert` commands. Persistent planning state. — OpenCode support: **Native** — OpenCode plugin.

### FlowDeck
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — AI-powered multi-agent workflow orchestration. Four-phase cycle: discuss → plan → execute → review. 25 specialist agents, 24 reusable workflow skills (TDD, security scan, deploy check, code review), 17 workflow commands, 15 pre-built orchestration flows including Spec-Driven Development (SDD). Persistent state via `.planning/STATE.md`. Wave-based parallel execution. AI Safety layer with patch trust scoring, edit gates, phase gating. — OpenCode support: **Native** — OpenCode plugin.

### Open Dynamic Workflows
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Dynamic multi-agent workflows for OpenCode. Local daemon runs generated orchestration script with concurrent agents, adversarial verification, crash-resume. OpenCode plugin adds workflow/ultracode triggers and planning UI. Bring your own model. — OpenCode support: **Native** — OpenCode plugin + local daemon.

### opencode-bmad-workflow
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — BMAD (Breakthrough Method of Agile AI-Driven Development) workflow plugin. Specialized agents for product management, architecture, development, QA. Automates epic planning, feature breakdown, sprint workflows, code reviews through structured multi-agent pipeline. — OpenCode support: **Native** — OpenCode plugin.

### GoopSpec
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Spec-driven development workflow. 5-phase workflow: Plan → Research → Specify → Execute → Accept. Contract gates for user confirmation, 12 specialized subagents, persistent memory system, wave-based execution with atomic commits, deviation rules. — OpenCode support: **Native** — OpenCode plugin.

### NERV
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Invisible engineering infrastructure. Spec-Driven Development pipeline, A2A task delegation hub, persistent semantic memory (MAGI). Scaffolds 45+ files via `nerv init` including SDD skills, slash commands, MCP servers, lifecycle plugins. — OpenCode support: **Native** — OpenCode plugin + scaffolding CLI.

### OpenCode Swarm
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Verification-gated swarm with architect planning, independent review, test engineering, security checks, resumable evidence. Multi-agent workflow with quality gates. — OpenCode support: **Native** — OpenCode plugin.

### Subtask2
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Extend opencode `/commands` into a powerful orchestration system with granular flow control. Task decomposition and dependency management. — OpenCode support: **Native** — OpenCode plugin.

### ForLoop Planner
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — Autopilot development platform. Plan with ForLoop agent, then Build, Test, Deploy on cloud in one go. Covers entire development lifecycle. — OpenCode support: **Native** — OpenCode plugin.

### open-plan-annotator
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Fully local agentic coding plugin that intercepts plan mode and opens an annotation UI in browser. Select text to strikethrough, replace, insert, or comment — then approve plan or request changes. — OpenCode support: **Native** — OpenCode plugin.

### Opencode Roadmap
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Strategic roadmap planning and multi-agent coordination plugin. Project-wide planning capabilities. — OpenCode support: **Native** — OpenCode plugin.

### anomalyco/opencode-sdk-js
- **Category**: 17: Agent SDKs
- **URL**: https://github.com/anomalyco/opencode-sdk-js
- **How it works**: 87 stars, actively maintained — Official JavaScript/TypeScript SDK for OpenCode. Handles sessions, file operations, streaming responses, plugin development, and programmatic agent control. Type-safe hooks and context APIs. Auto-generated types from OpenCode's internal type system. — OpenCode support: **Native** — official SDK from the OpenCode team.

### anomalyco/opencode-sdk-go
- **Category**: 17: Agent SDKs
- **URL**: https://github.com/anomalyco/opencode-sdk-go
- **How it works**: actively maintained — Official Go SDK for OpenCode. Generated with Fern to track OpenCode versions with no manual work per version bump. Core client, field types, and session management primitives. — OpenCode support: **Native** — official SDK from the OpenCode team.

### Acksell/opencode-go-sdk
- **Category**: 17: Agent SDKs
- **URL**: https://github.com/Acksell/opencode-go-sdk
- **How it works**: 1 star, maintained — Community Go SDK for OpenCode, generated with Fern. Tracks OpenCode with no manual work per version bump. — OpenCode support: **Native** — community SDK wrapping OpenCode APIs.

### obra/superpowers
- **Category**: 18: Discipline / Skill Packs (Superpowers / ponytail-style)
- **URL**: https://github.com/obra/superpowers
- **How it works**: 211,860 stars, actively maintained — Complete agentic skills framework & software development methodology. 14 composable skills: brainstorming, TDD, systematic-debugging, code review, git-worktrees, subagent-driven-development, etc. Auto-installs as OpenCode plugin via `plugin: ["superpowers@git+https://github.com/obra/superpowers.git"]`. — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/INSTALL.md` and `docs/README.opencode.md`; auto-installs on OpenCode restart.

### waybarrios/opencode-power-pack
- **Category**: 18: Discipline / Skill Packs (Superpowers / ponytail-style)
- **URL**: https://github.com/waybarrios/opencode-power-pack
- **How it works**: ~460 stars, actively maintained — 55 rigorous skills ported from Claude Code workflows to Codex, OpenCode, and Pi. Feature development (7-phase), code review, security audit, frontend design, MCP builder, skill creator, Hugging Face ML/training (13 skills), AWS/SageMaker cloud (5 skills). — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/plugins/opencode-power-pack.js` plugin; explicit OpenCode install docs.

### meaningfy-ws/skillery
- **Category**: 18: Discipline / Skill Packs (Superpowers / ponytail-style)
- **URL**: https://github.com/meaningfy-ws/skillery
- **How it works**: actively maintained — Collection of agent skills. On OpenCode: skill-packs (superpowers, stream-coding, ponytail) load from `.claude/` natively; OpenSpec, commit-commands, and gitnexus also supported. Cross-tool skill pack distribution. — OpenCode support: **Open standard** — loads standard SKILL.md packs into OpenCode's native skill directories.

### DietrichGebert/ponytail
- **Category**: 18: Discipline / Skill Packs (Superpowers / ponytail-style)
- **URL**: https://github.com/DietrichGebert/ponytail
- **How it works**: actively maintained — Ponytail discipline/ruleset for AI agents. Loads as always-on context every session. Registers `/ponytail` commands and ships skills activated when a task needs them. Available as `opencode-ponytail` npm package. — OpenCode support: **Documented port/adapter exists** — `opencode-ponytail` package; loads ruleset and skills into OpenCode.

### upstash/context7
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://github.com/upstash/context7
- **How it works**: 7,072 stars, actively maintained — The definitive docs-context MCP server. Fetches up-to-date, version-specific documentation and code examples straight from source. `resolve-library-id` and `get-library-docs` tools. Community-contributed library index. Explicit OpenCode install docs for both remote (`https://mcp.context7.com/mcp`) and local (`npx -y @upstash/context7-mcp`) configurations. — OpenCode support: **Open standard** — MCP server; OpenCode natively discovers MCP servers.

### sandbox-technologies/opencode-docs-mcp
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://github.com/sandbox-technologies/opencode-docs-mcp
- **How it works**: actively maintained — OpenCode Docs MCP Server. Self-hostable or remote-hosted at `https://tryinspector.com/api/opencode-docs/mcp`. Three tools: `SearchOpenCodeDocs` (query search), `GetOpenCodeDocPage` (full page content), `BrowseOpenCodeDocs` (table of contents). Covers 27 documents across Getting Started, Usage, Configure, Develop, Providers, Protocols, Security, Server, UI, and Developer Resources. — OpenCode support: **Open standard** — MCP server with explicit OpenCode config example.

### bgauryy/open-docs
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://github.com/bgauryy/open-docs
- **How it works**: actively maintained — Comprehensive technical documentation suite for OpenCode (27 documents, 310+ pages, 520+ code examples, 100+ diagrams). Deep technical insights into architecture, implementation, and development. Complements official user docs. Covers architecture, session management, tool system, LSP integration, provider system, ACP protocol, MCP integration, server architecture, TUI/desktop/web implementations, and SDKs. — OpenCode support: **Native** — documentation resource consumed by OpenCode users and agents; not a tool per se but essential docs-context infrastructure.

### Joaquinvesapa/sub-agent-statusline
- **Category**: 20: Statusline Tools
- **URL**: https://github.com/Joaquinvesapa/sub-agent-statusline
- **How it works**: actively maintained — Subagent Monitor for OpenCode. TUI sidebar plugin showing running/completed/failed subagents, elapsed time, and token/context usage. Compact home/footer summary when active subagent activity exists. Built with SolidJS in universal mode for OpenTUI compatibility. — OpenCode support: **Native** — OpenCode TUI sidebar plugin.

### eserete/opencode-token-tracker
- **Category**: 20: Statusline Tools
- **URL**: https://github.com/eserete/opencode-token-tracker
- **How it works**: 3 stars, actively maintained — Real-time token usage, cost, and latency tracking displayed in the TUI sidebar footer. Updates every 2 seconds during execution. Shows last request and session totals with cost estimates. — OpenCode support: **Native** — OpenCode TUI plugin.

### OpenCode Native Status Bar
- **Category**: 20: Statusline Tools
- **URL**: https://opencode.ai/docs/
- **How it works**: Core feature, actively maintained — Built-in status bar showing active model, session state, token usage, and agent mode (Plan vs. Build). Configurable via `tui.json`. — OpenCode support: **Native**

### kdcokenny/opencode-worktree
- **Category**: 21: Git-Worktree Helpers
- **URL**: https://github.com/kdcokenny/opencode-worktree
- **How it works**: 701 stars, 35 forks, actively maintained — Zero-friction git worktrees for OpenCode. Auto-spawns terminals, syncs files, cleans up on exit. Two tools: `worktree_create(branch, baseBranch?)` and `worktree_delete(reason)`. Creates worktree at `~/.local/share/opencode/worktree/<project-id>/<branch>`, runs post-create hooks (e.g., `pnpm install`), opens new terminal with OpenCode running. On delete: runs pre-delete hooks, commits all changes, removes worktree with `--force`. Config via `.opencode/worktree.jsonc`. Supports Ghostty, Kitty, tmux. Part of OCX ecosystem. — OpenCode support: **Native** — OpenCode plugin.

### felixAnhalt/opencode-worktree-session
- **Category**: 21: Git-Worktree Helpers
- **URL**: https://github.com/felixAnhalt/opencode-worktree-session
- **How it works**: actively maintained — OpenCode plugin that automatically manages Git worktrees for every AI session. Creates worktree in `.opencode/worktrees/`, refuses to run on `main` branch, pivots AI's cwd to worktree automatically. On session exit: stages all changes, generates commit message via OpenCode API, pushes to origin, removes worktree. Install via `@tmegit/opencode-worktree-session` npm package. — OpenCode support: **Native** — OpenCode plugin.

### athal7/opencode-devcontainers
- **Category**: 21: Git-Worktree Helpers
- **URL**: https://github.com/athal7/opencode-devcontainers
- **How it works**: actively maintained — OpenCode plugin for isolated branch workspaces using devcontainers OR git worktrees. Auto-assigned ports (13000–13099), session state management, automatic copying of gitignored secrets (.env, credentials), unified workspace cleanup. Supports both full container isolation (devcontainers) and lightweight filesystem isolation (worktrees). — OpenCode support: **Native** — OpenCode plugin.

### bradAGI/awesome-cli-coding-agents
- **Category**: 22: Awesome-Lists (AI coding agents, cross-tool ones only)
- **URL**: https://github.com/bradAGI/awesome-cli-coding-agents
- **How it works**: 308 stars, actively maintained — Comprehensive directory of 80+ terminal-native AI coding agents (open-source and proprietary) plus harnesses that orchestrate them. Sorted by GitHub stars within sections. OpenCode is listed prominently in the "Open Source" section with 193k stars noted. Also catalogs orchestrators (Claude Squad, Superset, herdr, cmux, agent-of-empires, hcom, etc.) many of which support OpenCode. — OpenCode support: **Open standard** — cross-tool discovery list; OpenCode is a first-class entry.

### ai-for-developers/awesome-ai-coding-tools
- **Category**: 22: Awesome-Lists (AI coding agents, cross-tool ones only)
- **URL**: https://github.com/ai-for-developers/awesome-ai-coding-tools
- **How it works**: 1.7k stars, actively maintained — Curated awesome-list of AI coding tools including agents, MCP servers, skills, and harnesses. OpenCode listed under "Coding Agents" section. Cross-tool coverage (Cursor, Claude Code, Codex, OpenCode, Aider, Cline, etc.). — OpenCode support: **Open standard** — cross-tool discovery list.

### kyrolabs/awesome-agents
- **Category**: 22: Awesome-Lists (AI coding agents, cross-tool ones only)
- **URL**: https://github.com/kyrolabs/awesome-agents
- **How it works**: actively maintained — Awesome list of AI Agents across categories (Software Development, Research, Productivity, etc.). OpenCode listed under Software Development alongside Claude Engineer, Cline, Stakpak, ReviewCerberus, Dorothy, Greywall, Maestro Orchestrate, amux, AgentsMesh, Bernstein. — OpenCode support: **Open standard** — cross-tool discovery list.

### awesome-opencode/awesome-opencode
- **Category**: 22: Awesome-Lists (AI coding agents, cross-tool ones only)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: actively maintained, community-driven — The definitive curated list of plugins, themes, agents, projects, and resources specifically for OpenCode. While not "cross-tool" in the broad sense, it is the canonical discovery hub for the OpenCode ecosystem and references many cross-tool compatible resources. — OpenCode support: **Native** — OpenCode-specific awesome-list.

### GetBindu/awesome-claude-code-and-skills
- **Category**: 22: Awesome-Lists (AI coding agents, cross-tool ones only)
- **URL**: https://github.com/GetBindu/awesome-claude-code-and-skills
- **How it works**: maintained — Awesome list focused on Claude Code but cross-references OpenCode-compatible resources (skills, MCP servers) where applicable. Includes skillreaper, pi-reflect, and other cross-tool utilities. — OpenCode support: **Open standard** — lists cross-tool resources usable with OpenCode.

### ai-boost/awesome-harness-engineering
- **Category**: 22: Awesome-Lists (AI coding agents, cross-tool ones only)
- **URL**: https://github.com/ai-boost/awesome-harness-engineering
- **How it works**: 705 stars, maintained — Awesome list for harness engineering. References bradAGI/awesome-cli-coding-agents and cross-tool agent infrastructure. — OpenCode support: **Open standard** — cross-tool discovery list referencing OpenCode ecosystem.

### sandervandegeijn/code-security-scanner
- **Category**: 23: Security Scanners for Agent Configs
- **URL**: https://github.com/sandervandegeijn/code-security-scanner
- **How it works**: actively maintained — Comprehensive security scanner built as a thin Python wrapper around `opencode run`. Six-phase methodology: Discovery → Dependency audit (with osv-scanner) → Per-file review → Confirmation pass → Semantic dedup → Business summary. Defines a custom `scanner` agent in `opencode.json` as a read-only jail (denies bash, edit, write, patch, task, skill, webfetch, websearch). Supports any opencode-supported provider (default: azure/gpt-5.5). `SECURITY_SCAN.md` for project context and whitelisting. — OpenCode support: **Native** — purpose-built around OpenCode's CLI and agent system.

### zm2231/z-audit
- **Category**: 23: Security Scanners for Agent Configs
- **URL**: https://github.com/zm2231/z-audit
- **How it works**: actively maintained — Security audit skill for Claude Code / OpenCode. 7-phase methodology: Stack Detection → Secrets & Credentials → Authentication & Authorization → API Security → Infrastructure-Specific → Security Headers & CORS → Dependencies → Data Exposure. Auto-detects tech stack and runs targeted vulnerability checks. — OpenCode support: **Documented port/adapter exists** — explicitly labeled for Claude Code / OpenCode; manual install works for both.

### remorses/opencode-injection-guard
- **Category**: 23: Security Scanners for Agent Configs
- **URL**: https://github.com/remorses/opencode-injection-guard
- **How it works**: 15 stars, actively maintained — Open-source prompt injection detection for OpenCode. Works with any model — not locked to OpenAI. Intercepts tool outputs via `tool.execute.after` hook and sends them to a separate judge model. If injection detected, original output is replaced with a warning before the main agent sees it. Opt-in via `.opencode/injection-guard.json` config. — OpenCode support: **Native** — OpenCode plugin.

### remorses/opencode-injection-guard
- **Category**: 24: Safety-Net / Guardrail Tools
- **URL**: https://github.com/remorses/opencode-injection-guard
- **How it works**: 15 stars, actively maintained — Prompt injection detection plugin for OpenCode. Intercepts tool outputs (bash, webfetch) via `tool.execute.after` hook, sends to a judge model for injection analysis. Replaces compromised output with a warning before the main agent sees it. Configurable scan patterns. — OpenCode support: **Native** — OpenCode plugin.

### boxpositron/envsitter-guard
- **Category**: 24: Safety-Net / Guardrail Tools
- **URL**: https://github.com/boxpositron/envsitter-guard
- **How it works**: actively maintained — Prevents agents/tools from reading or editing sensitive `.env*` files while allowing safe inspection via EnvSitter (keys + deterministic fingerprints; never values). Hooks into OpenCode's tool system to intercept read/edit/write/patch on `.env*` paths. — OpenCode support: **Native** — OpenCode plugin.

### Greywall
- **Category**: 24: Safety-Net / Guardrail Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode/kyrolabs lists) — actively maintained — Deny-by-default command sandbox for AI coding agents with filesystem isolation, network control via transparent proxy, built-in profiles for agents like Claude Code or OpenCode, and learning mode for auto-generating configs. — OpenCode support: **Documented port/adapter exists** — explicit OpenCode profile support.

### Daytona Sandbox Plugin
- **Category**: 24: Safety-Net / Guardrail Tools
- **URL**: https://github.com/daytonaio/daytona/tree/main/libs/opencode-plugin
- **How it works**: actively maintained (though Daytona repo is no longer maintained, the plugin remains functional) — Runs OpenCode sessions inside isolated Daytona sandboxes. Each session gets its own remote sandbox synced to a local git branch. Complete kernel/filesystem/network isolation. — OpenCode support: **Native** — official OpenCode plugin from Daytona.

### FlowDeck
- **Category**: 24: Safety-Net / Guardrail Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — actively maintained — AI Safety layer built into its workflow orchestration: patch trust scoring, edit gates, phase gating, arch constraint enforcement, failure replay, regression prediction. — OpenCode support: **Native** — OpenCode plugin with embedded safety layer.

### Opencode Hooks Plugin
- **Category**: 25: Hook Management CLIs
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (from awesome-opencode list) — maintained — Bridges Claude Code hooks definition to OpenCode hooks. Allows importing Claude Code-style hook definitions into OpenCode's plugin event system. — OpenCode support: **Documented port/adapter exists** — adapter from Claude Code hooks to OpenCode hooks.

### OpenCode Native Plugin System
- **Category**: 25: Hook Management CLIs
- **URL**: https://opencode.ai/docs/plugins/
- **How it works**: Core feature, actively maintained — OpenCode's plugin system IS its hook system. Plugins are JS/TS modules that return hook objects (`tool.execute.before`, `tool.execute.after`, `session.idle`, `file.edited`, etc.). Hooks are automatically discovered from `~/.config/opencode/plugins/` and `.opencode/plugins/`. No separate CLI needed — hooks are managed as code. — OpenCode support: **Native**

### okdk7788/opencode-self-improving-skills
- **Category**: 26: Self-Improving / Instinct-Mining Tools
- **URL**: https://github.com/okdk7788/opencode-self-improving-skills
- **How it works**: actively maintained — OpenCode plugin that implements a self-improvement loop for agent skills. Two companion skills + five custom tools:

### hqhq1025/skill-optimizer
- **Category**: 26: Self-Improving / Instinct-Mining Tools
- **URL**: https://github.com/hqhq1025/skill-optimizer
- **How it works**: ~125 stars, actively maintained — Agent Skills lifecycle toolkit (covered in Element 1, but core to this category):

### thousandflowers/skillreaper
- **Category**: 26: Self-Improving / Instinct-Mining Tools
- **URL**: https://github.com/thousandflowers/skillreaper
- **How it works**: 47 stars, actively maintained — Evidence-based pruning for AI agent configs. Reads real session transcripts to find skills, MCP servers, and agents loaded but never fired, then safely quarantines dead weight. Supports Claude Code, Codex CLI, Hermes, **OpenCode**, Cursor, and OpenClaw. Single static binary, zero telemetry. `reap` command shows exactly what costs you tokens. — OpenCode support: **Native** — explicitly lists OpenCode in supported platforms; reads OpenCode session transcripts.

### opencode-config
- **Category**: 2: Permission Modes (configs/presets)
- **URL**: https://github.com/joelhooks/opencode-config
- **How it works**: 362 stars, active (recent commits per repo activity) — Joel Hooks' full personal OpenCode setup: commands, custom MCP tools, agents, and a `permission` block in `opencode.jsonc` covering allow/ask/deny per agent (planner/worker/explore/archaeologist/beads/refactorer/reviewer each get different permission profiles) — OpenCode support: **Native** (it's a real `opencode.jsonc` config, directly consumable/adaptable by OpenCode; no adapter needed).

### opencode-permissions
- **Category**: 2: Permission Modes (configs/presets)
- **URL**: https://github.com/NjengaFelix/opencode-permissions
- **How it works**: 0 stars, 2 commits, recent — an OpenCode *Skill* (SKILL.md) packaging permission templates: "Production-Safe," "Developer-Friendly," and "Read-Only Exploration" presets, plus pattern-based bash allow/deny examples — OpenCode support: **Native** (ships as an OpenCode skill consumed directly via `~/.config/opencode/skills/`, and the JSON it generates is native `opencode.json` permission config).

### Sandboxing opencode on macOS (Amin's blog + repo profile)
- **Category**: 2: Permission Modes (configs/presets)
- **URL**: https://aminroosta.github.io/tools/llm/security/macos/2026/02/25/sandboxing-opencode-on-macos.html
- **How it works**: blog post w/ linked repo, dated Feb 25 2026 — a recommended `~/.config/opencode/opencode.json` permission profile pairing OpenCode's native permission block with a macOS `sandbox-exec` "seatbelt" wrapper (denies-by-default, allowlists specific external dirs, restricts `agent.build.tools`) — OpenCode support: **Native** (it's literally OpenCode's own config schema; the sandbox layer is OS-level, not OpenCode-specific).

### Entire CLI
- **Category**: 3: Checkpoints / Rewind Tools
- **URL**: https://github.com/entireio/cli
- **How it works**: 4.3k stars, 332 forks, latest release v0.6.1 (May 7, 2026), 4,266 commits, very active — Git-native session/checkpoint capture tool: hooks into commits, stores full prompt/response transcripts + file diffs on a separate `entire/checkpoints/v1` branch, supports `entire checkpoint rewind` and `entire session resume` — OpenCode support: **Native** (ships a first-class OpenCode integration — `entire enable --agent opencode` installs a real `.opencode/plugins/entire.ts` TypeScript plugin using OpenCode's plugin/event system; docs confirm session-detection via OpenCode's own `session.created`/`session.idle` events and transcript export via `opencode export`. Docs flag this specific integration as "in preview," Bun-runtime-dependent).

### opencode-rewind (opencode-checkpoint)
- **Category**: 3: Checkpoints / Rewind Tools
- **URL**: https://github.com/KyungJunAn/opencode-rewind
- **How it works**: 0 stars, 3 commits — a small OpenCode plugin (`opencode-checkpoint.js`) that snapshots the working tree to a separate `opencode/checkpoints` branch on every `session.idle` event, with `restore_checkpoint` and `list_checkpoints` agent-callable tools, using `git commit-tree` so it never touches your real branch — OpenCode support: **Native** (it's an OpenCode plugin built directly against OpenCode's plugin API and event system — `.opencode/plugin/` install path).

### opencode-dynamic-context-pruning (DCP)
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/Opencode-DCP/opencode-dynamic-context-pruning
- **How it works**: 3.9k stars, 216 forks, 1,365 commits, very active (npm: `@tarquinen/opencode-dcp`) — model-driven context pruning plugin: exposes a `compress` tool the model calls when it decides context is stale (not a static threshold trigger like native compaction), plus automatic deduplication of repeated tool calls and pruning of errored-tool inputs after N turns; protects `task`/`skill`/`todowrite`/etc. from pruning by default — OpenCode support: **Native** (published and installed as a first-class OpenCode plugin via `opencode plugin @tarquinen/opencode-dcp@latest --global`; config lives under `.opencode/dcp.json(c)`). Note: primary development has since shifted to a separate cross-harness tool called "Sleev" — DCP itself is now in maintenance mode per the repo's own README.

### magic-context (CortexKit)
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/cortexkit/magic-context
- **How it works**: recently updated (repo activity ~6 days old per search), part of "CortexKit" — background/automatic context manager: runs a separate "historian" model to compress older conversation while the main agent keeps working, persists cross-session project memory, and an "overnight dreamer" agent that consolidates and deduplicates memories — explicitly designed to disable itself if OpenCode's native compaction or DCP (above) is also active, to avoid double-compression — OpenCode support: **Native** (ships as an OpenCode plugin — see companion repo below — that directly detects and coordinates with OpenCode's own `compaction.auto`/`compaction.prune` settings).

### opencode-magic-context
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/g1331/opencode-magic-context
- **How it works**: the actual OpenCode plugin implementation of Magic Context (companion/fork of cortexkit/magic-context) — adds a TUI sidebar showing live context breakdown, token usage, and historian status directly in the OpenCode terminal, plus five agent-callable tools including `ctx_reduce` — OpenCode support: **Native** (built specifically as an OpenCode plugin, using OpenCode's plugin/TUI extension points).

### magic-compact
- **Category**: 4: Context Management Tools
- **URL**: https://github.com/aerovato/magic-compact
- **How it works**: ~129 stars (per SkillsLLM security-scan listing) — "lossless" context compression: instead of collapsing history into one generic summary, it condenses each old assistant turn into its own summary while preserving user messages and tool calls verbatim; ships a `/magic-compact [N]` command (N = turns to preserve) and a separate `/magic-trim [N]` for tool I/O pruning only; creates a session backup before compacting — OpenCode support: **Native** (explicit dual-platform plugin — README states "Lossless context compression plugin for Claude Code & OpenCode," installed via `opencode plugin magic-compact --global`; author notes OpenCode support will deepen as OpenCode's plugin API exposes more hooks, i.e. currently a bit behind the Claude Code side but fully functional).

### oh-my-openagent
- **Category**: 5: Hooks (collections/frameworks)
- **URL**: https://github.com/code-yeongyu/oh-my-openagent
- **How it works**: (formerly/also published as `oh-my-opencode`) — 67.3k stars, 5.5k forks, 11,932 commits, extremely active — the dominant OpenCode "batteries included" plugin: ships 54+ lifecycle hooks (61 with Team Mode enabled) across categories like rules-injection, todo-enforcement, comment-checking, auto-resume, and a **full Claude Code hooks-compatibility layer** (PreToolUse, PostToolUse, UserPromptSubmit, Stop events all supported) alongside its own agents/MCPs/tools — OpenCode support: **Native** (it *is* an OpenCode plugin, installed via `bunx oh-my-openagent install`, registered in `opencode.json`'s `plugin` array; the Claude Code hook compatibility is a bonus layer inside it, not the core mechanism). Note: repo/README states Anthropic has restricted OAuth access citing this project by name as a reason for blocking some OpenCode usage patterns (see the repo's own "Claude OAuth Access Notice" section) — relevant context if using it with a Claude subscription.

### Opencode Hooks Plugin
- **Category**: 5: Hooks (collections/frameworks)
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (listed entry, exact repo name not separately confirmed beyond the awesome-list description) — "Use Claude code hooks definition and hook them to opencode hooks" — a lightweight, single-purpose compatibility shim distinct from oh-my-openagent's bundled version, aimed at people who want *just* Claude Code hook-format support without the rest of oh-my-openagent's agent/MCP bundle — OpenCode support: **Documented port/adapter** (translates Claude Code's hooks JSON schema into OpenCode's native plugin hook calls; listed in the community awesome-opencode curated directory specifically under hook-compatibility tooling).

### OpenAgentsControl
- **Category**: 5: Hooks (collections/frameworks)
- **URL**: https://github.com/darrenhinde/OpenAgentsControl
- **How it works**: ~4.5–4.6k stars (star count fluctuates slightly across cached pages, consistently in this range), active — a plan-first, approval-gated agent framework with a `.opencode/plugin/` directory that auto-loads plugins on OpenCode startup, 7 specialized subagents, and a context/pattern-injection system (`/add-context`); its plugin layer implements hook-style lifecycle behavior (approval gates before write/edit/bash) — OpenCode support: **Native** (built directly on OpenCode's `.opencode/plugin/` and `.opencode/agent/` conventions; also separately distributed as a Claude Code plugin, but the OpenCode integration is first-class, not a port).

### Context7
- **Category**: 6: MCP Servers
- **URL**: https://github.com/upstash/context7
- **How it works**: 39.3k+ stars — fetches current, version-specific library documentation and injects it into the agent's context on request (triggered via "use context7" in the prompt) — OpenCode support: **Works via open standard** (plain MCP server, added under `opencode.json`'s `mcp` key like any other; no Claude-Code-specific dependency).

### GitHub MCP Server
- **Category**: 6: MCP Servers
- **URL**: https://github.com/github/github-mcp-server
- **How it works**: 27.4k+ stars — official GitHub server: repo/PR/issue management, code search, Actions logs — OpenCode support: **Works via open standard**, and additionally has an **explicit official OpenCode install guide** (`docs/installation-guides/install-opencode.md`) with exact `opencode.json` config examples for both Docker and OAuth/PAT auth flows — closer to "Native/documented" than most, since GitHub itself publishes the OpenCode-specific config.

### Playwright MCP
- **Category**: 6: MCP Servers
- **URL**: https://github.com/microsoft/playwright-mcp
- **How it works**: 30.6k+ stars — official Microsoft server for browser automation via structured accessibility snapshots — OpenCode support: **Works via open standard** (plain stdio MCP server).

### opencode-mcp (Traves-Theberge)
- **Category**: 6: MCP Servers
- **URL**: https://github.com/Traves-Theberge/opencode-mcp
- **How it works**: exposes **OpenCode itself** as an MCP server/subagent, so other MCP clients (Claude Desktop, Cursor, Claude Code, etc.) can delegate coding tasks *to* OpenCode — OpenCode support: **Native** (this tool's entire purpose is bridging into OpenCode's own headless/server API; it's not something OpenCode consumes, but something that consumes OpenCode).

### opencode-mcp (AlaeddineMessadi)
- **Category**: 6: MCP Servers
- **URL**: https://github.com/AlaeddineMessadi/opencode-mcp
- **How it works**: similarly bridges any MCP client to OpenCode's headless API (80 tools, 10 resources, 6 prompts) so e.g. Claude can delegate "build me a REST API" work to an autonomous OpenCode session — OpenCode support: **Native** (built directly against OpenCode's headless server API).

### opencode-docs-mcp
- **Category**: 6: MCP Servers
- **URL**: https://github.com/sandbox-technologies/opencode-docs-mcp
- **How it works**: a Mintlify-style MCP server that serves OpenCode's own documentation (search, get-page, browse-toc) — usable *from* OpenCode via its own `mcp` config, and useful for agents needing to answer questions about OpenCode itself — OpenCode support: **Works via open standard** (also ships an `opencode.json` config snippet directly in its README).

### Docker Sandboxes
- **Category**: 7: Sandboxing Tools
- **URL**: https://www.docker.com/blog/docker-sandboxes-a-new-approach-for-coding-agent-safety/
- **How it works**: official Docker initiative (blog-announced, in active development) — purpose-built local sandboxes that wrap coding agents (explicitly including OpenCode, alongside Claude Code, Gemini CLI, Codex, Kiro) in containers mirroring the local workspace with enforced boundaries — OpenCode support: **Documented port/adapter** (Docker explicitly lists OpenCode as one of the supported agents this feature targets; not a community plugin but a vendor-backed adapter).

### opencode-sandbox (npm package, via bubblewrap)
- **Category**: 7: Sandboxing Tools
- **URL**: https://npmx.dev/package/opencode-sandbox
- **How it works**: an OpenCode **plugin** (auto-installed from npm) that wraps every `bash` tool invocation using `@anthropic-ai/sandbox-runtime`, applying OS-level filesystem/network restrictions via Bubblewrap — no containers or VMs; intercepts via `tool.execute.before`/`tool.execute.after` hooks and gracefully falls back to unsandboxed execution if bubblewrap/init fails — OpenCode support: **Native** (built directly as an OpenCode plugin using OpenCode's own hook system; also directly builds on Anthropic's `sandbox-runtime` package, making it a genuine cross-tool bridge).

### thisisryanswift/opencode-sandbox
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/thisisryanswift/opencode-sandbox
- **How it works**: an OpenCode plugin that auto-provisions isolated sandboxes (Daytona, E2B, Sprites, or Docker fallback, auto-detected) per session; syncs project files in, respects `.gitignore` so secrets never enter the sandbox, translates paths transparently, and syncs changes back via git on idle — OpenCode support: **Native** (plugin architecture under `.opencode/plugin/`, directly using OpenCode's plugin/session lifecycle).

### comsysto/opencode-sandbox
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/comsysto/opencode-sandbox
- **How it works**: Docker + `mise`-based sandbox giving each project scoped filesystem access, independent per-project provider/API-key config, and persistent session state across container restarts; ships an interactive `ocs-init` setup wizard — OpenCode support: **Native** (purpose-built specifically to wrap OpenCode; generates `opencode.jsonc` as part of its own init flow).

### mattolson/agent-sandbox (agentbox)
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/mattolson/agent-sandbox
- **How it works**: general secure local dev environment for AI coding agents (not OpenCode-exclusive) with a policy-based network proxy restricting which provider endpoints are reachable — has a **documented OpenCode agent guide** (`docs/agents/opencode.md`) covering config-based permission setup and provider policy files specific to OpenCode — OpenCode support: **Documented port/adapter** (explicit first-party OpenCode documentation page, distinct from its Claude Code / Codex / Gemini docs).

### rivet-dev/sandbox-agent
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/rivet-dev/sandbox-agent
- **How it works**: Rust-based universal HTTP adapter for running coding agents (Claude Code, Codex, OpenCode, Amp, Pi) inside sandboxes and controlling them remotely; ships an **experimental OpenCode-compatible API** (`/opencode` endpoint) so OpenCode SDK/UI clients can connect through it — OpenCode support: **Documented port/adapter** (explicit "OpenCode Compatibility" doc page; flagged experimental by the maintainers, provider/model metadata "may differ from native OpenCode grouping").

### arezi/opencode-sandbox
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/arezi/opencode-sandbox
- **How it works**: and **[fabianlema/opencode-sandbox](https://github.com/fabianlema/opencode-sandbox)** — both simple Docker-wrapper scripts (mapped home directory / pre-installed dev tools respectively) that run the OpenCode binary inside a container — OpenCode support: **Native** (purpose-built OpenCode wrappers, though very thin — essentially `docker run` scripts, not deep integrations).

### JulScsl/opencode-sandbox
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/JulScsl/opencode-sandbox
- **How it works**: Windows-specific variant using Podman/Docker, bundles Serena alongside OpenCode — OpenCode support: **Native** (purpose-built OpenCode wrapper for Windows).

### zaid-marji/opencode-sandbox
- **Category**: 7: Sandboxing Tools
- **URL**: https://github.com/zaid-marji/opencode-sandbox
- **How it works**: minimal Docker wrapper mounting only the project directory plus a dedicated OpenCode-state directory, runs as non-root, documents optional hardening flags (`--read-only`, `--cap-drop=ALL`) — OpenCode support: **Native** (purpose-built OpenCode wrapper).

### awesome-opencode-subagents
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/ankitmundada/awesome-opencode-subagents
- **How it works**: "100+ subagents for opencode" (star count not independently confirmed in search results, but positioned by the author as "the definitive collection of OpenCode CLI subagents") — organized into 10 categories (core development, language specialists, infrastructure, quality/security, data/AI, developer experience, specialized domains, business/product, meta-orchestration, research/analysis); ships an interactive `install-agents.sh` script that browses categories and installs/uninstalls agents individually, plus a curl-based installer that doesn't require cloning — OpenCode support: **Native** (each subagent is a Markdown file with YAML frontmatter written specifically for OpenCode's `~/.config/opencode/agents/` / `.opencode/agents/` convention; the companion `awesome-gemini-cli-subagents` repo by the same author confirms a deliberate per-tool-format release pattern, not a blind cross-post).

### OpenAgentsControl
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/darrenhinde/OpenAgentsControl
- **How it works**: ~4.5–4.6k stars (see Element 5 for full detail) — ships 7 specialized subagents (task-manager, context-scout, context-manager, coder-agent, test-engineer, code-reviewer, external-scout) plus category specialists (frontend, devops, copywriter, technical-writer, data-analyst) as part of its broader plan-first framework — OpenCode support: **Native** (subagents defined directly in `.opencode/agent/` following OpenCode's own format; also separately distributed as a Claude Code plugin, but the OpenCode agents are first-class, not ported).

### oh-my-openagent
- **Category**: 8: Subagents (collections)
- **URL**: https://github.com/code-yeongyu/oh-my-openagent
- **How it works**: 67.3k stars (see Element 5) — ships a curated set of purpose-built agents (Sisyphus main orchestrator, Prometheus planner, Oracle for architecture/debugging, Librarian for docs/code search, Explore for fast grep, Hephaestus autonomous worker) with each tuned to a specific model — OpenCode support: **Native** (agents are core to the plugin's own OpenCode-specific architecture, not a separate "collection" bolted on).

### awesome-opencode
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: 8.5k stars, 605 forks, active (data-driven: entries are YAML files validated against a JSON schema, README auto-generated by CI) — the largest curated directory of OpenCode plugins, themes, agents, and resources, organized by category (plugins, themes, agents, MCP, resources) with live star-count badges per entry — OpenCode support: **Native** (this is *the* de facto community index for OpenCode-native resources specifically; not a cross-tool list with occasional OpenCode entries).

### opencode-marketplace (NikiforovAll)
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/NikiforovAll/opencode-marketplace
- **How it works**: CLI for installing OpenCode plugins from local directories or GitHub repos/subfolders; understands OpenCode's actual plugin directory layout (`command/`, `agent/`, `skill/` — recognizing both `.opencode/` and `.claude/` prefixed variants for cross-compat), supports install/update/list/scan(dry-run)/uninstall — OpenCode support: **Native** (built specifically around OpenCode's own plugin component layout, with explicit awareness of the `.opencode/` convention).

### opencode-market (CKGrafico)
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/CKGrafico/opencode-market
- **How it works**: CLI explicitly built to fill the "OpenCode has no official marketplace" gap (per the maintainer's own linked GitHub comment on an OpenCode issue); registers marketplaces from a repo's `marketplace.json`, installs plugins globally (`~/.agents/`) or to project-local `.opencode/` folders; notably also converts **Claude Code and GitHub Copilot** agents/skills into OpenCode-compatible form — OpenCode support: **Native**, plus **documented port/adapter** for its Claude Code / Copilot conversion feature specifically.

### opencode-plugin-marketplace (Tommertom)
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/Tommertom/opencode-plugin-marketplace
- **How it works**: community-driven marketplace exposing a `/plugin` slash command (`list`, `install <name>`, `create <name>`, `remove <name>`) directly inside the OpenCode TUI; explicitly flagged experimental by its author, and submissions must validate against a `schema/plugin.schema.json` — OpenCode support: **Native** (installs a real OpenCode command file at `~/.config/opencode/command/plugin.md`; built entirely around OpenCode's own command system).

### n-skills (numman-ali)
- **Category**: 9: Plugins / Plugin Marketplaces
- **URL**: https://github.com/numman-ali/n-skills
- **How it works**: curated marketplace distributed via the "openskills" universal installer; explicitly lists OpenCode as one of the supported targets alongside Claude Code, Cursor, Windsurf, and Cline, and states it "works with... anything that reads AGENTS.md" — OpenCode support: **Works via open standard** (relies on OpenCode's AGENTS.md / skill-discovery conventions rather than a bespoke OpenCode-only integration, and is explicitly cross-tool by design rather than OpenCode-native).

### oh-my-openagent's Background Task System
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/code-yeongyu/oh-my-openagent
- **How it works**: 67.3k stars (see Elements 5 & 8) — built-in background task manager (`BackgroundManager` + `ConcurrencyManager`) that launches multiple AI agent tasks simultaneously, each in an independent session, with three-level concurrency control (model > provider > default), live status tracking (`bg_<id>`, running/pending/completed states), and automatic notification on completion so the main session doesn't need to poll — enabled automatically under "ultrawork" mode or configurable individually — OpenCode support: **Native** (core subsystem of this OpenCode-native plugin, not a bolt-on). Caveat: a filed bug ([issue #3452](https://github.com/code-yeongyu/oh-my-openagent/issues/3452)) notes `opencode run` (headless/CI mode) can exit prematurely while background tasks are still active if no todos exist — worth checking before relying on it in CI.

### opencode-background-agents (kdcokenny)
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/kdcokenny/opencode-background-agents
- **How it works**: part of the "KDCO" plugin registry/ecosystem, installed via `ocx add kdco/background-agents` — async delegation plugin specifically designed to survive context compaction: background research/task results are persisted to disk as Markdown rather than kept only in the live context window, so a compaction event doesn't erase in-flight work; uses a "fire and forget, notify when ready" (waiter-service) model — OpenCode support: **Native** (installs directly as an OpenCode plugin under `.opencode/plugin/`; source is copyable manually if you don't want the `ocx` package manager dependency).

### opencode-background-task (zeigarnick)
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/zeigarnick/opencode-background-task
- **How it works**: MIT-licensed, lightweight standalone plugin exposing three agent-callable tools: `background_task` (launch async), `background_output` (poll/retrieve results by `task_id`), `background_cancel` (cancel one or all) — supports configurable concurrency limits, including per-provider and per-model caps — OpenCode support: **Native** (built directly against OpenCode's plugin system, installed via `.opencode/plugins/` + `opencode.json`'s `plugin` array).

### opencode-background (zenobi-us)
- **Category**: 11: Background Task Tools
- **URL**: https://github.com/zenobi-us/opencode-background
- **How it works**: a different flavor: manages long-running **shell processes** (build watchers, test runners, dev servers) rather than agent subtasks — supports tagging (`["build","critical"]`), listing/filtering by tag, killing individual processes, and persisting global-scoped processes across sessions — OpenCode support: **Native** (configured directly in OpenCode's `config.json`, built specifically for OpenCode's process-management needs — this is the tool to reach for if your "background task" need is dev-server/build-pipeline management rather than agent delegation).

### Open Code Review (OCR)
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/alibaba/open-code-review
- **How it works**: Alibaba-maintained, "battle-tested at Alibaba's scale" (star count not directly confirmed in results, but backed by a major-vendor org account) — hybrid architecture combining deterministic pipelines with an LLM agent for precise line-level review comments; built-in multi-language ruleset covering NPE, thread-safety, XSS, SQL injection; benchmarked at higher precision/F1 than general-purpose agents like Claude Code while using ~1/9 the tokens; ships both a CLI (`ocr review`, `ocr scan`) and an MCP server (`ocr_scan`, `ocr_heal`, `ocr_explain`) — OpenCode support: **Works via open standard** (the MCP server follows standard MCP, consumable by OpenCode's native MCP client like any other server; the CLI itself is agent-agnostic and provider-configurable rather than Claude-Code-specific).

### opencode-security-agent
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/red-orbita/opencode-security-agent
- **How it works**: purpose-built for OpenCode specifically — v2 is a **real-time defense plugin** using OpenCode's native `tool.execute.before` hook to block credential exfiltration, known-bad domains (hardcodes the domain from the real Postmark MCP backdoor incident), reverse shells, `curl|bash` pipes, and prompt-injection attempts *before* they execute — not just after-the-fact scanning; v1's static scanner (vulnerability-database scanning, source-integrity verification, coherence analysis) is still bundled; also ships a GitHub Action producing SARIF output that appears in the GitHub Security tab alongside CodeQL — OpenCode support: **Native** (built directly on OpenCode's plugin/hook system — this is the most OpenCode-specific tool found in this category, not a port from anywhere else).

### security-reviewer agent (Opencode-Workflows)
- **Category**: 12: Security-Review Tools
- **URL**: https://github.com/IgorWarzocha/Opencode-Workflows/blob/master/agents/security-reviewer/README.md
- **How it works**: part of a broader "Opencode-Workflows" example repo — a specialized OpenCode subagent for auditing AI-integrated codebases specifically (exposed API keys, insecure configs, framework-specific issues), with a skill-auto-selection mechanism that loads the relevant scanning skills based on detected tech stack — OpenCode support: **Native** (delivered as an OpenCode agent definition, using OpenCode's native agent + skill-loading conventions).

### opencode-primer
- **Category**: 13: Headless / CI Setups
- **URL**: https://github.com/wesammustafa/opencode-primer
- **How it works**: (repo slug: `wesammustafa/OpenCode-Everything-You-Need-to-Know`) — comprehensive reference/guide repo covering setup, agents, skills, plugins, MCP, and **headless CI** as a dedicated section — documents the full one-shot/headless command surface (`opencode run`, `--format json`, `--auto` "CI only" flag, `--mini` lightweight mode from v1.17.10+, `opencode stats`, `opencode export --sanitize`) and links out to CI recipes for both GitHub Actions and GitLab CI — OpenCode support: **Native** (this is a documentation/reference repo for OpenCode's own native headless commands, not a separate tool — included here because it's the most complete single write-up of the surface found in this sweep, useful as a map of what's already built in).

### opencode-shell-strategy
- **Category**: 13: Headless / CI Setups
- **URL**: https://github.com/anomalyco/opencode/pull/5995
- **How it works**: (linked via an ecosystem-page PR; standalone repo referenced but not directly resolved in search) — an **instructions file** (not a plugin) teaching the LLM to avoid interactive shell commands that hang in OpenCode's non-TTY headless environment — covers safe flags for package managers (`npm init -y`, `apt-get install -y`, `pip install --no-input`), Git operations (`git commit -m` instead of opening an editor, `--no-edit` on merges), and a banned-commands list (editors like `vim`/`nano`, pagers like `less`/`more`/`man`) that would otherwise hang a headless run waiting for interactive input — OpenCode support: **Native** (distributed as an OpenCode-consumable instructions/AGENTS.md-style file, specifically targeting OpenCode's non-TTY CI behavior; PR shows it being added to the official OpenCode ecosystem/plugins listing page).

### ocsight
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/heyhuynhgiabuu/ocsight
- **How it works**: the most feature-complete entry found: install via Homebrew/npm/direct binary; `ocsight summary`, `ocsight budget set --monthly <N>` with spending alerts, `ocsight live` real-time dashboard, session drill-down/browsing, pricing browser across 500+ models, multi-format export for reporting — OpenCode support: **Native** (built specifically to read OpenCode's local usage data; not a generic multi-tool tracker).

### opencode-token-monitor
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/Ainsley0917/opencode-token-monitor
- **How it works**: real-time OpenCode plugin (not just a log-reader) tracking input/output/reasoning/cache tokens live; agent×model and tool×command cost attribution; trend analysis with week-over-week comparison and cost-spike detection; ASCII terminal charts; configurable daily/weekly/monthly budget thresholds with toast notifications; exposes three agent-callable tools (`token_stats`, `token_history`, `token_export`) — OpenCode support: **Native** (installed directly via the `plugin` array in `opencode.json`; deepest integration of the group since it hooks live rather than reading exported data after the fact).

### opencode-tokenscope / opencode-tokenscope-plugin
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/ramtinJ95/opencode-tokenscope
- **How it works**: (also mirrored at `pantheon-org/opencode-tokenscope-plugin`) — the most analytically deep entry: per-provider-step telemetry (fresh input vs. cache read/write vs. output vs. reasoning), cache hit-rate and effective-rate analysis, **recursive subagent cost rollup** (child-session usage/cost from Task-tool-spawned subagents), context-budget breakdown by system override/skills/subagents/tool schemas, and explicit uncertainty warnings when pricing/metadata is incomplete — supports 41+ models with cache-aware pricing — OpenCode support: **Native** (built against `@opencode-ai/plugin >=1.1.48`, version-pinned and explicitly verified against OpenCode v1.17.18).

### opencode-usage (gaboe)
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/gaboe/opencode-usage
- **How it works**: simple CLI (`bunx opencode-usage`) with daily/monthly breakdowns, provider breakdown (Anthropic/OpenAI/Google/etc.), and an optional web dashboard (`--commander` flag) — OpenCode support: **Native**.

### opencode-stats (Cateds)
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/Cateds/opencode-stats
- **How it works**: terminal dashboard reading OpenCode's local SQLite DB or JSON exports; tokens, cost estimates, model/provider distribution, 365-day activity heatmap, image/text share-card export; explicitly "Inspired by Claude Code's `/stats` command" as an independent OpenCode-native reimplementation — OpenCode support: **Native**.

### opencode-dashboard (touchkale)
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/touchkale/opencode-dashboard
- **How it works**: single-file, zero-dependency Python HTTP dashboard; auto-refreshing, session history, per-day token/message charts, cost-by-model, tool usage, work-hour heatmap, click-to-filter by day/tool/agent/model; ships a macOS `.command` launcher for a standalone app-window experience — OpenCode support: **Native**.

### opencode-token-tracker (tongsh6)
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/tongsh6/opencode-token-tracker
- **How it works**: real-time tracking plugin with a clean CLI summary view (today's usage, by-model breakdown) and a `trend` subcommand for cost/token charts over configurable day ranges and widths — OpenCode support: **Native**.

### opencode-bar (opgginc)
- **Category**: 14: Usage / Cost Tracking Tools
- **URL**: https://github.com/opgginc/opencode-bar
- **How it works**: macOS **menu-bar** app (different form factor from the rest — always-visible, not a CLI/terminal dashboard); tracks usage across multiple providers simultaneously with color-coded progress indicators, EOM cost prediction via weighted averages, per-provider subscription-plan configuration, and auth-source labeling (detects whether a token came from OpenCode, VS Code, or system Keychain) — OpenCode support: **Native** (one of several sources it tracks, alongside other tools' auth stores — worth choosing this one specifically if you want a persistent menu-bar view rather than an on-demand CLI check).

### Orkas
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/Orkas-AI/Orkas
- **How it works**: open-source multi-agent desktop client (macOS/Windows/Linux); a "Commander" LLM decomposes goals and dispatches specialist sub-agents in parallel or series, with self-evolving agents (reflection + "skill crystallization") retaining private skills/memory across tasks; local-first (all data/keys stay on disk, model calls go direct to provider, never proxied); explicitly lists **OpenCode as one of the external CLI coding agents it can plug in and orchestrate**, alongside Claude Code, Codex, and Cline — OpenCode support: **Documented port/adapter** (OpenCode is named as a supported external CLI agent target in the project's own description, not merely "cross-tool" in the abstract).

### opencode-swarm
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/ZaxbyHub/opencode-swarm
- **How it works**: architect-centric agentic swarm **plugin for OpenCode itself** (not an external orchestrator) — turns a single OpenCode session into a hub-and-spoke team: one agent writes code, a different agent reviews it, another writes/runs tests, another checks security, with required gates that must pass before anything ships; installer auto-registers as an OpenCode plugin and disables the conflicting native explore/general agents; live roster viewable via `/swarm agents` — OpenCode support: **Native** (this is the deepest, most purpose-built entry in the category — built specifically as an OpenCode plugin, not adapted from elsewhere).

### opencode-orca
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/ex-machina-co/opencode-orca
- **How it works**: a different, smaller "Orca" project (not to be confused with the Orca/orca IDE below) — an OpenCode plugin implementing a Planner + Specialists team (Coder, Tester, Reviewer, Researcher, Document Writer, Architect) under a central "Orca" orchestrator, with per-agent supervision toggles configurable in `opencode.json` — OpenCode support: **Native** (purpose-built OpenCode plugin).

### Orca (stablyai)
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/stablyai/orca
- **How it works**: "AI Orchestrator for 100x builders" — an ADE (agent development environment, not a plugin) running Codex, Claude Code, **OpenCode**, or Pi side-by-side, each in its own git worktree, with a "fan one prompt across five agents, compare and merge the winner" workflow; desktop + mobile + VPS availability — OpenCode support: **Documented port/adapter** (OpenCode explicitly named as one of the four supported coding-agent backends).

### Vibe Kanban
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/BloopAI/vibe-kanban
- **How it works**: (referenced via the Agent-Analytics curated list) — Apache-2.0 kanban workspace for planning, running, reviewing, and shipping parallel coding-agent work "across Claude Code, Codex, Gemini CLI, **OpenCode**, and related agents" — OpenCode support: **Documented port/adapter** (explicitly named support).

### Agent Orchestrator (AgentWrapper / mirrored at Untrivial-ai)
- **Category**: 15: Agent-Team Frameworks
- **URL**: https://github.com/AgentWrapper/agent-orchestrator
- **How it works**: agent IDE managing fleets of coding agents (Claude Code, Codex, Cursor, Kimi Code, **opencode**, and others) sharing one workspace, with automatic CI-failure/review-comment/merge-conflict routing back to the right agent — OpenCode support: **Documented port/adapter** (OpenCode explicitly listed among supported terminal-based agents).

### Superpowers
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/obra/superpowers
- **How it works**: by Jesse Vincent (obra); reported star counts vary by source/date across the sweep's search results (89K+ per one March 2026 writeup, 129K+ by April 2026, 224K+ by June 2026 per another source — the discrepancy likely reflects genuinely explosive, ongoing growth rather than conflicting facts) — not a workflow-orchestration tool in the DAG sense but a **mandatory-workflow discipline framework**: composable Markdown skills enforcing brainstorm → design → plan → TDD implementation → two-stage review as an auto-triggering, non-optional pipeline; subagent-driven development with fresh context per task — OpenCode support: **Native** (explicitly listed as one of Superpowers' supported harnesses — Claude Code, Codex CLI/App, Factory Droid, Gemini CLI, **OpenCode**, Cursor, GitHub Copilot CLI — though installation is harness-specific: "OpenCode uses its own plugin install; install Superpowers separately even if you already use it in another harness," per ClaudePluginHub's listing). Covered in more depth under Element 18 (discipline/skill packs), where it more precisely belongs; flagged here because multiple sources describe it using workflow/pipeline language.

### opencode-workflows (mark-hingston)
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/mark-hingston/opencode-workflows
- **How it works**: the most "traditional workflow engine" entry found: a real deterministic pipeline plugin built on the Mastra workflow engine — JSON or type-safe TypeScript workflow definitions, step dependencies (`after:`), shell-command steps, event-based triggers (e.g. `file.change` with glob patterns, debounced 300ms to avoid rapid re-fires), and explicit support for orchestrating multiple AI agents in a deterministic pipeline — OpenCode support: **Native** (built specifically as an OpenCode plugin, workflows live under `.opencode/workflows/`).

### Open Dynamic Workflow
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/travisliu/open-dynamic-workflow
- **How it works**: local-first workflow *runner* orchestrating **external** coding-agent CLIs, explicitly including OpenCode alongside Codex, Gemini, Copilot, Antigravity, Pi, Cursor, and a deterministic mock provider for dry runs — supports `parallel()` fan-out + `agent()` fan-in summarization patterns, tool execution, child workflows, and goal-oriented loops; has explicit per-provider permission-flag mapping documented for OpenCode specifically (`dangerously-full-access` → `--dangerously-skip-permissions`) — OpenCode support: **Documented port/adapter** (OpenCode is one of several named, individually-mapped backend targets, with OpenCode-specific flag translation documented in the README).

### Open Dynamic Workflows (OpenCode plugin variant)
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (listed entry, distinct companion project to the above per the awesome-opencode directory's description) — "brings Claude-Code-style dynamic workflows and ultracode to OpenCode": a local daemon runs a generated orchestration script with concurrent agents, adversarial verification, and crash-resume; the OpenCode plugin half adds `/workflow`/`/ultracode` trigger commands plus a planning UI inside OpenCode — OpenCode support: **Native** (the plugin component is built specifically for OpenCode; MIT-licensed, model-agnostic — Anthropic, any OpenAI-compatible endpoint, or local Ollama).

### NERV
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/awesome-opencode/awesome-opencode
- **How it works**: (listed entry) — "invisible engineering infrastructure for AI agents": Spec-Driven Development pipeline, an A2A (agent-to-agent) task-delegation hub, persistent semantic memory (MAGI), and 9 specialized subagents for OpenCode; `nerv init` scaffolds 45+ files including SDD skills, slash commands, MCP servers, and lifecycle plugins — OpenCode support: **Native** (purpose-built OpenCode scaffold/framework).

### opencode-agent-orchestration-kit
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit
- **How it works**: a starter kit (not a generic engine) packaging product-development workflows as OpenCode agents/commands, with optional adapters for Open Design, Superpowers, Impeccable, Docker, and token-usage plugins; explicitly favors "local, inspectable configuration over hosted orchestration services" and documents who it's for vs. not for (small teams wanting repeatable workflows vs. those wanting a hosted multi-agent platform with billing/dashboards) — OpenCode support: **Native** (core kit built specifically around and requiring OpenCode).

### Opencode-Workflows (IgorWarzocha)
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/IgorWarzocha/Opencode-Workflows
- **How it works**: "an ever evolving repository of OpenCode workflow examples... I only left the stuff that actually works" — includes the "Ralph Wiggum Loop" (`/loop`, a deliberately simple while-loop pushing a task subagent through repeated implementation+verification cycles until 100% complete), a plugin-creation workflow bundle, model-specific focused-mode prompt injectors, and an `openspec-orchestrator` for strict spec formatting/validation — OpenCode support: **Native** (all examples are OpenCode agent/command/plugin files, not ported from elsewhere).

### opencode-orch-mode
- **Category**: 16: Workflow Orchestration Tools
- **URL**: https://github.com/agents-to-go/opencode-orch-mode
- **How it works**: an orchestration workflow specifically designed to keep smaller/faster/"dumber" models on-plan: a structured collaborative-planning-then-execution loop with continuous review/QA, using two named agents (e.g. `@grok` as executor, `@glm` as reviewer) cycling through numbered implementation/review files (`01-code.md`, `02-review.md`, etc.) until done — OpenCode support: **Native** (installs as a slash command in OpenCode's global config plus companion subagent Markdown files).

### ai-sdk-provider-opencode-sdk
- **Category**: 17: Agent SDKs
- **URL**: https://github.com/ben-vargas/ai-sdk-provider-opencode-sdk
- **How it works**: a Vercel AI SDK community provider that wraps OpenCode's SDK, letting developers call `generateText()` (and the rest of the Vercel AI SDK surface) against any model configured in OpenCode, auto-starting an OpenCode server if needed — supports full provider/model addressing (`anthropic/claude-sonnet-4-5-...`, `openai/gpt-5.3-codex-spark`, etc.) and custom settings (hostname, port, default agent, session title) — OpenCode support: **Native** (built directly on top of `@opencode-ai/sdk`, not a port from another tool — this is the standout entry for developers who want OpenCode's configured-provider access inside standard Vercel AI SDK code rather than calling OpenCode's SDK directly).

### opencode-mcp (Traves-Theberge)
- **Category**: 17: Agent SDKs
- **URL**: https://github.com/Traves-Theberge/opencode-mcp
- **How it works**: and **[opencode-mcp (AlaeddineMessadi)](https://github.com/AlaeddineMessadi/opencode-mcp)** — covered in full under Element 6 (MCP servers); both bridge external MCP clients into OpenCode's headless/server API, functioning as an alternate, protocol-level "SDK" for driving OpenCode from outside — OpenCode support: **Native** (built directly against OpenCode's headless server API — cross-referenced here rather than duplicated in full).

### Superpowers
- **Category**: 18: Discipline/Skill Packs (Superpowers/ponytail-style)
- **URL**: https://github.com/obra/superpowers
- **How it works**: by Jesse Vincent (obra) — star counts reported across sources in this sweep show explosive, ongoing growth (89K+ as of one March 2026 writeup, 129,443 by April 2026, 224,691 by June 2026 per a later source) — an agentic skills framework and software-development methodology enforcing a mandatory (non-optional, auto-triggering) pipeline: clarify → design → plan → red/green TDD implementation → two-stage review (spec compliance, then code quality), plus systematic-debugging (4-phase root-cause process) and subagent-driven-development with fresh context per task. Distributed through Anthropic's official Claude plugin marketplace and, separately, seven other harnesses. Skills are self-enforcing: the flagship `writing-skills` skill explicitly designs against agent rationalization under pressure ("agents are smart and will find loopholes... write skill before testing? Delete it. Start over.") — OpenCode support: **Native** (explicitly listed as one of Superpowers' supported harnesses; per ClaudePluginHub's own listing: "OpenCode uses its own plugin install; install Superpowers separately even if you already use it in another harness" — meaning the OpenCode installation path is real and distinct, not a generic fallback).

### opencode-power-pack
- **Category**: 18: Discipline/Skill Packs (Superpowers/ponytail-style)
- **URL**: https://github.com/waybarrios/opencode-power-pack
- **How it works**: 45 (README also cites 55 in places, likely reflecting recent additions) rigorous skills for Codex, OpenCode, and Pi: code review, security audit, feature development, frontend design, MCP tools, Hugging Face ML/training workflows, and more; explicitly positioned as **complementary to Superpowers** ("It complements obra/superpowers, which provides process skills such as brainstorming, TDD, debugging, and plan execution") rather than a competing discipline framework — ships immutable provenance tracking for every upstream-adapted skill, registers feature-development specialist roles as least-privilege, read-only OpenCode subagents, and lets Codex run the same phase assignments via its own native subagent workflow — OpenCode support: **Native** (adapted specifically for OpenCode as one of three named target harnesses, with OpenCode-specific subagent registration, not a blind cross-post).

### science-superpowers
- **Category**: 18: Discipline/Skill Packs (Superpowers/ponytail-style)
- **URL**: https://github.com/K-Dense-AI/science-superpowers
- **How it works**: a domain reimplementation of Superpowers for computational science rather than software engineering: same auto-triggering-skill architecture, but the central discipline is **pre-registration** (turning a fuzzy research interest into a precise, falsifiable question before running any code) instead of TDD — includes `framing-research-questions` and `surveying-prior-work` skills — OpenCode support: **Claimed but unverified** (the repo's own install docs explicitly detail Pi and Antigravity installation paths in depth, but do not clearly confirm a dedicated OpenCode install path in the material surfaced by this search — flagged rather than assumed; worth a direct repo check before relying on it for OpenCode specifically).

### Context7
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://github.com/upstash/context7
- **How it works**: 39.3k+ stars (see Element 6) — the originator of this category: indexes community-contributed library documentation, served via MCP; triggered with "use context7" or an explicit library slash-ID (`/supabase/supabase`) in the prompt to skip library-matching — OpenCode support: **Works via open standard** (plain MCP server; add the hosted endpoint `https://mcp.context7.com/mcp` with an `Authorization: Bearer` API key, or self-host, under OpenCode's `mcp` config like any other server).

### docs-mcp-server
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://github.com/arabold/docs-mcp-server
- **How it works**: explicitly positioned as an "Open-Source Alternative to Context7, Nia, and Ref.Tools" — builds a personal, always-current documentation index by fetching official docs from websites, GitHub, npm, PyPI, and local files; auto-probes for `llms.txt` at doc subpaths/site roots and prefers Markdown-native responses (via `Accept: text/markdown` content negotiation, including Cloudflare's Markdown-for-Agents support) over scraping HTML — OpenCode support: **Works via open standard** (long-running MCP endpoint, documented for Claude/Cline/Copilot/Gemini CLI/"other MCP clients" generically — OpenCode consumes it the same way any MCP client does).

### DeepWiki
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://deepwiki.com
- **How it works**: (by Cognition/Devin team) — different shape than pure docs lookup: turns any public GitHub repo into an AI-enhanced wiki with automated documentation, architecture diagrams, and interactive Q&A; exposes three MCP tools querying any public repo's auto-generated wiki on the fly — free for public repos — OpenCode support: **Works via open standard** (plain MCP server; useful specifically for "how does this codebase work internally" rather than "what's the current API surface," complementing rather than replacing Context7-style tools).

### Docfork
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://github.com/topics/mcp-server
- **How it works**: (per multiple comparison roundups) — MIT-licensed, open-source; claims 9,000+ libraries covered out of the box with automatic detection/download of docs, and a `dgrep init` flow that reads your `package.json` once and scopes documentation search to your actual dependencies ("Cabinets" for versioning) — OpenCode support: **Works via open standard** (plain MCP server per every comparison source found; widest claimed library coverage of the alternatives surveyed).

### Ref Tools
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://ref.tools
- **How it works**: closed-API, paid after a 200-credit free tier (~10 weeks average usage); differentiator is aggressive token efficiency — caps responses around 5K tokens using session-history awareness to stay lean under context pressure — OpenCode support: **Works via open standard** (MCP server; worth choosing specifically if context-window budget is the binding constraint, per its comparison-roundup positioning).

### Rtfmbro
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://mcp.directory/collections/top-alternatives-to-context7-mcp
- **How it works**: fetches version-aware documentation "just in time" directly from a package's GitHub repo, rather than Context7's pre-scan/index approach — OpenCode support: **Works via open standard** (plain MCP server per comparison sources).

### GitMCP
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://gitmcp.io
- **How it works**: and **[grep.app-backed "Grep" MCP](https://mcp.directory/collections/top-alternatives-to-context7-mcp)** — GitMCP provides direct GitHub API access to code/docs for any project; Grep searches across millions of GitHub repos via the grep.app API with language/repo/path filtering — OpenCode support: **Works via open standard** for both.

### Nia
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://trynia.ai
- **How it works**: Y Combinator-backed (raised $6.2M), indexes docs and codebases together, claims a 27% coding-agent performance improvement via "intelligent indexing and context sharing" (self-reported, not independently verified in this sweep) — OpenCode support: **Works via open standard**.

### Deepcon
- **Category**: 19: Docs-Context MCP Servers (Context7-style)
- **URL**: https://mcp.directory/blog/top-context7-mcp-alternatives
- **How it works**: differentiates on accuracy: cites a self-reported 90% score on a contextual benchmark vs. 65% for Context7 and 0% for unaugmented Claude Sonnet 4.5 (self-reported benchmark, not independently verified) — OpenCode support: **Works via open standard**.

### ocstatusline
- **Category**: 20: Statusline Tools
- **URL**: https://github.com/amirlehmam/ocstatusline
- **How it works**: explicitly "the OpenCode counterpart of ccstatusline" (the popular Claude Code statusline tool) — since OpenCode has no status-line hook, external-command slot, or pluggable built-in bar, this tool **inverts the model**: runs as a separate live daemon (`ocstatusline start`) that repaints instantly as your session produces tokens, switches model, or changes cost, meant to run alongside OpenCode in a separate pane/split rather than being injected into OpenCode's own TUI — reuses ~70% of ccstatusline's widget engine/Powerline/color/flex-width/config-TUI concepts; rich widget set: model, provider, agent/mode, token totals, cost, context length/%, context bar, session timer, git branch/dirty/ahead-behind/changes/SHA, working dir, custom text — OpenCode support: **Native** (purpose-built specifically as OpenCode's counterpart to an existing Claude Code tool; not itself an OpenCode plugin, but a companion process designed around OpenCode's actual architecture and limitations — the README states this workaround exists precisely *because* "OpenCode has no equivalent" to Claude Code's statusLine hook).

### opencode-status-line (markwilkening21)
- **Category**: 20: Statusline Tools
- **URL**: https://github.com/markwilkening21/opencode-status-line
- **How it works**: "inspired by cc-status-line" — a lightweight, fast standalone binary that connects to OpenCode's HTTP server (`--url`, required — "OpenCode does not expose an HTTP server by default, you need to start OpenCode with an explicit port"), themeable (built-in themes like Catppuccin or custom theme files), terminal-multiplexer-aware (tmux, zellij, wezterm), configurable refresh interval, PR status display (toggleable) — designed to run in a split pane (tmux/wezterm binding examples provided) — OpenCode support: **Native** (connects directly to OpenCode's own server API, purpose-built for OpenCode specifically, not adapted from elsewhere).

### opencode-status-bar (aacassandra)
- **Category**: 20: Statusline Tools
- **URL**: https://github.com/aacassandra/opencode-status-bar
- **How it works**: a different form factor: a tiny **macOS menu bar app** (not a terminal pane) showing OpenCode's live status at a glance — "no windows, no dock icon, no analytics, just a pixel in your menu bar"; supports multiple concurrent OpenCode sessions with priority surfacing (a session awaiting permission jumps above one that's just thinking); architecture is stateless/event-driven: an OpenCode plugin (`plugin/statusbar.ts`) writes JSON state files on lifecycle events, and a separate Swift app polls and renders them (0.4s interval) — OpenCode support: **Native** (the plugin half is a real OpenCode plugin using OpenCode's lifecycle events; the Swift app is a companion renderer, together forming a complete native-to-OpenCode pipeline).

### opencode-worktree
- **Category**: 21: Git-Worktree Helpers
- **URL**: https://skillsllm.com/skill/opencode-worktree
- **How it works**: the most OpenCode-specific entry found: an OpenCode plugin that creates isolated git worktrees where **each worktree automatically opens its own terminal with OpenCode already running inside it** — exposes `worktree_create` (auto-spawns terminal, starts OpenCode, syncs files) and `worktree_delete` (auto-commits changes, cleans up the worktree) as agent-callable tools/lifecycle hooks; explicitly notes it works in OpenCode Desktop too, but loses automatic terminal-spawning there (GUI-locked); pairs with a separate tool called "cmux" for agentic workflows — OpenCode support: **Native** (purpose-built OpenCode plugin, not adapted from another tool; the standout entry specifically because it automates the full create→terminal→launch→sync→teardown lifecycle rather than just worktree creation).

### git-worktree-runner (CodeRabbit)
- **Category**: 21: Git-Worktree Helpers
- **URL**: https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents
- **How it works**: cross-tool CLI (`git gtr new my-feature --ai`) explicitly supporting Claude, Cursor, **Opencode**, Copilot, and Gemini — OpenCode support: **Documented port/adapter** (OpenCode explicitly named among supported agents in the tool's own command surface, per the independent Upsun technical writeup).

### agentree
- **Category**: 21: Git-Worktree Helpers
- **URL**: https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents
- **How it works**: quick worktree creation for AI workflows generally (`agentree -b fix-auth`) — agent-agnostic rather than OpenCode-specific; no explicit per-agent adapter confirmed, but nothing in its design prevents `cd`-ing into the created worktree and launching OpenCode manually — OpenCode support: **Claimed but unverified** (works via the general git-worktree pattern any CLI agent benefits from, but no OpenCode-specific integration point or documentation confirming special OpenCode awareness was found — flagged rather than assumed equivalent to git-worktree-runner's explicit support).

### worktree-cli
- **Category**: 21: Git-Worktree Helpers
- **URL**: https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents
- **How it works**: targets AI workflows with MCP server integration, automatic setup hooks, and `.env` file copying, but per the source writeup is described as MCP-integrated **specifically for Claude Code** — OpenCode support: **Claimed but unverified** (no explicit OpenCode adapter found; MCP integration described is Claude-Code-specific per the source, so treat OpenCode compatibility as unconfirmed rather than assumed via the general MCP-openness argument used elsewhere in this sweep, since the *setup hooks* themselves may be Claude-Code-specific rather than protocol-level).

### gwq
- **Category**: 21: Git-Worktree Helpers
- **URL**: https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents
- **How it works**: status-dashboard tool showing all active worktrees across repositories, with tmux integration for managing long-running agent processes — agent-agnostic (works with whatever CLI agent you point it at, OpenCode included, since it operates at the worktree/tmux layer rather than the agent layer) — OpenCode support: **Works via open standard** in the loose sense of "operates below the agent layer" — not a protocol-based claim like MCP, but genuinely agent-agnostic by design rather than requiring per-agent adapters.

### jqueryscript/awesome-claude-code
- **Category**: 22: Awesome-Lists (AI Coding Agents, Cross-Tool)
- **URL**: https://github.com/jqueryscript/awesome-claude-code
- **How it works**: a Claude-Code-centric list, but many individual cataloged entries explicitly support/target OpenCode alongside Claude Code (e.g., claude-replay 720★ converts sessions from "Claude Code, Cursor, Codex, Gemini, OpenCode"; agentsys 878★ is an "automation toolkit... for Claude Code, OpenCode, Codex, Cursor, and Kiro"; medusa 643★ is a cross-agent security scanner) — OpenCode support: **Mixed per-entry** (the list itself is Claude-Code-branded, but functions as a de facto cross-tool discovery list since a meaningful fraction of entries explicitly support OpenCode — treat as "Documented port/adapter" for the specific entries that name OpenCode, not for the list as a whole).

### hashgraph-online/awesome-ai-plugins
- **Category**: 22: Awesome-Lists (AI Coding Agents, Cross-Tool)
- **URL**: https://github.com/hashgraph-online/awesome-ai-plugins
- **How it works**: explicitly framed as "for AI assistants including Claude Code, OpenAI Codex, Gemini, OpenCode and More" in its own title/description — genuinely cross-tool by design, not just by incidental entry overlap; catalogs plugins like Workflow Kit ("for Claude Code, Codex CLI, and OpenCode") and Claude Octopus (dispatches to 8 providers including OpenCode) — OpenCode support: **Works via open standard / documented per-entry** (the list's own framing includes OpenCode as a first-class target, not an afterthought).

### gmh5225/awesome-skills
- **Category**: 22: Awesome-Lists (AI Coding Agents, Cross-Tool)
- **URL**: https://github.com/gmh5225/awesome-skills
- **How it works**: cross-tool skills/resources list "for AI coding agents like Claude Code, Codex, Gemini CLI, GitHub Copilot, and more" — catalogs OpenCode-inclusive tools like skillreaper (session-transcript analysis for "Claude Code, Codex, Hermes, OpenCode, Cursor, and OpenClaw") and Skills宝 (a marketplace explicitly "across Claude Code, OpenCode, and more platforms") — OpenCode support: **Documented per-entry** (genuinely multi-harness list with OpenCode represented, though not as prominently as Claude Code).

### bradAGI/awesome-cli-coding-agents
- **Category**: 22: Awesome-Lists (AI Coding Agents, Cross-Tool)
- **URL**: https://github.com/bradAGI/awesome-cli-coding-agents
- **How it works**: explicitly scoped as "terminal-native AI coding agents and the harnesses that orchestrate them," listing OpenCode by name as one of the covered open-source tools alongside Pi, Aider, and Goose, plus platform agents (Claude Code, Codex, Gemini CLI); catalogs OpenCode-inclusive orchestration tools like Garcon (steers parallel sessions across "Claude Code, Codex, Cursor Agent, OpenCode, Amp, Droid, and Pi") and Agent AFK — OpenCode support: **Works via open standard / documented per-entry** (OpenCode named directly in the list's own scope description, not just in individual entries).

### RoggeOhta/awesome-codex-cli
- **Category**: 22: Awesome-Lists (AI Coding Agents, Cross-Tool)
- **URL**: https://github.com/RoggeOhta/awesome-codex-cli
- **How it works**: Codex-CLI-centric (150+ tools primarily for OpenAI Codex), but a meaningful minority of entries explicitly include OpenCode as a supported target — e.g., sync-agents-settings ("Sync MCP server configs from Claude Code to Gemini CLI, Codex CLI, OpenCode, Kiro, Cursor"), mco-org/mco ("Neutral orchestration layer for Claude Code, Codex CLI, Gemini CLI, OpenCode, Qwen Code") — OpenCode support: **Mixed per-entry** (same pattern as the Claude-Code-centric list above: the list itself isn't OpenCode-focused, but usefully surfaces OpenCode-compatible cross-tool entries you might otherwise miss by only searching OpenCode-specific lists).

### MEDUSA
- **Category**: 23: Security Scanners for Agent Configs
- **URL**: https://github.com/Pantheon-Security/medusa
- **How it works**: AI-first security scanner with 40,000+ detection patterns (star counts vary by mirror/fork found: 643★ per one listing, a separate fork "medusa1" cites 74+ analyzers/180+ AI-agent rules) — zero-setup, works out of the box; `medusa scan --git <URL>` vets any repo for AI supply-chain attacks (repo poisoning, prompt injection, MCP tool poisoning) before you clone; `medusa secrets scan` finds leaked API keys across "Claude / Cursor / Copilot / shell history" with 21 issuer types and interactive in-place redaction; v2026.7 added "Claude Code compromise detection" that explicitly vets **`.claude/` directory hooks, permissions, and skills** for injected instructions and backdoors — OpenCode support: **Claimed but unverified** (the specific "compromise detection" feature is documented as targeting the `.claude/` directory by name; no equivalent `.opencode/` directory scanning was confirmed in the material surfaced by this search, despite MEDUSA's broader scanning — general code/secrets/CVE scanning likely applies to any codebase including OpenCode projects, but the specific agent-config-directory vetting feature that makes this element distinct does not have confirmed OpenCode-directory coverage — flag for direct verification before relying on this specifically for `.opencode/` vetting).

### secure-skills (alonw0)
- **Category**: 23: Security Scanners for Agent Configs
- **URL**: https://github.com/alonw0/secure-skills
- **How it works**: "The SECURE open agent skills tool," a fork/variant published as `npx skillsio` — explicitly states "Supports OpenCode, Claude Code, Codex, Cursor, and 37 more" in its own description; runs an automated local security scan **before** any skill install (`skillsio add` triggers the scan automatically) rather than after-the-fact; applies ~81 regex rules plus a correlation engine derived directly from the Snyk ToxicSkills and Koi ClawHavoc research, organized into 8 threat categories — OpenCode support: **Native** (OpenCode explicitly named first in its own supported-agents list, and the tool operates at the skill-installation layer generically rather than being tied to any one agent's specific config-directory format — this is the standout entry specifically because OpenCode support is stated outright, not inferred).

### CC Safety Net (kenryu42/cc-safety-net)
- **Category**: 24: Safety-Net / Guardrail Tools
- **URL**: https://github.com/kenryu42/cc-safety-net
- **How it works**: the most comprehensive entry found: a coding-agent CLI hook catching destructive git/filesystem commands and secret-file access **before** they execute, working by *intent* rather than string-pattern matching — explicitly distinguishes `git checkout -b feature` (safe, allowed) from `git checkout -- file` (destructive, blocked); also catches `rm -rf` on destructive targets, `git reset --hard`, `git push --force`, `git stash clear`, `git clean -f`, `find -delete`, and `dd`/`mkfs`/`shred`; cross-platform (Windows/macOS/Linux) with OS-aware path/command handling — supports **ten** coding-agent CLIs: Claude Code, Codex, Gemini CLI, Copilot CLI, Antigravity CLI, Kimi Code, **OpenCode**, Pi, Cursor, and Amp Code — OpenCode support: **Native** (installs via `opencode plugin -g -f cc-safety-net@latest`, i.e. OpenCode's own native plugin command; the README documents a known OpenCode-specific caching quirk — stale cached plugin versions, tracked at [anomalyco/opencode#25293](https://github.com/anomalyco/opencode/issues/25293) — with a documented workaround of clearing `~/.cache/opencode/packages/`). Explicitly recommended as **defense-in-depth alongside sandboxing** (Element 7), not a replacement: "Sandboxing contains blast radius... Safety Net prevents footguns... catches git-specific mistakes that are technically 'safe' from the sandbox's perspective."

### Destructive Command Guard (dcg) — OpenCode integration
- **Category**: 24: Safety-Net / Guardrail Tools
- **URL**: https://gist.github.com/AlexMikhalev/bc7cc0f237bdb2a6fade347aba203acb
- **How it works**: a documented integration pattern (published as a gist/blog post, not a standalone repo) showing how to wire the `dcg` tool into OpenCode using its native `tool.execute.before`/`tool.execute.after` plugin hooks (available since OpenCode v1.4+) — intercepts commands before they run, catching the same class of AI-agent mistakes (a mistyped `rm -rf ./src`, an accidental `git reset --hard`, an unintended `git push --force`) — OpenCode support: **Native** (built directly against OpenCode's documented plugin `Hooks` interface; this is an integration guide rather than a packaged plugin, so implementation requires following the gist rather than a one-line install).

### OpenGuardrails
- **Category**: 24: Safety-Net / Guardrail Tools
- **URL**: https://openguardrails.com/
- **How it works**: "the open standard & benchmark for AI agent safety & security" — a broader policy-based approach rather than a fixed destructive-command blocklist: the agent fetches and reads a skill (`openguardrails.com/skill/SKILL.md`), drafts a policy describing what it may/may not do, the operator approves it, and OGR then enforces that policy on every subsequent action including the agent's own — explicitly invocable by pasting an install prompt into "Claude Code, Codex, **opencode**, OpenClaw…" — OpenCode support: **Works via open standard** (delivered as a skill/instructions file the agent reads and self-applies, rather than a hook-based plugin — a fundamentally different, more agent-agnostic mechanism than CC Safety Net's hook interception, and explicitly OpenCode-inclusive in its own onboarding instructions).

### hook-manager (bopen-tools)
- **Category**: 25: Hook Management CLIs
- **URL**: https://www.claudepluginhub.com/skills/b-open-io-bopen-tools-2/hook-manager
- **How it works**: the clearest fit found: "Discovers and installs automation hooks for Claude Code and Opencode, including security hooks, git reminders, and linting triggers"; manages hooks via natural-language commands — add, list, remove, update, validate — for lifecycle events like `PreToolUse`, `SessionStart`, `UserPromptSubmit`; ships a curated hook catalog (e.g., `protect-env-files` — blocks Write/Edit on `.env*` files, recommended universally as a zero-downside security safeguard; `auto-git-add`; `uncommitted-reminder`; `lint-on-save`/`lint-on-start`) — explicitly documents parallel install paths for both agents (`ls ~/.claude/hooks/` vs. `ls ~/.opencode/hooks/`), and its own instructions literally say "restart Claude Code (or Opencode) for the hook to take effect" — OpenCode support: **Native** (built with explicit, symmetric dual-agent support, not a Claude-Code tool with an incidental OpenCode mention — this is a skill/tool delivered via the bopen-tools collection specifically designed to manage hooks across both harnesses).

### EvoSkill
- **Category**: 26: Self-Improving / Instinct-Mining Tools
- **URL**: https://github.com/sentient-agi/EvoSkill
- **How it works**: the most substantial, research-backed entry found: an open-source framework that automatically discovers and synthesizes reusable agent skills from **failed trajectories** to improve coding-agent performance; explicitly extends the feedback-driven idea from GEPA (a single-file prompt-optimization technique) to full agent evolution — proposes multiple skill *and* prompt mutations jointly, evaluates new variants against held-out data, and produces an entirely new agent program each iteration rather than revising one prompt in place; includes "Harbor," a containerized-benchmark component for evaluation — compatible with Claude Code, Codex CLI, **OpenCode**, OpenHands, Goose, and more; model-agnostic (OpenRouter, Anthropic, OpenAI, Fireworks, and others) — OpenCode support: **Native** (the installer explicitly offers `--agents claude,opencode`-style harness selection, `brew install opencode` is listed as a first-class supported install path alongside Claude Code/Codex/Goose, and its own config format shows `name = "opencode"` as a valid `[harness]` value alongside `openhands` — this is a confirmed, first-class, non-incidental integration, not a generic "should work" claim).

### self-learning-skills (Kulaxyz)
- **Category**: 26: Self-Improving / Instinct-Mining Tools
- **URL**: https://github.com/Kulaxyz/self-learning-skills
- **How it works**: a lighter-weight, more targeted tool: "recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time" — distributed via the community "skills CLI" (`npx skills add kulaxyz/self-learning-skills`), which **auto-detects installed agents** and installs accordingly, explicitly naming "Claude Code, Cursor, Codex, Cline, **OpenCode**, and more" as detectable targets; also installable via a Claude-Code-style plugin marketplace command as an alternative path — OpenCode support: **Native** (OpenCode explicitly named among the CLI's auto-detected target agents, not merely implied by "and more").

### self-improving-agent (leohuang8688)
- **Category**: 26: Self-Improving / Instinct-Mining Tools
- **URL**: https://github.com/leohuang8688/self-improving-agent
- **How it works**: a more full-featured learning system, but built specifically as an **OpenClaw skill** (a different agent, not OpenCode) — features error learning (learns from mistakes to avoid repetition), recovery learning (learns successful recovery patterns), session learning, performance-metrics learning, and an extensible hook system with a Python CLI (`learn-errors`, `learn-recoveries`, export-to-markdown) — genuinely feature-rich, but its install path is `~/.openclaw/workspace/skills`, an OpenClaw-specific directory — OpenCode support: **Claimed but unverified** (no OpenCode-specific install path, config, or documentation confirming OpenCode compatibility was found; flagged rather than assumed compatible despite the generically-named repo — this may be portable in principle given it's Python-CLI-based rather than deeply OpenClaw-hook-dependent, but that portability is not demonstrated in the material found).


</CATALOG_DATA>
3. For each candidate, perform a lightweight check:
   - Does the repository exist?
   - Is it maintained?
   - Does it contain a valid SKILL.md?
4. Generate an `INDEX.md` inside the library folder documenting the PASS/FAIL status of each candidate. Do NOT mask errors. If a tool fails the check, mark it FAIL and list the reason.

### PART 5B — The Promotion Command

Create a new slash command `promote-skill.md` in your tool's command directory (as discovered in Part 1A):

--- FILE CONTENT ---
---
description: Promote a skill from the inert library to the active skills folder.
---

Promote skill: $ARGUMENTS

1. AUDIT BEFORE COPY: Fetch and read the skill's code/prompts. Write a structure audit to the chat.
2. COLLISION CHECK: Check the active skills folder for any existing skill with a similar name OR overlapping description/purpose. 
3. HUMAN APPROVAL: Stop and present the audit and collision check to the user. Request explicit approval to promote.
4. If approved, MOVE (do not copy) the skill folder from the library to the active skills folder. Update INDEX.md to reflect the promotion.


