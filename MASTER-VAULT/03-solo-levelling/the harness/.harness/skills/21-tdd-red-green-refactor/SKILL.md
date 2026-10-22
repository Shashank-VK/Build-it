---
name: tdd-red-green-refactor-loop
description: Enforces strict test-driven development (TDD) by requiring a failing test before implementation, minimal code to pass, and subsequent refactoring.
domain: Testing, QA & Formal Verification
version: 1.0.0
triggers:
  - "implement feature"
  - "fix bug"
  - "add test"
  - "refactor function"
tier: Essential
---

# TDD Red-Green-Refactor Loop Runbook

## 1. Objective
Enforce strict test-driven development (TDD). Code changes must never be introduced without a failing test that isolates the expected behavior or bug reproduction.

---

## 2. Deterministic Execution Steps

### 1. Red Phase (Failing Test)
1. Locate or create test file in `tests/` mirroring the target module.
2. Write a minimal unit test asserting the expected behavior, input/output contract, or bug edge case.
3. Run the test suite:
   ```bash
   pytest tests/test_target.py -k "test_new_behavior"
   ```
4. **Assertion Check**: The test MUST fail with an expected error (e.g., `AssertionError`, `NotImplementedError`, or `AttributeError`). If it passes unexpectedly, revise the assertion.

### 2. Green Phase (Minimal Passing Implementation)
1. Edit ONLY the target source file to satisfy the failing test.
2. Avoid premature optimization or writing extraneous logic.
3. Run the test suite:
   ```bash
   pytest tests/test_target.py -k "test_new_behavior"
   ```
4. **Assertion Check**: The test MUST pass with exit code 0.

### 3. Refactor Phase (Clean Code Hygiene)
1. Clean up duplicate logic, enforce type annotations, and ensure docstring accuracy.
2. Run full regression suite to ensure zero collateral damage:
   ```bash
   pytest tests/ -q
   ```
3. Run linter and typecheck:
   ```bash
   ruff check . && mypy --strict src/
   ```

---

## 3. Verification Assertions & Exit Criteria

1. **[Assertion TDD-01: Red Isolation]**: Initial test run demonstrated non-zero exit code with assertion failure.
2. **[Assertion TDD-02: Green Verification]**: Target test passes with exit code 0 after implementation.
3. **[Assertion TDD-03: Zero Regression]**: Entire test suite passes cleanly with zero broken legacy tests.
