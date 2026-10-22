# harness-templates/

These four files are pulled verbatim from:
**`walkinglabs/learn-harness-engineering`**
Path: `docs/en/resources/templates/`
Pulled: 2026-08-09 via Invoke-WebRequest (full content, not truncated)

## Files

| File | Walkinglabs Subsystem | Purpose |
|---|---|---|
| AGENTS.md | Instructions + Session Lifecycle | Drop into project root. Defines the 6-step startup workflow and end-of-session checklist. |
| init.sh | Session Lifecycle | Install deps (INSTALL_CMD), run baseline (VERIFY_CMD), print start command. Configure the three variables at the top. |
| claude-progress.md | State | Per-session progress log. Agent reads this first at startup and updates before handoff. |
| feature_list.json | Scope + Verification | Feature tracker. single_active_feature: true enforces one-at-a-time. Each feature has verification[] steps and evidence[] for proof. |

## Audit Notes

- All four files fetched via Invoke-WebRequest — fetch tool was truncating content mid-sentence.
- File sizes: AGENTS.md (1949 chars), init.sh (664 chars), claude-progress.md (1194 chars), feature_list.json (2007 chars).
- Verbatim source files. Edit variables and features before use.

## How to Use

1. Copy all four files to your project root.
2. Edit init.sh — set INSTALL_CMD, VERIFY_CMD, START_CMD to your project commands.
3. Edit claude-progress.md — fill in Current Verified State.
4. Edit feature_list.json — replace example features with your tasks.
5. Keep AGENTS.md as-is or adjust working rules to match your conventions.
6. Run the DoD template from research/04-harness-environment.md §1 startup sequence before each session.
