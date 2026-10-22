I have comprehensive coverage across all three tasks with primary-source verification. Let me compile my final research deliverable.

---

# PHASE 1 BATCH 3 — INTEGRATION & EXTENSIBILITY — BROAD MAPPER (R-A) DEEP RESEARCH

**Researcher A | P1-17 + P1-19 + P1-21 | Date: 2026-08-31 | Repo: `the harness`**
**Continuity:** `plan.md §2 Batch 3` · `phase-0/ARCHETYPES_AND_CRITERIA.md` C1-C6, SC-01..10 · Batches 1-2 converged (E1-E11, B1-B10 — NOT duplicated)

---

## 0. METHOD & COVERAGE

### 0.1 Search angles (13 distinct, 7 required) and ecosystems hit

| # | Angle | Ecosystems / surfaces touched | Primary sources |
|---|-------|------------------------------|-----------------|
| A1 | MCP core protocol evolution (transports, extensions, Tasks, Apps, Auth, Registry) | Claude, ChatGPT, VS Code Copilot, Cursor, Goose, Postman, MCPJam, PostHog Code | [`modelcontextprotocol.io`](https://modelcontextprotocol.io/) full docs + llms.txt |
| A2 | MCP registry + package types (npm/PyPI/NuGet/Cargo/OCI/MCPB) + aggregators | MCP Registry, GitHub, PulseMCP, Microsoft | [registry/about](https://modelcontextprotocol.io/registry/about), [package-types](https://modelcontextprotocol.io/registry/package-types) |
| A3 | MCP Apps extension (in-client interactive UI) | Claude, Claude Desktop, Copilot, Microsoft 365, Goose, Postman, ChatGPT, Cursor | [apps/overview](https://modelcontextprotocol.io/extensions/apps/overview) |
| A4 | MCP Tasks extension (async execution) | cross-client | [tasks/overview](https://modelcontextprotocol.io/extensions/tasks/overview) |
| A5 | Agent Skills open standard adoption | Claude Code, Claude, ChatGPT/Codex, Gemini CLI, VS Code, Copilot, Cursor, OpenCode, OpenHands, Letta, Goose, Roo, Junie, Spring AI, Databricks, Snowflake, Tabnine, Pulumi Neo, 40+ products | [agentskills.io](https://agentskills.io/home), [agentskills/agentskills repo](https://github.com/agentskills/agentskills) |
| A6 | Claude Code skills + plugins + hooks + MCP docs | Claude Code | [code.claude.com/docs](https://code.claude.com/docs/en/skills), [/plugins](https://code.claude.com/docs/en/plugins), [/hooks](https://code.claude.com/docs/en/hooks), [/mcp](https://code.claude.com/docs/en/mcp), [/features-overview](https://code.claude.com/docs/en/features-overview.md) |
| A7 | OpenAI/ChatGPT/Codex skills + plugins taxonomy | ChatGPT, Codex | [learn.chatgpt.com/docs/build-skills.md](https://learn.chatgpt.com/docs/build-skills.md), [build-plugins.md](https://learn.chatgpt.com/docs/build-plugins.md), [developers.openai.com/plugins/concepts/plugins.md](https://developers.openai.com/plugins/concepts/plugins.md) |
| A8 | Cursor plugins/skills/hooks/MCP + marketplace + Cursor Router | Cursor | [cursor.com/docs/plugins.md](https://cursor.com/docs/plugins.md), [/skills.md](https://cursor.com/docs/skills.md), [/hooks.md](https://cursor.com/docs/hooks.md), [cursor-router](https://cursor.com/help/models-and-usage/cursor-router.md) |
| A9 | Agent Plugins open standard | Amazon, Cursor, Microsoft, OpenAI, Vercel TSC | [agent-plugins.org](https://agent-plugins.org) |
| A10 | ACP (Agent Client Protocol) + registry | Zed, Obsidian, VS Code, Emacs, 39 agents (Claude, Codex, Cursor, Copilot, Devin, Gemini, Copilot) | [agentclientprotocol.com](https://agentclientprotocol.com), [registry](https://github.com/agentclientprotocol/registry), [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) |
| A11 | MCP proxy/gateway/hub/aggregator ecosystem | community OSS | [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) (3,482 servers), MCPHub, etc. |
| A12 | Model/provider abstraction | LiteLLM, OpenRouter, Vercel AI SDK, Cursor Router | [LiteLLM docs](https://docs.litellm.ai/docs/), [openrouter.ai](https://openrouter.ai/), [vercel/ai](https://github.com/vercel/ai) |
| A13 | Awesome-lists audit (hidden categories) | awesome-mcp-servers, awesome-mcp-clients, awesome-claude-code, awesome-agent-skills, awesome-claude-skills, mcp.so, MCPRegistry, Component | incl. [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code), [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), [mcp.so](https://mcp.so/), [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) |

**Stop rule per sub-area:** Tracked. MCP protocol (A1-A4) reached synonyms at ~5 fetches but new primitives (MCPB, Tasks, Apps) still surfaced; Skills (A5-A9) kept yielding new adopters and the Agent Plugins standard at every step; model abstraction (A12) is a stable, well-catalogued throne (LiteLLM/OpenRouter/AI SDK). A11/A13 are currently still productive — hidden categories keep appearing — so a conservative "not yet halted" is claimed, but the marginal novelty per fetch is now declining (proxy/gateway/token-saver are the main new clusters).

**Quality bar:** Every candidate has ≥2 independent sources (vendor docs crossed with a second vendor or OSS/repo). Vendor marketing cross-checked against actual manifests and repos (e.g., Cursor plugin manifests, OpenAI `.codex-plugin/plugin.json`, marketplace.json).

**Batch 1-2 non-duplication:** MCP was already flagged as Batch 3 territory; hooks as E10 Lifecycle Interception are referenced but not re-promoted. Skills/plugin mechanics per Batch 1 M7 hygiene (Skills category = Capability; individual skill = Resource; repo = Implementation) upheld.

---

## 1. P1-17 SWEEP — WHAT EXISTS, WHERE IT LIVES, HOW IT WORKS

### 1.1 MCP (Model Context Protocol) — now a Protocol with an extension layer

**Canonical name:** MCP (Model Context Protocol). Currently at a mid-2026 spec revision `2026-07-28` alongside `draft`, `2025-11-25`, `2025-06-18`, `2025-03-26`, `2024-11-05`.

**What it is (authoritative):** "An open-source standard for connecting AI applications to external systems" — data sources (files, DBs), tools, and workflows. Vendor-agnostic JSON-RPC client-server protocol. The "USB-C for AI" framing is the canonical metaphor.

**Definition in taxonomy terms:** MCP is a **Protocol** (level P). It is the substrate underlying the integration layer. It standardizes: server discovery, tool/resource/prompt primitives, transports (stdio/streamable-HTTP/legacy SSE), lifecycle, auth (DCR, client-registration, OAuth 2.1, CIMD), and now **official extensions** (`io.modelcontextprotocol/…`).

**Why it matters for the harness:** MCP is now the de-facto cross-ecosystem integration language. Its client list spans Claude, ChatGPT, VS Code Copilot, Cursor, Cline, Windsurf, Goose, Postman, MCPJam, PostHog Code, and dozens more (89 MCP clients catalogued in awesome-mcp-clients). For a harness, "which MCP servers are connected" becomes a portability/portability lever across all target archetypes C1-C6 (C4 agentic especially).

**Key 2026 protocol developments (beyond vendor docs):**

1. **MCP Registry** — official centralized metadata repo for publicly accessible servers, backed by Anthropic, GitHub, PulseMCP, Microsoft. `server.json` metadata: unique reverse-DNS name (`io.github.user/server`), package pointers (npm/PyPI/NuGet/Cargo/OCI/MCPB), execution instructions. Namespace auth via DNS/GitHub/HTTP verification; deliberately unopinionated, consumed by downstream aggregators (marketplaces) via REST API conforming to an OpenAPI spec. **Never directly consumed by host apps** — hosts consume registries/marketplaces. Currently preview.

2. **MCPB (!) — MCP Bundles** — packaging format for local stdio servers bundled with their runtime as single `.mcpb` archive, "so users can install it without Node or Python." Supported as a first-class registry package type (`registryType: mcpb`) with SHA-256 verification. This is a significant distribution/portability mechanism — the ability to distribute a tool server as a portable bundle across 89+ clients.

3. **MCP Apps extension (`io.modelcontextprotocol/ui`)** — lets MCP servers return interactive HTML interfaces (data viz, forms, dashboards) rendered inline in the client conversation in a sandboxed iframe with postMessage-based bidirectional communication. **Not in vendor docs; it's a spec-level extension.** 8+ clients (Claude, Claude Desktop, VS Code Copilot, M365 Copilot, Goose, Postman, MCPJam, ChatGPT, Cursor). This is the "interactive output surface" mechanism.

4. **MCP Tasks extension (`io.modelcontextprotocol/tasks`)** — asynchronous task execution: server returns a durable `taskId`, clients poll `tasks/get`, statuses `working/input_required/completed/failed/cancelled`, with `tasks/update` for mid-flight input and `tasks/cancel`. This is an **async job primitive at the protocol level** — distinct from (but connected to) Batch 1 E5 Background/queued execution.

5. **OAuth Client Credentials + Enterprise-Managed Authorization extensions** — machine-to-machine and centralized enterprise access control.

6. **Authorization depth:** the spec now has dedicated `authorization` pages (DCR, client-registration, security-considerations) — MCP is addressing the enterprise auth gap.

**Lifecycle role:** Connection/transport between any client and any server, at run-time (tool listing, tool call, resource read, prompts). MCP itself is a **protocol**, not a capability or a mechanism, but the *MCP Apps* extension is arguably a capability-like mechanism.

**Level:** Protocol. Related: A2A (agent-to-agent, cross-client), ACP (client-to-agent protocol), Agent Plugins (packaging), Skills (content).
**Tier preliminary:** **foundational** for a harness that must integrate many tools across archetypes. **Confidence: High** (multiple independent spec pages + 89-client adoption + registry).

**Cross-ecosystem terms:** MCP (Anthropic-originated, now open) ≡ "tool server / connector / plugin backend" (vendor-specific names for the same class of remote-capability endpoint).

---

### 1.2 MCP Registries & Marketplaces (the plumbing layer)

| Registry / Directory | Type | Notes |
|---|---|---|
| **MCP Registry** (official) | Central metadata registry | OpenAPI-specified; npm/PyPI/NuGet/Cargo/OCI/MCPB package types; namespace auth; not directly consumed by host apps |
| **mcp.so** | Community marketplace + directory | Categories: Dev Tools, AI & Agents, Cloud & Infra, **Memory & Knowledge**, Media & Design, plus novel nav: **Servers / Remote Servers / Clients / CLI / Loops / Skills / Agents** |
| **Glama.ai** (`glama.ai/mcp/servers`) | Community MCP registry + ratings + score badges | 90+ categories; the badge/rating layer |
| **PulseMCP** | Community directory + newsletter | Often-quoted source for MCP news/statistics |
| **awesome-mcp-servers** (punkpeye) | GitHub list | 93.6k stars, ~3,482 servers (~45 categories), MIT; originally the canonical "huge README" resource — still useful, but now curated/community, not authoritative |
| **mcpfinder** | MCP server that *finds MCP servers* | "Discovers, evaluates, installs 25K+ MCP servers across Official Registry, Glama,..." — a discovery-capability |
| **MCPHub** (samanhappy, 2.3k★) | MCP management/orche