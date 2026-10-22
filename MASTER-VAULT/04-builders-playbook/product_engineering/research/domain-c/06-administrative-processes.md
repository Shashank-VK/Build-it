# Domain C — AI Automating Organisational Work: Administrative Processes

**Workstream:** domain-c · **Area 6 of 8** · Researched 2026-10-10

> Scope: AI handling back-office administration — invoice/accounts-payable processing, expense handling, insurance claims, document-heavy compliance workflows, HR paperwork. High-volume, rules-bound, audit-sensitive. This is the oldest AI-automation territory (OCR + RPA predate LLMs) and has the most concrete numbers — but also the clearest evidence of brittleness.

**Plain-English terms:**
- **IDP (intelligent document processing)** — AI that reads documents (invoices, claims, forms) and extracts structured data: vendor, date, line items, totals. Concrete example: a scanned PDF invoice becomes rows in a spreadsheet without retyping.
- **RPA (robotic process automation)** — software bots that click through existing applications following fixed if-then rules. Deterministic: "if the button is blue, click it." Works until anything changes.
- **PO matching** — checking an invoice against its purchase order before paying. The step where most exceptions live.
- **Straight-through processing** — an invoice/claim going from arrival to payment with zero human touches. The headline metric; the exceptions are the real story.

---

## 1. How organisations deploy it

The standard AP/claims pipeline:

1. **Capture**: invoices arrive by email/portal → AI OCR/IDP extracts fields (vendor, number, dates, line items, totals).
2. **Validation**: totals checked, duplicates flagged, PO matched automatically.
3. **Exception routing**: clean invoices flow straight through; mismatches route to the right approver with the discrepancy highlighted.
4. **Posting & payment**: approved invoices posted to ERP (SAP, QuickBooks, etc.); payment runs scheduled.
5. **Audit trail**: every touch logged for compliance.

Human involvement concentrates at step 3 — "AP coordinator reviews flagged exceptions only."

## 2. Documented cases

