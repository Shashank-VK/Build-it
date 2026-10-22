# ARCHITECTURAL VERIFICATION REPORT: PHASE 1 BATCH 3
**Focus Area**: Integration, Model Abstraction & Extensibility (P1-23 & P1-24)  
**Verifier**: VERIFIER D — Architectural Verifier  
**Scope**: Abstraction Level Re-tagging, Semantic Plane Separation, Lifecycle/Tiering Classification, SC-Wiring Rationale, Redundancy Analysis (vs. Batch 1 E1–E11 & Batch 2 B1–B10), and Taxonomy Convergence.

---

## 1. Executive Summary & Verification Objectives

This report executes **P1-23** (Architectural Abstraction Re-tagging & Semantic Plane Separation) and **P1-24** (Lifecycle Role, Preliminary Tiering, SC-Wiring, Redundancy Boundary Analysis, and Taxonomy Slice Convergence) for **Phase 1 Batch 3: Integration & Extensibility**.

Based on empirical inputs from Researchers A and B, candidate items have been analyzed across the full integration lifecycle:
1. **Model Context Protocol (MCP) Triad & Primitives**: Disentangling protocol standards from client/server runtimes and registry implementations.
2. **Skills vs. Rules vs. Plugins Spectrum**: Enforcing strict `plan.md` hygiene where **Skills** is a capability category, **Individual Skill** (`SKILL.md`) is a Resource, and **GitHub Skills Repositories** are Implementations.
3. **Execution Plane vs. Control Plane**: Delineating non-deterministic model tool execution from deterministic lifecycle hook gating.
4. **Model Abstraction, Gateways & Dynamic Routers**: Distinguishing multi-provider abstraction capabilities from proxy runtimes (LiteLLM/Portkey) and routing mechanisms (RouteLLM/OpenRouter).
5. **Governance & Cascading Scoping**: Validating hierarchical discovery and resolution policies (`skills.json`, `plugins.json`, directory cascades).

---

## 2. Ontological Abstraction Framework

To prevent conceptual conflation, every candidate in Batch 3 is re-tagged against six strictly bounded architectural levels:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. CAPABILITY           What the agent harness fundamentally needs          │
│                         (e.g., On-demand procedural knowledge retrieval)    │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. MECHANISM            The technical pattern or algorithm used             │
│                         (e.g., Progressive disclosure via YAML frontmatter) │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. PROTOCOL / STANDARD  Formal interface contract across system boundaries  │
│                         (e.g., Model Context Protocol [MCP] v1.0, JSON-RPC) │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. FRAMEWORK / RUNTIME  Execution engine, daemon, or middleware layer       │
│                         (e.g., MCP Language Server client, LiteLLM proxy)   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. RESOURCE / ARTIFACT  Static document, configuration file, or asset       │
│                         (e.g., SKILL.md, AGENTS.md, hooks.json, schema)     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6. IMPLEMENTATION /     Concrete software repository, package, or vendor    │
│    TOOL / PRODUCT       (e.g., modelcontextprotocol/servers, RouteLLM)      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Deep-Dive Abstraction Re-Tagging & Semantic Plane Separation (P1-23)

### 3.1. MCP Spectrum (Protocol Triad & Primitives)

```
                       ┌─────────────────────────┐
                       │   MCP Client Runtime    │ (Framework/Runtime)
                       │   (Harness Tool Engine) │
                       └────────────┬────────────┘
                                    │ JSON-RPC 2.0 (Stdio / SSE)
                                    │ (Protocol / Standard)
                       ┌────────────┴────────────┐
                       │   MCP Server Runtime    │ (Framework/Runtime)
                       │   (sqlite, git, custom) │
                       └────────────┬────────────┘
                                    │ Exposes
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
   [MCP Tool Schema]        [MCP Resource]            [MCP Prompt]
   (Protocol Primitive)     (Protocol Primitive)      (Protocol Primitive)
```

*   **MCP Protocol (JSON-RPC 2.0 over Stdio/SSE)**: **`Protocol / Standard`**. Open specification governing two-way stateful transport between models and external resources/tools.
*   **MCP Client Subsystem**: **`Framework / Runtime`**. Harness-side middleware managing server lifecycles, capability negotiation, tool discovery, and JSON-RPC dispatching.
*   **MCP Server (Stdio / SSE Process)**: **`Framework / Runtime`**. Executable or microservice process hosting specific domain endpoints.
*   **MCP Registry / Marketplace**: **`Tool / Product / Repo`**. Distribution catalogue / discovery service for finding third-party MCP servers (e.g., `modelcontextprotocol/servers`, Smithery).
*   **MCP Primitives (Tools, Resources, Prompts, Sampling, Roots)**: **`Protocol / Standard (Primitives)`**. Semantic payload structures defined in the MCP specification.

