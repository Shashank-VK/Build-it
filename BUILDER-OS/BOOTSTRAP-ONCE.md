# SYSTEM 1: ONE-TIME UNIVERSAL HARNESS BOOTSTRAP PROMPT
#
# Paste this prompt ONCE into any AI coding harness (OpenCode, Claude Code,
# Antigravity, Cursor, Codex CLI, Windsurf, Cline).
# After running this once, you never need to paste it again. For all future
# projects, open `BUILDER-OS/` and give your PRD.
#
# ---------------------------------------------------------------------------
# WHAT THIS DOES
#   Step 1  Discover YOUR harness's config paths (never guess them).
#   Step 2  Install the Python verifier toolchain + pre-warm the CLIs.
#   Step 3  Install verified cross-tool skill packs (no caveman).
#   Step 4  Configure the 4 core MCP servers + install safety plugins.
#   Step 5  Author and install the 5 slash commands.
#   Step 6  Verify BUILDER-OS/ and write an honest provisioning receipt.
# ---------------------------------------------------------------------------

You are executing a one-time environment provisioning for this coding harness.

## HARD RULES
1. NEVER install, reference, or enable `JuliusBrussee/caveman` (strictly banned).
2. Do NOT guess your harness's config paths — discover them first in Step 1.
3. Never mask errors or fabricate outputs. Log actual results in
   `BUILDER-OS/.harness/.provisioned`.
4. Every `|| true` below is a *soft* step: if it fails, record the failure
   honestly in the receipt rather than pretending it succeeded.
5. Do NOT modify `MASTER-VAULT/` — it is a read-only archive.

---

## STEP 1: Tool Discovery Protocol (Identify Your Own Harness)

Before installing anything, inspect your environment and report:

1. **Harness Identity**: Which agent/IDE are you running in? (OpenCode,
   Claude Code, Antigravity, Cursor, Codex CLI, etc.)
2. **Skills Discovery Path**: Confirm which of these you read:
   - `~/.agents/skills/` (cross-tool open standard)
   - `~/.config/opencode/skills/` (OpenCode native)
   - `~/.claude/skills/` (Claude native)
   - `./.opencode/skills/` / `./.agents/skills/` (per-project)
3. **Slash Commands Path**: Confirm where custom slash commands live:
   - OpenCode: `~/.config/opencode/commands/` (global) or `.opencode/commands/` (project)
   - Claude Code: `.claude/commands/`
   - Codex CLI: `~/.codex/prompts/`
   - A command is a markdown file with optional frontmatter
     (`description:`, `agent:`, `model:`); the body is the prompt template.
4. **MCP Config File & Schema**:
   - OpenCode: `opencode.json` / `~/.config/opencode/opencode.jsonc` — `"mcp": { "<name>": {...} }`
   - Claude Code / Cursor / Antigravity: `.mcp.json` — `"mcpServers": { "<name>": {...} }`
   - Codex CLI: `config.toml` — `[mcp_servers.<name>]`
   - **MERGE, never overwrite.** If a server of the same name already exists,
     keep the existing entry and report the conflict.
5. **Pre-Tool Hook Support**: Confirm whether you support native pre-tool
   interception (`dod-gate.ts` in OpenCode, `PreToolUse` in
   `.claude/settings.json` in Claude Code). If not, the Git hard pre-commit
   hook in `BUILDER-OS/.git/hooks/pre-commit` is the fallback.

---

## STEP 2: Install Core Python Verifiers & Pre-Warm CLI Tools

```bash
# 1. Python test & lint toolchain (with PEP 668 fallback)
python3 -m pip install -q pytest flake8 ruff bandit pyyaml 2>/dev/null || \
  python3 -m pip install --user --break-system-packages -q pytest flake8 ruff bandit pyyaml || true

# 2. Pre-warm security scanner, loop-engineering CLI, and Meta Astryx UI CLI
npx -y skillsio --version 2>/dev/null || true
npx -y @cobusgreyling/loop --version 2>/dev/null || true
npx -y @astryxdesign/cli --version 2>/dev/null || true
```

---

## STEP 3: Install Verified Cross-Tool Skills (NO CAVEMAN)

The `skills` CLI (v1.7+) installs into the cross-tool `.agents/skills/` path
and auto-detects the running harness. Use `-g` for global (user-level)
installation and `--skill <name>` to install a single skill.

