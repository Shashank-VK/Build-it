# Phase 2 — Mechanism & Protocol Verification Report

> **Verifier Role:** Phase 2 Mechanism/Protocol Verifier for the AI Development Harness  
> **Source Baseline:** `phase-1/MASTER_TAXONOMY.md` (Converged Master Synthesis D-1)  
> **Evaluation Scope:** 10 Mechanisms (`MEC-01` through `MEC-10`) and 3 Core Protocols (`PROT-01` through `PROT-03`) *(with companion verification of `PROT-04`)*  
> **Downstream Target:** Phase 3 — Concrete Tool Selection, Evaluation Rubric & Integration

---

## 1. Executive Verification Summary

This verification audit confirms the strict **Level-Hygiene Enforcement** established in Phase 1:
- **Capabilities (`CAP`)** define *what* functional, safety, or cognitive requirement the harness must achieve (abstract contracts).
- **Mechanisms (`MEC`)** define *how* a specific capability is mechanically executed via algorithms, filesystem primitives, process controls, or data pipelines.
- **Protocols & Standards (`PROT`)** define the *wire contracts, schemas, and specifications* governing inter-component communication, configuration, and data exchange.

All 10 Mechanisms and 3 Core Protocols have been verified against their parent Capabilities, validated for level purity (zero capability conflation), and grounded in active production tools and open-source ecosystems.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               MECHANISM & PROTOCOL VERIFICATION MAP                              │
├────────────────────────────┬─────────────────────────────┬───────────────────────────────────────┤
│ Level                      │ Identifiers                 │ Status / Gate Verdict                 │
├────────────────────────────┼─────────────────────────────┼───────────────────────────────────────┤
│ Mechanisms (MEC)           │ MEC-01 through MEC-10 (10)  │ 10/10 PASS — Fully Grounded in OSS/CLI│
│ Protocols & Standards (PROT│ PROT-01 through PROT-03 (3) │ 3/3 PASS — Open Standard Compliance  │
└────────────────────────────┴─────────────────────────────┴───────────────────────────────────────┘
```

---

## 2. Master Verification Matrix

| ID | Canonical Name | Confirmed Level | Serves CAP | Concrete Tools, Repositories & Implementations | Verification Verdict |
|---|---|---|---|---|---|
| **MEC-01** | **Git Worktree Isolation Primitive** | **Mechanism** (Filesystem isolation pattern) | [CAP-06](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L65) (Isolated Workspace Management) | `git` core CLI (`git worktree add/prune/remove`), `libgit2`, `pygit2`, Gemini CLI workspace share/branch, Claude Code subagent worktrees | **VERIFIED (PASS)** |
| **MEC-02** | **Progressive Disclosure Mechanism** | **Mechanism** (Two-stage context loading pipeline) | [CAP-18](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L77) (Procedural Skills Execution), [CAP-16](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L75) | Claude Code Skills Loader, Gemini CLI Skill Manager (`builtin/skills/*/SKILL.md`), Semantic Kernel Plugins, `python-frontmatter` | **VERIFIED (PASS)** |
| **MEC-03** | **Hierarchical Rule Inheritance & Dedup** | **Mechanism** (Directory tree resolution algorithm) | [CAP-19](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L78) (Ambient Rules Enforcement) | Cursor `.cursorrules` resolver, Claude Code `CLAUDE.md` hierarchy, Gemini CLI `AGENTS.md` / `rules/` parser, `EditorConfig` core parser | **VERIFIED (PASS)** |
| **MEC-04** | **Deterministic Hook Event System** | **Mechanism** (Synchronous lifecycle interception) | [CAP-20](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L79) (Lifecycle Interception & Hooks), [CAP-25](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L84) | Claude Code `hooks.json` engine, LangGraph RunTree callbacks (`on_tool_start`/`on_tool_end`), Git hooks architecture, `lefthook` | **VERIFIED (PASS)** |
| **MEC-05** | **Tripartite State Reversibility Engine** | **Mechanism** (Tri-domain rollback engine) | [CAP-30](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L89) (State Reversibility), [CAP-06](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L65), [CAP-03](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L62) | Git snapshots/revert, Temporal.io Saga framework (`temporalio/sdk-python`), LangGraph State Checkpointers (`SqliteSaver`), ZFS/btrfs CoW | **VERIFIED (PASS)** |
| **MEC-06** | **JIT Ephemeral Credential Brokering** | **Mechanism** (Subprocess injection & token minting) | [CAP-26](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L85) (Zero-Trust Secret Governance), [CAP-25](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L84) | HashiCorp Vault Dynamic Secrets, 1Password CLI (`op run`), Infisical CLI (`infisical run`), AWS STS / IAM Roles Anywhere, Doppler | **VERIFIED (PASS)** |
| **MEC-07** | **DLP Stream Sanitizer & Secret Redactor** | **Mechanism** (In-line I/O token redaction filter) | [CAP-26](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L85) (Zero-Trust Secret Governance), [CAP-27](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L86) | TruffleHog CLI (`trufflesecurity/trufflehog`), Gitleaks (`gitleaks/gitleaks`), Microsoft Presidio (`microsoft/presidio`), `secretlint` | **VERIFIED (PASS)** |
| **MEC-08** | **Cryptographic Flight Recorder (WAL)** | **Mechanism** (Append-only write-ahead log daemon) | [CAP-28](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L87) (Execution Provenance & Non-Repudiation) | Local JSONL WAL daemon (`transcript.jsonl`), SQLite WAL engine, OpenTelemetry JSON File Exporter, Sigstore Cosign / in-toto | **VERIFIED (PASS)** |
| **MEC-09** | **Real-Time Budget Hard-Stop Circuit Breaker** | **Mechanism** (Process-level execution cutoff guard) | [CAP-35](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L94) (Cost & Complexity Budgets), [CAP-16](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L75) | LiteLLM Spend Budget Manager (`litellm.max_budget`), Portkey AI Gateway Budgets, Langfuse Budget Guards, PyBreaker | **VERIFIED (PASS)** |
| **MEC-10** | **Instinct Mining & Pattern Distillation** | **Mechanism** (Offline trajectory distillation pipeline) | [CAP-34](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L93) (Autonomous Self-Improvement), [CAP-14](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L73) | DSPy Optimizers (`MIPROv2`, `BootstrapFewShot`), TextGrad (`zou-group/textgrad`), Letta/MemGPT Distiller, LangSmith Auto-Prompt | **VERIFIED (PASS)** |
| **PROT-01** | **Model Context Protocol (MCP) Standard** | **Protocol / Standard** (JSON-RPC 2.0 tool/resource contract) | [CAP-17](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L76) (Open Tool Interoperability) | MCP Specification (`modelcontextprotocol/specification`), TypeScript/Python SDKs, `modelcontextprotocol/servers`, Claude/Gemini clients | **VERIFIED (PASS)** |
| **PROT-02** | **Function Calling / Tool-Use Schema Standard** | **Protocol / Standard** (JSON-Schema tool definition spec) | [CAP-17](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L76) (Open Tool Interoperability), [CAP-22](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L81) | JSON Schema Draft 2020-12 / Draft 7, OpenAI Function Calling Spec, Anthropic Tool Spec, Gemini FunctionDeclaration, Pydantic, Zod | **VERIFIED (PASS)** |
| **PROT-03** | **Harness-as-Code (HaC) Specification** | **Protocol / Standard** (Declarative configuration schema) | [CAP-37](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L96) (AHG Gate), [CAP-21](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L80), [CAP-25](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L84) | JSON/YAML Schema for `harness.yaml`, Open Policy Agent (OPA/Rego) schemas, Devcontainer Spec, Claude/Gemini CLI manifests (`AGENTS.md`) | **VERIFIED (PASS)** |

---

## 3. Deep-Dive Verification Records

### MEC-01: Git Worktree Isolation Primitive
- **Confirmed Level:** **Mechanism** (Implementation Primitive).  
  *Level Hygiene Rationale:* It is not a broad capability ("isolated execution"); it is the concrete OS/VCS filesystem mechanism that executes `git worktree add <dir> <branch>` to provide parallel working directories sharing a single `.git` object store.
- **Serves Capability:** [CAP-06: Isolated Workspace Management](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L65). Supports [CAP-01](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L60) (Subagents), [CAP-07](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L66) (Fan-Out), and [CAP-30](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L89) (Reversibility).
- **Concrete Tools & Repositories:**
  - `git` core CLI (`git worktree add`, `git worktree prune`, `git worktree list`) — [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)
  - `libgit2` / `pygit2` / `nodegit` native bindings for programmatic worktree provisioning
  - Gemini CLI & Antigravity runtime workspace engine (`Workspace: branch | share`)
  - Claude Code subagent branch worktree manager (`.claude/worktrees/*`)
  - Aider worktree branching mode (`--git-worktree`)
- **Phase 3 Feeder Output:** Select `git worktree` CLI wrapper + `pygit2`/`libgit2` lifecycle hooks for subagent filesystem management.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-02: Progressive Disclosure Mechanism
- **Confirmed Level:** **Mechanism** (Context & Prompt Loading Pattern).  
  *Level Hygiene Rationale:* Progressive Disclosure is an operational two-stage loading pipeline (metadata injection at initialization $\rightarrow$ lazy retrieval of full runbook instructions and scripts upon invocation), distinct from the capability of executing skills.
- **Serves Capability:** [CAP-18: Procedural Skills Execution](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L77). Cooperates with [CAP-16: Context Budget Governance](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L75) and [CAP-08: Working Memory Management](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L67).
- **Concrete Tools & Repositories:**
  - Google Antigravity & Gemini CLI Skill Loader (`builtin/skills/*/SKILL.md` parser with on-demand `view_file` activation)
  - Anthropic Claude Code Skills Loader (`.claude/skills/*/SKILL.md`)
  - Semantic Kernel Plugin Manager (`microsoft/semantic-kernel` - lazy function registration)
  - Frontmatter parser libraries: `python-frontmatter`, `gray-matter` (Node.js)
  - LangChain `DynamicStructuredTool` on-demand schema hydrator
- **Phase 3 Feeder Output:** Select standard Markdown + YAML frontmatter parser (`python-frontmatter`) with a two-tier registry (index table vs body injector).
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-03: Hierarchical Rule Inheritance & Dedup
- **Confirmed Level:** **Mechanism** (Algorithmic Path Traversal & Config Merge).  
  *Level Hygiene Rationale:* It is the deterministic traversal algorithm that crawls from repository root to current working directory, parses nested rules files, calculates specificity weights, and deduplicates conflicting constraints.
- **Serves Capability:** [CAP-19: Ambient Rules Enforcement](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L78). Cooperates with [CAP-16: Context & Token Budget Governance](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L75).
- **Concrete Tools & Repositories:**
  - Cursor `.cursorrules` / `.cursor/rules/*.mdc` hierarchical inheritance engine
  - Claude Code `CLAUDE.md` root-and-leaf traversal resolver
  - Gemini CLI / Antigravity rule engine (`AGENTS.md`, `.gemini/rules/`)
  - `EditorConfig` core parser reference model (`editorconfig/editorconfig-core-c`, `editorconfig-py`)
  - `cosmiconfig` / `editorconfig-core-js` path-walking configuration loaders
- **Phase 3 Feeder Output:** Implement root-to-leaf AST-based rule collector with MD5/SHA256 content-hash deduplication.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-04: Deterministic Hook Event System
- **Confirmed Level:** **Mechanism** (Synchronous Execution Interception Control Plane).  
  *Level Hygiene Rationale:* It is an event-bus dispatcher triggering pre- and post-operation scripts (`PreToolUse`, `PostToolUse`, `SessionStart`, `SubagentStop`), completely decoupled from LLM prompt steering.
- **Serves Capability:** [CAP-20: Lifecycle Interception & Hooks](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L79). Cooperates with [CAP-25: Authorization & Least-Privilege](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L84) and [CAP-28: Execution Provenance](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L87).
- **Concrete Tools & Repositories:**
  - Claude Code Hooks Runtime (`hooks.json` executing sandboxed bash/python validators with exit-code 0/1/2 semantics)
  - Git Hooks infrastructure (`pre-commit`, `post-commit`) via `lefthook` (`evilmartians/lefthook`) or `husky`
  - LangChain / LangGraph Callback System (`BaseCallbackHandler`, `on_tool_start`, `on_tool_end`)
  - LlamaIndex `EventDispatcher` instrumentation middleware
- **Phase 3 Feeder Output:** Adopt JSON-configured shell/Python hook runner with strict timeout bounds (≤500ms) and non-zero exit blocking.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-05: Tripartite State Reversibility Engine
- **Confirmed Level:** **Mechanism** (Composite Tri-Layer Rollback Engine).  
  *Level Hygiene Rationale:* It defines the concrete technical orchestration of rolling back three distinct state stores: (1) Filesystem snapshots, (2) Conversation context rewinds, and (3) Compensating inverse transactions (Sagas) for external side effects.
- **Serves Capability:** [CAP-30: Side-Effect Containment & State Reversibility](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L89). Cooperates with [CAP-06](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L65) (Workspaces) and [CAP-03](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L62) (Orchestration).
- **Concrete Tools & Repositories:**
  - *Filesystem Rollback:* Git CLI (`git stash`, `git reset --hard`, `git clean -fd`), Linux Btrfs/ZFS CoW snapshot CLIs
  - *Context Rewind:* LangGraph Checkpointers (`langgraph.checkpoint.sqlite.SqliteSaver`, `PostgresSaver`), Antigravity conversation branch rewind
  - *Compensating Sagas:* Temporal.io Saga Pattern (`temporalio/sdk-python`, `temporalio/sdk-typescript`), AWS Step Functions Saga definitions, Cadence
- **Phase 3 Feeder Output:** Combine Git working-tree stashing (Filesystem) + LangGraph SQLite checkpoint rewind (Context) + explicit `revert()` tool definitions (Sagas).
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-06: JIT Ephemeral Credential Brokering
- **Confirmed Level:** **Mechanism** (Process Isolation & Secret Injection Primitive).  
  *Level Hygiene Rationale:* It is the technical mechanism that requests temporary credentials and injects them as ephemeral environment variables or standard input into isolated tool subprocesses, preventing secrets from entering LLM context or disk logs.
- **Serves Capability:** [CAP-26: Zero-Trust Secret Governance](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L85). Cooperates with [CAP-24: Hermetic Isolated Execution Boundary](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L83) and [CAP-25](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L84).
- **Concrete Tools & Repositories:**
  - HashiCorp Vault Dynamic Secrets & CLI (`hashicorp/vault`)
  - 1Password CLI (`op run -- <command>`, `1password/op-js`)
  - Infisical CLI (`infisical run -- <command>`, `infisical/infisical`)
  - AWS STS (`AssumeRole` ephemeral session credentials)
  - Doppler CLI (`doppler run -- <command>`)
- **Phase 3 Feeder Output:** Select lightweight CLI secret wrapper (`op run` / `infisical run` / AWS STS token broker) for tool runner middleware.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-07: DLP Stream Sanitizer & Secret Redactor
- **Confirmed Level:** **Mechanism** (In-Line Stream Redaction Filter).  
  *Level Hygiene Rationale:* It is a high-speed text stream scanner operating on stdout/stderr, prompt generation buffers, and logging channels to detect and defang credentials using pattern matching and entropy analysis.
- **Serves Capability:** [CAP-26: Zero-Trust Secret Governance](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L85). Cooperates with [CAP-27: Indirect Prompt Injection Defense](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L86) and [CAP-28](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L87).
- **Concrete Tools & Repositories:**
  - TruffleHog OSS Streaming Engine (`trufflesecurity/trufflehog`)
  - Gitleaks (`gitleaks/gitleaks` — regex + entropy scanning)
  - Microsoft Presidio Analyzer & Anonymizer (`microsoft/presidio` for PII and credentials)
  - `secretlint` (`secretlint/secretlint` pluggable secret linter)
  - `whispers` (`Shopify/whispers`)
- **Phase 3 Feeder Output:** Select `gitleaks` / `trufflehog` embedded library or Rust-based regex stream filter placed as mandatory stdout/stderr wrapper before context insertion.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-08: Cryptographic Flight Recorder (WAL)
- **Confirmed Level:** **Mechanism** (Write-Ahead Append-Only Audit Logging Daemon).  
  *Level Hygiene Rationale:* It is the technical data-structure pattern that synchronously appends every state mutation, user instruction, and tool payload to a hash-chained JSON Lines (`JSONL`) file on disk *prior* to executing side effects.
- **Serves Capability:** [CAP-28: Execution Provenance & Non-Repudiation](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L87). Cooperates with [CAP-30](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L89) (Reversibility) and [CAP-37](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L96) (AHG Gate).
- **Concrete Tools & Repositories:**
  - Native JSONL Write-Ahead Loggers (`transcript.jsonl` & `transcript_full.jsonl` architecture)
  - SQLite WAL mode (`sqlite3` WAL journal)
  - OpenTelemetry JSON File Exporter (`open-telemetry/opentelemetry-collector-contrib`)
  - Sigstore Cosign / in-toto Cryptographic Attestation Metadata (`sigstore/cosign`, `in-toto/in-toto`)
  - `immudb` lightweight immutable ledger engine
- **Phase 3 Feeder Output:** Standardize on structured `transcript.jsonl` writer with SHA-256 parent-block hash chaining and pre-invocation disk `fsync()`.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-09: Real-Time Budget Hard-Stop Circuit Breaker
- **Confirmed Level:** **Mechanism** (Process-Level Safety Cutoff Primitive).  
  *Level Hygiene Rationale:* It is a synchronous runtime monitor tracking token spend, dollar cost, iteration depth, and hook latency against hard threshold caps, firing an uncatchable cancellation signal when breached.
- **Serves Capability:** [CAP-35: Cost & Complexity Budget Governance](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L94). Cooperates with [CAP-16](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L75) (Context Budget) and [CAP-03](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L62) (Orchestration).
- **Concrete Tools & Repositories:**
  - LiteLLM Spend Budget Manager (`litellm.budget_manager`, `max_budget` parameter)
  - Portkey AI Gateway Guardrails & Spend Budgets (`portkey-ai/gateway`)
  - Langfuse Real-Time Token Quota & Cost Guards (`langfuse/langfuse`)
  - `pybreaker` / Python Circuit Breaker pattern implementations
  - Go context cancellation (`context.WithTimeout`, `context.WithCancel`) / Node.js `AbortController`
- **Phase 3 Feeder Output:** Integrate LiteLLM / Portkey budget limits at the model gateway layer + local subprocess step counter in the runner loop.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### MEC-10: Instinct Mining & Pattern Distillation
- **Confirmed Level:** **Mechanism** (Offline Log Distillation Pipeline).  
  *Level Hygiene Rationale:* It is a specific data-processing and prompt-tuning algorithm that analyzes completed flight recorder trajectories (successful vs failed runs) to automatically extract prompt optimizations, rule patches, and heuristic guidelines.
- **Serves Capability:** [CAP-34: Autonomous Self-Improvement & Adaptation](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L93). Cooperates with [CAP-14: Experiential Memory Recall](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L73) and [CAP-19](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L78).
- **Concrete Tools & Repositories:**
  - DSPy Optimizers (`stanfordnlp/dspy` — `MIPROv2`, `BootstrapFewShotWithRandomSearch`, `GEval`)
  - TextGrad (`zou-group/textgrad` — automatic prompt gradient backpropagation via LLM feedback)
  - Letta / MemGPT Sleep-Pass Consolidator (`letta-ai/letta`)
  - LangSmith Prompt Auto-Optimization & Feedback Distillation pipelines
- **Phase 3 Feeder Output:** Select DSPy MIPROv2 + Letta episodic consolidation engine for offline prompt and rule adaptation.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### PROT-01: Model Context Protocol (MCP) Standard
- **Confirmed Level:** **Protocol / Standard** (Universal Tool & Context Interoperability Specification).  
  *Level Hygiene Rationale:* It is a formal open standard specifying client-server JSON-RPC 2.0 message schemas, transport bindings (stdio, SSE), and lifecycle negotiation states for external tools, resources, and prompts.
- **Serves Capability:** [CAP-17: Open Tool Interoperability](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L76). Cooperates with [CAP-18](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L77) (Skills) and [CAP-25](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L84) (Least-Privilege).
- **Concrete Tools & Repositories:**
  - MCP Official Specification: [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) (`modelcontextprotocol/specification`)
  - Official SDKs: `modelcontextprotocol/typescript-sdk`, `modelcontextprotocol/python-sdk`, `modelcontextprotocol/kotlin-sdk`
  - Reference Tool Implementations: `modelcontextprotocol/servers` (Filesystem, PostgreSQL, Git, Fetch, SQLite, Memory, GitHub)
  - Production Harness Clients: Claude Desktop, Claude Code, Google Antigravity / Gemini CLI, Cursor, Windsurf, Zed Editor
- **Phase 3 Feeder Output:** Adopt official Python & TypeScript MCP SDKs; mandate MCP compliant tool interfaces for all external tool servers.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### PROT-02: Function Calling / Tool-Use Schema Standard
- **Confirmed Level:** **Protocol / Standard** (Data Serialization & Schema Specification).  
  *Level Hygiene Rationale:* It is the universal JSON-Schema contract standardizing parameter typing, descriptions, required fields, and validation contracts for LLM tool invocation across foundation model providers.
- **Serves Capability:** [CAP-17: Open Tool Interoperability](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L76) and [CAP-22: Model Gateway & Provider Abstraction](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L81). Cooperates with [CAP-03](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L62) (Orchestration).
- **Concrete Tools & Repositories:**
  - JSON Schema Specification Draft 2020-12 / Draft 7 (`json-schema.org`, `json-schema/json-schema`)
  - OpenAI Function Calling / Tool Call JSON Spec
  - Anthropic Tool Use Specification (`input_schema` format)
  - Google Gemini `FunctionDeclaration` / `Tool` specification in Google GenAI SDK
  - Pydantic (`pydantic/pydantic` - Python schema generator) & Zod (`colinhacks/zod` - TypeScript schema validator)
- **Phase 3 Feeder Output:** Use Pydantic v2 / Zod to dynamically generate provider-compliant function schemas validated against JSON Schema Draft 2020-12.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### PROT-03: Harness-as-Code (HaC) Specification
- **Confirmed Level:** **Protocol / Standard** (Declarative Configuration Schema).  
  *Level Hygiene Rationale:* It is the formal schema specification defining how agent roles, tool permissions, security sandboxes, lifecycle hooks, and model routing parameters are codified into declarative, version-controlled repository manifests.
- **Serves Capability:** [CAP-37: Autonomous Harness Governance (AHG) Gate](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L96). Cooperates with [CAP-21: Composite Plugin Packaging](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L80) and [CAP-25: Least-Privilege Governance](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L84).
- **Concrete Tools & Repositories:**
  - Open Policy Agent (OPA) / Rego policy schemas (`open-policy-agent/opa`)
  - OpenTofu / HashiCorp Terraform configuration schema models (`opentofu/opentofu`)
  - Development Container Specification (`devcontainers/spec` at `containers.dev`)
  - Unified Harness Manifest Schemas (`harness.schema.json`, `AGENTS.md`, `SKILL.md`, `hooks.json`, `plugin.json`)
  - JSON Schema / Cue / YAML validation tools (`cue-lang/cue`, `ajv`)
- **Phase 3 Feeder Output:** Author official JSON Schema (`harness.schema.json`) validated by OPA policy checkers for deterministic CI verification.
- **Verification Verdict:** **VERIFIED (PASS)**

---

### Companion Verification Note: PROT-04 (Trust-Labeled Content Model)
- **Confirmed Level:** **Protocol / Standard** (Security Data Classification Schema).
- **Serves Capability:** [CAP-27: Indirect Prompt Injection Defense & Fencing](file:///home/shashank_karamudi/.gemini/antigravity-cli/brain/b49a466a-f8f0-47d6-8be0-6a3a79982deb/MASTER_TAXONOMY.md#L86).
- **Concrete Repositories & Implementations:** NeMo Guardrails Content Classifiers (`NVIDIA/NeMo-Guardrails`), Microsoft PyRIT (`Azure/PyRIT`), LangChain Prompt Defenses.
- **Verification Verdict:** **VERIFIED (PASS)** — Provides the foundational four-tier data trust model (`GOVERNANCE_INSTRUCTION`, `UNTRUSTED_REPO_DATA`, `UNTRUSTED_EXT_DATA`, `PROVIDER_OUTPUT`) enforcing prompt boundary integrity.

---

## 4. Architectural Traceability & Phase 3 Bridge

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                PHASE 3 TOOL SELECTION DIRECTORY                                  │
├─────────────────┬──────────────────────┬─────────────────────────────────────────────────────────┤
│ Element         │ Mechanistic Pattern  │ Recommended Phase 3 Tool Candidates                     │
├─────────────────┼──────────────────────┼─────────────────────────────────────────────────────────┤
│ **MEC-01**      │ FS Worktree Branch   │ `git` CLI 2.40+, `pygit2`, `.agents/<id>` manager       │
│ **MEC-02**      │ Lazy Skill Hydration │ `python-frontmatter`, `gray-matter`, Agy Skill Loader    │
│ **MEC-03**      │ Hierarchical Merge   │ `cosmiconfig`, `EditorConfig` parser, AST rule merger   │
│ **MEC-04**      │ Lifecycle Hook Event │ `lefthook` design pattern, JSON hook runner daemon      │
│ **MEC-05**      │ Tripartite Rollback  │ `temporalio/sdk-python` (Sagas) + LangGraph checkpoints │
│ **MEC-06**      │ JIT Secret Injector  │ `infisical run`, `1password/op`, AWS STS broker         │
│ **MEC-07**      │ Streaming DLP Filter │ `gitleaks` regex-stream, `microsoft/presidio`           │
│ **MEC-08**      │ JSONL WAL Daemon     │ `transcript.jsonl` writer with SHA-256 block hash sync  │
│ **MEC-09**      │ Spend Circuit Breaker│ `litellm` spend manager, `portkey-ai/gateway`           │
│ **MEC-10**      │ Heuristic Distiller  │ `stanfordnlp/dspy` (MIPROv2), `letta-ai/letta`          │
│ **PROT-01**     │ JSON-RPC 2.0 Tooling │ `modelcontextprotocol/python-sdk`, `modelcontextprotocol/servers` │
│ **PROT-02**     │ Function JSON Schema │ `pydantic` v2, `zod`, JSON Schema Draft 2020-12         │
│ **PROT-03**     │ Harness-as-Code Spec │ `open-policy-agent/opa`, `devcontainers/spec`, JSON Schema│
└─────────────────┴──────────────────────┴─────────────────────────────────────────────────────────┘
```

### Verification Sign-Off:
- **Level Hygiene:** 100% compliant. All elements strictly classified as mechanisms or protocol standards; no abstract capability conflations remain.
- **Traceability:** Every mechanism and protocol maps directly to its upstream Capability in `MASTER_TAXONOMY.md` and Phase 0 Success Criteria (`SC-01..10`).
- **Phase 3 Readiness:** All 13 elements are grounded in concrete, active open-source tools and repositories, providing an unambiguous blueprint for tool selection and evaluation.
