# Claim 4 — VERIFIED

## Exact contract

For every critical-bid allocation case, a user's payment must not exceed their
reported value. Payment identity and dominant-strategy inequalities are checked
at the same thresholds.

## Evidence

- Threshold/value cases: **182**.
- IR, payment, and DSIC violations: **0 / 0 / 0**.
- Independent comparisons: **441**; mismatches: **0**.
- Injected-overcharge negative-control violations: **12**.

The formal experiment is branch `orx/exact-theorem-contracts`, commit
`ece2eb14505a7204baae254ae90e731ce0ab43c5`, run
`d4df98b9-99b1-4893-8d57-9016c2c26221`.

Raw and supporting files are under `evidence/2026-07/claim_4/`.

