# Reproduction audit report

## Executive assessment

This is a clean-room, claim-by-claim audit of the ICML 2026 paper *Welfare-Optimal
Classification with Accuracy Auctions*. The recorded evidence-release gate
passes: the six claim pages, figures, notebook validation, upload allowlist,
hash checks, and secret scan are complete. The scientific assessment remains
scoped: Claims 1–5 pass their declared finite, conditional, or empirical
contracts; Claim 6 is blocked; no claim is falsified.

Passing a scoped contract does not replace a universal theorem proof. A blocked
claim is not a negative result when its paper configuration is underspecified.

## Paper-to-repository association

The paper studies a value-weighted accuracy auction. Weighted empirical-risk
minimization selects a classifier, the induced allocation is analyzed for
bid-monotonicity, and critical-value/Myerson payments support truthful reports.
The paper then studies bounded payment behavior for regularized linear models,
linear payment growth for noisy fixed-`k` nearest-neighbor models, and ACS
experiments involving payer counts, accuracy, and welfare.

The repository contains mechanism code, exact breakpoint checks, asymptotic
sweeps, held-out accuracy checks, ACS/Folktables routes, claim-level evidence,
and a publication manifest. It does not claim to contain the authors' private
training choices or missing Figure 3 raw data.

## Claim production ledger

| Claim | Producer | Evidence product | Assessment |
| --- | --- | --- | --- |
| C1 / Theorem 1 | `repro/src/verify_auctions.py` plus an independent lower-envelope checker | Exact breakpoint and threshold comparisons, negative control | `VERIFIED_SCOPED_PROOF_AUDIT` |
| C2 / Theorem 2 | `repro/src/verify_asymptotics.py` | Fixed-regularization sweep, stability-band checker, linear-growth control | `VERIFIED_SCOPED_CONDITIONAL` |
| C3 / Theorem 3 | `repro/src/verify_asymptotics.py` | Two fixed-`k` noisy routes, seed sweep, one-sided bounds, zero-noise control | `VERIFIED_SCOPED_CONDITIONAL` |
| C4 / Corollary 1 | `repro/src/verify_auctions.py` plus an independent payment identity | IR/threshold enumeration, DSIC checks, overcharge control | `VERIFIED_SCOPED_PROOF_AUDIT` |
| C5 / Figure 2 | `repro/src/verify_figure2.py` | Payer plateau and held-out accuracy association contracts | `VERIFIED_SCOPED_EMPIRICAL` |
| C6 / Figure 3 | `repro/src/verify_folktables.py` and `repro/src/verify_claim6_falsification.py` | Three ACS routes, two digitizations, and a quantifier audit | `BLOCKED_UNDER_SPECIFIED_PROTOCOL` |

## Controls and limitations

- C1 and C4 include independent checks and deliberately broken negative
  controls, so a passing result is more than a single implementation's output.
- C2 and C3 cover the recorded sample-size ranges and seeds; they remain finite
  evidence conditional on the declared model and parameter choices.
- C5 measures held-out classification accuracy rather than allocation rate and
  records its dataset and seed coverage.
- C6 reaches 19.52%, 19.91%, and 19.65% on three declared routes, while the
  paper's source digitizations support approximately 23%. Missing mappings,
  tuning protocol, seeds, raw values, and exact preprocessing prevent a valid
  universal conclusion.
- The published candidate is additive: all 17 judged Space paths were retained,
  and 85 uploaded hashes were checked. The recorded external score remains
  `5/12`; no score increase is claimed.

## Reproduction entry points

The locked entry point is:

```bash
uv run --frozen python repro/src/verify_auctions.py
```

The cumulative release is represented by `release/candidate-validation.json`.
Its expected nonzero status is part of the contract because Claim 6 is blocked.
Use the claim directories for recorded outputs before starting a new campaign.
