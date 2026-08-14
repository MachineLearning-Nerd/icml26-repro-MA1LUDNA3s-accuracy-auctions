# Source and evidence manifest

## Paper identity

| Field | Value |
| --- | --- |
| Title | *Welfare-Optimal Classification with Accuracy Auctions* |
| Authors | Bana Sadi; Eden Saig; Nir Rosenfeld |
| Venue | ICML 2026 |
| Authoritative source | [arXiv 2606.02435v2](https://arxiv.org/abs/2606.02435) |
| Reproduction identifier | `MA1LUDNA3s` |
| Audited PDF SHA-256 | `7671522004bedd62d9051e848cccf360d6fd4f17ecc681edfeb33990677c1f6a` |

The narrative report also records the SHA-256 of the ar5iv HTML source used for
the source audit: `abdd0eb6dbcb4bc119c71405ea5e0d944ec598efef39c8c8da776f545916654d`.

## Repository identity

- Original name: `icml26-repro-MA1LUDNA3s-accuracy-auctions`
- Target name: `icml26-welfare-optimal-classification`
- Owner and commit attribution: `MachineLearning-Nerd`
- Default branch target: `main`

## Evidence locations

| Evidence | Location | Role |
| --- | --- | --- |
| Claim contracts and outputs | `release/hf-space-text/evidence/2026-07/claim_1/` through `claim_6/` | Canonical claim-level methods, raw results, independent checks, controls, and limitations |
| Cumulative release validation | `release/candidate-validation.json` | File, figure, notebook, secret-scan, and formal-run gate |
| Published revision validation | `release/published-revision.json` | Additive upload and retained judged-path checks |
| Compute accounting | `release/compute.json` | Local/Hugging Face duration, hardware, and cost estimate |
| Durable artifacts | `.openresearch/artifacts/` | Machine-readable evidence for Claims 1–5 |
| Claim narrative | `reports/claim-by-claim/report.md` | Human-readable assessment and source audit |
| Reproduction notebook | `notebooks/accuracy_auctions_reproduction.py` | Self-contained tutorial and executable overview |
| Gate summary | `publication_gate.json` | Current scoped publication state |

`outputs/verdict.json` is retained for compatibility with the original small
check. It is not the canonical release result; see [`outputs/README.md`](outputs/README.md).
