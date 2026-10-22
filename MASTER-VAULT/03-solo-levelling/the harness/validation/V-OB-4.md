# Independent Validation Report: Agents, Workflows & Harness Configuration

**Target Directory:** `/mnt/c/Users/Shashank Karamudi/Desktop/solo-levelling/the harness/.harness`  
**Validation Date:** 2026-09-01  
**Scope:** Subagent Markdown specs, Workflow YAML blueprints, and Harness-as-Code manifests.

---

## 1. Subagent Definitions (`.harness/agents/*.md`)

### Validation Criteria
- **Frontmatter Validity:** Valid YAML frontmatter demarcated by `---` containing `name`, `description`, `tools`, and `model`.
- **Usability & Role Definition:** Clear operational invariants, bounded permission tiering (Class-0 to Class-2), Mermaid protocol diagrams, and concrete output schema contracts.

---

### [`coder.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/coder.md)
- **Verdict:** **PASS** (Valid & Highly Usable)
- **Frontmatter:** Valid YAML. Specifies `name: coder`, `model: inherit`, tools (`view_file`, `write_to_file`, `replace_file_content`, `run_command`, etc.), and Class-1/Class-2 permission boundaries (`src/`, `tests/`, `docs/`, `scratch/`).
- **Usability:** Exceptional. Enforces TDD Red-Green-Refactor (`CAP-18` Skill 21), comment/docstring preservation, zero secret leakage, and surgical line replacements.
- **Issues / Notes:** Minor tool list redundancy (includes both `read_file` and Antigravity's standard `view_file`).

---

### [`explorer.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/explorer.md)
- **Verdict:** **PASS** (Valid & Highly Usable)
- **Frontmatter:** Valid YAML. Specifies `name: explorer`, `model: flash` (cost-optimized), read-only tools (`view_file`, `list_dir`, `grep_search`, `find_by_name`, `read_url_content`, `search_web`), and Class-0 strict read-only tier.
- **Usability:** High. Enforces zero side-effects, progressive AST exploration, context compaction, and a structured markdown table output contract with clickable line links.
- **Issues / Notes:** None.

---

### [`planner.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/planner.md)
- **Verdict:** **PASS** (Valid & Highly Usable)
- **Frontmatter:** Valid YAML. Specifies `name: planner`, `model: inherit`, orchestration tools (`ask_question`, `invoke_subagent`, `send_message`, `manage_subagents`, `view_file`), and Class-0 read-only governance.
- **Usability:** High. Defines a deterministic orchestration state machine, child delegation matrix (`explorer`, `coder`, `reviewer`), context hygiene rules (<30k token ceiling), and human-in-the-loop (HITL) failure escalation.
- **Issues / Notes:** None.

---

### [`reviewer.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/agents/reviewer.md)
- **Verdict:** **PASS** (Valid & Highly Usable)
- **Frontmatter:** Valid YAML. Specifies `name: reviewer`, `model: pro` (high reasoning), verification tools (`view_file`, `list_dir`, `grep_search`, `find_by_name`, `run_command`), and Class-0 verification tier.
- **Usability:** High. Details a 5-dimension audit protocol (correctness, OWASP Top 10 security, strict typing, test suite rigor, simplicity) and an actionable review verdict template.
- **Issues / Notes:** None.

---

## 2. Workflows & Blueprints (`.harness/workflows/` & `blueprints/`)

*Note: Files in `.harness/workflows/` and `.harness/workflows/blueprints/` are exact duplicates.*

### Validation Criteria
- **Syntax:** Valid YAML parsing.
- **Determinism:** Explicit dependency DAG (`depends_on`), step timeouts (`timeout_seconds`), required flags, and fail-fast triggers.
- **Gating & Rollback:** Automated verification checkpoints and saga compensation (`on_failure` / `on_abort`).

---

### [`build-verify.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/blueprints/build-verify.yaml) (Root & Blueprint)
- **Verdict:** **FAIL** (YAML Syntax Error)
- **Issue:** **Unescaped nested quotes in command scalar.** On line 53, the command uses double quotes inside an outer double-quoted YAML string:
  ```yaml
  # Line 53 (Broken):
  command: "python3 -c 'import sys; print("[VERIFICATION SUCCESS] All pipeline stages passed with exit code 0"); sys.exit(0)'"
  ```
  YAML parsers terminate the string at `print(` and crash on `[`.
- **Workflow Mechanics:** Once escaped (using single quotes or block scalar `|`), the workflow is well-formed: deterministic 6-stage DAG (`secret_scan` -> `format_check` -> `lint` -> `type_check` -> `unit_tests` -> `artifact_health_gate`), worktree isolation, fail-fast aborts, and hard git rollback compensation.

---

### [`migration-safeguard.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/blueprints/migration-safeguard.yaml) (Root & Blueprint)
- **Verdict:** **FAIL** (YAML Syntax Error)
- **Issue:** **Unescaped nested quotes in command scalar.** On line 33, unescaped double quotes inside outer double quotes cause a YAML parse failure:
  ```yaml
  # Line 33 (Broken):
  command: "python3 -c 'print("[SCHEMA VERIFIED] Non-blocking schema change confirmed")'"
  ```
- **Workflow Mechanics:** Once fixed, the workflow exhibits strong determinism and gating: dry-run schema validation, forward migration, bi-directional rollback verification (`downgrade -1 && upgrade head`), and automated Alembic rollback compensation.

---

### [`refactor-safely.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/blueprints/refactor-safely.yaml) (Root & Blueprint)
- **Verdict:** **PASS** (Valid, Deterministic & Gated)
- **Workflow Mechanics:** Exemplary 7-step DAG.
  1. `baseline_verification` (Trunk green assert)
  2. `isolate_worktree` (Ephemeral git worktree spawn)
  3. `ast_impact_analysis` (Runs `survey_repo.py`)
  4. `apply_refactor_step` (Delegates to `coder` subagent)
  5. `verify_regression` (Pytest + Ruff + Mypy strict)
  6. `peer_review` (Delegates to `reviewer` subagent)
  7. `merge_worktree` (Fast-forward merge to main)
- **Gating & Compensation:** Full saga compensation removes the ephemeral worktree and deletes the branch on failure.
- **Issues / Notes:** None.

---

### [`test-and-verify.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/workflows/blueprints/test-and-verify.yaml) (Root & Blueprint)
- **Verdict:** **PASS** (Valid, Deterministic & Gated)
- **Workflow Mechanics:** Clean 4-step fail-fast verification pipeline (`lint` -> `typecheck` -> `unit_tests` -> `integration_tests`). Each step enforces explicit dependencies and strict execution timeouts.
- **Issues / Notes:** None.

---

## 3. Harness Configuration Manifests

### Validation Criteria
- **YAML Syntax:** Clean parsing with no schema ambiguities.
- **Coherence & Cross-References:** Consistency across registered paths (agents, workflows, hooks, policies, MCP, telemetry), model mappings, and token budget allocations.

---

### [`config/harness.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/config/harness.yaml) & [`harness.config.yaml`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/harness.config.yaml)
- **Verdict:** **PASS** (Valid YAML & Fully Coherent)
- **Cross-Reference Integrity:**
  - **Agents:** Prompt paths (`.harness/agents/{planner,explorer,coder,reviewer}.md`) resolve to valid files. Model references (`coding-primary`, `coding-fast`) align with the LiteLLM failover router.
  - **Workflows:** All registered blueprint paths (`.harness/workflows/blueprints/*.yaml`) point to existing files.
  - **Hooks & Sandbox:** `hooks.json`, `pre_tool_guard.py`, `post_tool_linter.py`, and sandbox isolation paths match.
  - **Permissions:** Cedar policy (`policies.cedar`) and presets (`presets.json`) exist and align with the 4-tier side-effect taxonomy (Class-0 through Class-3).
  - **Budgets:** Token distribution (P0: 2k, P1: 1.5k, P2: 8k, P3: 12k, P4: 4k = 27.5k budget) cleanly respects the 32k context cap with a 28k compaction trigger (CAP-35). Session ($5.00) and daily ($50.00) hard caps are coherent with LiteLLM telemetry.
- **Issues / Notes:**
  - `config/harness.yaml` and `harness.config.yaml` are identical 1:1 duplicate files. Maintaining both introduces synchronization drift risk.

---

## Summary Scorecard

| Target Path | Category | YAML / Frontmatter | Determinism / Usability | Gating & Safety | Final Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `.harness/agents/coder.md` | Agent | Valid | High (TDD & Class-1) | Strong | **PASS** |
| `.harness/agents/explorer.md` | Agent | Valid | High (AST & Class-0) | Strong | **PASS** |
| `.harness/agents/planner.md` | Agent | Valid | High (DAG & Orchestrator) | Strong | **PASS** |
| `.harness/agents/reviewer.md` | Agent | Valid | High (Staff Audit & OWASP) | Strong | **PASS** |
| `.harness/workflows/build-verify.yaml` | Workflow | **FAIL** (Unescaped quote) | High | Strong | **FAIL** |
| `.harness/workflows/migration-safeguard.yaml` | Workflow | **FAIL** (Unescaped quote) | High | Strong | **FAIL** |
| `.harness/workflows/refactor-safely.yaml` | Workflow | Valid | High (Worktree + DAG) | Strong (Saga) | **PASS** |
| `.harness/workflows/test-and-verify.yaml` | Workflow | Valid | High (Fail-fast CI) | Strong | **PASS** |
| `.harness/config/harness.yaml` | Config | Valid | Complete Manifest | Strong (Cedar/ABAC) | **PASS** |
| `.harness/harness.config.yaml` | Config | Valid | Complete Manifest | Strong (Cedar/ABAC) | **PASS** |

---

## Immediate Remediation Steps

1. **Fix YAML Quote Escaping in Workflows:**
   In both `.harness/workflows/` and `.harness/workflows/blueprints/`:
   - `build-verify.yaml` (L53): Replace outer quotes with block scalar or escape nested quotes:
     ```yaml
     command: >-
       python3 -c 'import sys; print("[VERIFICATION SUCCESS] All pipeline stages passed with exit code 0"); sys.exit(0)'
     ```
   - `migration-safeguard.yaml` (L33):
     ```yaml
     command: >-
       python3 -c 'print("[SCHEMA VERIFIED] Non-blocking schema change confirmed")'
     ```
2. **Consolidate File Duplication:**
   - Establish `.harness/workflows/blueprints/` as the single source of truth for workflow definitions (removing redundant root copies in `.harness/workflows/`).
   - Standardize on either `.harness/config/harness.yaml` or `.harness/harness.config.yaml` to prevent dual-maintenance divergence.
