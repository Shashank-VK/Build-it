# Notifications Discipline

- Central orchestration only: events → orchestrator → channels. No direct sends from features.
- Preferences + quiet hours + dedup windows enforced at the orchestrator.
- Every notification type has an eval (render + routing test) and an unsubscribe path.

Ref: `../how-to-use/00-rules.md` (notifications cards).
