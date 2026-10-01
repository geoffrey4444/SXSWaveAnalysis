"""Read SXS simulation metadata without loading waveform arrays."""

import sxs


def load_metadata(location: str = "SXS:BBH:0178") -> sxs.Metadata:
    """Load metadata for an SXS ID, optionally including a version and Lev.

    SXS may download and cache catalog information and metadata. An unversioned
    ID selects the latest available version and highest resolution. Disable
    automatic supersession so that the requested simulation is preserved.
    """
    simulation = sxs.load(location, auto_supersede=False)
    return simulation.metadata