---

### 3.2. Procedural Knowledge & Skills Spectrum (`plan.md` Hygiene)

```
 [Skills Capability] ─── (Capability: On-demand contextual workflow execution)
         │
         ├── [Progressive Disclosure] ─── (Mechanism: Metadata scan -> On-demand body read)
         │
         ├── [Individual Skill: SKILL.md] ─── (Resource / Artifact: Runbook + Frontmatter)
         │
         └── [GitHub Skills Repo / Pack] ─── (Implementation / Repo: Distribution bundle)
```

*   **Skills (Skill Execution System)**: **`Capability`**. The harness capability allowing autonomous agents to locate, ingest, and execute domain runbooks dynamically.
*   **Progressive Disclosure**: **`Mechanism`**. Two-phase context injection pattern: injecting only low-token metadata (name + description) at startup, deferring full body ingestion until explicit model activation.
*   **Individual Skill (`skills/<name>/SKILL.md`)**: **`Resource / Artifact`**. Concrete markdown file containing YAML metadata and procedural execution instructions.
*   **GitHub Skills Repository / Skill Pack**: **`Tool / Product / Repo`** (or **`Implementation`**). Versioned collection or external repository distributing multiple modular skills.

---

### 3.3. Contextual Constraints & Rules Spectrum

*   **Rules Enforcement System**: **`Capability`**. Harness capability that applies ambient behavioral constraints and coding standards based on the current workspace context.
*   **Directory & Project Rules (`GEMINI.md`, `AGENTS.md`, `.agents/rules/*.md`)**: **`Resource / Artifact`**. Static markdown documents defining invariant instructions and scoping boundaries.
*   **Hierarchical Rule Inheritance & Deduplication**: **`Mechanism`**. Algorithm that walks the directory tree from CWD to repo root, loads applicable rule files, and deduplicates them by resolved path.

---

### 3.4. Deterministic Interception & Lifecycle Hooks Spectrum

```
                       ┌─────────────────────────┐
                       │   Agent Execution Loop  │
                       └────────────┬────────────┘
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
   [PreToolUse Hook]                                 [PostToolUse Hook]
   - Deterministic Gate (Block/Allow/Ask)            - Auto-lint / Auto-format
   - Argument Rewrite / Sanitization                 - Diagnostic Capture
   (Control Plane: Mechanism)                        (Control Plane: Mechanism)
```

*   **Lifecycle Hooks System**: **`Capability`**. Harness control-plane capability allowing external scripts to intercept, validate, mutate, or abort agent actions synchronously.
*   **Deterministic Safety Gate (`PreToolUse` / `PostToolUse` / `Stop`)**: **`Mechanism`**. Synchronous programmatic interceptors enforcing hard invariant policies before/after non-deterministic model tool calls.
*   **Hook Configuration (`hooks.json`)**: **`Resource / Artifact`**. Configuration manifest defining event types, regex tool matchers, command bindings, and timeouts.

---

### 3.5. Composite Packaging & Plugins Spectrum

*   **Plugin Management System**: **`Capability`**. Harness capability for modular packaging, versioning, enabling/disabling, and namespacing multi-component agent extensions.
*   **Plugin Bundle / Manifest (`plugins/<name>/plugin.json`)**: **`Resource / Artifact`**. Manifest declaring a coherent bundle containing skills, rules, hooks, and MCP configurations.
*   **Plugin Discovery & Cascading Loader**: **`Mechanism`**. Engine that scans `.agents/plugins/` and `plugins.json`, resolves precedence, and instantiates bundled sub-resources.

---

### 3.6. Model Abstraction, Gateways & Dynamic Routers

```
                           ┌───────────────────────────┐
                           │   Model Gateway & Router  │ (Capability)
                           └─────────────┬─────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
     [Unified API Proxy]                             [Dynamic Model Routing]
     - OpenAI/Anthropic/Gemini Schema                - Flash vs. Pro tier cascading
     - Fallback / Load Balancing                     - Complexity classifier
     (Mechanism / Runtime: LiteLLM, Portkey)         (Mechanism: RouteLLM, OpenRouter)
```

