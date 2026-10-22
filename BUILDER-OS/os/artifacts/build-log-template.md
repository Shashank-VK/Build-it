# Solo AI Product Engineering System v1.0
# Build Log: [Project Name]

Started: [date]
Pitch: [link to pitch document]
Design Note: [link to design note, or "not required for this project"]
Appetite: [X days remaining as of build start]

## Session Log

### [Date] — Session [N]
Scopes worked: [which scope(s) were active this session]
Uphill/Downhill status: [for each scope — is it moving uphill (unknowns being resolved) or downhill (clear path)?]
Decisions made:
- [decision 1]: [why — flag irreversible decisions explicitly]
- [decision 2]: [why]
Rabbit holes encountered this session: [any that appeared mid-build]
Change events: [any requirement shifts, assumption failures, or scope changes — date-stamped]
Appetite consumed: [X days of original Y days remaining]
Next session plan: [what will be picked up next]

[Add one block per session. Do not overwrite — append.]
[This is the living record of decisions made during build.]
[It is the source of truth when the postmortem asks: "what was the state at launch time?"]

## Evidence

Evidence receipts are appended here as work lands. The coverage gate and the
claim check parse this section, so entries must be filled in literally:

    TEST: <path-to-test> exit <zero>
    RANGES: <file>:<start>-<end> sha <64-hex-digest>
    CLAIM: <what> | URL: <https-url> | HTTP: <3-digit-status> | DATE: <YYYY-MM-DD>

The `TEST` and `RANGES` rows are indented so they are guidance, not receipts —
an unfilled project fails the gates on purpose. Replace each one with a real
receipt (no leading indent) as the corresponding work completes. The `CLAIM`
row must be a single line beginning with `- CLAIM:`; add one per external
claim, or move unverifiable ones to a `## Quarantine` section below.
