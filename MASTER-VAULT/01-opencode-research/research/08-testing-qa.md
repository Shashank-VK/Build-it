# Phase 8 — Task 1: Testing/QA Automation for OpenCode

**Fetch date:** 2026-08-11
**Source URLs fetched directly:**
- github.com/michaljach/opencode-browser (README.md raw)
- github.com/microsoft/playwright-mcp (README.md raw)
- Playwright docs / QA agent pattern (web search + multiple sources)
**Verdict:** See recommendation section.

---

## Tool 1: michaljach/opencode-browser

### Status
- **GitHub page title (live fetch):** "GitHub - michaljach/opencode-browser: Browser automation plugin for
  OpenCode AI editor - Control Chrome/Edge with AI, automate web testing, scraping & form filling via
  MCP integration"
- **Status:** LIVE, maintained. README is current and detailed.
- **Star count:** Not visible from raw README; GitHub HTML confirmed page exists and is public.

### What it actually is
Not a standalone browser — it''s an OpenCode **plugin** wrapper around **browsermcp.io** (Browser MCP),
a third-party browser automation MCP server. The plugin adds:
- Speed-oriented browser guidance injected into the model prompt
- Tool-specific performance hints for expensive browser actions
- Fast retry behavior with no reconnect backoff
- Context preservation for browser state across session compactions

browsermcp.io provides the actual browser control (Chrome/Edge). The plugin tells OpenCode how to use it well.

### Exact Install Steps (from live README)

**Fastest path (creates/updates opencode.json automatically):**
```bash
npx opencode-browser init
```
For global (all projects):
```bash
npx opencode-browser init --global
```
Preview without writing:
```bash
npx opencode-browser init --print
```

**Prerequisites:**
1. Node.js installed
2. OpenCode installed and configured
3. Browser MCP Chrome/Edge extension installed from https://browsermcp.io/install

**Manual opencode.json (if not using init command):**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-browser"],
  "mcp": {
    "browsermcp": {
      "type": "local",
      "command": ["npx", "-y", "@browsermcp/mcp@0.1.3"],
      "enabled": true
    }
  }
}
```
Note: Version is pinned to 0.1.3 in the README — do not substitute @latest without checking.

**Advanced config (disable globally, enable per-agent):**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "browsermcp": {
      "type": "local",
      "command": ["npx", "-y", "@browsermcp/mcp@0.1.3"],
      "enabled": true
    }
  },
  "tools": { "browsermcp_*": false },
  "agent": {
    "browser-agent": {
      "tools": { "browsermcp_*": true }
    }
  }
}
```

### DoD Integration for a Frontend Project
The browsermcp toolset gives the agent direct browser control — navigate, click, fill forms, scrape.
For DoD §4 "Manual Verification Step":
- Agent can run a smoke test autonomously: open the app URL, navigate to key pages, check for JS errors.
- Cannot replace a real Playwright test suite — browsermcp is interactive/ad-hoc, not assertion-based.
- Best use: quick end-to-end sanity check within an OpenCode session as a DoD gate, NOT as the
  primary testing infrastructure.
- Limitation: requires the Chrome/Edge browser extension to be running — will NOT work headlessly
  or in CI. Sessions are interactive only.

---

## Tool 2: Playwright Test Agents (Planner/Generator/Healer)

### Status (from multiple web sources + playwright.dev citations)
- **Source:** Official Playwright framework (microsoft/playwright-mcp is the MCP bridge)
- **Status:** LIVE. Playwright AI agents (v1.56+) are confirmed real per multiple independent sources.
- **Init command confirmed:** `npx playwright init-agents --loop=opencode`
  (places agent definitions in .opencode/agents/)
- **MCP server:** microsoft/playwright-mcp — official Microsoft repository, actively maintained

### What it actually is
Three built-in Playwright agents (post-v1.56):
- **Planner:** Explores app, generates structured Markdown test plan
- **Generator:** Converts test plan into executable Playwright test files
- **Healer:** Diagnoses failing tests (selector issues, strict mode violations), proposes fix, reruns

