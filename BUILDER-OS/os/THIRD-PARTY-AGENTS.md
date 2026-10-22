# Third-Party Agents Registry

EXTERNAL coding agents catalogued in the corpus (B-category-catalogs/11-agents,
12-multi-agent, atlas/03b-agents, how-to-use/03-agents-harness-context.md).
This OS is agent-agnostic: the harness (skills, gates, evidence) works under
any of these; OpenCode-only behaviors are flagged, never assumed.

| Agent | Use / trigger |
|---|---|
| Claude Code | Agentic coding, fresh-context review pairing |
| Cursor | IDE-integrated agent runs |
| OpenAI Codex (incl. codex MCP) | Cloud/local agent delegation |
| Gemini CLI | Google-model agent runs |
| Cline | VS Code autonomous coding |
| Windsurf | Agentic IDE flows |
| Continue (continuedev) | Open-source IDE agents |
| Aider | Terminal pair-programming |
| GitHub Copilot (incl. copilot-sdk) | Completion + agent mode; SDK: https://github.com/github/copilot-sdk |
| Ar9av/agent-manual | Agent operations manual (reference): https://github.com/Ar9av/agent-manual |

Multi-agent patterns (orchestrator-workers, Two-Judge council, FCAR reviewer)
are OS-native (AGENTS.md C1–C5 + reviewer subagent) regardless of which
external agent below executes the work.
