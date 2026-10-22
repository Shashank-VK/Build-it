# Phase 3.5 Materialization Sprint — Agent M-A Execution Report

> **Sprint Role:** Agent M-A (Materialization Specialist)  
> **Target Path:** [`/mnt/c/Users/Shashank Karamudi/Desktop/solo-levelling/the harness/.harness/`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/)  
> **Source Specification:** [`harness-slice/HARNESS_SLICE.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/harness-slice/HARNESS_SLICE.md)  
> **Status:** **COMPLETE**

---

## 1. Materialized Artifacts Summary

All requested doc-stubs have been materialized into concrete, executable configuration files and scripts on disk:

```
.harness/
├── agents/
│   ├── planner.md                      # High-reasoning state-machine orchestrator
│   ├── explorer.md                     # Class-0 read-only AST & codebase research subagent
│   ├── coder.md                        # Sandboxed TDD implementation subagent
│   └── reviewer.md                     # Multi-perspective staff code review & security audit
├── workflows/
│   └── blueprints/
│       ├── build-verify.yaml           # Multi-stage CI verification DAG (Lint -> Type -> Test -> Gate)
│       ├── refactor-safely.yaml        # Atomic refactoring with git worktree isolation & rollback
│       ├── test-and-verify.yaml        # TDD Red-Green test execution pipeline
│       └── migration-safeguard.yaml    # Zero-downtime DB forward/rollback migration safeguard
├── hooks/
│   ├── hooks.json                      # In-process PreToolUse & PostToolUse lifecycle manifest
│   ├── pre_tool_guard.py               # Destructive command & secret leakage interceptor
│   └── post_tool_linter.py             # Post-tool auto-formatter (Ruff/Prettier) & AST syntax validator
├── config/
│   └── harness.yaml                    # Master Harness-as-Code declarative config
├── permissions/
│   ├── policies.cedar                  # Formally verified Cedar ABAC rules
│   └── presets.json                    # Archetype capability presets (C1–C6)
└── telemetry/
    ├── litellm-config.yaml             # Model gateway routing, failovers & $5 hard budget caps
    └── langfuse-config.json            # Trace attribution & token ledger configuration
```

---

## 2. Component Breakdown

### (1) Subagent Archetypes (`.harness/agents/`)

Each agent definition includes structured YAML frontmatter (`name`, `description`, `tools`, `model`, `permission`) and an operational persona:

- [`agents/planner.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/planner.md):
  - **Frontmatter**: `model: inherit`, tools: `[read_file, list_dir, grep_search, find_by_name, view_file, ask_question, invoke_subagent, send_message, manage_subagents]`, permission: `Class-0 (Read-Only Orchestration)`.
  - **Operating Directives**: Decomposes user requests into finite state machine DAGs, conducts Socratic requirement clarification ([`grill-me-socratic-planner`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/skills/36-grill-me-planner/SKILL.md)), delegates implementation to `coder` in isolated worktrees, and coordinates verification gates.
