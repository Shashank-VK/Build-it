# §19 — UX State Matrix

- **Workstream:** ux-states, research only. Researched 2026-10-10; all sources accessed 2026-10-10.
- **Claim labels:** **Verified** = authoritative/official source · **Corroborated** = ≥2 independent sources · **Inferred** = logical extension · **Proposed** = practitioner recommendation without hard evidence · **Unknown** = no reliable source.
- Source metadata for the underlying claims: `04-evidence-register.md`.

## How to use this matrix

1. **Enumerate, don't discover.** For every screen or component that displays data or accepts input, list the states below *before* building; do not discover them in production. Multiple practitioner sources independently prescribe this as a design-before-build artifact. **Corroborated.**
2. **Do NOT force irrelevant states onto every component.** Applicability is the first column of judgment: a static marketing page has no "partial completion"; a login form has no "stale data"; a read-only article has no "offline queue." For each surface, mark each state **applicable / not applicable / inherited** (inherited = handled by a parent shell, e.g. the app-level offline banner).
3. The "four empties" are genuinely different (first-use, no-results, cleared, error) — collapsing them is the most-cited generated-UI shortcut. **Corroborated.**
4. Never flash a "we don't know" empty state and then replace it with real data without an intervening loading state; never blank already-loaded data during refresh. **Corroborated.**

## Master matrix: states × concerns

For each state: visual treatment, user-facing message, recovery action, accessibility behaviour, telemetry, expected system behaviour.

| State | Visual treatment | User-facing message | Recovery action | Accessibility behaviour | Telemetry | Expected system behaviour |
|---|---|---|---|---|---|---|
| **Initial / pristine** | Default appearance; placeholders as format hints only, never as labels | None needed; helper text may orient | N/A | Labels programmatically associated; logical tab order | Impression / view event | No data fetched yet or cached frame shown; no spinners flashing for sub-second loads |
| **Loading — first** | Skeleton matching final geometry; delayed ~200ms so fast loads don't flash | None, or contextual copy for long waits ("Searching 47 sources…") | None; cancel control if wait may exceed ~10s | Region `aria-busy="true"`; status announced via live region | Load-start event with expected-content descriptor | Fetch begins; timeout budget defined; no interaction with unloaded controls |
| **Loading — refresh** | Old data stays visible; subtle inline indicator (spinner/progress on the region) | None | Cancel refresh optional | `aria-busy` on region; do not re-announce whole content | Refresh event | Never blank the screen; preserve scroll position, selection, open sheets |
| **Empty — first use** | Illustration or icon + explanation + primary CTA (verb-first) | What will live here, why it matters, the first step | Primary action (e.g. "Create project"); optional template/sample-data path | Headed region (`aria-labelledby`); CTA keyboard-reachable | Empty-viewed; CTA click-through rate | CTA routes to the creation flow; no dead ends |
| **Empty — no results** | Same shell; message echoes the active query/filters | "No X match 'query'." + suggestion to broaden | "Clear filters" (and optionally "Create X") | Announce result count change via live region | Zero-result query logged (feeds search-quality work) | Filters preserved; clearing restores the unfiltered list |
| **Empty — cleared** | Affirmative, calm treatment — this is a success state | "All caught up. Nothing needs review." | Optional: "View completed" / undo where relevant | Announced politely | Completion event | No error styling; do not suggest something is broken |
| **Success** | Inline confirmation or transient toast; checkmark + specifics | What happened, what changed, what now ("Report saved to your dashboard") | Next suggested action; undo where reversible | `role="status"` announcement; no focus theft | Success event with action + object IDs | State commits; no duplicate modal+toast for one outcome |
| **Validation error** | Inline at the field: red border + icon + text (never color alone); summary at top for long forms | Specific, blameless, fix-oriented ("Enter an email like name@domain.com") | Focus moves to first error; error clears when fixed | `aria-invalid`, `aria-describedby`, `role="alert"`; focus management on submit | Validation-failure event per field (aggregated) | All input preserved, including invalid entries; no clearing |
| **Server error (4xx/5xx)** | Inline banner or full-region error matching severity; no raw codes/traces | Plain language: what happened, whether data was saved, how to recover | Retry control; "Copy error details" for support; status-page link for outages | `role="alert"`; retry keyboard-reachable | Error event with code class + correlation ID (never PII in the message) | Auto-retry with backoff for idempotent reads, then user-initiated retry; idempotency keys before retrying non-idempotent writes |
| **Network failure / offline** | Persistent top banner, non-dismissible, self-clearing on reconnect; degraded controls visibly locked with reason | "You're offline. Changes will sync when you reconnect." | Mutations queued locally; manual "Retry now" optional | Banner `role="alert"`; queued-count announced | Offline-enter/exit; queue depth; replay success/failure | Queue in durable local storage; replay in order on reconnect; conflict resolution (last-write-wins or user merge); discard summary if anything dropped |
| **Permission denied (403)** | Real page, not a blank error; plain explanation | Who the resource belongs to / who can grant access, and how to request it | "Request access" action where a path exists | Focus to the explanation heading | Denied-access event (rate-watch for probing) | No data leaked in the denial (no existence oracle beyond policy) |
| **Unauthenticated (401)** | Redirect to sign-in with return-to-original-destination | "Sign in to continue" | Sign-in, then resume exactly where the user was | Focus to sign-in form | Auth-challenge event | In-progress work (drafts, form state) preserved across re-auth |
| **Expired session** | Pre-expiry warning with countdown + "Stay signed in"; post-expiry re-auth that preserves context | "Your session is about to expire." / "You've been signed out for security." | One-click session extension; re-auth returning to prior state | Warning announced assertively; countdown not the sole signal | Session-extended vs expired counts | Extend on explicit action only; never silently drop user input across expiry |
| **Partial completion / partial data** | Loaded sections render; failed sections marked with per-section retry | What loaded, what didn't, scoped to the failed part | Retry for the failed section only | Failed regions labelled; retry reachable | Partial-failure event per source | One broken widget never blanks the viewport; degraded sections don't block healthy ones |
| **Disabled** | Reduced opacity, no hover/pointer affordance | Reason + how to enable ("Available on the Pro plan", "Select an item first") | Action that removes the blocker where one exists | Disabled state exposed to AT (`aria-disabled`/native disabled) | Disabled-action attempts (signals confusion) | Disabled controls are not focusable traps; reasons are honest, not dark patterns |
| **Stale data** | Timestamp near the data ("Updated 2h ago") + refresh control | Freshness stated; nothing hidden | Refresh / "Check for updates" | Freshness text in the accessible name or adjacent text | Staleness-at-view distribution | Threshold-defined staleness; never silently serve stale as fresh |
| **Retry** | Control-local busy state; attempt counter where useful | "Retrying…" then outcome; no silent infinite loops | Auto-retry with exponential backoff, then user control | Attempts announced; final failure assertive | Retry attempts, backoff exhaustion | Cap auto-retries (e.g. 3), then stop and let the user decide |
| **Cancelled** | Immediate return to prior state; confirmation that nothing was committed | "Cancelled — no changes were made." | Resume/re-enter the flow; draft preserved | Announced via live region | Cancel event with stage reached | Side-effect-free cancel where promised; partial work preserved as draft |
| **Destructive-action confirmation** | Dialog naming the consequence on the button ("Delete 3 files"), destructive style, not default-focused | Irreversible consequence stated plainly | Confirm / Cancel; type-to-confirm or re-auth for catastrophic scope; undo window preferred for recoverable scope | Focus trapped in dialog; Esc cancels; focus returns to trigger | Confirmation shown vs confirmed vs cancelled | No action on dismiss; audit log for high-blast-radius actions |
| **No permission / paywalled** | Feature teaser with clear boundary, not a broken control | What the tier includes and what unlocks it | Upgrade path or request-access path | Same as permission denied | Paywall-viewed; conversion | Never a fake disabled control that looks broken |

