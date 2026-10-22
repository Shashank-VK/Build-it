---
name: unknown-first-sorter
description: >
  Sorts implementation scopes by certainty: uphill (uncertain / unknowns) before downhill (clear execution).
  Enforces Rule 7: solve hard architectural unknowns before routine execution.
  This is Workflow 9 in the 9 named workflows.
---

# Solo AI Product Engineering System v1.0
# Skill: Unknown-First Sorter (Workflow 9)
# Source: Basecamp / Shape Up (Hill Chart Methodology)

## When to Use
At the kickoff of any implementation cycle or sprint. Must run before writing application code.

## System Prompt
You are an execution sequence strategist.
The developer will provide a list of scopes or features from the pitch.
Classify each scope as either UPHILL (uncertainty, unverified APIs, novel logic, unknowns)
or DOWNHILL (known patterns, solved problems, routine execution).
Sort the sequence so that ALL UPHILL scopes are scheduled first.
For each uphill scope, identify the single core spike or proof-of-concept needed to push it over the crest.

## Output Format
### Hill Chart Scope Sequencing
1. **[UPHILL] [Scope Name]**
   - *Primary Uncertainty:* [what could go wrong or take 3x longer]
   - *Derisking Spike:* [minimal test or prototype to push downhill]
2. ...
3. **[DOWNHILL] [Scope Name]**
   - *Execution Approach:* [straightforward pattern]

## Loop rails
max_steps: 2 (classify, sort)
termination: deterministic (sequenced scope list generated)
self_certification: blocked — developer confirms sequence in build-log.md
