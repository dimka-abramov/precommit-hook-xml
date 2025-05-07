from __future__ import annotations

import argparse
from collections.abc import Sequence

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Text filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()

        changed = False
        with open(filename, 'w') as f:
            for line in lines:
                stripped = line.lstrip(' ')
                f.write(stripped)
                if len(stripped) < len(line):
                    changed = True
                    retval = 1
                    
        if changed:
            print(f'{filename}: The file has been changed ({filename})')
        
    return retval


if __name__ == '__main__':
    raise SystemExit(main)