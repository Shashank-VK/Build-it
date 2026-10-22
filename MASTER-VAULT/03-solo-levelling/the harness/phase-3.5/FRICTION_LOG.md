# Phase 3.5 — Empirical Validation & Friction Log

> **Date:** 2026-09-01 | **Status:** Active Empirical Validation Registry  
> **Source:** Live workflow test runs, hook gate executions, subagent orchestrations, and sandbox validations.  
> **Purpose:** Record empirical execution findings, harness friction points, MTTR metrics, and success criteria verdicts across archetypes (C1 Product Engineering, C2 Data/MLOps, C6 Modernization).

---

## 1. Validation History & Preliminary Findings

| Round | Task | Result | Friction Found | Fed Back To |
| :--- | :--- | :--- | :--- | :--- |
| **V1** | `pre_tool_guard.py` gate test | ✅ PASS — blocks `rm -rf`, `API_KEY`; passes benign | Regex guard brittle vs true sandbox | CAP-24 (bwrap sandbox) |
| **V2** | Skills authoring + index | ✅ PASS — Essential skills materialized & indexed | Progressive disclosure required | CAP-01/32 (skills repo) |
| **V3** | Coherence audit (spec vs disk) | ⚠️ GAPS IDENTIFIED — Materialization sprint completed | Blueprint vs working code divergence | Sprint M-A, M-B, G-D |

---

## 2. Materialization Sprint Results Summary

| Capability / Target | Status | Verification & Operational State |
| :--- | :---: | :--- |
| **`CAP-25` `policies.cedar`** | ✅ Materialized | Formally verified Cedar ABAC policy authored, enforcing 4-class side-effect taxonomy, archetype roles (C1–C6), path containment, and HITL gate tokens. |
| **`CAP-25` `presets.json`** | ✅ Materialized | Per-archetype capability matrices materialized for C1–C6 with tool allow/deny lists, allowed/denied paths, and HITL triggers. |
| **`CAP-22/35` `litellm-config.yaml`** | ✅ Materialized | LiteLLM budget router configuration materialized with latency-based fallback, failover tiers, local zero-cost models, and hard $5.00 session cap. |
| **`CAP-24` `sandbox/gate.sh`** | ✅ Materialized | True OS namespace sandbox (`bwrap`/Docker) materialized. Verified: blocks host modifications (EROFS on `/etc`), masks sensitive dirs via tmpfs, and isolates PID/network. |
| **`CAP-20/37` `post_tool_linter.py`** | ✅ Materialized | In-process AST linter hook materialized. Verified: catches Python `SyntaxError` with line/column caret diagnostics, validates JSON/YAML/shell, runs auto-formatters. |
| **`CAP-20` `hooks/hooks.json`** | ✅ Materialized | Fully escaped, verified JSON schema for pre-tool and post-tool lifecycle hooks. |
| **`CAP-01..40` Skills Materialization** | ✅ Materialized | Materialized top Essential skills under `.harness/skills/` with complete step-by-step runbooks. |

---

## 3. Empirical Validation Runs

### Validation Run: VAL-001 (Example Reference Template)

> **Run ID:** VAL-001  
> **Date:** 2026-09-01  
> **Archetype:** C1 (ProductEngineering)  
> **Target Repo:** `https://github.com/example-org/fullstack-ecommerce-sample` (Commit: `a3f91c0`)  
> **Workflow Used:** `.harness/workflows/build-verify.yaml`  
> **Status:** `TEMPLATE - replace with real data`

#### A. Execution Step Trace

| Step | Expected | Actual | Pass/Fail | Notes |
| :--- | :--- | :--- | :---: | :--- |
| **1. Repo Survey** | Generate `REPO_MAP.md` under 2,000 tokens identifying entrypoints and test commands | Produced structured map (1,420 tokens) resolving Next.js frontend + FastAPI backend | ✅ PASS | Skill `01-repo-surveyor-map` activated cleanly |
| **2. AST Navigation** | Trace auth middleware dependencies and call graph | Extracted JWT handler symbols and middleware chain | ✅ PASS | Class-0 read-only isolation maintained |
| **3. Pre-Tool Security Guard** | Intercept dangerous shell commands (`rm -rf`, raw API key writes) | Blocked simulated `rm -rf /` probe with exit code 1 | ✅ PASS | Hook `pre_tool_guard.py` triggered in <15ms |
| **4. Feature Implementation** | Add OAuth2 PKCE callback handler with TDD red-green cycle | Initial test failed (red), minimal handler implemented (green) | ✅ PASS | Skill `21-tdd-red-green-refactor` followed |
| **5. Post-Tool AST Linter** | Validate Python syntax and format code on file edit | Caught missing colon syntax error, provided line/col diagnostics, auto-remediated | ✅ PASS | Hook `post_tool_linter.py` auto-formatted diff |
| **6. Integration Verification** | Run unit + Playwright E2E matrix headlessly | 24 unit tests passed, 4 E2E browser journeys passed headlessly | ✅ PASS | Mock routes prevented external auth flakiness |
| **7. Sandbox Gate Check** | Container/bwrap sandbox prevents host filesystem mutation | Writes to `/etc` rejected with EROFS | ✅ PASS | `gate.sh` confirmed filesystem isolation |

