"""Compatibility namespace; the canonical API is secrip.products.secondbin."""

from secrip.products.secondbin import (
    __app_name__,
    __command_name__,
    __version__,
    Command,
    CommandRegistry,
    create_default_registry,
)

__all__ = [
    "__app_name__", "__command_name__", "__version__",
    "Command", "CommandRegistry", "create_default_registry",
]