**Applicability guidance (do not force-fit):** mark each cell per surface. Examples of legitimate opt-outs: *stale data* — N/A for immutable records; *offline queue* — N/A for read-only marketing pages (banner inherited from shell may still apply); *partial completion* — N/A for single-source screens; *destructive confirmation* — N/A where no destructive action exists; *session expiry* — inherited from the auth shell on most screens.

---

## Worked example 1: Data list / table (e.g., an orders list)

| State | Treatment in this surface |
|---|---|
| Initial | Table shell renders with column headers immediately (headers are known); body region skeleton. |
| Loading — first | 6–8 skeleton rows matching row geometry (avatar/text/amount cells); `aria-busy` on `<tbody>`-equivalent; delayed 200ms. |
| Loading — refresh | Existing rows stay; small spinner in the table toolbar ("Refreshing…"); sort/filter stay interactive. |
| Empty — first use | "No orders yet — when customers buy, they'll appear here." + [Create test order] or [View setup guide]. |
| Empty — no results | "No orders match 'refund' in the last 30 days." + [Clear filters]; filters visibly preserved. |
| Success | Bulk action (e.g. "Exported 42 orders") → toast "Export ready — download started." |
| Validation error | N/A for the list itself; invalid filter input (bad date) gets inline field error in the filter bar. |
| Server error | Inline error row-region: "Couldn't load orders. Check your connection." + [Retry]; toolbar intact. |
| Network failure / offline | App banner + table shows cached rows with "Last synced 12m ago" + refresh disabled with reason. |
| Permission denied | "You don't have access to order data. Ask a workspace admin." + [Request access]. |
| Partial | 9 of 10 columns' source failed → table renders with the failed column marked "Unavailable" + per-column [Retry]; never blank the table. |
| Stale | "Updated 5m ago" in toolbar; auto-refresh paused indicator when tab hidden. |
| Disabled | Bulk-action bar disabled until ≥1 row selected, with "Select orders to enable bulk actions." |
| Cancelled | Export cancelled → toast "Export cancelled — no file was created." |
| **Accessibility** | Sortable headers expose `aria-sort`; row selection via checkbox with labels; skeleton rows `aria-hidden` inside the busy region; live region announces "42 orders loaded" / "No orders match your filters." |
| **Telemetry** | list_viewed, filter_applied, zero_result_query, load_failed {class}, retry_clicked, export_started/completed/cancelled, bulk_action {action, count}. |
| **System** | Cursor-based pagination; column priority defined for narrow viewports (reflow to cards per §18-B3); never squeeze columns; row actions ≤3 inline then overflow menu. |

