"""Clean-room implementation of the accuracy-auction mechanism from
"Welfare-Optimal Classification with Accuracy Auctions" (arXiv 2606.02435). numpy, CPU.

Mechanism (Section 4):
  Allocation:  a(b) = a(hat_h),  hat_h = argmin_h (1/m) sum_i b_i * ell(y_i, f(x_i)) + lam*R(f)
               i.e. train a classifier with example weights = bids; a_i = 1{correct on x_i}.
  Payment:     Myerson critical bid  p_i = min{ z in [0,V] : a_i(z; b_-i) = 1 }  (0 if never correct).
  Theorem 1:   a_i(b_i; b_-i) weakly increasing in b_i  (monotonicity) for margin-based losses.
  Corollary 1: DSIC + individual rationality (p_i <= b_i).
  Theorem 2:   L2-regularized linear RRM total payments = O(1) in m.
  Theorem 3:   kNN total payments = Omega(m) under label noise.
"""
from __future__ import annotations
import numpy as np


# ------------------------------------------------------------------ L2 logistic regression (weighted)
def train_l2_logistic(X, y, w, lam=1e-2, lr=0.5, iters=400):
    """Minimize (1/m) sum_i w_i logloss(y_i, x_i.w') + lam |w'|^2  via gradient descent.
    Returns linear weights (incl. bias via augmented X)."""
    Xa = np.hstack([X, np.ones((len(X), 1))])
    n = Xa.shape[1]
    theta = np.zeros(n)
    m = len(y)
    ypm = np.where(y == 1, 1.0, -1.0)
    for _ in range(iters):
        s = Xa @ theta
        # weighted logloss grad: (1/m) sum w_i * (sigmoid(-y*s)*(-y)) * x
        sig = 1.0 / (1.0 + np.exp(np.clip(-ypm * s, -50, 50)))
        grad = (Xa * (w * (sig - 1) * ypm)[:, None]).mean(axis=0) + 2 * lam * np.r_[theta[:-1], 0]
        theta -= lr * grad
    return theta


def predict_linear(theta, X):
    Xa = np.hstack([X, np.ones((len(X), 1))])
    return np.where(Xa @ theta >= 0, 1, 0)


# ------------------------------------------------------------------ kNN
def knn_predict(Xtr, ytr, X, k=5):
    out = np.zeros(len(X), dtype=int)
    for i, x in enumerate(X):
        d = np.sum((Xtr - x) ** 2, axis=1)
        nn = ytr[np.argpartition(d, k)[:k]]
        out[i] = 1 if nn.mean() >= 0.5 else 0
    return out


# ------------------------------------------------------------------ pipelines (b -> allocation vector)
def make_logistic_pipeline(X, y, lam=1e-2, iters=350):
    def pipeline(b):
        theta = train_l2_logistic(X, y, b, lam=lam, iters=iters)
        pred = predict_linear(theta, X)
        return (pred == y).astype(int)
    return pipeline


def make_knn_pipeline(X, y, k=7):
    """Weighted kNN (example weights = bids), self-INCLUSIVE: point i is its own nearest neighbor
    (distance 0) carrying weight b_i. So raising b_i pushes i's classification toward its own label
    y_i (monotone). Under label noise, points whose label is the local minority need a positive
    critical bid -> Omega(m) payers (Theorem 3)."""
    Xa = X
    def pipeline(b):
        out = np.zeros(len(y), dtype=int)
        for i, x in enumerate(Xa):
            d = np.sum((Xa - x) ** 2, axis=1)            # self-distance 0 -> i is nearest
            nn = np.argpartition(d, k)[:k + 1]           # k+1 to safely include self
            vote1 = np.sum(b[nn] * (y[nn] == 1))
            vote0 = np.sum(b[nn] * (y[nn] == 0))
            out[i] = 1 if vote1 >= vote0 else 0
        return out
    return pipeline


# ------------------------------------------------------------------ critical bid + total payments
def critical_bid(pipeline, i, b_other, V, iters=16):
    """p_i = inf{z in [0,V] : a_i(z; b_-i)=1}, computed by bisection on the monotone allocation.
    Returns 0 if correct even at zero weight (easy user); V if never correct by V."""
    b = b_other.copy()
    b[i] = 0.0
    if pipeline(b)[i] == 1:
        return 0.0                                  # easy user: correct even when ignored
    lo, hi = 0.0, V
    for _ in range(iters):
        mid = 0.5 * (lo + hi); b[i] = mid
        if pipeline(b)[i] == 1:
            hi = mid
        else:
            lo = mid
    return float(hi)


def total_payments(pipeline, bids, V):
    m = len(bids); tot = 0.0; npay = 0
    for i in range(m):
        p = critical_bid(pipeline, i, bids.copy(), V)
        tot += p
        npay += (p > 0)
    return tot, npay

