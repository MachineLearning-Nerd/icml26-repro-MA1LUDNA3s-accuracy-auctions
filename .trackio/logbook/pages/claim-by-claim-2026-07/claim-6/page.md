# Claim 6 — BLOCKED

## Exact contract

The paper reports welfare improvement “up to 23%” and a relative accuracy
change near -21% against uniform allocation. Verification requires the
predeclared welfare band plus accuracy consistency. A falsification must match
every paper assumption and contradict the existential statement.

## Three verification routes

| Route | Distinct interpretation | Welfare gain | Relative accuracy change |
| --- | --- | ---: | ---: |
| 1 | Published task plus preprocessing sensitivities | 19.52% (95% CI 18.37–20.68) | -20.49% |
| 2 | Binary attributes plus semantic occupation groups | 19.91% (95% CI 18.71–21.11) | -20.62% |
| 3 | Inner-training-only nested regularization selection | 19.65% (95% CI 18.38–20.92) | -20.85% |

All routes use 30,000 ACS records. None enters the predeclared 20–26% mean
verification band.

## Mandatory fourth falsification route

Falsification was not established. Two independent Figure 3 digitizations
estimate welfare gains of 23.33% and 23.10%, consistent with the source. A
corrupted -9.33% endpoint is rejected as intended. The three alternate
configurations do not negate an existential “up to” statement, and the exact
author binary mappings, occupation boundaries, tuning protocol, seeds, and raw
Figure 3 data are unavailable.

The final verdict is therefore **BLOCKED**, not VERIFIED or FALSIFIED. Author
code or the missing specifications would unblock the claim.

The formal audit is branch
`orx/claim-6-falsification-and-quantifier-audit`, commit
`2088d5ee05a98759c47c6d13665ee158a8004575`, run
`aeccb3f2-f952-4438-908c-e0886bf4dcd1`.

Raw and supporting files are under `evidence/2026-07/claim_6/`.
