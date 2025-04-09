from __future__ import annotations

import argparse
import lxml.etree as etree
from collections.abc import Sequence

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='XML filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        tree = etree.parse(filename)
        tree.write(filename, pretty_print=True, encoding='UTF-8', xml_declaration=True)
        print(f'{filename}: The file has been updated ({filename})')
        retval = 1

    return retval


if __name__ == '__main__':
    raise SystemExit(main)