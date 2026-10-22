# Solo AI Product Engineering System v1.0
# Pitch: [Project Name]

Date: [date]
Appetite: [X days/hours] — hard limit.
Circuit breaker date: [date] — if minimum shippable version is not done by this date, kill the project.

## Problem
[1-2 paragraphs describing the specific problem and who has it.
Not the solution. The problem. What does the user currently do? What is painful about it?]

## Solution
[Fat-marker sketch description or breadboard — describe the flow and key interactions, not the implementation.
Enough to convey the shape of the solution. Not enough to be a spec. Rough is correct here.]

## Rabbit Holes
- [Known-bad approach 1]: [specific reason why it is too complex or wrong for this appetite]
- [Known-bad approach 2]: [specific reason]
[Document these BEFORE implementation. The point is to prevent relitigating them mid-build when someone (including future-you) proposes them again.]

## No-gos (explicitly NOT in this version — minimum 3 items required)
- [Excluded feature or use case 1]: [why it is excluded from THIS version]
- [Excluded feature or use case 2]: [why]
- [Excluded feature or use case 3]: [why]
[These are not just "out of scope" — they are explicit decisions to exclude, made deliberately.]

## Reversibility Assessment
[State whether this project creates irreversible commitments (data schema, external API contract, etc.)
List them explicitly. This classification determines how carefully Gate 4 must be applied.]
