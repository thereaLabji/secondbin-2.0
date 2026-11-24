"""Compatibility entry point for older SecondBIN imports."""

from secrip.products.secondbin.app import main

if __name__ == "__main__":
    raise SystemExit(main())
