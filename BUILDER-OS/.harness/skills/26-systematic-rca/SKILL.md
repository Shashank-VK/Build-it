---
name: bos-systematic-root-cause-analysis
domain: Debugging & Diagnostics
version: 1.0.0
tier: Essential
cap: CAP-32
triggers:
  - "debug"
  - "error"
  - "failing test"
  - "root cause"
  - "why is this broken"
---

# Systematic Root Cause Analysis (RCA)

## Objective
Apply a rigorous 5-phase scientific methodology and 5-Whys causal chain analysis to isolate, diagnose, and permanently resolve software defects without relying on speculative trial-and-error edits or introducing regressions.

## When to Activate
- Investigating failing unit, integration, or end-to-end tests.
- Triage of unexpected runtime exceptions, crash reports, or error logs.
- Diagnosing regressions introduced following a merge, dependency bump, or refactor.
- Resolving flaky or intermittent non-deterministic failures.

## Step-by-Step Runbook

### Phase 1 — Reproduce (Minimal Reproduction Case)
Never write fix code before achieving a 100% deterministic reproduction:
1. **Author Isolated Repro**: Construct the smallest possible standalone test script or test function (`test_repro.py` / `repro.test.ts`) that triggers the failure.
2. **Eliminate Noise**: Strip away extraneous dependencies, mock out external network/database calls, and pass minimal inputs.
3. **Assert Failure**: Execute the repro case and verify that it fails with the exact target assertion or stack trace.

```bash
# Example reproduction check:
pytest tests/reproduce_issue.py -q
```

---

### Phase 2 — Isolate (Delta Debugging & Binary Search)
Narrow down the failure boundary from the whole system to an exact line, expression, or function:
1. **Delta Debugging**: Use binary search across inputs, configurations, or Git history (`git bisect`) to identify the exact commit or input boundary causing the failure.
2. **Execution Flow Tracing**: Trace variable states backwards from the point of exception to where state invariant violation first occurred.
3. **Module Boundary Pinpointing**: Isolate whether the bug is located in the caller (invalid arguments), callee (internal logic bug), or data layer (corrupted state).

---

### Phase 3 — Hypothesize (Rank Top 3 Causes)
Formulate 3 distinct, falsifiable candidate root causes ranked in order of probability:

- **Hypothesis 1 ($H_1$)**: *[Highest probability]* e.g., Missing null-check / unhandled `None` state when payload key is omitted.
- **Hypothesis 2 ($H_2$)**: *[Moderate probability]* e.g., Race condition or out-of-order execution in asynchronous task queue.
- **Hypothesis 3 ($H_3$)**: *[Lower probability / Edge case]* e.g., Type coercion mismatch during JSON serialization/deserialization.

---

### Phase 4 — Test Hypotheses (Falsification Experiments)
Systematically prove or disprove each candidate hypothesis without modifying production logic:
1. **Targeted Diagnostic Tests**: For each hypothesis $H_i$, author an assertion that can **ONLY** pass if $H_i$ is true and fails if $H_i$ is false.
2. **Evaluate Evidence**: Run the diagnostic test against the observed system state.
3. **Eliminate Non-Causes**: Reject invalid hypotheses until a single verified root cause remains.

---

### Phase 5 — Fix + Verify (Remediation & Regression Shield)
Implement the permanent solution and prove system stability:
1. **Targeted Fix**: Modify the verified root-cause logic at the source.
2. **Repro Validation**: Run the minimal reproduction test written in Phase 1 to confirm it now passes cleanly.
3. **Full Regression Suite**: Run the complete test suite across the entire project to verify zero collateral damage or regressions.

```bash
# Full validation gate:
pytest tests/ -v
```

---

### Standard 5-Whys Diagnostic Template
When documenting the post-mortem or root cause, complete the following iterative 5-Whys template where each response becomes the premise for the subsequent question:

1. **Why #1**: Why did the test or system operation fail?
   - *Answer:* The service returned HTTP 500 on valid user login requests.
2. **Why #2**: Why did [the service return HTTP 500]?
   - *Answer:* A `KeyError: 'session_id'` unhandled exception was thrown in `auth_middleware.py`.
3. **Why #3**: Why was [`KeyError: 'session_id'` thrown]?
   - *Answer:* The new token refresh flow omitted the legacy session token field from the context payload.
4. **Why #4**: Why did [the new token refresh flow omit the legacy session token field]?
   - *Answer:* The API contract upgrade in PR #142 assumed all clients migrated to bearer headers without backward-compatibility fallback.
5. **Why #5**: Why was [the backward-compatibility fallback missing from PR #142]?
   - *Answer:* There was no automated contract-drift integration test validating legacy payload schemas against the auth middleware.

## Completion Gate
- Minimal reproduction test case is written, committed to the test suite, and passes with the fix applied.
- The single true root cause is conclusively proven and documented via the 5-Whys template.
- 100% of full project test suites pass without regression.

## Common Pitfalls
- **Shotgun Debugging**: Randomly editing lines in the hope of making an error disappear without an isolated reproduction case.
- **Symptom Patching**: Masking errors with broad catch blocks (`except Exception: pass`) or shallow fallback defaults instead of fixing the root causal state.
- **Skipping Regression Testing**: Assuming that fixing one function has no side effects on dependent modules without running the full test suite.
Ref: verbatim runbook from solo the-harness; skill card in `../how-to-use/01-skills.md`.
