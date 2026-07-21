"""Verify the six anchored claims of "Welfare-Optimal Classification with Accuracy Auctions"
(arXiv 2606.02435). Clean-room numpy, CPU."""
from __future__ import annotations
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import auctions as A

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "outputs")
os.makedirs(OUT, exist_ok=True)
results = {}
def banner(s): print("\n" + "=" * 78 + f"\n{s}\n" + "=" * 78)

V = 1.0  # bid max value


def make_data(m, dim=6, noise=0.3, seed=0, label_noise=0.0):
    rng = np.random.default_rng(seed)
    wstar = rng.standard_normal(dim)
    X = rng.standard_normal((m, dim))
    y = np.where(X @ wstar + rng.standard_normal(m) * noise >= 0, 1, 0)
    if label_noise > 0:
        flip = rng.random(m) < label_noise
        y[flip] = 1 - y[flip]
    bids = rng.uniform(0, V, m)
    return X, y, bids


def payments_with_ir(pipeline, bids, V):
    """Total payments honoring IR: p_i = critical_bid if a_i(bids)=1 else 0; returns (sum, npay, all_p)."""
    a = pipeline(bids)
    ps = np.zeros(len(bids))
    for i in range(len(bids)):
        if a[i] == 1:
            ps[i] = A.critical_bid(pipeline, i, bids.copy(), V)
    return float(ps.sum()), int((ps > 0).sum()), ps, a


# ---------------------------------------------------------------- Claim 1 (Theorem 1: monotonicity)
banner("CLAIM 1 (Theorem 1): allocation a_i is weakly increasing in bid b_i (L2 logistic)")
X, y, bids = make_data(120, seed=1)
pipe = A.make_logistic_pipeline(X, y)
violations = 0; tested = 0
grid_z = np.linspace(V / 20, V, 20)
for i in range(0, 120, 6):  # sample users
    seq = []
    for z in grid_z:
        b = bids.copy(); b[i] = z
        seq.append(pipe(b)[i])
    seq = np.array(seq)
    # weakly increasing: no 1->0 transition
    violations += int(np.any((seq[:-1] == 1) & (seq[1:] == 0)))
    tested += 1
c1 = violations == 0
print(f"  sampled {tested} users x 20 bid values; monotonicity violations (1->0 transitions): {violations} -> {'PASS' if c1 else 'FAIL'}")
results["c1_thm1_monotone"] = dict(passed=bool(c1), violations=int(violations), tested=int(tested))


# ---------------------------------------------------------------- Claim 4 (Corollary 1: IR, p_i <= b_i)
banner("CLAIM 4 (Corollary 1): individual rationality — payment never exceeds bid")
_, _, ps, _ = payments_with_ir(pipe, bids, V)
ir_ok = np.all(ps <= bids + 1e-9)
print(f"  max(p_i - b_i) over all users = {(ps - bids).max():.6f}  (must be <= 0) -> {'PASS' if ir_ok else 'FAIL'}")
results["c4_ir"] = dict(passed=bool(ir_ok), max_overpay=float((ps - bids).max()))


# ---------------------------------------------------------------- Claim 2 (Theorem 2: L2 payments O(1) in m)
banner("CLAIM 2 (Theorem 2): L2-linear total payments = O(1) (bounded) as m grows")
ms = [80, 240, 560]
c2_rows = []
for m in ms:
    X, y, bids = make_data(m, seed=7)
    pipe = A.make_logistic_pipeline(X, y, iters=300)
    tot, npay, _, _ = payments_with_ir(pipe, bids, V)
    c2_rows.append((m, tot, npay))
    print(f"  m={m:4d}: total payments = {tot:.3f}  (#payers = {npay})")
tots = [r[1] for r in c2_rows]
# O(1): total payments should NOT grow ~linearly with m; ratio last/first should be modest (< 3x for 7x m)
ratio = max(tots) / max(min(tots), 1e-6)
c2 = ratio < 3.0
print(f"  total-payment ratio (max m / min m) = {ratio:.2f} (m grew {ms[-1]//ms[0]}x) -> {'PASS (bounded)' if c2 else 'FAIL'}")
results["c2_thm2_l2_O1"] = dict(passed=bool(c2), ratio=float(ratio),
                              per_m={m: dict(total=float(t), payers=int(n)) for m, t, n in c2_rows})


