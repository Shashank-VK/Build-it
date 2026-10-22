# Phase 2 — Group C: Layer 3 (Integration & Extensibility) Ranking Report

> **Document Status:** CONVERGED & RANKED — Task `P2-08 / P2-09`  
> **Evaluation Rubric:** [`phase-2/RUBRIC.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-2/RUBRIC.md) (7 Dimensions, 1–5 Scale, Harm 4–5 Veto Rule)  
> **Input Taxonomies:** [`phase-1/MASTER_TAXONOMY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/MASTER_TAXONOMY.md) (§1, CAP-17..23) · [`phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md)  
> **Grounding:** Archetypes **C1–C6** & Success Criteria **SC-01..10** ([`phase-0/ARCHETYPES_AND_CRITERIA.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-0/ARCHETYPES_AND_CRITERIA.md))  
> **Ranked Artifact Saved:** [`phase-2/rankings/G3_INTEGRATION.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-2/rankings/G3_INTEGRATION.md)

---

## 0. Executive Summary & Veto Governance

This ranking evaluates the **7 Canonical Capabilities of Layer 3 (Integration & Extensibility)** under the 7-dimension Phase 2 Rubric. 

### The Harm 4–5 Veto Class Trigger:
Under the **Harm 4–5 Veto Rule** (`phase-2/RUBRIC.md` §2), any element with $\text{Harm-if-absent} \ge 4$ that directly protects **SC-07 (Security & 0-Leak)**, **SC-03 (MTTR Auto-Recovery)**, or **SC-08 (Artifact Health Gate)** cannot rank below median, regardless of baseline frequency:
1. **CAP-20 (Lifecycle Interception & Hooks):** **Harm = 5 (Catastrophic)**. Non-bypassable control plane primitive. Prompt steering alone cannot guarantee blocking of destructive commands (`rm -rf`, DB drop) or prevent raw credential leakage. **Triggers Harm 5 Veto $\rightarrow$ Rank 1 (Top S-Tier)**.
2. **CAP-22 (Model Gateway & Provider Abstraction):** **Harm = 4 (Major)**. Shields the harness against upstream vendor 429 rate limits, breaking API changes, and provider downtime via automated failover and retry chains. **Triggers Harm 4 Veto $\rightarrow$ Rank 2 (S-Tier)**.
3. **CAP-17 (Open Tool Interoperability — MCP):** **Harm = 4 (Major)**. Eliminates $M \times N$ custom integration fragmentation; connects agents to databases, browsers, and enterprise APIs. **Triggers Harm 4 Veto $\rightarrow$ Rank 3 (S-Tier)**.

---

## 1. Group C Master Ranked Table (CAP-17 .. CAP-23)

| Rank | ID | Capability Name | Freq (1-5) | Harm (1-5) | Ben (1-5) | Cmplx (1-5) | Maint (1-5) | Sec (1-5) | Gen (1-5) | Global Tier | Primary SC Wiring | Core Architectural Driver |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **1** | **CAP-20** | **Lifecycle Interception & Hooks** | 5 | 5 | 5 | 3 | 4 | 5 | 5 | **S** | SC-07, SC-03, SC-08 | Deterministic control-plane interceptor (`PreToolUse`, `PostToolUse`, `Stop`). |
| **2** | **CAP-22** | **Model Gateway & Provider Abstraction** | 5 | 4 | 5 | 4 | 4 | 3 | 5 | **S** | SC-02, SC-03, SC-05 | Universal provider-agnostic proxy, retry engine, & load balancer. |
| **3** | **CAP-17** | **Open Tool Interoperability (MCP)** | 5 | 4 | 5 | 3 | 4 | 2 | 5 | **S** | SC-02, SC-07, SC-05 | Standardized JSON-RPC client-server external tool/resource protocol. |
| **4** | **CAP-19** | **Ambient Rules Enforcement** | 5 | 3 | 4 | 4 | 3 | 4 | 5 | **S** | SC-02, SC-07, SC-08 | Path-scoped hierarchical directory constraint discovery & injection. |
| **5** | **CAP-18** | **Procedural Skills Execution** | 4 | 3 | 4 | 4 | 3 | 3 | 5 | **S** | SC-01, SC-02, SC-05 | On-demand procedural runbook loading via progressive disclosure. |
| **6** | **CAP-23** | **Dynamic Model Routing & Selection** | 4 | 2 | 4 | 3 | 3 | 3 | 4 | **A** | SC-05, SC-01, SC-02 | Cost-quality Pareto optimization via learned turn dispatch. |
| **7** | **CAP-21** | **Composite Plugin Packaging** | 3 | 2 | 4 | 3 | 3 | 2 | 4 | **A** | SC-01, SC-02, SC-07 | Multi-component distribution bundle (skills + rules + hooks + MCP). |

---

## 2. Archetype-Dependent Ranking Matrix (C1–C6)

In accordance with the **Anti-Averaging Principle** (`phase-0/ARCHETYPES_AND_CRITERIA.md` §3), capabilities are evaluated per archetype:

* **C1:** Product Engineering (0→1 → Scale)
* **C2:** Data, Analytics & MLOps Fabric
* **C3:** Automation & Browser Surface Ops
* **C4:** Agentic & Knowledge Synthesis Systems
* **C5:** Platform, Infra & DevOps (IaC)
* **C6:** Migration, Modernization & Strangler Rebuild

| ID | Capability Name | Global | C1 (Product) | C2 (Data/ML) | C3 (Browser/RPA) | C4 (Agent/Synthesis) | C5 (Platform/IaC) | C6 (Migration) | Bottleneck (p10) |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CAP-20** | **Lifecycle Interception & Hooks** | **S** | **S** | **S** | **S** | **S** | **S** | **S** | **S (Universal Veto)** |
| **CAP-22** | **Model Gateway & Provider Abstraction** | **S** | **S** | **S** | **S** | **S** | **S** | **S** | **S (Universal Bedrock)** |
| **CAP-17** | **Open Tool Interoperability (MCP)** | **S** | **S** | **S** | **S** | **S** | **S** | **S** | **S (Universal Bedrock)** |
| **CAP-19** | **Ambient Rules Enforcement** | **S** | **S** | **A** | **A** | **S** | **S** | **S** | **A (C2/C3)** |
| **CAP-18** | **Procedural Skills Execution** | **S** | **A** | **A** | **B** | **S** | **A** | **S** | **B (C3 Automation)** |
| **CAP-23** | **Dynamic Model Routing & Selection** | **A** | **A** | **S** | **A** | **S** | **B** | **A** | **B (C5 Platform)** |
| **CAP-21** | **Composite Plugin Packaging** | **A** | **A** | **A** | **B** | **A** | **A** | **B** | **B (C3/C6)** |

---

## 3. Individual Capability Scorecards & Batch-3 Grounding

### 1. CAP-20: Lifecycle Interception & Hooks
* **Scorecard:**
  * **Frequency:** `5` (Fires on every tool call, turn prompt, and session state transition).
  * **Harm if Absent:** `5` (**Catastrophic — Veto Class**; no deterministic mechanism to prevent destructive commands or data leaks).
  * **Benefit:** `5` (100% deterministic safety gating, argument mutation, and auto-formatting/linting).
  * **Complexity Cost (Inverse):** `3` (Requires subprocess IPC, JSON streaming, and timeout watchdogs).
  * **Maintenance Burden (Inverse):** `4` (POSIX script interfaces cleanly isolate hook code from prompts).
  * **Security/Risk Impact:** `5` (Strongest risk mitigation primitive; blocks unauthorized commands before OS execution).
  * **General Applicability:** `5` (Essential across all 6 archetypes).
* **Tiering:** **Global S** | `C1=S, C2=S, C3=S, C4=S, C5=S, C6=S`
* **SC Wiring:**
  * **SC-07 (SSHC — Security Conformance):** Hard-blocks unsandboxed egress and credential leakage before dispatch.
  * **SC-08 (AHG — Artifact Health Gate):** Enforces test and lint passes via `Stop` hooks before agent completion.
  * **SC-03 (MTTR-Step):** `PostToolUse` auto-formatters (Prettier/Ruff) immediately repair minor syntax errors.
* **Batch-3 Evidence:** B3-13, B3-14, B3-15, B3-23; Claude Code `.claude/settings.json` hook runner, Antigravity `hooks.json` engine (`PreToolUse`, `PostToolUse`, `Stop`).

---

### 2. CAP-22: Model Gateway & Provider Abstraction
* **Scorecard:**
  * **Frequency:** `5` (Traversed on 100% of LLM queries, subagent forks, and background evaluations).
  * **Harm if Absent:** `4` (**Major — Veto Class**; vendor outages, rate limits, and API schema shifts break the harness).
  * **Benefit:** `5` (Standardized OpenAI-compatible interface across 100+ models, automated retries, and fallback failover).
  * **Complexity Cost (Inverse):** `4` (Transparent proxy architecture cleanly decouples harness from provider SDKs).
  * **Maintenance Burden (Inverse):** `4` (Community proxy engines like LiteLLM absorb breaking vendor updates).
  * **Security/Risk Impact:** `3` (Centralizes credential isolation and enables egress DLP stream redaction).
  * **General Applicability:** `5` (Universal across all 6 archetypes).
* **Tiering:** **Global S** | `C1=S, C2=S, C3=S, C4=S, C5=S, C6=S`
* **SC Wiring:**
  * **SC-02 (TSR):** Prevents task abortion caused by transient 5xx provider outages or 429 rate limits.
  * **SC-03 (MTTR-Step):** Sub-second retry/failover chains mask upstream provider degradation.
  * **SC-05 (CPSR):** Standardized ledgering tracks token consumption and price parity across models.
* **Batch-3 Evidence:** B3-18, B3-19; LiteLLM, Portkey.ai, and OpenRouter architectures; V-D §3.6 provider abstraction layer.

---

### 3. CAP-17: Open Tool Interoperability (MCP Subsystem)
* **Scorecard:**
  * **Frequency:** `5` (Continuous tool execution for filesystem, databases, browsers, and external APIs).
  * **Harm if Absent:** `4` (**Major — Veto Class**; locks agents into bespoke silos; prevents access to external SaaS/DBs).
  * **Benefit:** `5` (Replaces $M \times N$ glue with JSON-RPC standard; grants instant access to 3,400+ servers).
  * **Complexity Cost (Inverse):** `3` (Requires managing child process lifecycles, JSON-RPC 2.0 framing, and SSE transports).
  * **Maintenance Burden (Inverse):** `4` (JSON-Schema contracts isolate tool implementations from the harness).
  * **Security/Risk Impact:** `2` (Spawning subprocesses and remote SSE servers expands the attack surface; requires roots gating).
  * **General Applicability:** `5` (Universal across all 6 archetypes).
* **Tiering:** **Global S** | `C1=S, C2=S, C3=S, C4=S, C5=S, C6=S`
* **SC Wiring:**
  * **SC-02 (TSR):** Directly powers task completion by connecting agents to external databases, issue trackers, and build tools.
  * **SC-07 (SSHC):** Stdio process boundaries and roots capability restrict filesystem traversal.
  * **SC-05 (CPSR):** Dynamic resource fetching replaces massive static prompt stuffing.
* **Batch-3 Evidence:** B3-01, B3-02, B3-05; Anthropic Model Context Protocol specification, Smithery/Glama registries, V-C Translation Matrix.

---

### 4. CAP-19: Ambient Rules Enforcement
* **Scorecard:**
  * **Frequency:** `5` (Discovered and applied on every single conversation turn).
  * **Harm if Absent:** `3` (Leads to syntax/architectural drift, ignored conventions, broken test patterns, and rework).
  * **Benefit:** `4` (Aligns generated code with repo-specific idioms, style guidelines, and test conventions automatically).
  * **Complexity Cost (Inverse):** `4` (Simple markdown file discovery format: `AGENTS.md`, `.cursorrules`, `.claude/rules/*.md`).
  * **Maintenance Burden (Inverse):** `3` (Rules accumulate and risk staleness/conflicts without anti-bloat pruning).
  * **Security/Risk Impact:** `4` (Defines directory-level security boundaries, though dependent on model adherence).
  * **General Applicability:** `5` (Universal across all 6 archetypes).
* **Tiering:** **Global S** | `C1=S, C2=A, C3=A, C4=S, C5=S, C6=S`
* **SC Wiring:**
  * **SC-02 (TSR):** Prevents structural errors and framework violations.
  * **SC-08 (AHG):** Significantly increases first-pass linter, typecheck, and formatting pass rates.
  * **SC-05 (CPSR):** Hierarchical rule deduplication (MEC-03) prevents context bloat from repeating parent rules.
* **Batch-3 Evidence:** B3-10, B3-11, B3-12; `awesome-cursorrules` (40k+ stars), cursor.directory, V-D §3.3 deduplication walk.

---

### 5. CAP-18: Procedural Skills Execution
* **Scorecard:**
  * **Frequency:** `4` (Activated on-demand for multi-step domain workflows and runbooks).
  * **Harm if Absent:** `3` (Complex workflows must be manually re-prompted; models drift during multi-step execution).
  * **Benefit:** `4` (**Progressive Disclosure — MEC-02** saves 85%+ startup context tokens; provides step-by-step checklists).
  * **Complexity Cost (Inverse):** `4` (Clean schema: `SKILL.md` + YAML frontmatter + `scripts/` + `references/`).
  * **Maintenance Burden (Inverse):** `3` (Runbooks require periodic updates as external tool CLIs evolve).
  * **Security/Risk Impact:** `3` (Executable scripts run with host permissions; requires supply-chain verification CAP-31).
  * **General Applicability:** `5` (Universal across all 6 archetypes for multi-step recipes).
* **Tiering:** **Global S** *(Master Taxonomy Foundational Core)* | `C1=A, C2=A, C3=B, C4=S, C5=A, C6=S`
* **SC Wiring:**
  * **SC-01 (TTFUA):** Runbooks guide agents directly toward working preview artifacts without trial-and-error.
  * **SC-02 (TSR):** Step-by-step procedures eliminate omitted steps and hallucinated workflows.
  * **SC-05 (CPSR):** Metadata-only startup injection protects context budgets against prompt bloating.
* **Batch-3 Evidence:** B3-06, B3-07, B3-09; Antigravity SKILL standard, OpenAI/Claude subagent runbooks, V-D §3.2 level-hygiene.

---

### 6. CAP-23: Dynamic Model Routing & Tier Selection
* **Scorecard:**
  * **Frequency:** `4` (Evaluated on every turn/subagent dispatch in multi-model harnesses).
  * **Harm if Absent:** `2` (Static model pinning works reliably, but incurs severe token cost and latency penalties).
  * **Benefit:** `4` (Achieves 85–95% of frontier reasoning performance at **50–75% lower inference cost** via fast/cheap utility models).
  * **Complexity Cost (Inverse):** `3` (Requires prompt complexity classifier, matrix routing models, or threshold calibration).
  * **Maintenance Burden (Inverse):** `3` (Routing weights and preference classifiers must be retuned as new model generations release).
  * **Security/Risk Impact:** `3` (Neutral; requires fallback gates so security tasks are not routed to under-capable models).
  * **General Applicability:** `4` (High impact for token-heavy engineering in C1, C2, C4; lower for small one-off scripts).
* **Tiering:** **Global A** | `C1=A, C2=S, C3=A, C4=S, C5=B, C6=A`
* **SC Wiring:**
  * **SC-05 (CPSR):** Primary metric driver for achieving $< \$0.80$ (C1) and $< \$1.20$ (C4) cost targets.
  * **SC-01 (TTFUA):** Fast-tier utility models provide sub-second time-to-first-token on initial setup.
  * **SC-02 (TSR):** Preserves high-reasoning context for complex architectural synthesis.
* **Batch-3 Evidence:** B3-20, B3-21; LMSYS RouteLLM benchmark data, OpenRouter Auto routing metrics, V-D §3.6 Pareto frontier.

---

### 7. CAP-21: Composite Plugin Packaging & Distribution
* **Scorecard:**
  * **Frequency:** `3` (Evaluated during workspace bootstrap, extension install, or configuration load).
  * **Harm if Absent:** `2` (Subcomponents can still be configured manually as loose files; causes config friction, not execution failure).
  * **Benefit:** `4` (Bundles skills, rules, hooks, and MCP configs into a single versioned manifest `plugin.json` for 1-click sharing).
  * **Complexity Cost (Inverse):** `3` (Requires manifest validator, namespace isolation, and dependency resolution).
  * **Maintenance Burden (Inverse):** `3` (Bundled packages require synchronized versioning across internal subcomponents).
  * **Security/Risk Impact:** `2` (Bundled third-party packages expand supply-chain risk vectors, requiring manifest scanning).
  * **General Applicability:** `4` (Valuable for team/enterprise setups; less critical for solo developer sandboxes).
* **Tiering:** **Global A** | `C1=A, C2=A, C3=B, C4=A, C5=A, C6=B`
* **SC Wiring:**
  * **SC-01 (TTFUA):** 1-click capability bootstrapping accelerates project initialization.
  * **SC-02 (TSR):** Guarantees all matching rules, skills, and MCP servers required for a stack are present together.
  * **SC-07 (SSHC):** Manifest declarations enable upfront permission scoping and security auditability.
* **Batch-3 Evidence:** B3-16, B3-17, B3-24; Continue Hub / VS Code extension bundles, Antigravity `plugins/<name>/plugin.json` spec.

---

## 4. Phase 2 Gate Sign-Off & Next Steps

* **Group C Allocation Summary:**
  * **S-Tier (Foundational):** `CAP-20`, `CAP-22`, `CAP-17`, `CAP-19`, `CAP-18`
  * **A-Tier (Important):** `CAP-23`, `CAP-21`
* **Artifact Verified:** Written and synchronized to [`phase-2/rankings/G3_INTEGRATION.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-2/rankings/G3_INTEGRATION.md).
* **Phase 2 Status:** Group C is fully grounded and ready for integration into the Master Synthesis [`RANKINGS.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-2/RANKINGS.md) and Phase 3 Tool Selection.
iminates prompt trial-and-error, driving agents directly toward valid preview artifacts.
  - **SC-02 (TSR):** Step-by-step checklists eliminate omitted migrations, missed tests, or broken contracts.
  - **SC-05 (CPSR):** Metadata-only startup injection protects context budgets against prompt bloating.
- **Evidence & Grounding from Batch 3:**
  - `BATCH-3_INTEGRATION_EXTENSIBILITY.md` (B3-06, B3-07, B3-09).
  - Antigravity SKILL standard and OpenAI/Claude subagent prompt runbooks.
  - V-C §2 and V-D §3.2 level-hygiene enforcement (Skill Capability vs `SKILL.md` Resource vs GitHub Pack).

---

```
================================================================================
RANK 6: CAP-23 — Dynamic Model Routing & Tier Selection
================================================================================
```

### Scorecard
- **Frequency:** `4` — Evaluated on every turn or subagent spawn in tiered multi-model harnesses.
- **Harm if Absent:** `2` — Static model pinning works reliably, but incurs severe financial waste and latency penalties on simple utility tasks.
- **Benefit:** `4` — Achieves 85–95% of frontier reasoning performance at **50–75% lower inference cost** by routing lightweight tasks (formatting, syntax checks, basic summarization) to fast/cheap models (Flash/Haiku) and reserving frontier models (Pro/Opus) for deep logic.
- **Complexity Cost (Inverse):** `3` — Requires intent classification, matrix routing models, or threshold calibration; potential misclassification risk on ambiguous queries.
- **Maintenance Burden (Inverse):** `3` — Routing weights and preference classifiers must be retuned as new model generations release.
- **Security/Risk Impact:** `3` — Neutral; requires guardrail fallback to ensure security-critical tasks are never routed to under-capable models.
- **General Applicability:** `4` — Highly impactful for token-heavy engineering (C1, C2, C4); less critical for small low-volume spikes.

### Tier Summary
- **Global Tier:** **A (Important)**
- **Per-Archetype Tiers:** `C1=A, C2=S, C3=A, C4=S, C5=B, C6=A`
- **Primary SC Wiring:**
  - **SC-05 (CPSR — Cost per Run):** Primary architectural lever for achieving $< \$0.80$ (C1) and $< \$1.20$ (C4) cost targets.
  - **SC-01 (TTFUA):** Fast-tier utility models provide sub-second time-to-first-token on initial setup.
  - **SC-02 (TSR):** Preserves high-reasoning context for complex architectural synthesis.
- **Evidence & Grounding from Batch 3:**
  - `BATCH-3_INTEGRATION_EXTENSIBILITY.md` (B3-20, B3-21).
  - LMSYS RouteLLM benchmark data and OpenRouter Auto routing metrics.
  - V-D §3.6 routing Pareto frontier analysis.

---

```
================================================================================
RANK 7: CAP-21 — Composite Plugin Packaging & Distribution
================================================================================
```

### Scorecard
- **Frequency:** `3` — Evaluated during workspace initialization, plugin installation, or environment bootstrapping.
- **Harm if Absent:** `2` — Subcomponents (skills, rules, hooks, MCP configs) can still be manually installed as loose files; creates configuration friction and discoverability loss, but not execution failure.
- **Benefit:** `4` — Bundles heterogeneous extension primitives into a single versioned, namespaced manifest (`plugin.json`); enables 1-click team sharing and atomic capability toggling.
- **Complexity Cost (Inverse):** `3` — Requires manifest schema validation, namespace collision resolution, and dependency graph loading.
- **Maintenance Burden (Inverse):** `3` — Composite bundles require synchronized versioning across internal skills, rules, and hook scripts.
- **Security/Risk Impact:** `2` — Bundled third-party packages increase supply-chain risk vectors, necessitating static manifest scanning (CAP-31).
- **General Applicability:** `4` — Highly valuable for enterprise and team environments; less critical for individual solo developer sandboxes.

### Tier Summary
- **Global Tier:** **A (Important)**
- **Per-Archetype Tiers:** `C1=A, C2=A, C3=B, C4=A, C5=A, C6=B`
- **Primary SC Wiring:**
  - **SC-01 (TTFUA):** Instant capability bootstrapping accelerates project initialization.
  - **SC-02 (TSR):** Guarantees that all matching rules, skills, and MCP servers required for a tech stack are present together.
  - **SC-07 (SSHC):** Manifest declarations enable upfront permission scoping and security auditability.
- **Evidence & Grounding from Batch 3:**
  - `BATCH-3_INTEGRATION_EXTENSIBILITY.md` (B3-16, B3-17, B3-24).
  - VS Code/Continue Hub plugin bundles, Antigravity `plugins/<name>/plugin.json` specification.
  - V-D §3.5 level hygiene separating plugin management capabilities from static bundle manifests.

---

## 4. Cross-Element Interactions & Tension Pre-Scan (P2-15)

The Group C capabilities interact in ways that create critical architectural synergies and trade-offs:

```
                      ┌─────────────────────────────────┐
                      │    CAP-21 Composite Plugins     │ (Bundles all 4)
                      └─┬─────────────┬─────────────┬───┘
                        │             │             │
        ┌───────────────┘             │             └───────────────┐
        ▼                             ▼                             ▼
┌──────────────┐              ┌──────────────┐              ┌──────────────┐
│ CAP-17: MCP  │              │ CAP-18: Skill│              │ CAP-19: Rules│
│ (Tool Layer) │              │ (Runbooks)   │              │ (Ambient)    │
└───────┬──────┘              └───────┬──────┘              └───────┬──────┘
        │                             │                             │
        └──────────────────────┬──────┴─────────────────────────────┘
                               ▼
                ┌──────────────────────────────┐
                │ CAP-20: Lifecycle Hooks Gate │ (Deterministic Control Plane)
                └──────────────┬───────────────┘
                               ▼
                ┌──────────────────────────────┐
                │ CAP-22: Model Gateway        │ (Transport & Retry)
                └──────────────┬───────────────┘
                               ▼
                ┌──────────────────────────────┐
                │ CAP-23: Dynamic Router       │ (Cost/Quality Pareto)
                └──────────────────────────────┘
```

1. **Deterministic Control Plane (CAP-20) vs. Non-Deterministic Tools (CAP-17):**
   - *Tension:* Adding MCP servers expands the tool space and attack surface.
   - *Resolution:* CAP-20 `PreToolUse` hooks deterministically intercept all `tools/call` JSON-RPC payloads before execution, enforcing CapBAC permission allowlists and sanitizing arguments.
2. **Context Budgeting (CAP-18 / CAP-19) vs. Token Bloat:**
   - *Tension:* Stacking ambient rules and extensive runbooks exhausts the LLM context window.
   - *Resolution:* CAP-18 utilizes **Progressive Disclosure** (injecting only name and description at startup), while CAP-19 uses **Hierarchical Deduplication** to load only rules relevant to the active directory tree.
3. **Model Gateways (CAP-22) vs. Dynamic Routing (CAP-23):**
   - *Synergy:* CAP-22 provides the physical connection, retry mechanism, and translation across 100+ LLMs; CAP-23 sits on top of CAP-22 as the intelligent policy brain deciding which specific model tier receives each turn.

---

## 5. Phase 2 Gate Recommendations & Sign-Off

### Summary of Tier Allocations:
- **Foundational (S-Tier):**
  - **CAP-20:** Lifecycle Interception & Hooks (Rank 1 — Harm 5 Veto)
  - **CAP-22:** Model Gateway & Provider Abstraction (Rank 2 — Harm 4 Veto)
  - **CAP-17:** Open Tool Interoperability [MCP] (Rank 3 — Harm 4 Veto)
  - **CAP-19:** Ambient Rules Enforcement (Rank 4 — Foundational Core)
  - **CAP-18:** Procedural Skills Execution (Rank 5 — Foundational Core)
- **Important (A-Tier):**
  - **CAP-23:** Dynamic Model Routing & Tier Selection (Rank 6 — Pareto Optimizer)
  - **CAP-21:** Composite Plugin Packaging & Distribution (Rank 7 — Modular Bundler)

### Gate P2-Group-C Verdict:
**PASS (Approved for Tool Selection in Phase 3).**  
All 7 capabilities in Group C are rigorously grounded in Batch 3 evidence, mapped across Archetypes C1–C6, and wired to measurable Phase 0 Success Criteria. Proceed to Phase 3 tool selection and concrete implementation mapping.