```bash
# Core SDLC, Socratic Planning, TDD, Bounded Loops & Council Review
npx -y skills add Forward-Future/loopy --skill loopy -g || true
npx -y skills add mattpocock/skills -g || true
npx -y skills add addyosmani/agent-skills -g || true
npx -y skills add ngmeyer/skills -g || true

# UI/UX Laws, Anti-Slop Design Taste, Apple Fluid Motion & Copy Polish
npx -y skills add keysjoao/laws-of-ux-skills -g || true
npx -y skills add Leonxlnx/taste-skill -g || true
npx -y skills add emilkowalski/skills -g || true
npx -y skills add hardikpandya/stop-slop -g || true

# Live 30-Day Research & Golden-Path Self-Learning
npx -y skills add mvanhorn/last30days-skill -g || true
npx -y skills add kulaxyz/self-learning-skills -g || true

# Discipline Pack (Layer-1 interactive use only)
npx -y skills add obra/superpowers -g || true
```

> Use `--list` first to preview what a repo contains, and `--copy` instead of
> symlinking if your filesystem does not support symlinks.

---

## STEP 4: Pre-Warm & Configure Universal MCP Servers + Safety Net

### 4a. Cache the stdio MCP server packages

```bash
for pkg in "@modelcontextprotocol/server-filesystem" "@playwright/mcp" "@browsermcp/mcp" "@modelcontextprotocol/server-github" "@upstash/context7-mcp"; do
  ver=$(npm view "$pkg" version 2>/dev/null) && npm cache add "$pkg@$ver" >/dev/null 2>&1 || true
done
```

### 4b. Merge the 4 core MCP servers into your harness's MCP config

Using the file and schema discovered in Step 1:

- **`context7`** — Remote `https://mcp.context7.com/mcp`
  (or local stdio `npx -y @upstash/context7-mcp`)
- **`playwright`** — Local stdio `npx -y @playwright/mcp@latest`
- **`filesystem`** — Local stdio `npx -y @modelcontextprotocol/server-filesystem .`
- **`github`** — Local stdio `npx -y @modelcontextprotocol/server-github`
  (reads `GITHUB_TOKEN` from the environment)

**Merge rules:** preserve every pre-existing server entry (including any
custom `environment` block such as `GHIDRA_INSTALL_DIR` / `JAVA_HOME`).
Only add the 4 above. Never rewrite the file wholesale.

### 4c. Install harness-specific safety plugins

- **OpenCode**: `opencode plugin add cc-safety-net@latest`
  (the `plugin` command takes the package as a positional argument — there is
  no `-g`/`-f` flag)
- **Claude Code / others**: use the vendor's documented plugin installer.

### 4d. Install the 5 slash commands

Author these as markdown files in the commands directory discovered in Step 1.
Each file needs a `description:` in frontmatter; the body is the prompt.

| Command | File | Purpose |
|---|---|---|
| `/idea` | `idea.md` | Capture a raw idea into `feature_list.json` and open the Socratic interview. |
| `/loop-status` | `loop-status.md` | Report current loop state: active feature, step count, spend, quarantine. |
| `/loop-doctor` | `loop-doctor.md` | Diagnose a stuck loop: identical repeated calls, step budget, unresolved blockers. |
| `/pause` | `pause.md` | Safely park the current feature: flush the build log, clear `in_progress`. |
| `/council` | `council.md` | Run the Two-Judge council review via the `two-judge-verification` skill. |

---

## STEP 5: Verify `BUILDER-OS/` & Write `.provisioned` Receipt

1. Run `bash BUILDER-OS/scripts/setup.sh` and `bash BUILDER-OS/scripts/verify.sh`.
   Both must exit `0`. `verify.sh` must leave zero side effects
   (no `__pycache__`, no `.pytest_cache`, no `.ruff_cache`, `guard.log` unchanged).
2. Confirm `BUILDER-OS/AGENTS.md`, `BUILDER-OS/CLAUDE.md`, and
   `BUILDER-OS/.cursorrules` are present and byte-identical.
3. Confirm `MASTER-VAULT/` is untouched (SHA parity against its `MANIFEST.json`).
4. Write the provisioning receipt to `BUILDER-OS/.harness/.provisioned` in
   `key=value` lines. Record **actual** outcomes, including failures:

```
date=<UTC ISO-8601>
harness=<name>
skills_global=<n installed>
skills_failed=<comma-separated list, or none>
mcp_config=<path>
mcp_servers=<comma-separated names>
mcp_failed=<comma-separated list, or none>
plugins=<comma-separated list, or none>
commands=<comma-separated list, or none>
pip=ok|partial
npx_cache=<n>/<n>
playwright=ok|skipped|failed
verify=pass|fail
```

Honesty rule: if a step failed, write the failure. A receipt that claims
success for something that did not install is worse than no receipt.

---

## STEP 6: Final Report

Report to the user:
- Harness identity and the paths you discovered in Step 1.
- A table of every install step: **status, count, and any failure reason**.
- The output of `BUILDER-OS/scripts/verify.sh`.
- Confirmation that `MASTER-VAULT/` was not modified.

When this completes, the environment is provisioned for the lifetime of the
machine. Future sessions only need to `cd BUILDER-OS/` and give a PRD.
