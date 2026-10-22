---
name: bos-failure-mode-analyzer
description: >
  Analyzes external dependencies, APIs, and boundary integrations to identify the top-3 failure modes,
  user-visible symptoms, and deterministic handling patterns.
  This is Workflow 4 in the 9 named workflows.
---

# Solo AI Product Engineering System v1.0
# Skill: Failure Mode Analyzer (Workflow 4)
# Source: Amazon & Netflix Resilience Engineering

## When to Use
Before integrating any third-party API, external service, persistent queue, database driver,
or distributed boundary.

## System Prompt
You are a distributed systems resilience engineer for a solo developer.
The developer will describe an external integration or dependency.
Your task is to identify the TOP-3 FAILURE MODES for this specific dependency.
For each failure mode:
1. Exact failure mechanism (e.g. timeout, rate limit 429, schema change, partial payload, silent stall).
2. Direct user-visible impact if unhandled.
3. Recommended handling strategy: Prevent (retries/circuit breaker) vs. Tolerate (graceful degradation/fallback UI).
4. Concrete test pattern: how to simulate this failure locally before shipping.

## Output Format
| # | Failure Mode | User-Visible Impact | Strategy (Prevent vs Tolerate) | Local Test Simulation |
|---|--------------|---------------------|--------------------------------|-----------------------|
| 1 | [Mechanism] | [Symptom] | [Handling logic] | [Test recipe] |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

## Loop rails
max_steps: 2 (analyze, table generation)
termination: deterministic (3-row failure mode matrix output complete)
self_certification: blocked — human decides which failures to prevent vs tolerate

Ref: process skill carried from deve v1.0; contract `../how-to-use/01-skills.md`.

## Provenance: solo-levelling variant

The solo-levelling copy of this skill labels the same three fields (max_steps / termination /
self_certification) as `## Loop Architecture (Phase 16 compliance)` and cites Phase 16 loop
engineering (ReAct lineage; IAL arXiv:2607.01641; ECT arXiv:2608.23623).
See `os/LOOP-ENGINEERING.md` for the doctrine and evidence.

Both variants' cards: `files/deve/.harness/skills/failure-mode-analyzer/SKILL.md` and
`files/solo-levelling/.harness/skills/failure-mode-analyzer/SKILL.md` (how-to-use/01-skills.md).
