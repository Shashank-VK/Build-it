# Phase 1 — Batch 3: Integration & Extensibility — Converged Taxonomy Slice

> **Status:** CONVERGED — P1-17..24 (researchers P1-17..21, verifiers P1-22..24) | **Date:** 2026-08-31 / 09-01
> **Dispatch:** Via WSL `agy` (antigravity CLI) — plan §8.1 WSL dispatch. All 4 agents returned.
> Inputs: [`R-A_BROAD_MAPPER_AGY.md`](R-A_BROAD_MAPPER_AGY.md) (19K) · [`R-B_CHALLENGER_AGY_.md`](R-B_CHALLENGER_AGY_.md) (18K) · [`V-C_ADVERSARIAL_AGY.md`](V-C_ADVERSARIAL_AGY.md) (30K) · [`V-D_ARCHITECTURAL_AGY.md`](V-D_ARCHITECTURAL_AGY.md) (32K)
> Repo: `the harness` | Grounding: `plan.md §2 Batch 3` · `phase-0/ARCHETYPES_AND_CRITERIA.md` C1-C6, SC-01..10 · `phase-1/batch-1` + `batch-2` converged capabilities (E1-E11, B1-B10)

---

## 0. Method & Coverage

- **R-A (Broad Mapper, via agy):** MCP protocol as convergence of the M×N integration problem (adopted Claude Code, Antigravity, Cursor, Cline/Roo, OpenHands, Continue). Distinguished **Rules** (passive), **Skills** (procedural runbooks via progressive disclosure), **Hooks** (deterministic lifecycle gates), **Plugins** (composite bundles). Model abstraction via **AI Gateways** (LiteLLM, Portkey) + **Learned Routers** (RouteLLM, OpenRouter). MCP registries: mcp.so, Glama, PulseMCP, awesome-mcp-servers.
- **R-B (Challenger, via agy):** 5 distinct semantic planes. **Function calling vs tool use vs skill vs skill pack vs plugin** disambiguated. **MCP Triad** (client ↔ server ↔ registry). **Execution vs Control plane** (non-deterministic model tools vs deterministic lifecycle hooks). Context budgeting + multi-tier model routing. Governance cascading (`skills.json`/`plugins.json`).
- **V-C (Adversarial, via agy):** P1-22 translation check across 5 ecosystems (Anthropic, OpenAI, MS Semantic Kernel, LangChain/LlamaIndex, Cursor/Cline/Windsurf). Verdict: **8 DISTINCT, 2 MERGED, 2 KILLED**. 5-layer integration architecture.
- **V-D (Architectural, via agy):** P1-23 re-tag (6 levels). 24-row converged B3 master table with lifecycle, tier, SC-wiring, redundancy vs Batch 1/2.

---

## 1. Converged Batch 3 Master Table (V-D B3-01..24)

*Level: Capability / Mechanism / Protocol / Framework / Resource / Implementation-Tool. Tier: foundational / important / specialized / situational.*

