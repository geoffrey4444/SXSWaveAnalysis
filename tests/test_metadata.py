"""Offline tests: no catalog or waveform downloads are required."""

import runpy
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import sxs

from sxs_wave_analysis.metadata import load_metadata


@pytest.mark.parametrize("location", ["SXS:BBH:0178", "SXS:BBH:0178v3.0/Lev5"])
def test_preserves_requested_simulation(monkeypatch, location):
    """Do not silently analyze a replacement simulation or a different Lev."""
    metadata = sxs.Metadata(
        alternative_names=["SXS:BBH:0178"],
        reference_mass1=0.6,
        reference_mass2=0.4,
        reference_dimensionless_spin1=[0.0, 0.0, 0.5],
    )

    def fake_load(requested, *, auto_supersede):
        assert requested == location
        assert auto_supersede is False
        return SimpleNamespace(metadata=metadata)

    monkeypatch.setattr(sxs, "load", fake_load)
    result = load_metadata(location)
    assert result["alternative_names"] == ["SXS:BBH:0178"]
    assert result["reference_mass1"] / result["reference_mass2"] == pytest.approx(1.5)
    assert result["reference_dimensionless_spin1"] == [0.0, 0.0, 0.5]


def test_example_prints_metadata_for_0178(monkeypatch, capsys):
    def fake_load(location, *, auto_supersede):
        assert location == "SXS:BBH:0178"
        assert auto_supersede is False
        return SimpleNamespace(metadata=sxs.Metadata(reference_mass1=0.6))

    monkeypatch.setattr(sxs, "load", fake_load)
    example = Path(__file__).resolve().parents[1] / "examples" / "read_metadata.py"
    monkeypatch.setattr(sys, "argv", [str(example)])
    runpy.run_path(str(example), run_name="__main__")
    output = capsys.readouterr().out
    assert "SXS:BBH:0178" in output
    assert "'reference_mass1': 0.6" in output
