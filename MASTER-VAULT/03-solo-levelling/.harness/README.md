# Solo AI Product Engineering System v1.0
# AI Development Harness (.harness/)

> **Status:** Operational Harness v1.0.0
> **Architecture:** Harness-as-code for a solo product engineer utilizing AI co-pilots under deterministic lifecycle interception, formal ABAC security, and bounded execution loops.

## Core Directories & Files

| Path | Description |
|------|-------------|
| `config/harness.yaml` | Master harness configuration and loop engineering rails |
| `hooks/hooks.json` | Pre- and post-tool lifecycle interceptors |
| `hooks/pre_tool_guard.py` | 0-false-positive security guard for command and injection defense |
| `permissions/policies.cedar` | Formally verified Cedar ABAC policy rules (deadlock-free) |
| `permissions/presets.json` | Per-archetype role permissions (C1 Product to C4 Research) |
| `sandbox/gate.sh` | Docker, bubblewrap (bwrap), or masked credential command runner |
| `telemetry/litellm-config.yaml` | Multi-model routing (Claude, Gemini Flash/Lite) and daily spend caps |
| `mcp/tools.yaml` | MCP tool specifications for artifact and governance automation |
| `skills/` | The 9 OS Workflow skills matching the human-AI delegation taxonomy |
| `workflows/` | Deterministic YAML state machines governing the 9 OS workflows |

## Safety & Governance Principles

1. **Security First (SC-07):** Pre-tool guard blocks destructive file deletions, piped script injections, force-pushes to main, and unquoted secret parameters.
2. **Loop Rails (Phase 16):** Global `max_steps=15` rail; consecutive identical tool calls fatal error (IAL debounce); external exit gate mandatory.
3. **Deadlock-Free ABAC:** Class 3 irreversible mutations permitted only with explicit human approval token.
4. **Isolated Adversarial Review:** Gate 4 FCAR executions must run in isolated fresh contexts.