These are Playwright-native — they live in .opencode/agents/ after init. They are distinct from
browsermcp: they generate and maintain real assertion-based .spec.ts test files, not just
interactive browser sessions.

### Exact OpenCode MCP Config (from microsoft/playwright-mcp README, direct fetch)
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": ["npx", "@playwright/mcp@latest"],
      "enabled": true
    }
  }
}
```
Note: The playwright-mcp README has an explicit "opencode" section (lines 332-350) confirming
this exact format. The command does not use -y flag (unlike browsermcp).

### Important Caveat from playwright-mcp README
The README explicitly recommends CLI+SKILLS over MCP for coding agents:
> "Modern coding agents increasingly favor CLI-based workflows exposed as SKILLs over MCP because
> CLI invocations are more token-efficient: they avoid loading large tool schemas and verbose
> accessibility trees into the model context."
> MCP is recommended for "exploratory automation, self-healing tests, or long-running autonomous
> workflows where maintaining continuous browser context outweighs token cost concerns."

For the healer workflow (self-healing tests), MCP is the right choice. For triggering test runs
as DoD verification (just run npm test / npx playwright test), MCP is overkill — just use bash.

### DoD Integration for a Frontend Project
The Playwright agent system IS the right tool for §4 if the project has a real frontend:
1. Planner generates test plan from PRD / seed test — human reviews
2. Generator produces .spec.ts files — saved to repo
3. On each DoD gate: run `npx playwright test` via init.sh''s VERIFY_CMD
4. Healer activates when tests fail — agent repairs broken selectors without manual intervention
5. Evidence captured: test output → recorded in feature_list.json evidence[]

This maps directly to the DoD flow. The test files are durable repo artifacts (not chat-only),
exactly as walkinglabs'' AGENTS.md requires.

---

## Other OpenCode Testing/QA Tools Surfaced

### mdc-git/opencode-playwright-interactive
A persistent, interactive browser and Electron QA environment for OpenCode, powered by a
JavaScript REPL and Playwright. Useful for projects targeting Electron apps. Not broadly
applicable; niche.

### upex-galaxy/agentic-qa-boilerplate
Multi-agent QA boilerplate for OpenCode. Full QA lifecycle (planning, testing, regression).
Not a single plugin — a project template. Worth bookmarking for a QA-heavy project.

### fugazi/test-automation-skills-agents
Tool-agnostic QA skill set for coding agents. Can be embedded in OpenCode via SKILL.md.
Lighter-weight than the Playwright agent suite; not as structured.

### remorses/opencode-injection-guard (already in catalog)
Not a testing tool, but relevant to QA: provides real-time prompt injection detection,
which is a form of adversarial testing against the agent itself.

---

## Recommendation

**For a project with a real frontend — use both, for different purposes:**

| Tool | Purpose | When |
|---|---|---|
| Playwright agents (Planner/Generator/Healer) | Primary test suite infrastructure — generates .spec.ts files, self-heals | First-time test creation + ongoing maintenance |
| browsermcp (opencode-browser) | In-session smoke testing — quick DoD gate, visual sanity | During a feature iteration before committing |
| `npx playwright test` via VERIFY_CMD in init.sh | Hard DoD gate — the actual pass/fail signal | Every session end, as a DoD §4 requirement |

Setup order:
1. Install playwright-mcp in opencode.json (MCP server for healer workflow)
2. Run `npx playwright init-agents --loop=opencode` to create agent definitions
3. Create seed.spec.ts (initialization logic for agents to reference)
4. Install opencode-browser for interactive smoke testing
5. Set VERIFY_CMD=npx playwright test in init.sh

DO NOT use browsermcp as a substitute for real tests — it is interactive-only, not
assertion-based, and cannot run in CI. The Playwright test suite is the DoD gate; browsermcp
is the in-session sanity layer.