## Worked example 2: Form submission (e.g., account settings / checkout form)

| State | Treatment in this surface |
|---|---|
| Initial / pristine | Labels above fields; helper text where format is non-obvious; required-vs-optional marked consistently; no errors shown. |
| Loading | Only if the form loads existing values: skeleton or disabled fields with subtle indicator; never an interactive-looking empty form that then jumps. |
| Validation error (inline) | On blur: field gets red border + icon + specific message ("Add an @ symbol — e.g. name@domain.com"); `aria-invalid`/`aria-describedby`; error persists until the input is actually valid. |
| Validation error (submit) | Focus moves to first invalid field; long forms get a top summary with anchor links to each field; all input preserved. |
| Server error | All values preserved; error lands in the same place as client errors ("We couldn't save your changes — our servers are having trouble. [Try again]"); correlation ID available via "Copy error details." |
| Network failure | Submit queues as draft locally where safe; banner "You're offline — your changes are saved on this device and will sync." Never silently discard. |
| Success | Specific confirmation: "Profile updated — your new display name is visible to your team." + next step; focus to confirmation for screen-reader users (GOV.UK pattern). |
| Disabled | Submit disabled *during* the request with inline spinner ("Saving…"); disabled-before-validity is discouraged — prefer enabled submit that explains on click, or state why disabled. |
| Cancelled | "Discard changes?" confirm only if dirty; on confirm, restore prior values; toast "Changes discarded." |
| Expired session | Draft preserved; re-auth; return to the form with all input intact. |
| Destructive confirm | "Delete account" → dialog naming consequence + type-to-confirm; never the default-focused button. |
| **Accessibility** | Native `<label>`s; `autocomplete` tokens set; `inputmode`/`type` matched to data (email/tel) to summon the right mobile keyboard; error summary focus on submit-fail. |
| **Telemetry** | form_started, field_error {field, rule}, submit_attempted, submit_failed {class}, submit_succeeded, time_to_complete, draft_restored. |
| **System** | Idempotency key on submit (no double charges/orders on retry/double-click); client and server validation share one schema; double-submit prevented at the button. |

## Worked example 3: Long-running async action (e.g., video export / report generation / bulk import)

| State | Treatment in this surface |
|---|---|
| Initial | Action described with honest duration expectation ("Exports usually take 2–5 minutes") before the user commits. |
| Loading — running | Determinate progress bar with real percentage + stage ("Uploading… / Processing… / Rendering…"); contextual copy beats a bare spinner for multi-minute waits; user can navigate away — completion notified (toast + notification center entry), not a blocking modal. |
| Success | "Your export is ready." + download/open action; entry persists in a history/activity log (not only a transient toast). |
| Partial | 47 of 50 rows imported → "47 imported, 3 skipped." with the 3 listed and per-item [Retry]/[Download error report]; never report "done" when it wasn't. |
| Server error | Plain-language cause + [Retry] that resumes from the last checkpoint rather than restarting; checkpointing is the expected system behaviour for long jobs. |
| Network failure | Job continues server-side where possible; client shows "Connection lost — your export is still running. We'll notify you." Reconnect re-attaches to job status. |
| Cancelled | [Cancel] prominent during the run; on cancel: "Export cancelled — partial output was discarded." Server cleans up staging artifacts (documented failure mode: cancel races leaving partial files). |
| Expired session | Job ownership survives re-auth; status re-attaches on return. |
| Stale | Status polling shows "Last checked 30s ago" with manual refresh; polling backs off when tab hidden. |
| **Accessibility** | Progress exposed via `role="progressbar"` with `aria-valuenow`; stage changes announced politely; completion announced assertively; reduced-motion respected. |
| **Telemetry** | job_started, job_progress {stage, pct}, job_completed {duration}, job_failed {stage, class}, job_cancelled {stage}, notification_delivered. |
| **System** | Server-side job record with idempotency key; resumable checkpoints; cancel propagates to workers (AbortController lineage); no silent restarts; history retained per the product's retention policy. |

---

## Anti-patterns this matrix is designed to prevent

- Flashing an empty state before data arrives (no loading state in between).
- Blanking loaded content during refresh.
- One "Something went wrong" for every failure class, with no recovery path.
- Toast-only critical outcomes (screen-reader/magnifier users miss them; no replay).
- Auto-retrying non-idempotent writes (duplicate charges/orders).
- Collapsing first-use, no-results, cleared, and error empties into one message.
- Confirmation dialogs on reversible actions (habituation) and missing ones on irreversible ones.
- Silent staleness — serving cached data as if it were fresh.

*Polish details: `01-polish-details.md`. Demo checklist: `03-demo-authenticity.md`. Evidence: `04-evidence-register.md`.*
