# Baseline source audit

Retrieved on 2026-07-23 with the explicit User-Agent recorded in
`source_record.json`. The primary ar5iv HTML has SHA-256
`abdd0eb6dbcb4bc119c71405ea5e0d944ec598efef39c8c8da776f545916654d`.

The exact formal and empirical anchors are:

- Theorem 1: `#Thmtheorem1`; for every user, every fixed profile of other bids,
  allocation is weakly increasing in that user's bid for the score-based ERM
  allocation of Equation 5. Appendix A.5 assumes a monotonically decreasing
  margin loss and exact loss minimization.
- Corollary 1: `#Thmcorollary1`; Myerson's payment rule makes the monotone
  allocation DSIC. Individual rationality additionally uses truthful bidding
  and the normalization that a zero bid entails zero payment.
- Informal Theorem 2: `#Thmtheorem2`; formal Theorem 4:
  `#Thmtheorem4`. The expectation is over i.i.d. random datasets. Assumptions
  include a linear classifier, L2 regularization, fixed lambda, bounded feature
  norm and density, bounded valuations, nonzero expected weighted signal, and a
  convex Lipschitz proxy loss differentiable near zero. Both expected payer
  count and expected revenue are bounded independently of sample size.
- Informal Theorem 3: `#Thmtheorem3`; formal Theorem 6:
  `#Thmtheorem6`. For a fixed sufficiently large k, a distribution must contain
  a positive-probability bounded region with conditional label probability
  strictly between eta and 1-eta, and neighbor valuations must have a
  sufficiently smooth density. Expected payer count and revenue are Omega(m).
- Figure 2: `#S7.F2`, Section 7.1 `#S7.SS1`. The plateau experiment uses
  balanced class-conditional Gaussians, d=16, class-mean distance 0.5, equal
  valuations, varying sigma, exact payments, and multiple trials. The
  accuracy/payment experiment uses m=500, sigma=1, varying mean separation and
  dimension; accuracy is actual classification accuracy.
- Figure 3: `#S7.F3`, Section 7.2 `#S7.SS2`. The Folktables ACSIncome setup uses
  New Jersey, random 30,000-example subsets split 60/40, and multiple trials.
  Feature-based values improve welfare by up to 5%. Label-based values
  `v(0)=1, v(1)=v+` yield reported gaps of +23% welfare and -21% accuracy.
  Thus the paper does not describe the 23% endpoint as a modest accuracy loss.

This baseline remains a judged numerical sanity-check control; no theorem is
treated as proven by its existing finite numerical sweep.