*   **Model Gateway & API Translation**: **`Capability`**. Harness capability providing provider-agnostic LLM interfacing, automatic retries, fallback handling, and telemetry.
*   **Unified Multi-Provider Proxy (LiteLLM, Portkey)**: **`Tool / Product / Framework`**. Middleware runtime translating generic OpenAI-format requests to provider-specific endpoints.
*   **Dynamic Model Routing & Cost Cascading**: **`Capability`**. Strategy for routing prompts to low-cost vs. high-capability models based on task complexity and budget thresholds.
*   **Model Router Engine (RouteLLM, OpenRouter)**: **`Tool / Product / Mechanism`**. Concrete routing implementations using classifier models or matrix weights to optimize cost/quality tradeoffs.

---

### 3.7. Execution Plane vs. Control Plane Semantic Matrix

To maintain rigorous separation between non-deterministic model operations and deterministic governance:

| Semantic Plane | Component Candidate | Primary Operator | Determinism | Failure Recovery | Primary Artifact / Standard |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Control Plane** | **Lifecycle Hooks** | Harness Runtime / Shell Script | **100% Deterministic** | Hard stop / Deny / Force continuations | `hooks.json` |
| **Control Plane** | **Rules & Scoping** | Directory Walker Engine | **Deterministic Loading** | Path deduplication / Priority cascade | `AGENTS.md`, `skills.json` |
| **Control Plane** | **Model Gateway & Router**| Routing Matrix / Classifier | **Deterministic / Hybrid** | Failover / Exponential backoff | LiteLLM config, RouteLLM |
| **Execution Plane**| **Skills System** | LLM Selection + Agent Engine | **Non-Deterministic Invocation**| Re-prompting / Self-correction | `SKILL.md` |
| **Execution Plane**| **MCP Tool Calling** | LLM Tool Use / JSON-RPC | **Non-Deterministic Dispatch** | Exception returned to context | MCP Tool JSON Schema |
| **Execution Plane**| **Model Tool Calling** | Foundation Model Core | **Probabilistic Schema Gen** | Harness schema validation retry | OpenAI Tool Call Spec |

---

## 4. Lifecycle Role & Preliminary Tiering Matrix (P1-24)

### Lifecycle Stages Defined:
*   **`build-time`**: Configuration authoring, packaging, linting, manifest registration, static hierarchy parsing.
*   **`run-time`**: Dynamic discovery, progressive loading, model invocation, JSON-RPC tool dispatch, real-time safety gating.
*   **`review-time`**: Execution transcript logging, audit trails, token attribution, post-run verification.

### Preliminary Tiers Defined:
*   **`Foundational` (P0)**: Non-negotiable architectural bedrock required for baseline agent operation and safety.
*   **`Important` (P1)**: Production-grade capability essential for enterprise reliability, cost containment, and extensibility.
*   **`Specialized` (P2)**: High-value domain capability required for complex multi-system or regulated workflows.
*   **`Situational` (P3)**: Optional convenience, experimental pattern, or edge-case integration.

---

## 5. Success Criteria (SC) Wiring Rationale

Every Batch 3 candidate is mapped to the core Success Criteria:

```
                     ┌──────────────────────────────────────────────┐
                     │          CORE SUCCESS CRITERIA               │
                     └──────┬────────────────────┬───────────┬──────┘
                            │                    │           │
             ┌──────────────┘                    │           └──────────────┐
             ▼                                   ▼                          ▼
      [ SC-02: TSR ]                      [ SC-05: COST ]             [ SC-07: SECURITY ]
  (Task Success Rate)                   (Token / API Budget)        (Sandboxing & Safety)
  - Procedural runbooks (Skills)        - Progressive disclosure    - Deterministic PreToolUse
  - External tools (MCP)                - Model routing (Flash/Pro) - Stdio sandbox permissions
  - Retries & fallbacks                 - Rule deduplication        - Argument sanitization
```

1.  **`SC-02 TSR (Task Success Rate)`**:
    *   *Skills*: Provides verified procedural checklists, reducing multi-step drift and execution hallucination.
    *   *MCP*: Grants access to real-time external data/systems (DBs, issue trackers, internal APIs).
    *   *Model Gateways*: Eliminates rate-limit/downtime failures via automated provider failovers.
