"""Build the reader-facing report figures from committed evidence."""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS = ROOT / ".openresearch" / "artifacts"
IMAGES = ROOT / "reports" / "claim-by-claim" / "images"
NAVY = "#17324D"
BLUE = "#2878B5"
TEAL = "#2A9D8F"
GOLD = "#E9C46A"
ORANGE = "#F4A261"
RED = "#D55E5E"
GRAY = "#64748B"
LIGHT = "#E7EEF5"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def finish(fig, name: str) -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    fig.savefig(IMAGES / name, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def headline() -> None:
    fig = plt.figure(figsize=(12, 5.4), layout="constrained")
    grid = fig.add_gridspec(1, 2, width_ratios=(1.05, 1.35))
    ax = fig.add_subplot(grid[0, 0])
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 2)
    ax.axis("off")
    for index in range(6):
        x = index % 3
        y = 1 - index // 3
        color = TEAL if index < 5 else ORANGE
        ax.add_patch(
            plt.Rectangle(
                (x + 0.08, y + 0.12),
                0.84,
                0.76,
                facecolor=color,
                edgecolor="none",
            )
        )
        ax.text(
            x + 0.5,
            y + 0.60,
            f"Claim {index + 1}",
            ha="center",
            va="center",
            color="white",
            fontsize=12,
            weight="bold",
        )
        ax.text(
            x + 0.5,
            y + 0.35,
            "VERIFIED" if index < 5 else "BLOCKED",
            ha="center",
            va="center",
            color="white",
            fontsize=9,
        )
    ax.set_title("Final evidence verdicts", color=NAVY, weight="bold", pad=12)

    ax = fig.add_subplot(grid[0, 1])
    routes = load(ARTIFACTS / "claim_6" / "prior_route_results.json")
    labels = ["Paper"] + [f"Route {index}" for index in range(1, 4)]
    values = [23.0] + [row["welfare_gain_percent"] for row in routes]
    colors = [NAVY, BLUE, TEAL, GOLD]
    bars = ax.bar(labels, values, color=colors, width=0.66)
    ax.axhspan(20, 26, color=TEAL, alpha=0.10, label="predeclared source band")
    ax.axhline(23, color=NAVY, linestyle="--", linewidth=1.2)
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.45,
            f"{value:.1f}%",
            ha="center",
            color=NAVY,
            weight="bold",
        )
    ax.set_ylim(0, 28)
    ax.set_ylabel("Welfare gain vs. unweighted baseline")
    ax.set_title(
        "Claim 6: substantial, but below the declared band",
        color=NAVY,
        weight="bold",
    )
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.18)
    ax.legend(frameon=False, loc="lower left")
    fig.suptitle(
        "Five claims reach direct evidence; one remains honestly blocked",
        color=NAVY,
        fontsize=16,
        weight="bold",
    )
    finish(fig, "headline.png")


def mechanism_certificates() -> None:
    c1 = load(ARTIFACTS / "claim_1" / "verifier_output.json")
    c4 = load(ARTIFACTS / "claim_4" / "verifier_output.json")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), layout="constrained")
    values = [c1["primary_antecedent_cases"], c1["independent_comparisons"]]
    axes[0].bar(["Primary", "Independent"], values, color=[BLUE, TEAL])
    axes[0].set_yscale("log")
    axes[0].set_ylabel("Exact cases checked (log scale)")
    axes[0].set_title("Claim 1: monotonicity certificate", weight="bold")
    for index, value in enumerate(values):
        axes[0].text(
            index,
            value / 1.9,
            f"{value:,}",
            ha="center",
            color="white",
            weight="bold",
        )
    axes[0].text(
        0.5,
        0.03,
        "0 violations • 12 control witnesses",
        transform=axes[0].transAxes,
        ha="center",
        color=NAVY,
        fontsize=9,
        weight="bold",
    )
    values = [c4["threshold_value_cases"], c4["independent_checks"]]
    axes[1].bar(["Threshold/value", "Independent"], values, color=[BLUE, TEAL])
    axes[1].set_ylabel("Exact cases checked")
    axes[1].set_title("Claim 4: IR/payment certificate", weight="bold")
    for index, value in enumerate(values):
        axes[1].text(
            index,
            value - 28,
            f"{value:,}",
            ha="center",
            color="white",
            weight="bold",
        )
    axes[1].text(
        0.5,
        0.03,
        "0 violations • 12 overcharge detections",
        transform=axes[1].transAxes,
        ha="center",
        color=NAVY,
        fontsize=9,
        weight="bold",
    )
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.18)
    finish(fig, "mechanism-certificates.png")


