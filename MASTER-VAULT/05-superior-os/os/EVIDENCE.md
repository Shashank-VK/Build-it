# Evidence Discipline

Adapted from the Phase 1 proof system that built `../how-to-use/` (707 cards, zero silent drops).

## Change coverage
Every behavior change ships a receipt in `projects/<name>/build-log.md` under `## Evidence`:
`- TEST: <test-path> exit 0` and `- RANGES: <file>:<start>-<end> sha <64hex>`.
`task coverage-gate` enforces it. No receipt → no merge.

## Claim evidence
Every external claim (version, URL, capability) ships a row:
`- CLAIM: <what> | URL: <https> | HTTP: <200> | DATE: <iso>`.
`task claim-check` enforces shape. Failures go to `## Quarantine`, never invented.

## Quarantine
Unresolved items need human approval with a dated exception. Zero unresolved quarantine at launch (Gate 6).
