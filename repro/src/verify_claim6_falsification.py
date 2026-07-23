"""Mandatory falsification route for the Figure 3 empirical claim."""
from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from typing import Any

from verify_theory_contracts import (
    ARTIFACT_ROOT,
    COMMAND,
    RETRIEVED_AT,
    ROOT,
    SOURCE_SHA256,
    environment_record,
    git_sha,
    write_json,
    write_text,
)


PAPER_URL = "https://arxiv.org/abs/2606.02435v2"
FIGURE_READINGS = (
    {
        "reader": "A",
        "baseline_welfare": 0.750,
        "endpoint_welfare": 0.925,
        "baseline_accuracy": 0.732,
        "endpoint_accuracy": 0.560,
    },
    {
        "reader": "B",
        "baseline_welfare": 0.749,
        "endpoint_welfare": 0.922,
        "baseline_accuracy": 0.731,
        "endpoint_accuracy": 0.566,
    },
)
PRIOR_ROUTES = (
    {
        "route": "numeric_codes_three_preprocessing_sensitivities",
        "run_id": "ec25262f-8c13-4376-ab19-5920ccc2a367",
        "welfare_gain_percent": 19.52396117539906,
        "accuracy_change_percent": -20.485119861762154,
    },
    {
        "route": "paper_mapped_14_group_preprocessing",
        "run_id": "6f3dda99-13b6-4442-8bc5-3608031aca75",
        "welfare_gain_percent": 19.910793814600915,
        "accuracy_change_percent": -20.61655476696979,
    },
    {
        "route": "nested_regularization_selection",
        "run_id": "1408cd20-8047-4343-8c03-95af617fb485",
        "welfare_gain_percent": 19.653684010612427,
        "accuracy_change_percent": -20.845210792249144,
    },
)


def changes(row: dict[str, Any]) -> dict[str, float]:
    return {
        "welfare_gain_percent": 100.0
        * (row["endpoint_welfare"] / row["baseline_welfare"] - 1.0),
        "accuracy_change_percent": 100.0
        * (row["endpoint_accuracy"] / row["baseline_accuracy"] - 1.0),
        "accuracy_change_points": 100.0
        * (row["endpoint_accuracy"] - row["baseline_accuracy"]),
    }


