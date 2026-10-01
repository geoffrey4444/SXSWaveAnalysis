# SXSWaveAnalysis

A Python starting point for analyzing [SXS](https://www.black-holes.org/)
numerical-relativity waveforms, with a setup script for Codex cloud environments
and an offline pytest suite.

## Install

Use Python 3.12 and Git on Linux or macOS:

```bash
git clone https://github.com/geoffrey4444/SXSWaveAnalysis.git
cd SXSWaveAnalysis
PYTHON=python3.12 bash scripts/setup.sh
```

If your selected Python 3.12 interpreter is already `python3`, use
`bash scripts/setup.sh`. The script creates `.venv`, installs the project and
its test dependencies, and checks dependency compatibility.

Runtime dependencies are **numpy**, **matplotlib**, **sxs**, **qnmfinder**, and
**scri**. Tests use **pytest**. All dependency declarations live in
[`pyproject.toml`](pyproject.toml). `qnmfinder` is installed from
[its upstream repository](https://github.com/keefemitman/qnmfinder), pinned to
commit `71bfa283599f0cc6f0c6afdb33c4bdcac96c8c84`; it is not currently on PyPI.
Other dependencies use minimum versions, so this is a starter environment, not
a fully locked analysis environment.

For an existing virtual environment, install with:

```bash
python -m pip install -e '.[test]'
```

## Read metadata for SXS:BBH:0178

```bash
.venv/bin/python examples/read_metadata.py
```

The example prints the simulation's metadata. The underlying SXS call is:

```python
import sxs

simulation = sxs.load("SXS:BBH:0178", auto_supersede=False)
metadata = simulation.metadata
print(metadata)
```

This accesses metadata without loading waveform or horizon arrays. The first
run needs internet access to retrieve catalog information and metadata; SXS
manages its own local cache. `auto_supersede=False` preserves the requested
simulation rather than substituting a different simulation.

You can pass another SXS location as the first argument:

```bash
.venv/bin/python examples/read_metadata.py SXS:BBH:0178
```

An unversioned ID uses the latest data version and highest available resolution.
For reproducible analyses, record the catalog tag and specify a data version
and Lev supported by the simulation. See the
[SXS simulation tutorial](https://sxs.readthedocs.io/en/main/tutorials/02-Simulation/).

## Tests

```bash
.venv/bin/python -m pytest
```

The tests replace SXS network access with synthetic metadata. GitHub Actions
installs the environment, checks that all requested packages import, and runs
pytest on Linux with Python 3.12. Run the metadata example separately to check
live catalog access.

## Codex cloud setup

Create a cloud environment with this repository. Ask its setup agent to use
Python 3.12 and run the following install command:

```bash
bash scripts/setup.sh
```

Use `.venv/bin/python` for subsequent commands, including tests. This avoids
depending on virtual-environment activation persisting between shell sessions.
To refresh dependencies after changing `pyproject.toml`, run:

```bash
.venv/bin/python -m pip install -e '.[test]'
```

Setup requires access to PyPI and GitHub. Running the live SXS example also
requires network access to the SXS catalog and its data hosts (including GitHub,
CaltechDATA, and Zenodo as applicable). Enable that access for tasks that download
data, or prepare the SXS cache during setup. Ordinary tests require no downloads.
Set `MPLBACKEND=Agg` for plotting without a display. See the official
[cloud environment documentation](https://learn.chatgpt.com/docs/environments/cloud-environments).
Test the setup and publish the environment before starting new cloud tasks.
In the legacy cloud environment UI, use the same script as the setup command
and the dependency refresh command as the optional maintenance command.

[`AGENTS.md`](AGENTS.md) records the repository's install and test commands.
The repository supplies the environment setup; connecting it to Codex is a
separate account setting.

## Layout and data

- `src/sxs_wave_analysis/`: reusable analysis helpers.
- `examples/`: executable examples.
- `tests/`: offline pytest tests.
- `scripts/setup.sh`: local and cloud dependency setup.
- `data/`, `results/`, `outputs/`: ignored locations for downloads and results.

The gitignore also excludes macOS invisible files, virtual environments, Python
and notebook caches, editor files, local secrets, and common waveform data files.

## License

This repository's code is released under the [MIT License](LICENSE).
SXS data and dependencies retain their own licenses and citation requirements.
