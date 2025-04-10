from __future__ import annotations

import argparse
import hashlib
import lxml.etree as etree
from collections.abc import Sequence

def calculate_md5(filename: str) -> str:
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def pretty_print_xml_file(filename: str) -> None:
    tree = etree.parse(filename)
    tree.write(filename, pretty_print=True, encoding='UTF-8', xml_declaration=True)

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='XML filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        before = calculate_md5(filename)
        pretty_print_xml_file(filename)
        after = calculate_md5(filename)
        if before != after:
            print(f'{filename}: The file has been changed ({filename})')
            retval = 1

    return retval


if __name__ == '__main__':
    raise SystemExit(main)