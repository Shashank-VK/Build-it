# Solo AI Product Engineering System v1.0
# FCAR — Fresh Context Adversarial Review Rubric

## Protocol (non-optional)

Step 1: Write this rubric BEFORE the artifact is complete. Writing it after allows reverse-engineering to match.
Step 2: Open a NEW AI context with NO memory of the original artifact's authoring process.
Step 3: Provide ONLY: (a) the artifact to review, and (b) this locked rubric. Nothing else.
Step 4: AI evaluates each rubric item and returns: pass/fail per item, and for each fail, specific failing evidence quoted from the artifact verbatim.
Step 5: Human reviews FCAR output. If any item fails: revise the artifact and repeat from Step 2.
Step 6: If a rubric item fails and human believes the failure is acceptable: document the exception EXPLICITLY in the artifact. The waiver is visible to any future reviewer. No silent skips.

## CRITICAL RULE
This skill MUST be invoked in a fresh context with no memory of the artifact's creation.
Running FCAR in the same context that authored the artifact = reviewer collusion.
It defeats the entire mechanism. It is the failure mode Phase 14 was designed to prevent.

## The Locked Rubric

A design note, PRD, or pitch PASSES if ALL of these are true:

| # | Item | What PASS looks like | What FAIL looks like |
|---|------|----------------------|----------------------|
| 1 | Every claimed benefit/technical claim is sourced | "Response time reduced by X% [as measured in staging test on Date Y]" | "Response time will be faster" (no source) |
| 2 | Non-Goals section present with at least 2 specific exclusions | "Does not support mobile app. Does not support team accounts." | "Out of scope for now" (vague) |
| 3 | No technical claim asserted without named source | "Uses PostgreSQL because SQLite max row size is insufficient (confirmed in test)" | "PostgreSQL is more scalable" (asserted without evidence) |
| 4 | Success metric is measurable and specific | "Error rate below 1% within 10 minutes of deploy" | "Users will be satisfied" |
| 5 | Alternatives Considered lists at least 1 rejected alternative with specific reason | "Plaid API rejected: requires PCI compliance review out of scope for this appetite" | "Considered other options but chose this approach" |

## FCAR System Prompt (use this exactly, verbatim)

System: You are a document quality reviewer. You have no prior knowledge of this project.
Task: You will be given an artifact and an evaluation rubric.
Step 1: Read the rubric carefully. Do not refer to anything outside the artifact and rubric.
Step 2: For each rubric item, evaluate the artifact against it. Binary only: pass or fail.
Step 3: For each item that FAILS, quote the specific failing text from the artifact verbatim.
Step 4: Return a table: Rubric Item | Pass/Fail | Evidence (quoted from artifact if fail).
Do not suggest improvements. Do not be diplomatic. Do not explain what would make it better.
Your job is binary: pass or fail, with specific evidence. Nothing else.

## Confirmed Test Result (Phase 14 — injected flaw test)

Flaw injected: A PRD contained "response time will be under 50ms" with no source or benchmark.
Mechanism run: FCAR in fresh context.
Result: Rubric item 3 FAILED. FCAR quoted the specific sentence as unsourced.
Verdict: Mechanism confirmed working. This rubric catches confident-but-unsourced claims.
