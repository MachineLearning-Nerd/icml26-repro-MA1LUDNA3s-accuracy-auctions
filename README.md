# Claim-by-claim reproduction: five verified, one blocked

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/blob/master/notebooks/accuracy_auctions_reproduction.py)

We reproduced all six judged claims in
*Welfare-Optimal Classification with Accuracy Auctions* (arXiv 2606.02435).
Claims 1–5 are **VERIFIED** under explicit machine-checkable contracts. Claim 6
is **BLOCKED** after three faithful 30,000-person routes and a fourth
falsification audit: the routes found 19.52%, 19.91%, and 19.65% welfare gains
versus the paper's “up to 23%,” while closely matching its reported accuracy
change. The paper's existential wording and missing preprocessing/tuning
details prevent a valid verification or assumption-complete counterexample.

This replaces the earlier small single-seed checks with exact breakpoint
certificates (Claims 1 and 4), 64× asymptotic sweeps with 20 seeds (Claims 2 and
3), and actual held-out classification accuracy over 890 datasets (Claim 5).
Claim 6 uses ACS/Folktables records and documents every unresolved
substitution. Formal runs used an 8-core local Apple CPU; only Claim 6 moved to
Hugging Face `cpu-upgrade` after the local host was measured at sustained
overload. No GPU was used.

- [Illustrated claim-by-claim report](reports/claim-by-claim/report.md)
- [Self-contained Marimo tutorial](notebooks/accuracy_auctions_reproduction.py)
- [Durable machine-readable evidence](.openresearch/artifacts)

| Claim | Paper result | Observed evidence | Assessment |
|---|---|---|---|
| 1 | Bid-monotone weighted ERM | 24,543 primary and 206,325 independent comparisons; zero violations | **VERIFIED** |
| 2 | Linear-classifier payments are \(O(1)\) | Payment/payer tail exponents 0.0730/0.0081 over \(m=250\ldots16,000\) | **VERIFIED** |
| 3 | Noisy k-NN payments are \(\Omega(m)\) | Exponents 1.0112 and 1.0210 over \(m=500\ldots32,000\) | **VERIFIED** |
| 4 | No payment exceeds reported value | 182 primary and 441 independent cases; zero violations | **VERIFIED** |
| 5 | Payer plateau and negative accuracy association | Seven plateau contracts and six held-out-accuracy contracts pass | **VERIFIED** |
| 6 | Welfare gain up to 23%; reported relative accuracy change -21% | Welfare +19.52% to +19.91%; accuracy -20.49% to -20.85% | **BLOCKED** |

## Experiment log

Every formal experiment inherited the exact command
`uv run --frozen python repro/src/verify_auctions.py`; variants are committed
code, never command-line knobs.

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| `master` | Publication surface | Not run as an experiment (publication surface) | README, report, and notebook target after approval | — |
| [`orx/frozen-judged-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/tree/orx/frozen-judged-baseline) | Immutable judged baseline | `uv run --frozen python repro/src/verify_auctions.py` | Existing toy checks reproduced | Local CPU, 5m02s |
| [`orx/exact-theorem-contracts`](https://github.com/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/tree/orx/exact-theorem-contracts) | Exact Claims 1 and 4 contracts | `uv run --frozen python repro/src/verify_auctions.py` | Claims 1 and 4 VERIFIED | Local CPU, 4m16s |
| [`orx/assumption-faithful-asymptotics`](https://github.com/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/tree/orx/assumption-faithful-asymptotics) | 64× Claims 2 and 3 sweeps | `uv run --frozen python repro/src/verify_auctions.py` | Claims 2 and 3 VERIFIED | Local CPU, 2m30s |
| [`orx/faithful-figure-2-payments-and-accuracy`](https://github.com/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/tree/orx/faithful-figure-2-payments-and-accuracy) | Real held-out accuracy and plateau sweeps | `uv run --frozen python repro/src/verify_auctions.py` | Claim 5 VERIFIED | Local CPU, 4m11s |
| [`orx/folktables-figure-3-welfare-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/tree/orx/folktables-figure-3-welfare-audit) | Claim 6 route 1: published ACS task | `uv run --frozen python repro/src/verify_auctions.py` | +19.52%; BLOCKED by preregistered band | HF CPU, 12m41s |
| [`orx/paper-mapped-folktables-preprocessing`](https://github.com/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/tree/orx/paper-mapped-folktables-preprocessing) | Claim 6 route 2: binary attributes and semantic occupation groups | `uv run --frozen python repro/src/verify_auctions.py` | +19.91%; BLOCKED by 0.09 point | HF CPU, 13m29s |
| [`orx/nested-regularization-folktables-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/tree/orx/nested-regularization-folktables-audit) | Claim 6 route 3: inner-training-only tuning | `uv run --frozen python repro/src/verify_auctions.py` | +19.65%; BLOCKED | HF CPU, 13m46s |
| [`orx/claim-6-falsification-and-quantifier-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-MA1LUDNA3s-accuracy-auctions/tree/orx/claim-6-falsification-and-quantifier-audit) | Claim 6 route 4: mandatory counterexample search | `uv run --frozen python repro/src/verify_auctions.py` | Falsification not established; BLOCKED | HF CPU, 12m43s |

Notebook validation uses the pinned Marimo 0.15.5 runtime. That version predates
the `marimo check` command, so the notebook is instead byte-compiled and fully
executed through `marimo export html`; the export completes without failed
cells.

---

# Repro — Welfare-Optimal Classification with Accuracy Auctions
ICML 2026 Agent Reproduction Challenge. OpenReview `MA1LUDNA3s`. arXiv `2606.02435`.
6 claims / 12 pts. Clean-room numpy verification of the accuracy-auction mechanism
(monotonicity, Myerson payments, L2 O(1) vs kNN Ω(m) payment scaling, IR, welfare). Owner: loop12pt.
