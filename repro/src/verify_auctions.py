"""Fixed OpenResearch entrypoint for the cumulative reproduction campaign.

Every experiment node invokes this file through the inherited command. The
legacy judged checks run first as regressions, followed by the stronger claim
contracts implemented by the current branch.
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
print("CUMULATIVE_REGRESSION: legacy judged checks", flush=True)
run("legacy_verify_auctions.py")
print("CUMULATIVE_REGRESSION: exact theorem contracts", flush=True)
run("verify_theory_contracts.py")
print("CUMULATIVE_REGRESSION: assumption-faithful asymptotics", flush=True)
run("verify_asymptotics.py")
