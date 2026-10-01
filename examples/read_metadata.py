"""Print SXS:BBH:0178 metadata; run after installing this project."""

import argparse
from pprint import pprint

from sxs_wave_analysis.metadata import load_metadata


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "location",
        nargs="?",
        default="SXS:BBH:0178",
        help="SXS ID, optionally with version and Lev (default: SXS:BBH:0178)",
    )
    args = parser.parse_args(argv)
    metadata = load_metadata(args.location)
    print(f"Metadata for {args.location}:")
    pprint(dict(metadata), sort_dicts=False)


if __name__ == "__main__":
    main()
