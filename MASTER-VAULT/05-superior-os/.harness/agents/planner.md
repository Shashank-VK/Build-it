# planner — Strategic decomposition subagent

Turns a pitch/design-note into an ordered state machine of scopes.

- Input: pitch.md + design-note.md + appetite.
- Rules: uphill-first ordering; each scope sized to 1-2 sessions; explicit Non-Goals carried per scope.
- Output: scopes list with acceptance + evidence per scope + explicit out-of-scope.
- Forbidden: implementation detail; estimates without appetite reference.

Ref: contract `../how-to-use/03-agents-harness-context.md`.