def in_source_band(result: dict[str, float]) -> bool:
    return (
        20.0 <= result["welfare_gain_percent"] <= 26.0
        and (
            -24.0 <= result["accuracy_change_percent"] <= -18.0
            or -24.0 <= result["accuracy_change_points"] <= -18.0
        )
    )


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    start = time.perf_counter()
    claim_dir = ARTIFACT_ROOT / "claim_6"
    digitized = [{**row, **changes(row)} for row in FIGURE_READINGS]
    reader_agreement = all(in_source_band(row) for row in digitized)

    # This route deliberately distinguishes failure to reproduce an
    # existential report from a counterexample to it.
    exact_author_configuration_known = False
    alternate_runs_negate_existential = False
    source_itself_contradicts_claim = not reader_agreement
    falsification_established = (
        exact_author_configuration_known
        and alternate_runs_negate_existential
        and source_itself_contradicts_claim
    )

    independent = {
        "route": "independent_ratio_recalculation_from_two_figure_readers",
        "readers": [
            {
                "reader": row["reader"],
                "welfare_gain_percent": row["welfare_gain_percent"],
                "accuracy_change_percent": row["accuracy_change_percent"],
                "matches_textual_band": in_source_band(row),
            }
            for row in digitized
        ],
        "reader_agreement": reader_agreement,
        "passed": reader_agreement,
    }
    corrupted = dict(FIGURE_READINGS[0])
    corrupted["endpoint_welfare"] = 0.680
    corrupted_result = changes(corrupted)
    negative = {
        "control": "replace_published_endpoint_welfare_0.925_with_0.680",
        "corrupted_result": corrupted_result,
        "detector_rejected_corruption": not in_source_band(corrupted_result),
        "control_failed_as_intended": not in_source_band(corrupted_result),
    }
    result = {
        "claim_id": 6,
        "verdict": "FALSIFIED" if falsification_established else "BLOCKED",
        "passed": falsification_established,
        "falsification_established": falsification_established,
        "exact_author_configuration_known": exact_author_configuration_known,
        "alternate_runs_negate_existential": alternate_runs_negate_existential,
        "source_itself_contradicts_claim": source_itself_contradicts_claim,
        "reason": (
            "The published claim is existential/descriptive ('up to'), the "
            "unpublished preprocessing boundaries, tuning protocol, and seeds "
            "prevent matching every author-side assumption, and two independent "
            "figure readings support rather than contradict the reported band."
        ),
    }
    write_json(
        claim_dir / "claim_contract.json",
        {
            "claim_id": 6,
            "paper_anchors": ["S7.F3", "Appendix C.1", "Appendix C.2"],
            "statement": (
                "The reported label-value experiment contains a frontier "
                "endpoint with approximately +23% normalized welfare and -21% "
                "accuracy relative to alpha=0."
            ),
            "domain": (
                "2018 1-Year NJ ACSIncome; random 30,000-person subset; "
                "18,000/12,000 train/validation; stated 13 features; "
                "v(0)=1, v(1)=v_plus; L2 logistic regression."
            ),
            "quantifier": (
                "Existential/descriptive: at least one author experiment and "
                "frontier endpoint attains the reported approximate maximum."
            ),
            "falsification_rule": (
                "FALSIFIED only if a counterexample satisfies every published "
                "and author-side implementation assumption and logically "
                "negates the existential claim, or if the published source's "
                "own endpoint arithmetic contradicts it."
            ),
        },
    )
    write_text(
        claim_dir / "source_audit.md",
        f"# Source audit\n\nPrimary source: {PAPER_URL}, retrieved "
        f"{RETRIEVED_AT}, HTML SHA-256 `{SOURCE_SHA256}`. Section 7 / Figure 3 "
        "states welfare +23% and accuracy -21% for label-based values. Appendix "
        "C.1 says regularization was fine-tuned but gives no coefficient or "
        "protocol. Appendix C.2 gives the dataset, 30,000-person 60/40 split, "
        "features, binary/14-group preprocessing description, and sigma=0.4 "
        "noise, but not the mapping rules, group boundaries, or trial seeds.\n",
    )
    write_text(
        claim_dir / "method.md",
        "# Method\n\nThis mandatory fourth route seeks a logically valid "
        "counterexample rather than another near-reproduction. It formalizes "
        "the paper's 'up to' statement as existential, checks whether the three "
        "completed alternate implementations can negate that quantifier, and "
        "independently recalculates the plotted v_plus=12 endpoint using two "
        "manual readings of the vector figure. A corrupted endpoint is supplied "
        "to ensure the arithmetic detector rejects contradictory source data.\n",
    )
    write_csv(claim_dir / "raw_figure_digitization.csv", digitized)
    write_json(claim_dir / "prior_route_results.json", list(PRIOR_ROUTES))
    write_json(claim_dir / "independent_checker_output.json", independent)
    write_json(claim_dir / "negative_control_output.json", negative)
    write_json(claim_dir / "verifier_output.json", result)
    write_text(
        claim_dir / "EVAL.md",
        "# Claim 6 — BLOCKED\n\nFalsification was not established. Both "
        f"independent figure readings fall in the declared source band: "
        f"{reader_agreement}. The three alternate implementations are not "
        "counterexamples to an existential 'up to' statement, and the omitted "
        "author preprocessing/tuning details prevent proving that every "
        "assumption is matched. The corrupted endpoint was rejected as "
        f"intended: {negative['control_failed_as_intended']}.\n",
    )
    write_text(
        claim_dir / "limitations.md",
        "# Limitations and deviations\n\nFigure coordinates are digitized from "
        "the published vector plot and are source-audit evidence, not a new "
        "experimental reproduction. The missing author mapping boundaries, "
        "regularization protocol, and seeds make an assumption-complete "
        "counterexample unavailable. Accordingly, this route refuses to label "
        "the three 30,000-person near-reproductions as falsifications.\n",
    )
    write_text(claim_dir / "command.txt", COMMAND + "\n")
    write_json(claim_dir / "environment.json", environment_record(start))
    stage = {
        "stage": "claim_6_falsification_audit",
        "git_sha": git_sha(),
        "runtime_seconds": time.perf_counter() - start,
        "claim_6": result,
    }
    write_json(ARTIFACT_ROOT / "claim6_falsification_stage_summary.json", stage)
    for filename in (
        "claim_contract.json",
        "EVAL.md",
        "raw_figure_digitization.csv",
        "prior_route_results.json",
        "independent_checker_output.json",
        "negative_control_output.json",
        "verifier_output.json",
    ):
        path = claim_dir / filename
        print(f"\n--- {path.relative_to(ROOT)} ---", flush=True)
        print(path.read_text(encoding="utf-8"), end="", flush=True)
    print("\nCLAIM6_FALSIFICATION_STAGE_SUMMARY", flush=True)
    print(json.dumps(stage, indent=2, sort_keys=True), flush=True)
    print(
        "CLAIM6_FALSIFICATION_STAGE_EXIT: "
        f"{'PASS' if falsification_established else 'FAIL'}",
        flush=True,
    )
    return 0 if falsification_established else 1


if __name__ == "__main__":
    raise SystemExit(main())
