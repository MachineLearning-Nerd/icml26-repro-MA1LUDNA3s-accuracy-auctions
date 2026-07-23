"""Fixed OpenResearch entrypoint for the cumulative reproduction campaign.

Every experiment node invokes this file through the inherited command. Only
accepted claim contracts are cumulative; the frozen baseline retains the
legacy judged checks.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def run(script: str) -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "repro" / "src" / script)],
        cwd=ROOT,
        check=False,
    )
    if completed.returncode:
        raise SystemExit(completed.returncode)


print(
    "OPENRESEARCH_FIXED_COMMAND: "
    "uv run --frozen python repro/src/verify_auctions.py",
    flush=True,
)
print("CUMULATIVE_REGRESSION: exact theorem contracts", flush=True)
run("verify_theory_contracts.py")
print("CUMULATIVE_REGRESSION: assumption-faithful asymptotics", flush=True)
run("verify_asymptotics.py")
print("CUMULATIVE_REGRESSION: faithful Figure 2", flush=True)
run("verify_figure2.py")
print("CUMULATIVE_REGRESSION: Folktables Figure 3", flush=True)
run("verify_folktables.py")
