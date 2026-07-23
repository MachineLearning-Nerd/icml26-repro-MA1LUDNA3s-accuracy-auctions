# Claim 2 — VERIFIED

## Exact contract

Under the theorem's L2-regularized linear-classifier setting, expected total
payment remains bounded in sample size. The operational contract uses
predeclared tail-exponent, convergence, stability-band, and control checks.

## Evidence

- Sample sizes: 250–16,000 (**64×**); **20 seeds**.
- Tail exponent, total payment: **0.0730**.
- Tail exponent, payer count: **0.0081**.
- Optimization convergence: all runs.
- Independent brute-force payers outside stability band: **0**.
- Injected linear-growth control exponent: **1.0000**, rejected as intended.

The formal experiment is branch `orx/assumption-faithful-asymptotics`, commit
`51bf840`, run `2242b9a6-fea8-4d5b-925e-a27d9d363de8`.

Raw and supporting files are under `evidence/2026-07/claim_2/`.

