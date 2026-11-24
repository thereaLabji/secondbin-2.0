"""SecondBIN product API under the Secrip namespace."""

__version__ = "2.0.0.dev1"
__app_name__ = "SecondBIN"
__command_name__ = "sBIN"

from .commands import Command, CommandRegistry, create_default_registry

__all__ = [
    "Command",
    "CommandRegistry",
    "create_default_registry",
    "__version__",
    "__app_name__",
    "__command_name__",
]