2.  **`SC-05 Cost & Token Budgeting`**:
    *   *Progressive Disclosure*: Preserves context window by withholding runbook bodies until explicitly needed.
    *   *Model Routing*: Shifts 60–80% of lightweight classification/formatting turns from expensive frontier models to fast/low-cost models.
    *   *Rule Deduplication*: Prevents redundant injection of parent directory guidelines.
3.  **`SC-07 Security & Sandboxing`**:
    *   *Lifecycle Hooks*: Hard-blocks destructive commands (e.g., `rm -rf`, credential leaks, unauthorized git pushes) deterministically before execution.
    *   *MCP Scoping*: Restricts remote server access via transport-level permission overrides and environment isolation.

---

## 6. Redundancy & Boundary Analysis with Batch 1 (E1–E11) and Batch 2 (B1–B10)

To ensure the harness architecture remains clean and orthogonal, Batch 3 candidates are rigorously checked against existing capabilities from Batch 1 (Execution & Tools) and Batch 2 (Context, Memory & Reasoning):

```
┌───────────────────────────────────────┬───────────────────────────────────────┬────────────────────────────────────────┐
│ Batch 1 / Batch 2 Capability          │ Batch 3 Candidate                     │ Boundary Delineation & Non-Redundancy  │
├───────────────────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────┤
│ E1/E2: Native Tools (file/terminal)   │ MCP Tool Extensibility                │ Native tools are hardcoded in harness; │
│                                       │                                       │ MCP is an open external RPC bridge.    │
├───────────────────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────┤
│ E6: Subagent Orchestration            │ Plugins & Composite Bundles           │ E6 handles autonomous agent spawning;  │
│                                       │                                       │ Plugins handle static asset packaging. │
├───────────────────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────┤
│ B1/B9: Context & Prompt Assembly      │ Rules System (Hierarchical)           │ B1/B9 assemble static session prompts; │
│                                       │                                       │ Rules dynamically resolve directory    │
│                                       │                                       │ context via filesystem traversal.      │
├───────────────────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────┤
│ B1: Context Window Budgeting          │ Skills Progressive Disclosure         │ B1 manages global truncation/sliding;  │
│                                       │                                       │ Skills manages on-demand runbook fetch │
├───────────────────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────┤
│ B4: Static Model Configuration        │ Model Gateway & Dynamic Router        │ B4 binds a fixed model name; Gateway   │
│                                       │                                       │ dynamically routes, falls back, & load │
│                                       │                                       │ balances across heterogeneous APIs.    │
├───────────────────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────┤
│ B7: Reactive Wakeup / Event Loop      │ Lifecycle Hooks Engine                │ B7 wakes agent on async messages;      │
│                                       │                                       │ Hooks intercept synchronously to block │
│                                       │                                       │ or mutate actions (control plane).     │
└───────────────────────────────────────┴───────────────────────────────────────┴────────────────────────────────────────┘
```

---

## 7. Master Taxonomy Slice Rows (Consolidated Master Table)

Below is the verified, converged master taxonomy table covering every candidate in Phase 1 Batch 3:

