# CLAUDE.md — AI Development Harness Bridge

This workspace is governed by the **AI Development Harness**, an enterprise-grade agent orchestration and safety substrate. All agent executions, subagent dispatches, and tool invocations operate under continuous behavioral guardrails, formal policy validation, and deterministic lifecycle interception.

When operating in this repository, agents must strictly adhere to the harness architecture, respect permission boundaries, and execute through established validation gates.

## Mandatory Behaviors

1. **`rule-preserve-code-integrity`**: Preserve existing comments, docstrings, architectural rationale, and unrelated functions. Prefer surgical line replacements over destructive overwrites.
2. **`rule-strict-typing-hygiene`**: Maintain strict type annotations across interfaces, models, and function signatures. Never bypass typing rules with untyped bypasses.
3. **`rule-zero-secret-leakage`**: Never write, log, or hardcode API keys, tokens, credentials, or high-entropy secrets into files or commit history.
4. **`rule-verification-before-done`**: Always run verification gates (`task verify`) and verify exit code 0 before concluding any modification.
5. **`rule-anti-bloat`**: Keep changes minimal, modular, and focused. Avoid unnecessary external dependencies, premature abstractions, or dead code.

## Quick Reference

- **Run Tests**: `task test` (runs pytest suite with exit-on-first-failure)
- **Check Permissions**: `cat .harness/permissions/presets.json` (view archetype permissions)
- **List Skills**: `task skills-list` (lists all 40 registered skills & tiers)
- **Run Sandbox Gate**: `task sandbox -- <command>` (executes isolated bubblewrap/docker command)

## Key Files

| Path | Description |
|---|---|
| [`.harness/hooks/hooks.json`](file:///.harness/hooks/hooks.json) | Deterministic in-process pre/post tool interceptor manifest |
| [`.harness/permissions/policies.cedar`](file:///.harness/permissions/policies.cedar) | Formally verified Cedar ABAC security & permission rules |
| [`.harness/permissions/presets.json`](file:///.harness/permissions/presets.json) | Role-based tool access presets and HITL escalation triggers |
| [`.harness/telemetry/litellm-config.yaml`](file:///.harness/telemetry/litellm-config.yaml) | LiteLLM routing matrix, model failovers, and budget caps |
| [`.harness/sandbox/gate.sh`](file:///.harness/sandbox/gate.sh) | Linux namespace / container blast-radius isolation script |
