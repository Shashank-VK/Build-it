# Phase 2 — Ranking Rubric (P2-01)

> **Purpose:** Every element in the Master Taxonomy is scored on a consistent 1-5 rubric so rankings are traceable, not intuition. Establishes S/A/B/C/D tiers per archetype.
> **Date:** 2026-09-01 | **Input:** `phase-1/MASTER_TAXONOMY.md` (48 elements) + `phase-0/ARCHETYPES_AND_CRITERIA.md` (C1-C6, SC-01..10)

## The 7 Rubric Dimensions (1-5 each)

| Dim | What it measures | 1 = | 5 = | Primary SC wired (from V-D P0-10) |
|-----|------------------|-----|-----|-----------------------------------|
| **1. Frequency** | How often needed across the 6 archetypes | Rarely (≤1 archetype, occasional) | Every run, all archetypes | SC-01, SC-04, SC-05 |
| **2. Harm if absent** | Capability/reliability/safety loss without it | Negligible; alternative exists | Catastrophic (SC-07 leak, SC-02 <50%) | SC-07, SC-03, SC-08, SC-06 |
| **3. Benefit** | Actual outcome improvement when present | Marginal | ≥+10pp TSR, major cost/safety win | SC-02, SC-08 |
| **4. Complexity cost** | Conceptual/config complexity it adds (inverse) | High (config hell, cognitive load) | Negligible (transparent) | SC-05 |
| **5. Maintenance burden** | Ongoing upkeep cost (inverse) | Heavy (drift, breakage) | Auto-maintaining | SC-10, SC-09 |
| **6. Security/risk impact** | Reduces risk (+) vs introduces new risk (−) | Introduces real risk | Strong risk reduction (block before exec) | SC-07 |
| **7. General applicability** | Transfers across project types | Single archetype only | All 6 archetypes | Variance-preservation rule |

## Tier Derivation (weighted, not fake precision)

| Capability's profile | Tier | Meaning |
|---------------------|------|---------|
| High Frequency (≥4) AND High Benefit (≥4) AND Low Harm-if-absent ≤2 wins | **S** | Fundamental / extremely important — non-negotiable core (mirrors the Master Taxonomy Foundational tier) |
| High on 2-3 dims, medium on rest, harm-if-absent ≥3 | **A** | Highly valuable for most serious workflows |
| Medium across the board; archetype-specific value | **B** | Useful, meaningful, not universally necessary |
| Low frequency, narrow archetype, situational | **C** | Specialized / situational |
| Redundant, declining, weak evidence, niche | **D** | Niche / redundant / declining / low priority |

**Harm 4-5 veto rule (from V-D):** any element with Harm-if-absent ≥4 that mitigates SC-07/SC-03/SC-08 CANNOT rank below median, regardless of Frequency. SC-07 (zero-leak) items are explicit veto class.

## Archetype-Dependent Rankings

Every element gets a **per-archetype tier** (S/A/B/C/D for C1-C6), NOT just one global tier. A global tier is provided for reference but never used to average away archetype differences.

## Scorecard Format (one per element)

```
Element: CAP-18 Procedural Skills Execution
  Frequency: 4  (skills used across C1/C4/C6 build + run)
  Harm if absent: 3 (no runbook capability → re-prompting waste, SC-01 penalty)
  Benefit: 4 (+progressive disclosure saves context; SC-05)
  Complexity: 3 (skill authoring adds authoring burden)
  Maintenance: 3 (skills rot; need pruning)
  Security: 3 (untrusted skill supply chain — mitigated by CAP-31)
  Generality: 5 (all archetypes have procedural needs)
  → Global tier: A | Per-archetype: C1=A, C2=B, C3=B, C4=S, C5=B, C6=B
  SC wiring: SC-01 (TTFUA), SC-05 (cost via progressive disclosure), SC-08 (gate)
  Evidence: batch-3 B3-06/07, translation matrix
```