| Candidate Identifier & Name | Re-tagged Architectural Level | Lifecycle Role | Preliminary Tier | Primary SC Wiring | Redundancy Status vs. Batch 1/2 | Definitive Architectural Specification & Role in Harness |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B3-01: Model Context Protocol (MCP)** | **Protocol / Standard** | `run-time` | **Foundational** | **SC-02 TSR** | Non-redundant (External tool standard vs. E1-E5 native tools) | Open standard specification (JSON-RPC 2.0) defining client-server contracts for exposing tools, resources, and prompt templates. |
| **B3-02: MCP Client Subsystem** | **Framework / Runtime** | `run-time` | **Foundational** | **SC-02 TSR**, **SC-07 Security** | Interfaces with E1-E11 tool executor | Harness runtime middleware responsible for server lifecycle, capability negotiation, tool registration, and RPC dispatching. |
| **B3-03: MCP Server Runtime (Stdio / SSE)** | **Framework / Runtime** | `run-time` | **Important** | **SC-02 TSR**, **SC-07 Security** | Non-redundant (External processes managed outside core harness) | Isolated daemon process running locally (via `stdio`) or remotely (via `SSE`/HTTP) exposing domain capabilities. |
| **B3-04: MCP Registry & Catalogs** | **Tool / Product / Repo** | `build-time` | **Specialized** | **SC-02 TSR** | Non-redundant (Catalog service) | Centralized or federated repositories for discovering, indexing, and downloading MCP server packages (e.g., `modelcontextprotocol/servers`). |
| **B3-05: MCP Primitives (Tools, Resources, Prompts, Sampling)** | **Protocol / Standard (Primitives)** | `run-time` | **Important** | **SC-02 TSR**, **SC-05 Cost** | Refines B9 Prompt & E1-E5 Tool schemas | Core protocol data structures representing callable functions (`Tools`), read-only contextual data (`Resources`), and templates (`Prompts`). |
| **B3-06: Skills Capability** | **Capability** | `run-time` | **Foundational** | **SC-02 TSR**, **SC-05 Cost** | Non-redundant (Procedural workflow retrieval vs. B9 static context) | The capability of the agent harness to selectively load and follow structured procedural runbooks. |
| **B3-07: Individual Skill Resource** | **Resource / Artifact** | `build-time`, `run-time` | **Foundational** | **SC-02 TSR** | Non-redundant (Specific runbook artifact vs. generic documentation) | Modular filesystem package rooted at `SKILL.md` with YAML frontmatter (`name`, `description`) and optional `scripts/` and `references/`. |
| **B3-08: GitHub Skills Repositories / Packs** | **Implementation / Repo** | `build-time` | **Situational** | **SC-02 TSR** | Non-redundant (External package repositories) | Versioned Git repositories containing collections of domain skills for team or public consumption. |
| **B3-09: Progressive Disclosure Mechanism** | **Mechanism** | `run-time` | **Foundational** | **SC-05 Cost**, **SC-02 TSR** | Optimizes B1 context budgeting | Two-stage loading mechanism: injects metadata into system prompt; loads full skill body only upon model activation. |
| **B3-10: Rules Enforcement Capability** | **Capability** | `run-time` | **Foundational** | **SC-07 Security**, **SC-02 TSR** | Complements B9 system prompt assembly | The capability to discover and apply directory-scoped constraints, conventions, and boundary rules to agent operations. |
| **B3-11: Directory & Project Rules** | **Resource / Artifact** | `build-time`, `run-time` | **Foundational** | **SC-07 Security**, **SC-02 TSR** | Non-redundant (Ambient contextual rules vs. procedural skills) | Markdown files (`GEMINI.md`, `AGENTS.md`) placed in workspace paths declaring mandatory standards for that tree. |
| **B3-12: Rule Deduplication & Hierarchical Inheritance** | **Mechanism** | `run-time` | **Important** | **SC-05 Cost**, **SC-07 Security** | Non-redundant (Filesystem traversal logic) | CWD-to-root traversal algorithm that aggregates applicable rules, resolves conflicts, and deduplicates identical paths. |
| **B3-13: Lifecycle Hooks Capability** | **Capability** | `run-time` | **Foundational** | **SC-07 Security**, **SC-02 TSR** | Control plane counterpart to E2/B7 execution | Harness capability to execute external synchronous scripts at defined agent lifecycle events to inspect or mutate state. |
| **B3-14: Deterministic Policy Gates (`PreToolUse` / `PostToolUse`)** | **Mechanism** | `run-time` | **Foundational** | **SC-07 Security** | Wraps E1-E11 tool execution with hard deterministic checks | Synchronous interceptors returning `allow`, `deny`, `ask`, or argument mutations (`overwrite`) before execution proceeds. |
| **B3-15: Hook Configuration Manifest** | **Resource / Artifact** | `build-time`, `run-time` | **Foundational** | **SC-07 Security** | Non-redundant (Configuration schema) | JSON configuration file (`hooks.json`) defining matchers, shell command handlers, and execution timeouts. |
| **B3-16: Plugins Packaging Capability** | **Capability** | `build-time`, `run-time` | **Important** | **SC-02 TSR**, **SC-07 Security** | Complements E6 multi-agent packaging | Capability to encapsulate, distribute, namespace, and toggle multi-component customizations as a unified package. |
| **B3-17: Plugin Manifest & Bundle** | **Resource / Artifact** | `build-time` | **Important** | **SC-02 TSR** | Non-redundant (Distribution package artifact) | Directory package rooted at `plugin.json` containing bundled skills, rules, hooks, and MCP server configurations. |
| **B3-18: Model Gateway & Translation** | **Capability** | `run-time` | **Foundational** | **SC-02 TSR**, **SC-05 Cost** | Upgrades B4 static model provider bindings | Harness capability providing provider-agnostic LLM interfacing, schema translation, failover, and retry management. |
| **B3-19: Multi-Provider Proxy (LiteLLM / Portkey)** | **Tool / Product / Framework** | `run-time` | **Important** | **SC-02 TSR**, **SC-05 Cost** | Middleware sitting between harness and foundation models | Open-source or hosted proxy service standardizing 100+ LLM APIs into OpenAI-compatible format with built-in resilience. |
| **B3-20: Dynamic Model Routing Capability** | **Capability** | `run-time` | **Important** | **SC-05 Cost**, **SC-02 TSR** | Non-redundant (Dynamic model tier selection) | Capability to dynamically route individual turns to cost-effective or high-reasoning models based on prompt complexity. |
| **B3-21: Model Router Engines (RouteLLM / OpenRouter)** | **Tool / Product / Mechanism** | `run-time` | **Specialized** | **SC-05 Cost** | Implementation of B3-20 routing capability | Classifier-based matrix engines routing requests between lightweight (e.g., Flash) and heavyweight (e.g., Pro) LLMs. |
| **B3-22: Function Calling vs. Tool Use Schemas** | **Protocol / Standard** | `run-time` | **Foundational** | **SC-02 TSR** | Low-level protocol powering E1-E11 tool invocations | Structured JSON Schema specifications defining model input arguments and response formatting for tool execution. |
| **B3-23: Execution Plane vs. Control Plane Architecture** | **Architectural Pattern** | `build-time`, `run-time` | **Foundational** | **SC-07 Security**, **SC-02 TSR** | Foundational architectural boundary separating harness layers | Structural separation between non-deterministic LLM-driven actions (Execution) and deterministic harness policy/safety gating (Control). |
| **B3-24: Governance Scoping & Cascade Hierarchy** | **Mechanism / Pattern** | `run-time` | **Important** | **SC-07 Security**, **SC-05 Cost** | Governs loading order across B3-06, B3-10, B3-13, B3-16 | Resolution priority cascade: Workspace Project > Declared JSON Configs (`skills.json`/`plugins.json`) > Global Config > Built-ins. |

