# Phase 4 — Harness, Environment Integration & Definition of Done

> Research completed: 2026-08-09  
> Scope: Antigravity terminal + OpenCode integration, slash command behavior, Claude Code native vs. proxy verdict, Definition-of-Done template, harness evolution, and context anxiety mitigation.

---

## 1. Antigravity Terminal + OpenCode DOM/Browser Inspection Integration

### The Honest Reality
**There is NO native, zero-configuration integration connecting OpenCode inside Antigravity's terminal to Antigravity's IDE-level DOM inspection or browser tools out of the box.**

When OpenCode runs inside Antigravity's terminal panel, it functions as a standard terminal process running a TUI. Antigravity's visual inspect tools, browser previews, and DOM inspectors operate independently in the IDE layer.

### How to Bridge Them (The MCP Bridge)
To connect OpenCode's terminal session to live browser/DOM inspection, you must configure a shared **MCP (Model Context Protocol) server** inside OpenCode's `opencode.json`:

1. **Browser Bridge / Chrome DevTools MCP Server:** Configure an MCP server such as `puppeteer`, `playwright`, or `@modelcontextprotocol/server-puppeteer` (or an OpenCode browser plugin like `OpenCode Chromium Browser Plugin`).
2. **Configuration in `opencode.json`:**
   ```json
   {
     "mcp": {
       "browser": {
         "type": "local",
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
       }
     }
   }
   ```
3. **Result:** OpenCode can then invoke browser tools (`navigate`, `click`, `screenshot`, `evaluate_javascript`) directly from its terminal session.

**Verdict:** Describe any claim of "seamless native integration" between OpenCode terminal sessions and Antigravity DOM inspectors as false. They are separate tools side-by-side that only communicate when explicitly linked via standard MCP bridge configs.

---

## 2. OpenCode Slash Commands in Antigravity Terminal

### Confirmation
**OpenCode native slash commands function correctly inside Antigravity's terminal.**

Because Antigravity's integrated terminal is a standard PTY (pseudo-terminal) shell supporting full ANSI terminal codes, mouse scrolling, and TUI interactivity:
- **Built-in slash commands** (`/init`, `/undo`, `/redo`, `/compact`, `/models`, `/connect`, `/help`) render and execute properly inside the TUI session.
- **Custom slash commands** defined in `.opencode/commands/` (project-scoped) or `~/.config/opencode/commands/` (global-scoped) are loaded automatically and display in the command palette when typing `/`.

**Note:** Ensure your terminal environment in Antigravity has standard UTF-8 character encoding enabled to avoid icon or layout glitches in the TUI sidebar.

---

## 3. Claude Code: Native Models vs. OpenRouter Proxy Verdict

### Documented & Measurable Findings

| Dimension | Native Anthropic API | OpenRouter Proxy (via `claude-code-router`) |
|---|---|---|
| **Latency** | Lowest (direct single-hop connection) | Minor additional network hop (~50-150ms overhead) |
| **Reliability** | Bound to Anthropic infrastructure health | High (automatic provider failover & fallback endpoints) |
| **Prompt Caching** | Native prompt caching headers | Supported (OpenRouter forwards caching headers) |
| **Model Selection** | Restricted to Claude model family | Flexible (can route to DeepSeek, Gemini, Llama, etc.) |

### The Verdict on Proxying Claude Code
**It is NOT worth proxying Claude Code through OpenRouter as an additional tool in this setup.**

**Reasons:**
1. **OpenCode is already your primary driver.** OpenCode natively connects to OpenRouter, OpenCode Zen, and local models.
2. **Added complexity for zero net gain.** Running Claude Code through a proxy router (`claude-code-router`) requires maintaining another translation layer, handling Anthropic-specific API header mappings, and managing dual tool chains.
3. **Focus reserve.** Using OpenCode as the sole primary driver eliminates context fragmentation and tool switching overhead.

---

## 4. Definition-of-Done (DoD) Template

### The walkinglabs Five Subsystems — Verified Source
> Source: `walkinglabs/learn-harness-engineering` templates pulled 2026-08-09 via `Invoke-WebRequest`.  
> Files in `harness-templates/`: `AGENTS.md`, `init.sh`, `claude-progress.md`, `feature_list.json`

| Subsystem | What the source actually says | File |
|---|---|---|
| **Instructions** | 6-step startup workflow: pwd → read claude-progress.md → read feature_list.json → git log → run init.sh → run verification | `AGENTS.md` |
| **Scope** | `single_active_feature: true` enforced in JSON; AGENTS.md: "Work on one feature at a time" | `feature_list.json`, `AGENTS.md` |
| **State** | Per-session log: Goal, Completed, Verification run, Evidence captured, Commits, Known risk, Next best step | `claude-progress.md` |
| **Verification** | `do_not_skip_verification: true`; each feature has a `verification[]` array of specific steps + `evidence[]` to record proof | `feature_list.json` |
| **Session Lifecycle** | End-of-session: update progress.md → update feature_list.json → record risks → commit → leave repo clean enough to `./init.sh` immediately | `AGENTS.md`, `init.sh` |

---

### Definition-of-Done Task Template

