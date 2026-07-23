# Claim 5 — VERIFIED

## Exact contract

Payer counts plateau with sample size across variance settings, and higher
held-out classification accuracy—not allocation rate—is associated with a
lower payer proportion.

## Evidence

- Plateau study: **350 datasets**, m=4,096–65,536, seven variance settings,
  ten seeds; every upper 99% slope bound satisfies the contract.
- Accuracy study: **540 datasets**, six dimensions, nine signal settings, ten
  seeds.
- Mean Spearman associations: **-0.698 to -0.981**; every upper 99% bound is
  negative.
- Shuffled-label control removes the relationship.
- Independent missed-payer screen: **0**.

The formal experiment is branch
`orx/faithful-figure-2-payments-and-accuracy`, commit
`8c78c9e8a1e115e830f5b4082aa2821892df3a57`, run
`fe5ad2f9-f5bc-4bcd-b5c6-fe42efdde61b`.

Raw and supporting files are under `evidence/2026-07/claim_5/`.