### Invoice processing — the numbers
- **Baseline [Verified — Ardent Partners State of ePayables 2024]**: companies without automation average **$12.88 and 17.4 days per invoice**; best-in-class save $10+ per invoice and ~2 weeks.
- **Certas Energy** (UK's largest independent fuel distributor) [vendor-published via ABBYY/Blue Prism — **Corroborated**, vendor-framed]: up to **30 minutes → ~1 minute per invoice** using ABBYY OCR + Blue Prism digital workers.
- **PAPCO** (energy supplier, 600,000+ invoices/year from 1,000+ vendors) [vendor-published via ABBYY — **Unverified**]: ~50% cut in manual AP labour; daily processing time cut by up to 6 hours; invoice approval from an hour a day to minutes.
- **Meridian / InvoiceToData** (logistics firm) [vendor case study — **Unverified**]: onboarding under a day; **~30 seconds per invoice** including human review of exceptions; **97% reduction** in per-invoice time. Notable detail: the AI handled even badly-scanned fax invoices — robustness on ugly inputs is the differentiator, not clean PDFs.
- **Tesco PLC** [academic case-study table citing company sources — **Corroborated**]: OCR invoice processing cut back-office processing time by roughly one-third.

### Insurance claims — Greek insurer (Archeiothiki "AI Flows")
- **What [Verified — IndexBox, Oct 2026]**: at one of Greece's biggest insurance providers, health-insurance claim settlement went from **14 days to ~1 minute** (payout next day). The system processes **~1,500 claims/day** — scanning paperwork, extracting details, verifying against policy and insurer rules.
- **The under-reported win**: the system made it possible to **review every single case instead of a sample**, catching fraud that sampling missed. Automation changed the *assurance model*, not just the speed.
- Deployed across ~100 workflows for 10 clients (banks, insurers, healthcare).

### RPA brittleness — the negative evidence
- **Practitioner account (Ryan McCain, Medium, Mar 2026 — first-hand/community)**: a CFO's company spent 18 months building an RPA "digital workforce" for invoice/PO matching; "a vendor added a hyphen to a date field on their invoice template. The entire pipeline choked." The team spent more time fixing bot mistakes than the bots saved — **net negative on productivity**. "That is not automation. That is just relocating the manual labor from data entry to bot maintenance."
- **Industry pattern (coasty.ai practitioner analysis — Corroborated direction, numbers Unverified)**: ~**30% of RPA projects abandoned within 12 months**; large RPA shops spend **30–50% of annual budget on maintenance** rather than new automations; failure rates on changing UIs climb above 15%. "A single UI refresh can require a full bot rebuild."
- **The 3 AM pager (coasty.ai)**: unattended invoice-clearing bots halt on SAP UI updates; on-call developers patch selectors and redeploy. Automation becomes "a liability instead of a safety net."
- **Shared-services failure taxonomy (iteratorshq practitioner analysis — first-hand/community)**: finance AP routing assumes clean POs; expense approvals depend on undocumented "CC this person or it stalls" rules; reconciliations quietly depend on one analyst's spreadsheet; month-end numbers are right only because someone manually fixes them before the deck. "The undocumented exception is the problem, and the automation just made it move faster."

## 3. Measured outcomes

| Metric | Value | Label |
|---|---|---|
| Cost/time per invoice, unautomated baseline | $12.88 / 17.4 days | Verified (Ardent Partners 2024) |
| Per-invoice time, Certas Energy | 30 min → ~1 min (−93%) | Corroborated, vendor-published |
| Manual AP labour, PAPCO | −50% | Unverified (vendor) |
| Per-invoice time, Meridian | −97% (~30 sec) | Unverified (vendor) |
| Insurance claim settlement, Greek insurer | 14 days → ~1 min | Verified (press) |
| RPA projects abandoned within 12 months | ~30% | Corroborated direction (practitioner) |
| RPA annual budget spent on maintenance | 30–50% | Unverified (practitioner) |

## 4. Failure modes

1. **Template drift**: a vendor changes an invoice layout; pixel-coordinate or selector-based extraction breaks silently or crashes.
2. **Undocumented-exception automation**: the bot encodes the happy path; the real process lives in unwritten rules and one person's spreadsheet.
3. **Silent wrong-number extraction**: the bot grabs the wrong total and posts it — worse than a crash, because nothing alerts.
4. **PO-matching gaps**: invoices without clean POs stall; approval routing to departed managers; vendor-name duplicates ("three spellings of the same vendor").
5. **Maintenance-load inversion**: bot upkeep exceeds the labour saved (the 18-month net-negative case).
6. **Compliance theatre**: structured e-invoicing (e.g. Italy's SDI) removes OCR but *not* the approval/exception work — automating capture doesn't automate judgment.

## 5. Human oversight / approval design

- **Exception-only review**: humans handle mismatches, unusual line items, missing PO matches — not every invoice.
- **Tolerance thresholds**: auto-post below amount/vendor-risk limits; anything above routes to approval.
- **Maker-checker**: AI extracts (maker), human approves payment (checker) — standard financial control, preserved.
- **Extraction-confidence flags**: low-confidence fields highlighted for review rather than silently posted.
- **Change monitoring**: alerts when vendor templates or ERP UIs change, before the bot fleet breaks.

## 6. Cost vs benefit

- The business case is the clearest in Domain C: $12.88 → <$3 per invoice at volume pays back fast *when the process is standardised first*.
- The failure case is equally clear: automating an undocumented, exception-heavy process with brittle RPA yields net-negative productivity plus a maintenance burden of 30–50% of budget.
- Practitioner consensus: standardise and document the process *before* automating; IDP (AI reading documents) is more durable than RPA (bots clicking UIs) because it doesn't depend on screen layouts.

## 7. Data governance / privacy

- Invoices and claims contain PII, bank details, salary-adjacent data — extraction pipelines need encryption, access logging, and retention limits.
- Claims automation in insurance/healthcare touches medical data (HIPAA/GDPR special-category data) — the Greek case's every-case review is a privacy surface as well as a fraud win.
- Vendor IDP/RPA platforms become sub-processors with broad financial-data access; data-residency and deletion rights need contracts, not assumptions.

## 8. Open gaps

- Few independent measurements of *sustained* straight-through-processing rates (vendors quote peaks).
- The maintenance-burden figures (30–50%) are practitioner-reported, not from controlled studies.
- Little public data on fraud/error rates *introduced* by mis-extraction vs caught by automation.
