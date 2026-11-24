"""Compatibility exports for the canonical Secrip SecondBIN command API."""

from secrip.products.secondbin.commands import (
    Command,
    CommandRegistry,
    create_default_registry,
)

__all__ = ["Command", "CommandRegistry", "create_default_registry"]
