# Independent Validation Report: Spec vs Code Gap

**Target Specification:** [`HARNESS_SLICE.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/harness-slice/HARNESS_SLICE.md)  
**Evaluated Target:** [`.harness/`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/) and Repository Root Files  
**Audit Scope:** 12 Canonical Spec Subsystems, Materialization Depth, Behavioral Divergence, Coherent Runnability.

---

## Executive Verdict

> **VERDICT: SUBSTANTIALLY MATERIALIZED & FUNCTIONAL CONFIGURATION HARNESS (8/12 Fully Materialized, 2 Partially Materialized, 2 Missing at Root)**
> 
> The `.harness/` tree has progressed from an early conceptual skeleton into a **structured, syntactically valid, and partially executable harness-as-code package**. Core security gates (`pre_tool_guard.py`, `gate.sh`), hook manifests (`hooks.json`), agent personas, and full MCP server topologies are now physically present on disk. 
> 
> However, **the harness is not yet a standalone, auto-bootstrapping runtime engine**. It operates as a *declarative governance and interceptor substrate* that requires an external driver agent (such as Antigravity, Claude Code, or LangGraph) to load its manifests and orchestrate tool dispatches.

---

## 1. Subsystem Coverage Table

| # | Spec Subsystem | Grounding Path in Spec | Materialized `.harness/` Artifact | Status | Operational State |
| :-: | :--- | :--- | :--- | :---: | :---: |
| **1** | **Agent Archetypes** | `HARNESS_SLICE.md §1` | [`.harness/agents/`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/) (`planner.md`, `explorer.md`, `coder.md`, `reviewer.md`) | ✅ **Materialized** | **Operational** (Structured prompts & tool permissions) |
| **2** | **Procedural Skills Catalog** | `HARNESS_SLICE.md §6` | [`.harness/skills/`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/skills/) (`index.json` + 5 concrete skills) | ⚠️ **Partial** | **Operational** (5 ready; 35 catalog stubs) |
| **3** | **Lifecycle Hooks & Interceptors** | `HARNESS_SLICE.md §4.1-4.3` | [`.harness/hooks/`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/hooks/) (`hooks.json`, `pre_tool_guard.py`, `post_tool_linter.py`) | ✅ **Materialized** | **Operational** (Executable Python & exit codes) |
| **4** | **Tool Interoperability (MCP Hub)** | `HARNESS_SLICE.md §3` | [`.harness/mcp/mcp_servers.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/mcp/mcp_servers.json) (7 S-Tier servers) | ✅ **Materialized** | **Operational** (Valid JSON Schema contract) |
| **5** | **Permissions & Policy Engine** | `HARNESS_SLICE.md §5` | [`.harness/permissions/`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/permissions/) (`policies.cedar`, `presets.json`) | ✅ **Materialized** | **Declarative** (Valid Cedar & Presets JSON) |
| **6** | **Deterministic Workflows** | `HARNESS_SLICE.md §1` | [`.harness/workflows/`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/) (4 YAML DAG blueprints) | ✅ **Materialized** | **Operational** (Executable DAG specifications) |
| **7** | **Model Gateway & Cost Caps** | `HARNESS_SLICE.md §7.1` | [`.harness/telemetry/litellm-config.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/telemetry/litellm-config.yaml) | ✅ **Materialized** | **Operational** (Directly consumable by LiteLLM) |
| **8** | **Telemetry & Tracing** | `HARNESS_SLICE.md §7.2` | [`.harness/telemetry/langfuse-config.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/telemetry/langfuse-config.json) | ✅ **Materialized** | **Operational** (Consumable by Langfuse SDK) |
| **9** | **OS Sandbox Boundary** | `HARNESS_SLICE.md §7.3` | [`.harness/sandbox/gate.sh`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/sandbox/gate.sh) | ✅ **Materialized** | **Operational** (Bwrap/Docker namespace isolation) |
| **10** | **Master Harness Manifest** | `HARNESS_SLICE.md §7.3` | [`.harness/harness.config.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/harness.config.yaml) | ✅ **Materialized** | **Operational** (Unified single-source config) |
| **11** | **Ambient Rules Manifest** | `HARNESS_SLICE.md §2` | Root [`AGENTS.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/AGENTS.md) vs Spec Manifest | ⚠️ **Diverged** | **Non-Operational** (Root file is a batch log) |
| **12** | **Host Bridges & Git Gate** | `HARNESS_SLICE.md §4.4` | `lefthook.yml`, `Taskfile.yml`, `.gemini/`, `CLAUDE.md` | ❌ **Missing** | **Non-Operational** (Files missing at repo root) |

---

## 2. Materialization vs Stub Breakdown