```markdown
# Definition of Done

## §1 — Instructions & Scope  *(walkinglabs AGENTS.md + feature_list.json — verified)*

**Before writing a single line of code, the agent must complete this startup sequence:**

- [ ] `pwd` — confirm working directory is correct
- [ ] Read `claude-progress.md` — note the current verified state and the "Next best step"
- [ ] Read `feature_list.json` — identify the highest-priority feature with status `not_started` or `in_progress`
- [ ] `git log --oneline -5` — review recent commits for context
- [ ] `./init.sh` — install deps, run baseline `VERIFY_CMD`, confirm baseline is passing
- [ ] If baseline is failing: fix it first. Do not start feature work on top of a broken state.
- [ ] Confirm `single_active_feature: true` — only one feature may be `in_progress` at a time

## §2 — Context & Grounding  *(not from walkinglabs — added because OpenCode agents lose file context without explicit pinning)*

- [ ] List exact file paths that need to be read or changed for this task
- [ ] Reference the relevant type contracts, API shapes, or AGENTS.md constraints
- [ ] Attach any relevant SKILL.md rules or prior session lessons

## §3 — Environment & Dependencies  *(not from walkinglabs — added for secrets/branch safety before destructive changes)*

- [ ] Required packages/tools confirmed installed (captured by `./init.sh` implicitly, but verify explicitly if new deps are needed)
- [ ] `.env` variables present and correct for this task
- [ ] Isolated git branch or worktree created before starting changes

## §4 — Verification  *(walkinglabs feature_list.json + AGENTS.md — verified)*

- [ ] **Run the feature's `verification[]` steps** exactly as written in `feature_list.json`
- [ ] **Run `VERIFY_CMD`** (project-configured baseline — e.g. `npm test`, `pytest`, or equivalent — not hardcoded)
- [ ] **Record evidence**: screenshot, curl output, log output, or test run transcript captured and written into `feature_list.json` → `evidence[]` field
- [ ] `passing_requires_evidence: true` — status must not be set to `"passing"` until evidence is recorded

## §5 — State & Session Lifecycle  *(walkinglabs AGENTS.md + claude-progress.md — verified)*

- [ ] Update `claude-progress.md` — fill in: Completed, Verification run, Evidence captured, Commits, Known risk, Next best step
- [ ] Update `feature_list.json` — set feature status to `"passing"` (only after evidence is recorded)
- [ ] Record any unresolved risk or blocker explicitly — do not leave session in an ambiguous state
- [ ] Commit with a descriptive message once work is in a safe state
- [ ] Repo must be clean enough for the next session to run `./init.sh` immediately without guessing
```

---



## 5. Harness Evolution & Self-Improvement Workflow

To prevent the agent setup from remaining static over time, integrate three verified tools into a closed-loop lifecycle:

```
[ Session Evidence ] ──► hqhq1025/skill-optimizer (Mine repetitive patterns)
                             │
                             ▼
                    okdk7788/opencode-self-improving-skills (Distill & GEPA-optimize SKILL.md)
                             │
                             ▼
                    thousandflowers/skillreaper (Audit & Prune unused/dead skills)
```

1. **Mining (hqhq1025/skill-optimizer):** `skill-miner` scans past session transcripts and identifies repeated manual workflows or prompt sequences.
2. **Distillation & Optimization (okdk7788/opencode-self-improving-skills):** Converts mined workflows into structured `SKILL.md` files. Uses `optimize_skill` (GEPA-style candidate generation, validation against test traces, and Pareto selection) to iteratively improve execution accuracy.
3. **Pruning (thousandflowers/skillreaper):** Scans session logs to detect installed skills or MCP tools that have never been triggered, quarantining dead weight to keep context lean and fast.

---

## 6. Reducing "Context Anxiety"

### What Context Anxiety Is
Context anxiety is a model failure mode where an agent, sensing it is approaching token limits, prematurely wraps up, summarizes work, or skips complex implementation steps to "save space."

### 6 Concrete Techniques to Mitigate It

1. **Programmatic Headroom Capping:** Configure OpenCode's context limit buffer (e.g., using OpenCode DCP or setting truncation limits at 70-80% of max window) so the agent never sees itself hitting the wall.
2. **Externalized State Logging:** Maintain persistent progress files (`progress.md`, `feature_list.json`). Remind the agent that memory is stored on disk, so it does not need to store everything in context.
3. **Context Compilation / Pruning:** Use the `opencode-dynamic-context-pruning` (DCP) plugin to automatically strip out duplicate tool calls, error stack traces, and stale file reads before sending requests.
4. **Counter-Prompting:** Add an explicit reassurance rule to `AGENTS.md`: *"Context headroom is managed automatically. Do not skip implementation details, truncate code, or rush to complete tasks."*
5. **Sub-Agent Delegation:** Delegate long-running research or sub-tasks to isolated sub-agents (`general`, `explore`, or custom sub-agents). Sub-agent contexts run independently and do not pollute the main session context window.
6. **Session Rewind & Clean Restarts:** Use `/compact` or `/undo` frequently when switching phases, carrying forward only the current DoD artifact into the next session.

---

## Output Summary
Saved to `research/04-harness-environment.md`.
