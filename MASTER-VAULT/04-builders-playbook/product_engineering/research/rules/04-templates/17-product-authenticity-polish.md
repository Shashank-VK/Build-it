# Template 17 — Product Authenticity & Polish Checklist

**Use when:** before any user-facing launch or demo that represents the product. "Authentic" = what the user sees is what the product is; "polished" = the details hold up under attention. Check literally — this is a Gawande-style killer-items list.

## 1. Visual identity

- [ ] Logo, name, and visual language are consistent across every surface (no mixed identities)
- [ ] No default-framework styling visible where the brand should be (unstyled scaffolds, default fonts on key surfaces)
- [ ] Favicon, title tags, and social/OG metadata present and correct
- [ ] Visual quality holds at the marketing surface *and* three clicks deep (polish can't be landing-page-only)

## 2. Functional completeness

- [ ] Every visible control does something real — no dead buttons, dead links, or decorative inputs
- [ ] Every advertised capability works on real data (see template 07's reality inventory for demos)
- [ ] No "coming soon" placeholders on primary flows (or they're honest, dated, and rare)
- [ ] Permissions/roles actually enforced, not just hidden in the UI

## 3. Responsive

- [ ] Core flows verified at 360px / 768px / 1280px on a real device (template 12, §3)
- [ ] No horizontal scroll, no overlapping text, no unreachable controls at any width
- [ ] Touch targets and hover-independence verified on mobile

## 4. Accessibility

- [ ] Keyboard-only completion of core flows
- [ ] Focus visible; semantic markup; icon-only controls named
- [ ] Contrast AA on body text; reduced-motion respected
- [ ] Form errors associated and announced

## 5. Content quality

- [ ] Zero lorem ipsum, TODO, or placeholder copy anywhere user-visible
- [ ] Copy is in the user's language — no developer jargon in user-facing text
- [ ] Empty states are helpful (explain + next action), not blank
- [ ] Dates, numbers, currencies localised

## 6. Realistic demos

- [ ] Demo uses production-shaped data, not perfect fixtures
- [ ] Simulated capabilities disclosed wherever the demo is shown (template 07)
- [ ] The demo path is a real code path — no demo-only branches

## 7. UX states

- [ ] Loading, empty, error, offline, permission-denied, rate-limited, destructive-confirm, and success states all designed and verified (template 12, §2)

## 8. Security

- [ ] ASVS L1 gap register complete for the launched surface (template 13)
- [ ] No secrets in client-visible code, URLs, or error messages
- [ ] Auth and session behaviour sane (logout works, sessions expire, passwords handled per ASVS)

## 9. Privacy

- [ ] Data collection disclosed; consent where required
- [ ] Minimum-necessary data actually practised (no speculative harvesting)
- [ ] Data deletion / export path exists where regulation or promise requires it
- [ ] Third-party scripts/trackers inventoried and justified

## 10. Trust

- [ ] Pricing/fees shown honestly — no drip pricing or hidden costs
- [ ] Claims on the marketing surface are true of the product *today* (AP-14)
- [ ] Contact/support path real and monitored; status page exists if uptime is promised
- [ ] Terms and policies present, readable, and consistent with behaviour

## Acceptance criteria

- [ ] Every section checked or N/A with a written reason — no silent skips
- [ ] Failures are filed as blocking bugs with owners, not noted and shipped
- [ ] A second person (not the builder) ran this checklist

## Anti-patterns this blocks

AP-03 (generic design) · AP-12/13/15 (interaction/responsive/states gaps) · AP-14 (misleading demos) · AP-08 (security/privacy theatre).