#### B. Friction Points
- **FP-01 (Regex Guard False-Positive on UUIDs)**: `pre_tool_guard.py` entropy check flagged a legitimate mock JWT test token in a test fixture. Remediated by adding test fixture paths (`tests/fixtures/*`) to entropy ignore scope.
- **FP-02 (LiteLLM Initial Cold-Start Latency)**: First upstream request through proxy experienced ~800ms cold start before connection pooling kicked in. Subsequent latency averaged 120ms.
- **FP-03 (Playwright Headless Display Server Warning)**: Warning emitted regarding missing X11 display in WSL environment; resolved by forcing `--headless` flag in `playwright.config.ts`.

#### C. Metrics & Success Criteria Verdict

| Metric | Measured Value | Target SLA | Verdict |
| :--- | :--- | :--- | :---: |
| **Total Tokens Used** | 42,650 tokens (Prompt: 34,100 / Completion: 8,550) | $\le 100,000$ | 🟢 MET |
| **Total Cost (USD)** | $0.184 USD | $\le \$5.00$ / session | 🟢 MET |
| **MTTR (Mean Time to Rollback)** | 4.2 seconds (via `git worktree` discard) | $\le 30$ seconds | 🟢 MET |
| **Human Interventions Count** | 0 (fully autonomous execution to green gate) | 0 blocking alerts | 🟢 MET |

##### Success Criteria (SC-01 .. SC-10) Evaluation:

| Criterion | Description | Result | Details |
| :--- | :--- | :---: | :--- |
| **SC-01** | Zero Unbounded Context Floods | ✅ PASS | Context remained $<45\text{k}$ tokens with bounded tree traversal |
| **SC-02** | Strict Read-Only Exploration | ✅ PASS | No file mutations occurred during discovery stages |
| **SC-03** | TDD Red-Green-Refactor Enforcement | ✅ PASS | Failing test verified before implementation patch applied |
| **SC-04** | AST & Syntax Verification Gate | ✅ PASS | `post_tool_linter.py` caught and resolved syntax errors |
| **SC-05** | Pre-Tool Side-Effect Interception | ✅ PASS | Destructive commands intercepted and blocked |
| **SC-06** | Cedar Policy ABAC Compliance | ✅ PASS | Role and path access adhered to C1 ProductEngineering preset |
| **SC-07** | Hermetic Sandbox Isolation | ✅ PASS | `gate.sh` confirmed write protection outside workspace |
| **SC-08** | Budget & Spend Circuit Breaker | ✅ PASS | LiteLLM tracked spend under $0.20 with zero overruns |
| **SC-09** | Reversible Atomic Worktree Mutations | ✅ PASS | Worktree cleaned up cleanly without branch pollution |
| **SC-10** | Clean Regression Test Gate | ✅ PASS | Full test suite passed with 0 failures |

---

## 4. Blank Empirical Validation Run Template

*Copy this block for each new empirical test run.*

```markdown
### Validation Run: VAL-XXX

> **Run ID:** VAL-XXX  
> **Date:** YYYY-MM-DD  
> **Archetype:** [C1 (ProductEngineering) | C2 (DataMLOps) | C6 (Modernization)]  
> **Target Repo:** `<repo-url-or-local-path>` (Commit: `<git-sha>`)  
> **Workflow Used:** `.harness/workflows/<workflow-name>.yaml`  
> **Status:** [IN_PROGRESS | SUCCESS | FAILED]

#### A. Execution Step Trace

| Step | Expected | Actual | Pass/Fail | Notes |
| :--- | :--- | :--- | :---: | :--- |
| **1. Repo Survey** | | | | |
| **2. Planning & Alignment** | | | | |
| **3. Implementation** | | | | |
| **4. Lint & Syntax Gate** | | | | |
| **5. Test Execution** | | | | |
| **6. Security & Sandbox** | | | | |

#### B. Friction Points
- **FP-01 (<Short Title>)**: Description of friction, root cause, and immediate or recommended fix.
- **FP-02 (<Short Title>)**: Description.

#### C. Metrics & Success Criteria Verdict

| Metric | Measured Value | Target SLA | Verdict |
| :--- | :--- | :--- | :---: |
| **Total Tokens Used** | | $\le 100,000$ | |
| **Total Cost (USD)** | | $\le \$5.00$ | |
| **MTTR (Mean Time to Rollback)** | | $\le 30\text{s}$ | |
| **Human Interventions Count** | | 0 | |

##### Success Criteria (SC-01 .. SC-10) Evaluation:

| Criterion | Description | Result | Details |
| :--- | :--- | :---: | :--- |
| **SC-01** | Zero Unbounded Context Floods | | |
| **SC-02** | Strict Read-Only Exploration | | |
| **SC-03** | TDD Red-Green-Refactor Enforcement | | |
| **SC-04** | AST & Syntax Verification Gate | | |
| **SC-05** | Pre-Tool Side-Effect Interception | | |
| **SC-06** | Cedar Policy ABAC Compliance | | |
| **SC-07** | Hermetic Sandbox Isolation | | |
| **SC-08** | Budget & Spend Circuit Breaker | | |
| **SC-09** | Reversible Atomic Worktree Mutations | | |
| **SC-10** | Clean Regression Test Gate | | |
```
