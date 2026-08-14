# ICML 2026 reproduction — Welfare-Optimal Classification with Accuracy Auctions

**Collection status:** `VERIFIED_SCOPED_WITH_BLOCKED_CLAIM`

**Evidence-release gate:** `PASSED`

**Strict paper-level gate:** `NOT_READY` for universal proof replacement or
exact recovery of the unavailable Figure 3 configuration.

**Owner and attribution:** `MachineLearning-Nerd`

This repository audits *Welfare-Optimal Classification with Accuracy Auctions*
by Bana Sadi, Eden Saig, and Nir Rosenfeld. The authoritative audited source is
[arXiv 2606.02435v2](https://arxiv.org/abs/2606.02435), listed as an ICML 2026
paper. The downloaded PDF SHA-256 is
`7671522004bedd62d9051e848cccf360d6fd4f17ecc681edfeb33990677c1f6a`.
The competition/reproduction identifier is `MA1LUDNA3s`.

The original repository name was
`icml26-repro-MA1LUDNA3s-accuracy-auctions`. The target public name is
`icml26-welfare-optimal-classification`.

## What the paper is doing

The paper treats prediction accuracy as a scarce resource whose value differs
across users. A classifier induces an allocation: a user receives the resource
when the prediction is correct. The system therefore needs to maximize
value-weighted welfare while eliciting private user values truthfully.

The proposed accuracy auction uses weighted empirical-risk minimization to
choose the classifier, proves bid-monotone allocation for score-based models,
and uses critical-value/Myerson payments for truthful reporting. The paper
also studies payment scaling: regularized linear classifiers have bounded
payments, while noisy fixed-k k-nearest-neighbor models can have linear payment
growth. Its experiments examine payer counts, held-out accuracy, welfare, and
the accuracy/welfare trade-off on ACS data.

## Evidence status by paper claim

The labels below describe the finite, conditional, or empirical contract that
was actually checked. They do not turn numerical evidence into a replacement
for the paper's universal proofs.

| Claim | Paper target | Scoped status | Recorded evidence |
| --- | --- | --- | --- |
| C1 | Theorem 1 — bid-monotone weighted ERM allocation | `VERIFIED_SCOPED_PROOF_AUDIT` | 24,543 primary and 206,325 independent comparisons; zero violations; 12 negative-control witnesses |
| C2 | Theorem 2 — regularized linear payments are `O(1)` | `VERIFIED_SCOPED_CONDITIONAL` | 64× sample-size sweep, 20 seeds, tail exponents 0.0730/0.0081, stability-band checker |
| C3 | Theorem 3 — noisy k-NN payments are `\(\Omega(m)\)` | `VERIFIED_SCOPED_CONDITIONAL` | Two fixed-`k` routes, 20 seeds, positive 99% tail bounds, exponents 1.0112/1.0210, zero-noise control |
| C4 | Corollary 1 — individual rationality and payment ≤ value | `VERIFIED_SCOPED_PROOF_AUDIT` | 182 primary and 441 independent threshold cases; zero violations; overcharge control detects 12 violations |
| C5 | Figure 2 — payer plateau and accuracy association | `VERIFIED_SCOPED_EMPIRICAL` | Plateau and held-out-accuracy contracts pass; 350 plateau and 540 accuracy datasets |
| C6 | Figure 3 — welfare up to 23% and approximately −21% accuracy change | `BLOCKED_UNDER_SPECIFIED_PROTOCOL` | Four routes and two figure digitizations cannot close missing preprocessing/tuning/seed assumptions; not falsified |

Claims 1–5 are verified only under their declared scopes. Claim 6 remains
blocked because the paper's “up to 23%” statement is existential: routes below
23% neither verify nor disprove the existence of the author's configuration.

## Claim-to-evidence production paths

| Claim | Producer path | Canonical evidence |
| --- | --- | --- |
| C1 monotonicity | `repro/src/verify_auctions.py` → exact breakpoint/threshold checks and independent lower-envelope checker | `release/hf-space-text/evidence/2026-07/claim_1/` |
| C2 linear payments | `repro/src/verify_asymptotics.py` → fixed-`lambda` sweep, stability-band checker, and linear-growth negative control | `release/hf-space-text/evidence/2026-07/claim_2/` |
| C3 k-NN payments | `verify_asymptotics.py` → two fixed-`k` routes, 20 seeds, and no-noise control | `release/hf-space-text/evidence/2026-07/claim_3/` |
| C4 individual rationality | `verify_auctions.py` → critical-value payments and DSIC/IR enumeration; independent payment identity | `release/hf-space-text/evidence/2026-07/claim_4/` |
| C5 Figure 2 | `repro/src/verify_figure2.py` → plateau and held-out-accuracy association checks | `release/hf-space-text/evidence/2026-07/claim_5/` |
| C6 Figure 3 | `repro/src/verify_folktables.py` and `verify_claim6_falsification.py` → four declared routes and figure digitization | `release/hf-space-text/evidence/2026-07/claim_6/` |
| Aggregate release | `release/candidate-validation.json` and `publication_gate.json` → six claim pages, manifests, figures, notebook, and secret scan | `release/` and `reports/claim-by-claim/report.md` |

## Experiment branches

Every formal experiment inherited:

```text
uv run --frozen python repro/src/verify_auctions.py
```

| Final branch | Purpose | Outcome |
| --- | --- | --- |
| `main` | Canonical publication surface | README, report, notebook, and scoped gate |
| `baseline/frozen-judged-baseline` | Immutable judged baseline | Historical toy checks |
| `audit/exact-theorem-contracts` | Exact C1/C4 contracts | Scoped proof audits |
| `research/assumption-faithful-asymptotics` | C2/C3 64× asymptotic sweeps | Scoped conditional evidence |
| `research/figure-2-payments-accuracy` | C5 plateau and held-out accuracy | Scoped empirical evidence |
| `research/claim-6-route-1` | Published ACS/Folktables route | +19.52%; blocked by declared band |
| `research/claim-6-route-2` | Paper-mapped preprocessing route | +19.91%; blocked by 0.09 point |
| `research/claim-6-route-3` | Nested-regularization route | +19.65%; blocked |
| `audit/claim-6-falsification` | Quantifier and falsification audit | Falsification not established; blocked |
| `release/claim-by-claim-evidence` | Cumulative evidence release candidate | C1–C5 pass; C6 intentionally blocks |

The old `master` and `orx/*` names are retained only in `BRANCH_AUDIT.md` as
provenance; they are not the final public branch policy.

## Recorded release evidence

- Claims verified: 5/6; Claim 6: blocked; no claim is marked falsified.
- Formal cumulative run: 773 seconds, with the expected nonzero exit because
  Claim 6 is blocked.
- Local formal runs used an 8-core Apple CPU; Claim 6 routes used Hugging Face
  `cpu-upgrade`; no GPU was used.
- Published Space: `DineshAI/MA1LUDNA3s`, revision
  `1d9f5ffa9259a22f633cc426250fc3f190158186`.
- Recorded live judge head: 5/12; no score increase is claimed.
- The additive release candidate preserved all 17 judged Space paths and
  verified 85 uploaded file hashes.

## Reproduce and inspect

The locked environment is declared in `pyproject.toml` and `uv.lock`.

```bash
uv sync --frozen
uv run --frozen python repro/src/verify_auctions.py
uv run --frozen python -m py_compile notebooks/accuracy_auctions_reproduction.py
uv run --frozen marimo export html notebooks/accuracy_auctions_reproduction.py \
  -o /tmp/accuracy-auctions-notebook.html
```

The full formal command can take several minutes and intentionally exits
nonzero when the blocked Claim 6 contract is included. Use the claim evidence
directories and `release/candidate-validation.json` to inspect the recorded
release without rerunning the full campaign.

## Repository contents

- `repro/src/` — mechanism, asymptotic, Figure 2, Folktables, and falsification
  verifiers.
- `release/hf-space-text/evidence/` — canonical claim-by-claim contracts,
  methods, raw outputs, independent checkers, negative controls, and limits.
- `.openresearch/artifacts/` — durable machine-readable evidence for Claims 1–5.
- `reports/claim-by-claim/report.md` — illustrated narrative report.
- `notebooks/accuracy_auctions_reproduction.py` — self-contained tutorial.
- `release/` — release manifest, commands, compute accounting, and published
  Space validation.
- `outputs/` — historical compatibility artifacts; see `outputs/README.md`.

## Citation

```bibtex
@article{sadi2026welfare,
  title   = {Welfare-Optimal Classification with Accuracy Auctions},
  author  = {Sadi, Bana and Saig, Eden and Rosenfeld, Nir},
  journal = {arXiv preprint arXiv:2606.02435},
  year    = {2026},
  note    = {ICML 2026}
}
```

## Thank you

Thank you to Bana Sadi, Eden Saig, and Nir Rosenfeld for making the accuracy
auction mechanism, payment analysis, and experimental targets precise enough
to support a claim-by-claim clean-room audit. This repository is unofficial;
the authors did not review or endorse these results.
