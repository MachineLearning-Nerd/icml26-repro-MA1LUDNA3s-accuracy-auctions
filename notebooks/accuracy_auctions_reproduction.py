import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    return mo, np, pd, plt


@app.cell
def _(mo):
    mo.md(
        r"""
        # Accuracy auctions: an evidence-first reproduction

        **Result:** five of six judged claims are **VERIFIED** under explicit,
        executable contracts. Claim 6 is **BLOCKED** after three faithful
        reproduction routes and a fourth falsification audit.

        This notebook embeds the accepted evidence. It is a tutorial and
        exploration surface—not a substitute for the formal fixed-command runs.
        """
    )
    return


@app.cell
def _(pd):
    claim_results = pd.DataFrame(
        [
            ("Claim 1", "Bid monotonicity", "VERIFIED", 24543, "exact antecedents"),
            ("Claim 2", "Linear-model payments O(1)", "VERIFIED", 140, "seed × size runs"),
            ("Claim 3", "Noisy k-NN payments Ω(m)", "VERIFIED", 280, "seed × size × k runs"),
            ("Claim 4", "Individual rationality", "VERIFIED", 182, "threshold/value cases"),
            ("Claim 5", "Figure 2 payment patterns", "VERIFIED", 890, "plateau + accuracy datasets"),
            ("Claim 6", "Up to 23% welfare gain", "BLOCKED", 4, "distinct research routes"),
        ],
        columns=["claim", "statement", "status", "coverage", "coverage_unit"],
    )
    claim_results
    return (claim_results,)


@app.cell
def _(claim_results, mo, plt):
    colors = claim_results["status"].map({"VERIFIED": "#168aad", "BLOCKED": "#f4a261"})
    fig, ax = plt.subplots(figsize=(8.6, 3.2))
    ax.barh(claim_results["claim"], [1] * 6, color=colors)
    for row_i, row in claim_results.iterrows():
        ax.text(
            0.03,
            row_i,
            f"{row.status} — {row.statement}",
            va="center",
            color="white" if row.status == "VERIFIED" else "#392f2a",
            fontweight="bold",
        )
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.invert_yaxis()
    ax.spines[:].set_visible(False)
    ax.set_title("Formal outcome by claim", loc="left", fontweight="bold")
    fig.tight_layout()
    mo.vstack([fig, mo.md("*Five verified contracts; one unresolved empirical claim.*")])
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## How an accuracy auction works

        Each user reports a value for receiving an accurate prediction.
        Weighted empirical risk minimization chooses a classifier and therefore
        an allocation. If raising one user's bid can never remove that user from
        the allocation, a critical-bid payment makes truthful reporting optimal.

        The reproduction turns that argument into a finite certificate over all
        objective breakpoints:

        1. enumerate the relevant bid intervals and tied optima;
        2. compare allocation sets on both sides of every threshold;
        3. derive critical payments;
        4. check payment, individual rationality, and strategy inequalities;
        5. inject reversed thresholds and overcharges to prove the checks detect
           the intended errors.
        """
    )
    return


@app.cell
def _(pd):
    theory = pd.DataFrame(
        [
            ("Monotonicity primary", 24543, 0, "reversed threshold", 12),
            ("Monotonicity independent", 206325, 0, "reversed threshold", 12),
            ("IR / payment / DSIC", 182, 0, "overcharge", 12),
            ("IR independent", 441, 0, "overcharge", 12),
        ],
        columns=["check", "cases", "violations", "negative_control", "control_witnesses"],
    )
    theory
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Scaling is about exponents, not three points

        Claims 2 and 3 concern asymptotic behavior. We therefore use 64×
        sample-size ranges, twenty deterministic seeds, confidence bounds, an
        independent payer screen, and controls tied to the theorem assumptions.
        """
    )
    return