| # | Canonical | Definition | Level | Lifecycle | Tier | SC Wiring | Redundancy vs Batch 1/2 |
|---|-----------|------------|-------|-----------|------|-----------|--------------------------|
| **B3-01** | **Model Context Protocol (MCP)** | Open standard (JSON-RPC 2.0, stdio/SSE) client-server contract: tools, resources, prompts, sampling. M×N → M+N. | Protocol/Standard | run | **FOUNDATIONAL** (0.95) | SC-02 TSR | Non-redundant (external tool std vs E1-E5 native) |
| **B3-02** | **MCP Client Subsystem** | Harness middleware: server lifecycle, capability negotiation, tool registration, RPC dispatch. | Framework/Runtime | run | **FOUNDATIONAL** | SC-02, SC-07 | Interfaces E1-E11 |
| **B3-03** | **MCP Server Runtime** | Isolated daemon (stdio local / SSE remote) exposing domain capabilities. | Framework/Runtime | run | **IMPORTANT** | SC-02, SC-07 | Non-redundant (external processes) |
| **B3-04** | **MCP Registry & Catalogs** | Discovery/index/download of MCP servers (mcp.so, Glama, PulseMCP, awesome-mcp-servers ~3,482). | Tool/Product/Repo | build | **SPECIALIZED** | SC-02 | Catalog service |
| **B3-05** | **MCP Primitives (Tools/Resources/Prompts/Sampling)** | Core protocol data structures. | Protocol/Standard | run | **IMPORTANT** | SC-02, SC-05 | Refines B9 + E1-E5 schemas |
| **B3-06** | **Skills Capability** | Selective load + follow of structured procedural runbooks on demand. | **Capability** | run | **FOUNDATIONAL** | SC-02, SC-05 | Non-redundant (procedural vs B9 static) |
| **B3-07** | **Individual Skill Resource** | `SKILL.md` + YAML frontmatter (name, description) + `scripts/` + `references/`. | Resource/Artifact | build → run | **FOUNDATIONAL** | SC-02 | Non-redundant runbook artifact |
| **B3-08** | **GitHub Skills Repositories / Packs** | Versioned skill collections for team/public consumption. | Implementation/Repo | build | **SITUATIONAL** | SC-02 | External package sources |
| **B3-09** | **Progressive Disclosure** | Two-stage: metadata injected at startup; full body only on model activation. | Mechanism | run | **FOUNDATIONAL** | SC-05, SC-02 | Optimizes B1 budget |
| **B3-10** | **Rules Enforcement** | Discover + apply directory-scoped constraints/conventions. | **Capability** | run | **FOUNDATIONAL** | SC-07, SC-02 | Complements B9 |
| **B3-11** | **Directory & Project Rules** | `AGENTS.md`, `GEMINI.md`, `.cursorrules` declaring tree-level standards. | Resource/Artifact | build → run | **FOUNDATIONAL** | SC-07, SC-02 | Ambient vs procedural |
| **B3-12** | **Rule Dedup & Hierarchical Inheritance** | CWD→root traversal, resolve conflicts, dedupe by path. | Mechanism | run | **IMPORTANT** | SC-05, SC-07 | Filesystem logic |
| **B3-13** | **Lifecycle Hooks** | External synchronous scripts at defined events to inspect/mutate/abort. | **Capability** | run | **FOUNDATIONAL** | SC-07, SC-02 | Control-plane counterpart to E2/B7 |
| **B3-14** | **Deterministic Policy Gates** | `PreToolUse`/`PostToolUse`/`Stop` returning allow/deny/ask/mutate. | Mechanism | run | **FOUNDATIONAL** | SC-07 | Wraps E1-E11 |
| **B3-15** | **Hook Configuration Manifest** | `hooks.json`: matchers, handlers, timeouts. | Resource/Artifact | build → run | **FOUNDATIONAL** | SC-07 | Config schema |
| **B3-16** | **Plugin Packaging** | Encapsulate/distribute/namespace/toggle multi-component extensions. | **Capability** | build → run | **IMPORTANT** | SC-02, SC-07 | Complements E6 |
| **B3-17** | **Plugin Manifest & Bundle** | `plugin.json` bundling skills, rules, hooks, MCP configs. | Resource/Artifact | build | **IMPORTANT** | SC-02 | Distribution package |
| **B3-18** | **Model Gateway & Translation** | Provider-agnostic LLM interfacing, schema translation, failover, retry, telemetry. | **Capability** | run | **FOUNDATIONAL** | SC-02, SC-05 | Upgrades B4 static bindings |
| **B3-19** | **Multi-Provider Proxy (LiteLLM/Portkey)** | Middleware standardizing 100+ LLM APIs to OpenAI-compatible format. | Tool/Product/Framework | run | **IMPORTANT** | SC-02, SC-05 | Middleware |
| **B3-20** | **Dynamic Model Routing** | Route turns to cost-optimal vs high-reasoning models by complexity + budget. | **Capability** | run | **IMPORTANT** | SC-05, SC-02 | Non-redundant tier selection |
| **B3-21** | **Model Router Engines (RouteLLM/OpenRouter)** | Classifier/matrix routing for cost-quality Pareto. | Tool/Product/Mechanism | run | **SPECIALIZED** | SC-05 | Implements B3-20 |
| **B3-22** | **Function Calling / Tool-Use Schemas** | Structured JSON-Schema output contracts. | Protocol/Standard | run | **FOUNDATIONAL** | SC-02 | Powers E1-E11 |
| **B3-23** | **Execution vs Control Plane** | Separation: non-deterministic LLM actions vs deterministic policy gating. | Architectural Pattern | build → run | **FOUNDATIONAL** | SC-07, SC-02 | Foundational boundary |
| **B3-24** | **Governance Scoping & Cascade** | Priority cascade: workspace > `skills.json`/`plugins.json` > global > built-ins. | Mechanism/Pattern | run | **IMPORTANT** | SC-07, SC-05 | Load order gov |

---

## 2. V-C 8 Canonical Primitives + Translation Matrix

**8 DISTINCT (V-C canonical):** Tool/Function Call · Open Tool Protocol (MCP) · Procedural Skill · Composite Plugin · Passive Steering Rules · Deterministic Hook · Model Gateway · Adaptive Router.