### Materialized Subsystems (8 / 12)
1. **Agent Archetypes (`.harness/agents/`)**: All 4 subagent files ([`planner.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/planner.md), [`explorer.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/explorer.md), [`coder.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/coder.md), [`reviewer.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/reviewer.md)) contain complete YAML frontmatter (tools, model, permission tier) and markdown system prompts with Mermaid flowcharts.
2. **Lifecycle Hooks (`.harness/hooks/`)**: [`hooks.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/hooks/hooks.json) maps tool calls to [`pre_tool_guard.py`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/hooks/pre_tool_guard.py) and [`post_tool_linter.py`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/hooks/post_tool_linter.py). Tested and verified: exits with code `2` on `rm -rf /` and exit `0` on benign commands.
3. **MCP Tool Configuration (`.harness/mcp/`)**: [`mcp_servers.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/mcp/mcp_servers.json) contains all 7 S-tier server definitions (`filesystem`, `git`, `context7_docs`, `postgres_readonly`, `playwright_browser`, `memory_graph`, `fetch_safe`).
4. **Permissions Engine (`.harness/permissions/`)**: [`policies.cedar`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/permissions/policies.cedar) formalizes Class 0–3 side-effect boundaries and path blacklists. [`presets.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/permissions/presets.json) defines tool allowlists and HITL triggers for archetypes C1–C6.
5. **Deterministic Workflows (`.harness/workflows/`)**: [`test-and-verify.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/test-and-verify.yaml), [`migration-safeguard.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/migration-safeguard.yaml), [`build-verify.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/build-verify.yaml), and [`refactor-safely.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/refactor-safely.yaml) provide concrete DAG definitions.
6. **Model Gateway (`.harness/telemetry/litellm-config.yaml`)**: Features model fallback hierarchies (Claude 3.7 Sonnet $\to$ Gemini 2.5 Pro $\to$ DeepSeek R1 Local) and hard spend caps ($5/session, $50/day).
7. **Telemetry Tracking (`.harness/telemetry/langfuse-config.json`)**: Configured with flush intervals and archetype session tags.
8. **OS Sandbox Execution Gate (`.harness/sandbox/gate.sh`)**: Implements 202 lines of Bash isolation detecting `bwrap` or `docker`, enforcing read-only root mounts, unsharing namespaces, and mounting empty `tmpfs` over sensitive credentials (`~/.ssh`, `~/.aws`).
9. **Master Configuration (`.harness/harness.config.yaml`)**: Consolidates agents, tools, sandbox, MCPs, permissions, budgets, and hooks into a unified 182-line specification.

### Partially Materialized / Diverged Subsystems (2 / 12)
1. **Procedural Skills Catalog (`.harness/skills/`)**:
   - [`index.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/skills/index.json) indexes all 40 skills.
   - **5 concrete skills** are fully written: `01-repo-surveyor-map` (with working [`survey_repo.py`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/skills/01-repo-surveyor-map/scripts/survey_repo.py)), `07-api-contract-first`, `08-database-schema-architect`, `21-tdd-red-green-refactor`, and `31-owasp-top10-vuln-scanner`.
   - **35 skills remain catalog-only stubs** without physical `SKILL.md` files on disk.
2. **Ambient Rules Manifest (`AGENTS.md`)**:
   - Spec defined `AGENTS.md` as the core agent contract (5 ambient rules, side-effect classes).
   - The actual root [`AGENTS.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/AGENTS.md) is currently used as an *agent execution registry tracking solo-levelling batch workflows*. The ambient contract is only stored inside [`HARNESS_SLICE.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/harness-slice/HARNESS_SLICE.md) and [`harness.config.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/harness.config.yaml).

### Missing Subsystems (2 / 12)
1. **Git Security & Task Automation**: `lefthook.yml` and `Taskfile.yml` are specified in the directory tree but not created at the project root.
2. **Host / IDE Bridge Symlinks**: `.gemini/` symlinks (`hooks.json`, `mcp_config.json`) and `CLAUDE.md` do not exist at root.

---

## 3. Remaining Divergences & Architectural Nuances

1. **Root `AGENTS.md` Collision**:
   The workspace root `AGENTS.md` is tracking research agents (`wf_c917d118`, `R-A`, `V-C`). To avoid collision, the ambient harness rules must either be prepended to `AGENTS.md` or loaded via `.harness/harness.config.yaml`.
2. **Progressive Disclosure "Ghost Skills"**:
   35 of the 40 skills in `skills/index.json` lack physical files. If an agent attempts progressive disclosure (`view_file` on `skills/16-fastapi-async/SKILL.md`), it will receive a file-not-found error.
3. **Cedar ABAC Enforcement**:
   [`policies.cedar`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/permissions/policies.cedar) is written, but there is no Cedar CLI binary or in-process WASM evaluator currently wired into `pre_tool_guard.py`—the guard currently enforces safety via regular expressions and path boundaries.

---

## 4. Is the Harness Genuinely Runnable as a Coherent Unit?

### Assessment
* **As a Configuration & Governance Substrate for an AI Agent:** **YES.**  
  An agent running Claude Code, Antigravity, or Gemini CLI can immediately ingest `.harness/harness.config.yaml`, discover all subagent personas, bind the 7 MCP servers from `mcp_servers.json`, execute pre/post tool hooks via `hooks.json`, route bash commands through `sandbox/gate.sh`, and load the 5 primary skills.
* **As an Autonomous Standalone Daemon:** **NO (by design).**  
  The harness is an *as-code harness skeleton*, not a compiled standalone server. It does not spawn its own background daemon process; rather, host agents execute its scripts and read its declarative schemas.

---

## 5. Remaining Gaps & Action Items

1. **Deploy Root Manifests**: Materialize `lefthook.yml`, `Taskfile.yml`, and symlink `.gemini/hooks.json` $\to$ `.harness/hooks/hooks.json`.
2. **Reconcile Root Manifest**: Merge the ambient behavioral contract (`HARNESS_SLICE.md §2`) into the top of root [`AGENTS.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/AGENTS.md).
3. **Progressive Skill Stubs**: Populate the remaining 35 skill directories with minimal template `SKILL.md` runbooks to ensure 100% path resolution.
4. **Wire Cedar into Guard**: Connect `pre_tool_guard.py` to a lightweight Cedar policy evaluator or schema validator to complete formal Class 0–3 policy enforcement.
