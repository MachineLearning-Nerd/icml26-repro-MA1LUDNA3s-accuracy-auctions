# Reproduction command record

## Fixed experiment command

Every formal experiment node used the command copied verbatim from
`orx exp status`:

```text
uv run --frozen python repro/src/verify_auctions.py
```

The root and children inherited this command unchanged. Experimental variation
is committed in code.

## Formal orchestration

The campaign used these experiment nodes:

```text
orx exp run 235affd6-a3ef-466e-b175-4adbb1e3c2c4 --backend local
orx exp run bba55fd8-2ebc-462e-a923-e3063749caf6 --backend local
orx exp run 9917b5f4-c512-4df3-8de9-464bd7a62392 --backend local
orx exp run 1141626a-6241-4d19-bb25-7abd535869ed --backend local
orx exp run 47e51ede-8bac-48a8-9992-a958a6dbe69a --backend hf --flavor cpu-upgrade
orx exp run 75d92879-8844-4fa4-bbad-d7da38e561db --backend hf --flavor cpu-upgrade
orx exp run a81a8546-84d5-4173-a8a6-e27c52cb1eef --backend hf --flavor cpu-upgrade
orx exp run 12981fa4-f517-4c68-915e-52190e3687d4 --backend hf --flavor cpu-upgrade
```

The HF runs used image
`ghcr.io/astral-sh/uv:python3.12-bookworm-slim`. The exact fixed command remains
the one above; backend and image selection are scheduler metadata, not
experimental knobs.

Runs were monitored with:

```text
orx exp wait <experiment-id> --timeout 480
orx runs 570feffb-1d87-4ba4-bab3-9e453ae6ab90
orx logs <run-id>
```

## Source and startup audit

```text
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx projects --json
orx project view 570feffb-1d87-4ba4-bab3-9e453ae6ab90
orx runs 570feffb-1d87-4ba4-bab3-9e453ae6ab90
git status --short
git rev-parse HEAD
df -h .
```

The paper HTML was retrieved with an explicit browser User-Agent and hashed
with SHA-256. The exact judged Space revision was downloaded before candidate
work, then hashed into its protected manifest.

## Presentation and release validation

```text
uv run --frozen python repro/src/build_report_figures.py
uv run --frozen python -m py_compile notebooks/accuracy_auctions_reproduction.py
uv run --frozen marimo check notebooks/accuracy_auctions_reproduction.py
uv run --frozen marimo export html notebooks/accuracy_auctions_reproduction.py -o /tmp/accuracy-auctions-notebook.html
git diff --check
jq -e . release/hf-space-text/logbook.json
```

The `marimo check` invocation is retained because it was requested, but pinned
Marimo 0.15.5 reports that the subcommand does not exist. The byte compilation
and full HTML export are the successful fallback validations.

The release gate also parses every JSON file, resolves every logbook page,
checks all report image targets, verifies the old path set is a subset of the
candidate, recomputes the 85-file SHA-256 upload manifest, and scans the
candidate for common credential formats without printing any matched value.
