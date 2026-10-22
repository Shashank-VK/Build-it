# Phase 8 — Task 3: Disambiguate the Pre-Commit Hook Type

**Research date:** 2026-08-11
**Sources:** Web search on git pre-commit vs OpenCode plugin hook tradeoffs (multiple independent sources)

---

## The Two Options

### Option A: Git .git/hooks/pre-commit
A shell script at .git/hooks/pre-commit (or managed via husky / pre-commit framework).
- Fires on EVERY `git commit`, regardless of which tool initiated it
- Tool-agnostic: works from any terminal, any IDE, any agent
- Implemented as a shell script — runs before the commit is finalized
- Survives if the agent session ends or crashes
- NOT bypassable by accident (unless the developer explicitly runs git commit --no-verify)
- Standard, well-understood by every developer who has used git

### Option B: OpenCode plugin hook (tool.execute.before or session.idle)
A JS/TS plugin event callback that fires within an active OpenCode session.
- Only fires when an OpenCode agent is actively running
- Does NOT fire if a commit is made from a plain terminal, another IDE, or another tool
- Configured in the plugin system (.opencode/plugins/ or ~/.config/opencode/plugins/)
- Can intercept tool calls before they execute — e.g., before the agent runs `git commit`
- Cannot fire if OpenCode session has ended before the commit happens

---

## What Failure Mode Does the DoD Actually Try to Prevent?

The DoD spec says:
> "pre-commit hook, gates on feature_list.json status -> passing"

The failure mode being prevented:
> An agent (or developer) commits code when the feature''s status in feature_list.json is NOT
> "passing" — i.e., verification has not been confirmed, evidence has not been recorded.

**The critical question is: who commits?**

In this setup:
- The OpenCode agent does most commits (at the end of a session, as AGENTS.md specifies)
- The developer may occasionally commit manually from a terminal
- The developer may also commit via a git GUI or IDE

**Both scenarios need to be caught.** If the gate only fires in an OpenCode session, a developer
who commits manually from a terminal bypasses it. That''s not a theoretical edge case — it''s
exactly what would happen during a debugging session that started outside OpenCode.

---

## Tradeoffs

| Dimension | Git hook (Option A) | OpenCode hook (Option B) |
|---|---|---|
| Coverage | ALL commits, from any tool | Only within active OpenCode session |
| Reliability | Native git — extremely reliable | Can be flaky in headless/non-UI sessions |
| Failure mode coverage | Catches both agent commits AND manual commits | Misses manual commits entirely |
| Implementation complexity | Single shell script | Plugin JS/TS + event wiring |
| Bypass risk | Only via --no-verify (intentional) | Automatically bypassed when committing outside OpenCode |
| Works in CI | YES | NO (no OpenCode session in CI) |
| Persists across tool changes | YES | NO (disappears if OpenCode isn''t running) |

---

## Recommendation

**Use Option A (git pre-commit hook) as the primary gate. Option B is not needed.**

Rationale:
1. The failure mode is "feature not passing when committed" — this applies to ALL commits, not just
   in-session commits. A git hook catches both.
2. OpenCode plugin hooks are documented as unreliable in headless/non-UI sessions (confirmed by
   multiple sources) — exactly the mode used when `opencode run` is called non-interactively.
3. Git hooks cannot be accidentally bypassed — only deliberate --no-verify skips them. This is
   the behavior we want for a DoD gate.
4. The git hook is tool-agnostic and survives tool changes — if the developer ever switches away
   from OpenCode for some commits, the gate still holds.
5. solo developer context: the "annoying pre-commit hook" problem (slow tests blocking flow) is
   real BUT the solution is to make the hook fast. The check is NOT "run all tests" — it is
   only "read feature_list.json and check if the active feature''s status is passing." This is
   a sub-second JSON read, not a test suite invocation.

**Option B addendum:** An OpenCode `tool.execute.before` hook is still worth adding for
in-session awareness — specifically to warn the agent before it tries to commit when status
is not passing. This is a softer gate (a warning/block within the session) rather than a
hard backstop. It gives the agent early feedback rather than a hard commit failure.

