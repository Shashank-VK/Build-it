# Solo AI Product Engineering System v1.0
# Release and Experimentation System

## Default Deploy Procedure

1. Confirm Launch Checklist is complete (Gate 6 passes — every item checked).
2. PRE-COMMIT THE ROLLBACK THRESHOLD before touching the deploy button:
   Write down: "If [specific metric] exceeds [X]% within 10 minutes of deploy, I roll back immediately."
   Write it in the launch checklist. This decision is made BEFORE deploy, not in the moment.
3. Deploy.
4. Monitor the defined metric for 10 minutes.
5. If threshold is crossed: ROLL BACK IMMEDIATELY. No exceptions. No deliberation.
6. If 10 minutes pass without threshold crossing: deployment is stable. Monitor for 24 hours at reduced attention.

## A/B Experimentation Protocol

- Write the hypothesis and success metric BEFORE launching the test. Never after.
- Define the minimum detectable effect and required sample size BEFORE looking at any results.
- Run to completion. Do NOT stop early because early results look good.
- Decision rule: if the primary metric achieves the pre-defined success criterion, ship the winner. If not, do not ship.

## Headless Pipeline Adaptations (non-user-facing workloads)

For batch pipelines, personal automation tools, and headless systems:
- PR/FAQ → Problem Statement + ROI calculation (automation save time vs. build time comparison)
- UX Flows → Input/Output/Error Specification (what triggers it, what it outputs, what happens on failure)
- Launch Checklist item 6 (adversarial auth test) → Confirm graceful handling of API errors (403, 429, 5xx)
- Launch Checklist item 7 (load test) → Test with full realistic data volume in single dry run
- Deployment monitoring → Job success/failure alert + output spot-check (verify actual output is correct)
- A/B experimentation → Does not apply to personal tools with no users to split
