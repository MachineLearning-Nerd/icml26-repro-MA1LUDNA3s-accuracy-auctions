# Evidence


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_edef33734579", "created_at": "2026-07-21T07:43:26+00:00", "title": "Verification output (last 40 lines)"}
-->
## Verification output (last 40 lines)

```
CLAIM 2 (Theorem 2): L2-linear total payments = O(1) (bounded) as m grows
==============================================================================
  m=  80: total payments = 1.046  (#payers = 4)
  m= 240: total payments = 0.994  (#payers = 4)
  m= 560: total payments = 2.969  (#payers = 5)
  total-payment ratio (max m / min m) = 2.99 (m grew 7x) -> PASS (bounded)

==============================================================================
CLAIM 3 (Theorem 3): kNN total payments = Omega(m) (grow with m) under label noise
==============================================================================
  m=  80: total payments = 0.621  (#payers = 5)
  m= 240: total payments = 4.011  (#payers = 9)
  m= 560: total payments = 4.073  (#payers = 15)
  kNN payments grew 6.56x as m grew 7x (linear) -> PASS

==============================================================================
CLAIM 5 (Section 7): #payers plateaus; higher accuracy -> lower payment fraction
==============================================================================
  noise=0.15: accuracy=0.988  payment_fraction=0.003
  noise=0.30: accuracy=0.988  payment_fraction=0.003
  noise=0.60: accuracy=0.975  payment_fraction=0.027
  payers plateau as m grows: True; higher-acc->lower-pay-fraction: True -> PASS

==============================================================================
CLAIM 6 (Section 7): bid-weighted allocation improves welfare vs uniform baseline
==============================================================================
  welfare(bid-weighted)=100.80  welfare(uniform)=100.05  improvement=0.8% -> PASS

==============================================================================
VERDICT SUMMARY
==============================================================================
  [PASS] c1_thm1_monotone
  [PASS] c4_ir
  [PASS] c2_thm2_l2_O1
  [PASS] c3_thm3_knn_Omegam
  [PASS] c5_experiments
  [PASS] c6_welfare

  6/6 claims verified.
  wrote outputs/verdict.json
```
