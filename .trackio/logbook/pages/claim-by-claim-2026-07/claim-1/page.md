# Claim 1 — VERIFIED

## Exact contract

For weighted empirical risk minimization, holding all other bids fixed, a
selected user's allocation cannot change from 1 to 0 when that user's bid
increases. Tied optima are included.

## Evidence

- Primary exact antecedents: **24,543**; violations: **0**.
- Independent optimal-pair comparisons: **206,325**; violations: **0**.
- Reversed-threshold negative-control witnesses: **12**.

This is a finite breakpoint certificate, not a sampled bid grid. The formal
experiment is branch `orx/exact-theorem-contracts`, commit
`ece2eb14505a7204baae254ae90e731ce0ab43c5`, run
`d4df98b9-99b1-4893-8d57-9016c2c26221`.

Raw and supporting files are under `evidence/2026-07/claim_1/`.

