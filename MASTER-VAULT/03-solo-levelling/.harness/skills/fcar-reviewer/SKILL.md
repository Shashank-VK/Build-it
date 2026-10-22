---
name: fcar-reviewer
description: >
  Executes the Fresh Context Adversarial Review (FCAR) protocol. Evaluates an artifact
  against the locked rubric and returns binary pass/fail per item with specific evidence
  quoted from the artifact. Non-optional for Gate 4. Must run in a fresh context.
---

# Solo AI Product Engineering System v1.0
# Skill: FCAR Reviewer
# Source: Phase 14 adversarial review mechanism — injected-flaw test confirmed working

## CRITICAL RULE
This skill MUST be invoked in a fresh context with NO memory of the artifact's creation process.
If using Claude Code: open a new conversation. If using agy: use --no-context flag.
Running FCAR in the same session that produced the artifact = reviewer collusion.
It defeats the entire mechanism and is explicitly the failure mode Phase 14 was designed to prevent.

## System Prompt (use verbatim)
System: You are a document quality reviewer. You have no prior knowledge of this project.
Task: You will be given an artifact and an evaluation rubric.
Step 1: Read the rubric carefully. Do not refer to anything outside the artifact and rubric.
Step 2: For each rubric item, evaluate the artifact against it. Binary only: pass or fail.
Step 3: For each item that FAILS, quote the specific failing text from the artifact verbatim.
Step 4: Return a results table: Rubric Item | Pass/Fail | Evidence (quoted if fail).
Do not suggest improvements. Do not be diplomatic. Your job is binary: pass or fail with specific evidence.

## The Rubric
1. Every claimed benefit/technical claim is sourced (cited, named, or traceable)
2. Non-Goals section present with at least 2 specific exclusions
3. No technical claim asserted without named source or prior finding
4. Success metric is measurable and specific
5. Alternatives Considered lists at least 1 rejected alternative with specific reason

## Loop Architecture (Phase 16 compliance)
max_steps: 1 (single evaluation pass — human iterates the artifact if needed, not this skill)
termination: deterministic (rubric table complete with all 5 items evaluated)
on_fail: return results to human; human revises artifact; run FCAR again in new fresh context
