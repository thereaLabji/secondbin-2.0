"""Interactive SecondBIN terminal."""

from __future__ import annotations

import sys

from secondbin import __version__
from secondbin.commands import create_default_registry


def main() -> int:
    registry = create_default_registry()
    print(f"SecondBIN (sBIN) {__version__}")
    print("Type 'help' to see available commands. Type 'exit' to quit.")

    while True:
        try:
            line = input("sBIN> ")
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            continue

        if not registry.execute(line):
            break

    return 0


if __name__ == "__main__":
    sys.exit(main())