- [`agents/explorer.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/explorer.md):
  - **Frontmatter**: `model: flash`, tools: `[read_file, list_dir, grep_search, find_by_name, view_file, read_url_content, search_web]`, permission: `Class-0 (Strict Read-Only)`.
  - **Operating Directives**: Rapid codebase topology mapping, symbol navigation, and call-hierarchy tracing. Returns compact symbol reference tables with markdown line links (`file:///path/to/file#L10-L45`) to prevent context bloat.
- [`agents/coder.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/coder.md):
  - **Frontmatter**: `model: inherit`, tools: `[read_file, list_dir, grep_search, find_by_name, view_file, write_to_file, replace_file_content, run_command]`, permission: `Class-1 & Class-2` within `./src`, `./tests`, `./docs`, `./scratch`.
  - **Operating Directives**: Enforces `rule-preserve-code-integrity` (never deletes docstrings or existing logic without cause), executes strict Red $\to$ Green $\to$ Refactor loops, and respects pre/post tool hooks.
- [`agents/reviewer.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/reviewer.md):
  - **Frontmatter**: `model: pro`, tools: `[read_file, list_dir, grep_search, find_by_name, view_file, run_command]`, permission: `Class-0 (Read-Only Verification)`.
  - **Operating Directives**: Audits diffs across 5 dimensions: Correctness, OWASP Top 10 vulnerabilities, Type hygiene (`mypy --strict`, `tsc --noEmit`), Test assertion rigor, and Anti-bloat.

---

### (2) Deterministic Workflow Blueprints (`.harness/workflows/blueprints/`)

- [`workflows/blueprints/build-verify.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/blueprints/build-verify.yaml):
  - **Stages**: `secret_scan` $\to$ `format_check` $\to$ `lint_static_analysis` $\to$ `type_check` $\to$ `unit_tests` $\to$ `artifact_health_gate`.
  - **Compensation**: Automatically triggers `git reset --hard HEAD` on pipeline abort to maintain trunk health.
- [`workflows/blueprints/refactor-safely.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/blueprints/refactor-safely.yaml):
  - **Stages**: `baseline_verification` $\to$ `isolate_worktree` $\to$ `ast_impact_analysis` $\to$ `apply_refactor_step` $\to$ `verify_regression` $\to$ `peer_review` $\to$ `merge_worktree`.
  - **Compensation**: Cleans up ephemeral worktrees (`.worktrees/refactor-sandbox`) and deletes scratch branches upon failure.
- [`workflows/blueprints/test-and-verify.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/blueprints/test-and-verify.yaml):
  - Enforces fast-fail unit and integration testing matrices (`pytest`, `vitest`).
- [`workflows/blueprints/migration-safeguard.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/blueprints/migration-safeguard.yaml):
  - Validates schema dry-runs, forward migrations, and rollback reversibility (`alembic downgrade -1`) on isolated DB instances.

---

### (3) Deterministic Lifecycle Interceptors (`.harness/hooks/`)

- [`hooks/hooks.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/hooks/hooks.json):
  - Wires `PreToolUse` (and `pre_tool_call`) on `run_command` and `write_to_file` to `pre_tool_guard.py`.
  - Wires `PostToolUse` (and `post_tool_call`) on `write_to_file` and `replace_file_content` to `post_tool_linter.py`.
- [`hooks/pre_tool_guard.py`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/hooks/pre_tool_guard.py):
  - **Empirical Protection**: Intercepts destructive shell commands (`rm -rf /`, `mkfs`, `dd`, fork bombs, `chmod -R 777`, `curl | sh`, force-push to `main`).
  - **Secret Defense**: Blocks exposure of AWS keys (`AKIA...`), GitHub tokens (`ghp_...`, `github_pat_...`), GitLab tokens, Private Key headers, and JWT strings with exit code `2`.
- [`hooks/post_tool_linter.py`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/hooks/post_tool_linter.py):
  - Formats modified code via `ruff` and `prettier`.
  - Executes AST syntax checks (`ruff check --select=E9,F63,F7,F82` / `py_compile` / JSON validation) and injects syntax errors directly to `stderr`.

---

### (4) Harness-as-Code Configuration (`.harness/config/harness.yaml`)

- [`config/harness.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/config/harness.yaml):
  - **Agents & Tools**: Maps all 4 subagent archetypes, tools, boundaries, and prompt paths.
  - **MCP Substrate**: Registers 7 S-Tier servers (`filesystem`, `git`, `context7_docs`, `postgres_readonly`, `playwright_browser`, `memory_graph`, `fetch_safe`).
  - **Permissions Engine**: Configures Cedar ABAC with the 4-Class Side-Effect Taxonomy (Class 0 Autonomous Read $\to$ Class 3 HITL Irreversible).
  - **Budgets & Telemetry**: Enforces $5.00 session spend caps, $50.00 daily caps, and P0–P4 token allocations.

---

## 3. Empirical Verification & Friction Log

| Verification Check | Target / Input | Observed Result | Status |
| :--- | :--- | :--- | :---: |
| **Destructive Command Gate** | `rm -rf /` | `[SECURITY REJECTION: DESTRUCTIVE COMMAND]` (Exit Code 2) | **PASS** |
| **Secret Exfiltration Gate** | `export AWS_SECRET_KEY=AKIAIOSFODNN7EXAMPLE` | `[SECURITY REJECTION: SECRET EXPOSURE]` (Exit Code 2) | **PASS** |
| **Benign Test Execution** | `pytest tests/unit -v` | Permitted (Exit Code 0) | **PASS** |
| **False-Positive Long String Test** | `git checkout a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0` | 40-char SHA permitted (Exit Code 0) | **PASS** |
| **Post-Tool Linter (Valid)** | `test_valid.py` | Formatted cleanly (Exit Code 0) | **PASS** |
| **Post-Tool Linter (Syntax Error)** | `test_invalid.py` (`def broken_syntax(:`) | AST syntax error reported to `stderr` (Exit Code 1) | **PASS** |

### Friction & Remediations
1. **Regex False Positives**: The earlier heuristic regex `\b[A-Za-z0-9_]{20,}\b` caused false alarms on benign Git commit SHAs, UUIDs, and module paths. Remediated by replacing it with high-confidence pattern matching for known credential headers and key-value bindings.
2. **Lifecycle Hook Cross-Compatibility**: Claude Code and Antigravity handle hook keys differently (`PreToolUse` vs `pre_tool_call`). Remediated by defining aliases for both in [`hooks/hooks.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/hooks/hooks.json).
3. **Executable Bits**: Explicitly marked Python hook scripts with `chmod 0755` permissions to allow direct execution.

Deliverables recorded in [`phase-3.5/M_A_AGY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3.5/M_A_AGY.md).
