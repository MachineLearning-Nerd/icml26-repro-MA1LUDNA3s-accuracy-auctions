# Branch audit and naming policy

## Target policy

The target public branch set has one default branch and purpose-prefixed
experiment branches:

- `main` — canonical publication surface and default branch
- `baseline/*` — immutable judged baselines
- `research/*` — scoped experiment routes
- `audit/*` — theorem, quantifier, and falsification audits
- `release/*` — cumulative evidence release

All approved commits are attributed to `MachineLearning-Nerd`. The legacy
`master` and `orx/*` names are historical provenance only and are scheduled for
removal from the public remote during the migration.

## Mapping

| Final branch | Legacy source | Purpose |
| --- | --- | --- |
| `main` | `master` | Canonical publication surface |
| `baseline/frozen-judged-baseline` | `orx/frozen-judged-baseline` | Immutable judged baseline |
| `audit/exact-theorem-contracts` | `orx/exact-theorem-contracts` | C1/C4 exact theorem contracts |
| `research/assumption-faithful-asymptotics` | `orx/assumption-faithful-asymptotics` | C2/C3 asymptotic routes |
| `research/figure-2-payments-accuracy` | `orx/faithful-figure-2-payments-and-accuracy` | C5 payer and accuracy checks |
| `research/claim-6-route-1` | `orx/folktables-figure-3-welfare-audit` | C6 published ACS route |
| `research/claim-6-route-2` | `orx/paper-mapped-folktables-preprocessing` | C6 paper-mapped preprocessing route |
| `research/claim-6-route-3` | `orx/nested-regularization-folktables-audit` | C6 nested-regularization route |
| `audit/claim-6-falsification` | `orx/claim-6-falsification-and-quantifier-audit` | C6 quantifier/falsification audit |
| `release/claim-by-claim-evidence` | current `master` | Cumulative evidence release candidate |

The legacy `orx/claim-by-claim-evidence-release-candidate` ref is not promoted
to a final branch because the current `master` contains the canonical release
surface and its published evidence metadata.

## Migration checklist

Before publication, verify all of the following against the remote:

- default branch is `main`;
- exactly the ten final branches above are public;
- no `master` or `orx/*` ref remains;
- every reachable commit on the final branches has `MachineLearning-Nerd`
  author and committer identity;
- README links and repository metadata use the target repository name.