@app.cell
def _(np, pd, plt):
    scaling = pd.DataFrame(
        [
            ("Regularized linear: payment", 0.0730, "O(1) contract"),
            ("Regularized linear: payers", 0.0081, "O(1) contract"),
            ("k-NN, k=31", 1.0112, "Ω(m) contract"),
            ("k-NN, k=63", 1.0210, "Ω(m) contract"),
            ("Injected linear control", 1.0000, "negative control"),
        ],
        columns=["series", "tail_exponent", "role"],
    )
    fig_scaling, ax_scaling = plt.subplots(figsize=(8.5, 3.5))
    scaling_colors = np.where(
        scaling["role"].eq("negative control"),
        "#d62828",
        np.where(scaling["tail_exponent"] < 0.5, "#168aad", "#52b788"),
    )
    ax_scaling.barh(scaling["series"], scaling["tail_exponent"], color=scaling_colors)
    ax_scaling.axvline(0, color="#444", linewidth=0.8)
    ax_scaling.axvline(1, color="#444", linewidth=1, linestyle="--")
    ax_scaling.set_xlabel("tail log-log exponent")
    ax_scaling.set_title("Observed payment-scaling exponents", loc="left", fontweight="bold")
    ax_scaling.invert_yaxis()
    fig_scaling.tight_layout()
    fig_scaling
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Figure 2 uses real held-out accuracy

        The earlier judged logbook used allocation rate as an accuracy proxy.
        The new check trains classifiers and measures held-out classification
        accuracy. Across six feature dimensions, the accuracy–payer-proportion
        Spearman association is always negative; shuffled labels remove it.
        Payer-count plateaus are tested separately over sample sizes
        4,096–65,536 and seven variance settings.
        """
    )
    return


@app.cell
def _(pd):
    figure2 = pd.DataFrame(
        {
            "dimension": [2, 4, 8, 16, 32, 64],
            "spearman_mean": [-0.698, -0.812, -0.873, -0.921, -0.954, -0.981],
            "upper_99pct_bound_negative": [True] * 6,
        }
    )
    figure2
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Why the 23% welfare claim remains blocked

        A close result is not automatically a verification, and a lower result
        is not automatically a falsification. The paper says “up to,” an
        existential claim. Three defensible configurations below 23% cannot
        prove that the authors' unreported configuration cannot attain it.
        """
    )
    return


@app.cell
def _(pd):
    claim6 = pd.DataFrame(
        [
            ("Paper headline", 23.00, -21.00, "reported"),
            ("Route 1: published task", 19.52, -20.49, "blocked"),
            ("Route 2: semantic groups", 19.91, -20.62, "blocked"),
            ("Route 3: nested tuning", 19.65, -20.85, "blocked"),
            ("Digitization A", 23.33, -23.50, "source check"),
            ("Digitization B", 23.10, -22.57, "source check"),
        ],
        columns=["route", "welfare_gain_pct", "accuracy_change_pct", "evidence_role"],
    )
    claim6
    return (claim6,)


@app.cell
def _(claim6, mo):
    metric = mo.ui.dropdown(
        options={
            "Welfare gain (%)": "welfare_gain_pct",
            "Relative accuracy change (%)": "accuracy_change_pct",
        },
        value="Welfare gain (%)",
        label="Compare:",
    )
    metric
    return (metric,)


@app.cell
def _(claim6, metric, plt):
    selected_column = metric.value
    fig_claim6, ax_claim6 = plt.subplots(figsize=(8.5, 3.7))
    colors_claim6 = claim6["evidence_role"].map(
        {"reported": "#264653", "blocked": "#f4a261", "source check": "#2a9d8f"}
    )
    ax_claim6.barh(claim6["route"], claim6[selected_column], color=colors_claim6)
    ax_claim6.axvline(0, color="#555", linewidth=0.8)
    ax_claim6.set_xlabel(metric.options[selected_column] if False else selected_column.replace("_", " "))
    ax_claim6.set_title("Claim 6: paper, routes, and source readings", loc="left", fontweight="bold")
    ax_claim6.invert_yaxis()
    fig_claim6.tight_layout()
    fig_claim6
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## What would resolve Claim 6?

        An assumption-complete test needs the authors' exact binary attribute
        mappings, occupation-group boundaries, preprocessing and regularization
        protocol, seeds, or raw Figure 3 outputs. Without them, the honest
        verdict is **BLOCKED**.

        The formal evidence was generated by:

        ```text
        uv run --frozen python repro/src/verify_auctions.py
        ```

        Every accepted claim directory contains a source audit, machine-readable
        contract, raw outputs, independent checker, negative control, verifier,
        locked environment, and limitations. No GPU was used.
        """
    )
    return


if __name__ == "__main__":
    app.run()
