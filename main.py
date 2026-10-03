"""Emberville Desktop — A local helper for Emberville gothic-farm folders, ember notes, and candlelit photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='emberville_desktop',
        description='A local helper for Emberville gothic-farm folders, ember notes, and candlelit photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Emberville Desktop')
    print('Keep the gothic farm on disk before a night update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