def asymptotic_scaling() -> None:
    c2 = load(ARTIFACTS / "claim_2" / "raw_summary.json")
    c3 = load(ARTIFACTS / "claim_3" / "raw_summary.json")
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), layout="constrained")
    s2 = c2["summaries"]
    m2 = np.array([row["m"] for row in s2])
    y2 = np.array([row["mean_total_payment"] for row in s2])
    lo2 = np.array([row["payment_ci99_low"] for row in s2])
    hi2 = np.array([row["payment_ci99_high"] for row in s2])
    axes[0].plot(m2, y2, marker="o", color=BLUE, linewidth=2)
    axes[0].fill_between(m2, lo2, hi2, color=BLUE, alpha=0.14)
    axes[0].set_xscale("log", base=2)
    axes[0].set_ylim(bottom=0)
    axes[0].set_title("Claim 2: linear-model payments stay bounded", weight="bold")
    axes[0].set_xlabel("Sample size m")
    axes[0].set_ylabel("Mean total payment (99% CI)")
    axes[0].text(
        0.04,
        0.92,
        f"tail exponent = {c2['payment_tail_loglog_exponent']:.3f}",
        transform=axes[0].transAxes,
        color=TEAL,
        weight="bold",
    )

    s3 = c3["summaries"]
    m3 = np.array([row["m"] for row in s3])
    per = np.array([row["mean_revenue_per_user"] for row in s3])
    lo = np.array([row["revenue_per_user_ci99_low"] for row in s3])
    hi = np.array([row["revenue_per_user_ci99_high"] for row in s3])
    axes[1].plot(m3, m3 * per, marker="o", color=ORANGE, linewidth=2)
    axes[1].fill_between(m3, m3 * lo, m3 * hi, color=ORANGE, alpha=0.16)
    axes[1].set_xscale("log", base=2)
    axes[1].set_yscale("log", base=2)
    axes[1].set_title("Claim 3: noisy k-NN payments grow linearly", weight="bold")
    axes[1].set_xlabel("Sample size m")
    axes[1].set_ylabel("Mean total payment (99% CI)")
    axes[1].text(
        0.04,
        0.92,
        f"tail exponent = {c3['tail_loglog_exponent']:.3f}",
        transform=axes[1].transAxes,
        color=RED,
        weight="bold",
    )
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.18)
    finish(fig, "asymptotic-scaling.png")


def figure2_checks() -> None:
    plateau = load(ARTIFACTS / "claim_5" / "raw_plateau_summary.json")
    accuracy = load(ARTIFACTS / "claim_5" / "raw_accuracy_summary.json")
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), layout="constrained")
    palette = plt.cm.viridis(np.linspace(0.12, 0.92, len(plateau["settings"])))
    for setting, color in zip(plateau["settings"], palette):
        rows = setting["per_m"]
        axes[0].plot(
            [row["m"] for row in rows],
            [row["mean_payers"] for row in rows],
            marker="o",
            linewidth=1.6,
            color=color,
            label=f"σ={setting['sigma']}",
        )
    axes[0].set_xscale("log", base=2)
    axes[0].set_xlabel("Sample size m")
    axes[0].set_ylabel("Mean paying users")
    axes[0].set_title("Claim 5a: payer counts plateau", weight="bold")
    axes[0].legend(frameon=False, ncol=2, fontsize=8)

    rows = accuracy["dimensions"]
    dims = np.array([row["dimension"] for row in rows])
    means = np.array([row["accuracy_payment_spearman_mean"] for row in rows])
    lows = np.array([row["accuracy_payment_spearman_ci99_low"] for row in rows])
    highs = np.array([row["accuracy_payment_spearman_ci99_high"] for row in rows])
    axes[1].errorbar(
        dims,
        means,
        yerr=np.vstack((means - lows, highs - means)),
        fmt="o-",
        color=TEAL,
        capsize=4,
        linewidth=2,
    )
    axes[1].axhline(0, color=GRAY, linestyle="--", linewidth=1)
    axes[1].set_xscale("log", base=2)
    axes[1].set_ylim(-1.05, 0.1)
    axes[1].set_xlabel("Feature dimension")
    axes[1].set_ylabel("Spearman ρ (99% CI)")
    axes[1].set_title("Claim 5b: accuracy vs. payer fraction", weight="bold")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.18)
    finish(fig, "figure2-checks.png")


def claim6_audit() -> None:
    import csv

    with (ARTIFACTS / "claim_6" / "raw_route_summary.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        routes = list(csv.DictReader(handle))
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.7), layout="constrained")
    names = ["Numeric", "Mapped", "Nested C"]
    welfare = np.array([float(row["welfare_gain_percent"]) for row in routes])
    wlow = np.array([float(row["welfare_ci99_low"]) for row in routes])
    whigh = np.array([float(row["welfare_ci99_high"]) for row in routes])
    axes[0].errorbar(
        names,
        welfare,
        yerr=np.vstack((welfare - wlow, whigh - welfare)),
        fmt="o",
        markersize=8,
        capsize=5,
        color=BLUE,
    )
    axes[0].axhspan(20, 26, color=TEAL, alpha=0.12)
    axes[0].axhline(23, color=NAVY, linestyle="--", label="paper: +23%")
    axes[0].set_ylim(15, 27)
    axes[0].set_ylabel("Welfare gain (%)")
    axes[0].set_title("Three 30k routes: near, not equivalent", weight="bold")
    axes[0].legend(frameon=False)

    accuracy = np.array([float(row["accuracy_change_percent"]) for row in routes])
    alow = np.array([float(row["accuracy_ci99_low"]) for row in routes])
    ahigh = np.array([float(row["accuracy_ci99_high"]) for row in routes])
    axes[1].errorbar(
        names,
        accuracy,
        yerr=np.vstack((accuracy - alow, ahigh - accuracy)),
        fmt="o",
        markersize=8,
        capsize=5,
        color=ORANGE,
    )
    axes[1].axhspan(-24, -18, color=TEAL, alpha=0.12)
    axes[1].axhline(-21, color=NAVY, linestyle="--", label="paper: −21%")
    axes[1].set_ylim(-25, -16)
    axes[1].set_ylabel("Relative accuracy change (%)")
    axes[1].set_title("Accuracy tradeoff aligns across routes", weight="bold")
    axes[1].legend(frameon=False)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.18)
    finish(fig, "claim6-audit.png")


if __name__ == "__main__":
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.labelcolor": NAVY,
            "axes.titlecolor": NAVY,
            "xtick.color": GRAY,
            "ytick.color": GRAY,
        }
    )
    headline()
    mechanism_certificates()
    asymptotic_scaling()
    figure2_checks()
    claim6_audit()