---

## 8. Architectural Recommendations & Verifier Verdict

1.  **Strict Ontological Delineation**:
    *   Treat **Skills** as a capability and `SKILL.md` as a resource. Never conflate an external GitHub repository of skills with the harness skill execution engine.
    *   Maintain the boundary between **Hooks** (deterministic control-plane gates) and **Tools** (non-deterministic execution-plane operations).
2.  **Safety & Cost Hardening**:
    *   Mandate `PreToolUse` hook enforcement for all destructive tools (`run_command`, remote mutations) to satisfy **`SC-07 Security`**.
    *   Enforce **Progressive Disclosure** across all skill and rule discovery mechanisms to preserve context budgets (**`SC-05 Cost`**).
3.  **Model Interoperability**:
    *   Decouple harness core from specific model SDKs by routing model invocations through a **Model Gateway** abstraction, enabling dynamic cost-tier cascading (Flash vs. Pro) and automatic outage failover.

---

## 9. References & Sources

*   [Model Context Protocol (MCP) Specification (Anthropic, 2024)](https://modelcontextprotocol.io/introduction)
*   [Antigravity Customization Architecture & Skills Guide (Google, 2025)](file:///home/shashank_karamudi/.gemini/antigravity-cli/builtin/skills/agy-customizations/SKILL.md)
*   [Antigravity Lifecycle Hooks Specification](file:///home/shashank_karamudi/.gemini/antigravity-cli/builtin/skills/agy-customizations/docs/hooks.md)
*   [Antigravity Plugins & Packaging Specification](file:///home/shashank_karamudi/.gemini/antigravity-cli/builtin/skills/agy-customizations/docs/plugins.md)
*   [Antigravity MCP Integration Guide](file:///home/shashank_karamudi/.gemini/antigravity-cli/builtin/skills/agy-customizations/docs/mcp_servers.md)
*   [LiteLLM Multi-Provider Proxy Architecture](https://docs.litellm.ai/)
*   [RouteLLM: Learning to Route LLMs for Cost-Quality Tradeoffs (Ong et al., LMSYS, 2024)](https://github.com/lm-sys/RouteLLM)
*   [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)
