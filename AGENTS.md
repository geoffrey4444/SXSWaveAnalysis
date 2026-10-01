# Working in SXSWaveAnalysis

- Use Python 3.12 as the baseline runtime.
- Install with `bash scripts/setup.sh`; use `.venv/bin/python` for commands.
- Run `.venv/bin/python -m pytest` and `git diff --check` before finishing code changes.
- Keep default tests offline. Mock SXS downloads and use small synthetic fixtures.
- Put reusable Python code in `src/sxs_wave_analysis/` and examples in `examples/`.
- Keep dependencies in `pyproject.toml`; `requirements.txt` delegates to it.
- Put downloaded data in `data/` and generated products in `results/` or `outputs/`.
  These directories and common waveform binary formats are ignored by Git.
- Record simulation ID, catalog/data version, resolution, waveform conventions,
  and units when adding scientific analyses. Do not silently supersede simulations.
