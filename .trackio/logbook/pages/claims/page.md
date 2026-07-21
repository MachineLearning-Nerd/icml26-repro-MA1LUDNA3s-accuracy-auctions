# Claims


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_a3c488760435", "created_at": "2026-07-21T07:43:25+00:00", "title": "Claims to reproduce"}
-->
## Claims to reproduce

1. Theorem 1 proves that allocations produced by weighted empirical risk minimization are monotonically increasing in each user's individual bid, which enables construction of a truthful payment rule via Myerson's Lemma (Theorem 1).
2. Theorem 2 proves that for L2-regularized linear classifiers, the expected total payments collected by the accuracy auction are O(1), i.e., bounded by a constant independent of the number of samples m (Theorem 2).
3. Theorem 3 proves that k-nearest-neighbor classifiers exhibit Ω(m) expected total payments under label noise, showing that the choice of learning algorithm materially affects auction revenue/payment scaling (Theorem 3).
4. Corollary 1 establishes individual rationality: no user's payment ever exceeds their reported valuation for accuracy under the mechanism (Corollary 1).
5. Experiments show the number of paying users plateaus quickly as sample size increases across different variance parameter settings, and higher model accuracy is associated with lower payment proportions (Section 7, Figure 2).
6. Optimizing the accuracy-auction objective against a uniform-allocation baseline yields social welfare improvements of up to 23% with only modest accuracy tradeoffs (Section 7, Figure 3).
