# Claim 3 — VERIFIED

## Exact contract

Under label noise, k-nearest-neighbor total payments grow at least linearly in
sample size. The contract tests two fixed neighborhood sizes, uncertainty
across seeds, and the theorem's noise dependence.

## Evidence

- Sample sizes: 500–32,000 (**64×**); **20 seeds**.
- Tail exponent for k=31: **1.0112**.
- Tail exponent for k=63: **1.0210**.
- All one-sided 99% tail lower bounds are positive.
- With label noise removed: total payment **0**, payers **0**.

The formal experiment is branch `orx/assumption-faithful-asymptotics`, commit
`51bf840`, run `2242b9a6-fea8-4d5b-925e-a27d9d363de8`.

Raw and supporting files are under `evidence/2026-07/claim_3/`.

