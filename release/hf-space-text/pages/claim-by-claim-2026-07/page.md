# Claim-by-claim evidence (2026-07)

This additive evidence release replaces no prior page. It preserves the exact
judged revision `c55042270cb78121f72a1a0ce1fffe8ef25bbaaa` and adds rigorous
contracts for all six claims.

## Outcome

| Claim | Verdict | Headline evidence |
| --- | --- | --- |
| [1](#/claim-1) | **VERIFIED** | 24,543 primary and 206,325 independent comparisons; zero violations |
| [2](#/claim-2) | **VERIFIED** | 64× sample-size sweep; payment/payer exponents 0.0730/0.0081 |
| [3](#/claim-3) | **VERIFIED** | 64× sweep; k-NN exponents 1.0112 and 1.0210 |
| [4](#/claim-4) | **VERIFIED** | 182 primary and 441 independent IR cases; zero violations |
| [5](#/claim-5) | **VERIFIED** | 350 plateau and 540 real held-out-accuracy datasets |
| [6](#/claim-6) | **BLOCKED** | Three 30,000-person routes plus a fourth falsification audit |

Every formal node inherited exactly:

```text
uv run --frozen python repro/src/verify_auctions.py
```

The environment is pinned by `uv.lock` under Python 3.12. Each evidence
directory contains a source audit, contract, method, raw outputs, verifier,
independent checker, negative control, environment, command, evaluation, and
limitations. Negative controls must fail as intended.

No GPU was used. Claims 1–5 ran on local CPU. Claim 6 used Hugging Face
`cpu-upgrade` only after local CPU overload was documented.