| Canonical | Anthropic | OpenAI | MS SK | LangChain | Cursor/Cline | Portability | Verdict |
|---|---|---|---|---|---|---|---|
| Open Tool Protocol | MCP Server/Client | Custom Actions | SK Connectors | MCP Adapters | Cline/Cursor MCP | Portable Open Std | **DISTINCT** |
| Primitive Tool | Tool Definition | `tools:[function]` | KernelFunction | BaseTool | Tool Call Handler | Universal | **DISTINCT** |
| Procedural Skill | Slash/Skill | GPT Instructions | SK Native Function | PromptTemplate+ToolNode | Windsurf Rule | Portable Pattern | **DISTINCT** |
| Composite Plugin | Plugin Archive | GPT Store Bundle | PluginDirectory | Toolkit/LlamaPack | VS Code/Cursor Plugin | Packaging Format | **DISTINCT** |
| Passive Rules | `CLAUDE.md` | Assistant instructions | System Message | SystemMessagePromptTemplate | `.cursorrules` | Prompt Component | **DISTINCT** |
| Deterministic Hook | Pre/PostToolUse | Middleware/Webhook | FunctionFilter | CallbackHandler | onWillExecuteCommand | Architectural Pattern | **DISTINCT** |
| Model Gateway | API Proxy | API Proxy | IChatCompletionService | BaseChatModel | Provider Switcher | Infra Primitive | **DISTINCT** |
| Adaptive Router | Manual selector | Router (tiered) | Model Selector | RouterRunnable | OpenRouter Auto | Algorithmic Mechanism | **DISTINCT** |
| Progressive Disclosure | Tier 1-3 | Retrieval aug | Dynamic filter | Dynamic selector | Lazy indexer | Mechanism | **MERGED** |
| Slash Command | `/goal /plan` | GPT Action trigger | Invocation Command | Command Parser | Command Palette | UI/UX Sugar | **KILLED** |
| Agent Function | Subagent tool | Assistant call | KernelPlugin.Functions | ToolNode Worker | Subagent Dispatch | Redundant Name | **KILLED** |

---

## 3. 5-Layer Integration Architecture (V-C)

```
Layer 5: Control & Governance      Lifecycle Hooks | Permission Cascades | Policy Gateways
Layer 4: Procedural Context        Procedural Skills (Runbooks) | Passive Steering Rules
Layer 3: Distribution/Packaging    Composite Plugins (Skill Packs / Extension Manifests)
Layer 2: Inter-Process Interface   Open Tool Protocol (MCP / JSON-RPC / SSE / Stdio)
Layer 1: Transport & Dispatch      Universal Model Gateways | Adaptive Routers
Execution Primitive Base           Primitive Tools / Function Calling Engine
```

---

## 4. Kill / Merge / Demote Log

| Action | Count | Details |
|--------|-------|---------|
| KEEP distinct | 8 (V-C) / 24 rows (V-D) | Tool, MCP, Skill, Plugin, Rules, Hook, Gateway, Router |
| MERGE | 2 | Progressive Disclosure → Skill/Adaptive Context; Context Rules → Passive Steering |
| KILL | 2 | Slash Command (UI sugar), Agent Function (identical `{name, arguments}` payload) |

**Level-hygiene (V-D):** Skills = Capability (B3-06) vs `SKILL.md` = Resource (B3-07) vs GitHub repo = Implementation (B3-08); Hooks = Capability (B3-13) vs `hooks.json` = Resource (B3-15); Gateway = Capability (B3-18) vs LiteLLM = Tool (B3-19); Router = Capability (B3-20) vs RouteLLM = Tool (B3-21).

---

## 5. Cross-Batch Boundary (V-D)

- **E1-E5 Native Tools ↔ B3-01 MCP / B3-22 Function Calling:** native = hardcoded in harness; MCP = protocol-defined external RPC. Non-redundant.
- **E2 / B7 ↔ B3-13/B3-14 Hooks:** hooks are deterministic control-plane gates wrapping non-deterministic execution. Boundary = determinism.
- **B4 ↔ B3-18/19 Gateway:** B4 was static model provider binding; B3-18 is provider-agnostic abstraction layer. Upgrade.
- **B9 System Prompt ↔ B3-10/11 Rules + B3-06/07 Skills:** B9 = static context assembly; B3-10/06 = ambient constraints + procedural. Complements, not duplicates.

---

## 6. Sources & Dispatch Notes

**Dispatch friction (integration finding — logged `ISSUES.md` #7/#8):** native Workflow failed twice (R-A terminal, R-B JSON write); `opencode run` produced 0 bytes on this socket; **WSL `agy --print | tee literal_path` is the reliable dispatcher**.

**Sources (primary):** MCP spec [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction) · LiteLLM [docs.litellm.ai](https://docs.litellm.ai/) · RouteLLM [github.com/lm-sys/RouteLLM](https://github.com/lm-sys/RouteLLM) · JSON-RPC 2.0 [jsonrpc.org](https://www.jsonrpc.org/specification) · Antigravity agy-customizations SKILL docs (hooks.md / plugins.md / mcp_servers.md, read by V-D) · awesome-mcp-servers (punkpeye, ~3,482 servers).

**Last verified:** 2026-09-01.