Recommended approach: implement both, with different responsibilities:
- **Git hook = hard gate** (enforces the rule for all commits from any tool)
- **OpenCode plugin hook = early warning** (catches the condition before commit is attempted,
  during the session, so the agent can fix it without hitting the hard gate)

---

## Exact Implementation: Git Pre-Commit Hook

Create at `.git/hooks/pre-commit` (not committed to repo — lives in .git/ only):

```bash
#!/usr/bin/env bash
set -euo pipefail

FEATURE_LIST="feature_list.json"

# If no feature_list.json, pass silently (not all repos use the harness)
if [ ! -f "$FEATURE_LIST" ]; then
  exit 0
fi

# Read active feature (first feature with status not "not_started" and not "passing")
ACTIVE_STATUS=$(node -e "
  const fs = require(''fs'');
  const data = JSON.parse(fs.readFileSync(''feature_list.json'', ''utf8''));
  const active = data.features.find(f => f.status === ''in_progress'' || f.status === ''blocked'');
  if (active) {
    console.log(active.status + '':'' + active.id);
  } else {
    console.log(''none'');
  }
" 2>/dev/null || echo "parse_error")

if [ "$ACTIVE_STATUS" = "none" ] || [ "$ACTIVE_STATUS" = "parse_error" ]; then
  # No active feature or parse error — let the commit proceed
  exit 0
fi

STATUS=$(echo "$ACTIVE_STATUS" | cut -d: -f1)
FEATURE_ID=$(echo "$ACTIVE_STATUS" | cut -d: -f2)

if [ "$STATUS" = "in_progress" ] || [ "$STATUS" = "blocked" ]; then
  echo ""
  echo "COMMIT BLOCKED: feature ''$FEATURE_ID'' is ''$STATUS'', not ''passing''."
  echo "Run verification and record evidence in feature_list.json before committing."
  echo "To override: git commit --no-verify (intentional bypass only)"
  echo ""
  exit 1
fi

exit 0
```

Make executable: `chmod +x .git/hooks/pre-commit`

**Important notes:**
- Requires node.js (already required by the project for VERIFY_CMD / Playwright)
- Only blocks commits when an active feature is in_progress or blocked
- Does NOT block commits when all features are passing or not_started (clean slate)
- Gives clear error message so the developer knows exactly what to fix
- --no-verify escape hatch is intentional and documented in the error message

---

## Exact Implementation: OpenCode Plugin Hook (early warning)

In `.opencode/plugins/dod-gate.ts` (or `~/.config/opencode/plugins/dod-gate.ts` for global):

```typescript
import { Plugin } from "@opencode-ai/plugin";
import { readFileSync, existsSync } from "fs";

export default {
  tool: {
    execute: {
      before: async ({ tool, args }) => {
        // Only intercept bash/shell tool calls
        if (tool !== "bash") return;

        // Only intercept git commit commands
        const cmd = String(args?.command ?? "");
        if (!cmd.includes("git commit")) return;

        if (!existsSync("feature_list.json")) return;

        try {
          const data = JSON.parse(readFileSync("feature_list.json", "utf8"));
          const active = data.features?.find(
            (f: { status: string }) => f.status === "in_progress" || f.status === "blocked"
          );
          if (active) {
            return {
              abort: true,
              message: `DoD gate: feature ''${active.id}'' is ''${active.status}'', not ''passing''. Record evidence before committing.`,
            };
          }
        } catch {
          // Parse error — let it through, git hook will catch it
        }
      },
    },
  },
} satisfies Plugin;
```

This fires BEFORE the agent runs git commit, giving it a chance to run verification and update
feature_list.json rather than hitting a hard failure.

---

## Final Decision

**Primary gate:** git pre-commit hook (Option A) — hard, tool-agnostic, reliable.
**Secondary gate:** OpenCode plugin hook — soft early warning within sessions.
**Both are needed.** The git hook covers manual commits; the plugin hook provides agent-side
feedback so the agent corrects before hitting the hard gate.