# ---------------------------------------------------------------- Claim 3 (Theorem 3: kNN payments Omega(m))
banner("CLAIM 3 (Theorem 3): kNN total payments = Omega(m) (grow with m) under label noise")
c3_rows = []
for m in ms:
    X, y, bids = make_data(m, seed=9, label_noise=0.15)
    pipe = A.make_knn_pipeline(X, y, k=7)
    tot, npay, _, _ = payments_with_ir(pipe, bids, V)
    c3_rows.append((m, tot, npay))
    print(f"  m={m:4d}: total payments = {tot:.3f}  (#payers = {npay})")
tots3 = [r[1] for r in c3_rows]
slope = (tots3[-1] - tots3[0]) / (ms[-1] - ms[0])
c3 = tots3[-1] > 2.0 * tots3[0] and slope > 0
print(f"  kNN payments grew {tots3[-1]/max(tots3[0],1e-6):.2f}x as m grew {ms[-1]//ms[0]}x (linear) -> {'PASS' if c3 else 'FAIL'}")
results["c3_thm3_knn_Omegam"] = dict(passed=bool(c3), growth_ratio=float(tots3[-1]/max(tots3[0],1e-6)),
                                    per_m={m: dict(total=float(t), payers=int(n)) for m, t, n in c3_rows})


# ---------------------------------------------------------------- Claim 5 (experiments: payers plateau; accuracy↑ -> pay fraction↓)
banner("CLAIM 5 (Section 7): #payers plateaus; higher accuracy -> lower payment fraction")
# payers vs m (use c2 logistic rows): #payers should plateau (not grow like m)
payers = [r[2] for r in c2_rows]
plateau = payers[-1] < 2.0 * payers[0] and payers[-1] < 0.5 * ms[-1]
# higher accuracy -> lower payment fraction: vary noise, measure accuracy & pay_fraction
af = []
for noise in [0.15, 0.3, 0.6]:
    X, y, bids = make_data(160, seed=3, noise=noise)
    pipe = A.make_logistic_pipeline(X, y)
    a = pipe(bids)
    acc = a.mean()
    tot, npay, _, _ = payments_with_ir(pipe, bids, V)
    frac = tot / max(bids.sum(), 1e-9)
    af.append((noise, acc, frac))
    print(f"  noise={noise:.2f}: accuracy={acc:.3f}  payment_fraction={frac:.3f}")
# higher accuracy should correlate with lower payment fraction
accs = [r[1] for r in af]; fracs = [r[2] for r in af]
corr_ok = (accs[0] >= accs[-1] and fracs[0] <= fracs[-1])  # low-noise(high acc)->low frac
c5 = bool(plateau and corr_ok)
print(f"  payers plateau as m grows: {plateau}; higher-acc->lower-pay-fraction: {corr_ok} -> {'PASS' if c5 else 'FAIL'}")
results["c5_experiments"] = dict(passed=bool(c5), plateau=bool(plateau), corr=bool(corr_ok),
                                accuracy_payment=[dict(noise=float(n), acc=float(a), frac=float(f)) for n, a, f in af])


# ---------------------------------------------------------------- Claim 6 (welfare improvement vs uniform)
banner("CLAIM 6 (Section 7): bid-weighted allocation improves welfare vs uniform baseline")
X, y, bids = make_data(200, seed=5)
pipe = A.make_logistic_pipeline(X, y)
a_bids = pipe(bids)
a_unif = pipe(np.ones_like(bids))
welfare_bids = float(np.sum(bids * a_bids))
welfare_unif = float(np.sum(bids * a_unif))   # same bids, but allocation from uniform training
improve = (welfare_bids - welfare_unif) / max(welfare_unif, 1e-9) * 100
c6 = improve > 0
print(f"  welfare(bid-weighted)={welfare_bids:.2f}  welfare(uniform)={welfare_unif:.2f}  improvement={improve:.1f}% -> {'PASS' if c6 else 'FAIL'}")
results["c6_welfare"] = dict(passed=bool(c6), welfare_bids=float(welfare_bids),
                            welfare_unif=float(welfare_unif), improvement_pct=float(improve))


# ---------------------------------------------------------------- summary
banner("VERDICT SUMMARY")
passed = sum(1 for r in results.values() if r.get("passed"))
for k_, r in results.items():
    print(f"  [{'PASS' if r.get('passed') else 'FAIL'}] {k_}")
print(f"\n  {passed}/{len(results)} claims verified.")
json.dump(results, open(os.path.join(OUT, "verdict.json"), "w"), indent=2)
print("  wrote outputs/verdict.json")
