# AI Development Harness — Versioned Configuration (.harness/)

> **Status:** v1.0.0 — materialized + validated (Phase 3.5) | **Last verified:** 2026-09-01
> **This is harness-as-code.** The set of capabilities/tools/guards an agent operates under. Diffable, reversible, maintainable.

## What's here

| Path | Purpose | Element |
|------|---------|---------|
| `agents/` (planner/explorer/coder/reviewer) | Delegated subagent definitions | CAP-01 |
| `workflows/` + `workflows/blueprints/` | Deterministic workflow blueprints | CAP-04 |
| `hooks/hooks.json` + `pre_tool_guard.py` + `post_tool_linter.py` | Lifecycle interception + security gates | CAP-20/37 |
| `permissions/policies.cedar` + `presets.json` | ABAC policy + per-archetype presets | CAP-25 |
| `sandbox/gate.sh` | OS sandbox invocation (bwrap/docker) | CAP-24 |
| `mcp/mcp_servers.json` | MCP server config | CAP-17 |
| `skills/` (index + 5 materialized) | Procedural skills (progressive disclosure) | CAP-18 |
| `telemetry/litellm-config.yaml` + `langfuse-config.json` | Model gateway + cost budget | CAP-22/35 |
| `config/harness.yaml` + `harness.config.yaml` | Harness-as-code manifest | PROT-03 |

## Operating rules for future agents

1. **Security first (SC-07):** never bypass `pre_tool_guard.py`; treat `rm -rf`, secrets, force-push-to-main as blocked.
2. **Skills (progressive disclosure):** load skill body only on trigger; keep index lean.
3. **Budget:** LiteLLM $5/session hard cap; watch cost attribution.
4. **Sandbox:** route untrusted commands through `sandbox/gate.sh`.
5. **Any change to this directory** = harness version bump (semver) + update `update.md`.

## Validation evidence (Phase 3.5)
- Guard blocks `rm -rf /`, AWS/GitHub keys, force-push-to-main (exit 2); passes benign (exit 0). ✅
- All JSON configs valid. ✅
- Skills index + repo-surveyor `survey_repo.py` functional. ✅

## Versioning
- v1.0.0 = materialization sprint complete (2026-09-01). Future: bump on capability/tool/policy change. Re-check quarterly (CR-01) or on breaking change.