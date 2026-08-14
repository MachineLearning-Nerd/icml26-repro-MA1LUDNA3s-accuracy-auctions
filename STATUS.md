# Audit status

## Current assessment

- Overall: `VERIFIED_SCOPED_WITH_BLOCKED_CLAIM`
- Evidence-release gate: `PASSED`
- Strict paper-level gate: `NOT_READY`
- Claims: 5 verified under declared scopes, 1 blocked, 0 falsified
- Attribution target: `MachineLearning-Nerd`

Claim 6 is blocked because the reported Figure 3 result is existential and the
paper does not specify enough preprocessing, tuning, seed, or raw-data details
to verify or falsify the authors' exact configuration. The observed routes are
evidence about those routes, not a universal counterexample.

## Source and release

- Paper: *Welfare-Optimal Classification with Accuracy Auctions*
- Authors: Bana Sadi, Eden Saig, and Nir Rosenfeld
- Source: [arXiv 2606.02435v2](https://arxiv.org/abs/2606.02435)
- Audited PDF SHA-256: `7671522004bedd62d9051e848cccf360d6fd4f17ecc681edfeb33990677c1f6a`
- Competition identifier: `MA1LUDNA3s`
- Published Space revision: `1d9f5ffa9259a22f633cc426250fc3f190158186`
- Recorded judge result: `5/12`; no score increase is claimed
- Formal cumulative run: 773 seconds; its nonzero exit was expected because
  Claim 6 is blocked

The canonical machine-readable record is [`publication_gate.json`](publication_gate.json).
The detailed evidence release is under [`release/`](release/), and the
claim-by-claim narrative is [`reports/claim-by-claim/report.md`](reports/claim-by-claim/report.md).
