"""Built-in commands for the SecondBIN terminal."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable
import os
import shlex


@dataclass(frozen=True)
class Command:
    name: str
    description: str
    handler: Callable[[list[str]], bool]


class CommandRegistry:
    """Maps command names to handlers.

    A handler returns True to keep the shell running, or False to exit.
    """

    def __init__(self) -> None:
        self._commands: dict[str, Command] = {}

    def register(self, command: Command) -> None:
        key = command.name.casefold()
        if not key or any(ch.isspace() for ch in key):
            raise ValueError("Command names must be non-empty and contain no spaces.")
        if key in self._commands:
            raise ValueError(f"Command already registered: {command.name}")
        self._commands[key] = command

    def execute(self, line: str) -> bool:
        try:
            parts = shlex.split(line, posix=(os.name != "nt"))
        except ValueError as exc:
            print(f"sBIN: invalid command syntax: {exc}")
            return True

        if not parts:
            return True

        name, args = parts[0].casefold(), parts[1:]
        command = self._commands.get(name)
        if command is None:
            print(f"sBIN: unknown command: {parts[0]!r}. Type 'help' for commands.")
            return True

        try:
            return command.handler(args)
        except Exception as exc:  # Keep a command failure from killing the shell.
            print(f"sBIN: {name} failed: {exc}")
            return True

    def all(self) -> list[Command]:
        return sorted(self._commands.values(), key=lambda item: item.name)


def create_default_registry() -> CommandRegistry:
    registry = CommandRegistry()

    def help_command(args: list[str]) -> bool:
        if args:
            print("Usage: help")
            return True
        print("SecondBIN commands:")
        for item in registry.all():
            print(f"  {item.name:<10} {item.description}")
        return True

    def clear_command(args: list[str]) -> bool:
        if args:
            print("Usage: clear")
            return True
        os.system("cls" if os.name == "nt" else "clear")
        return True

    def echo_command(args: list[str]) -> bool:
        print(" ".join(args))
        return True

    def version_command(args: list[str]) -> bool:
        from secondbin import __version__
        print(f"SecondBIN (sBIN) {__version__}")
        return True

    def date_command(args: list[str]) -> bool:
        print(datetime.now().astimezone().strftime("%Y-%m-%d"))
        return True

    def time_command(args: list[str]) -> bool:
        print(datetime.now().astimezone().strftime("%H:%M:%S %Z"))
        return True

    def pwd_command(args: list[str]) -> bool:
        print(Path.cwd())
        return True

    def ls_command(args: list[str]) -> bool:
        target = Path(args[0]).expanduser() if args else Path.cwd()
        if not target.exists():
            print(f"sBIN: path does not exist: {target}")
            return True
        if target.is_file():
            print(target.name)
            return True
        for item in sorted(target.iterdir(), key=lambda p: (not p.is_dir(), p.name.casefold())):
            suffix = "/" if item.is_dir() else ""
            print(f"{item.name}{suffix}")
        return True

    def cd_command(args: list[str]) -> bool:
        if len(args) > 1:
            print("Usage: cd [directory]")
            return True
        target = Path(args[0]).expanduser() if args else Path.home()
        try:
            os.chdir(target)
        except OSError as exc:
            print(f"sBIN: cannot change directory: {exc}")
        return True

    def exit_command(args: list[str]) -> bool:
        return False

    for command in (
        Command("help", "Show available commands", help_command),
        Command("clear", "Clear the terminal", clear_command),
        Command("echo", "Print text", echo_command),
        Command("version", "Show SecondBIN version", version_command),
        Command("date", "Show the local date", date_command),
        Command("time", "Show the local time", time_command),
        Command("pwd", "Show the current directory", pwd_command),
        Command("ls", "List files and directories", ls_command),
        Command("cd", "Change the current directory", cd_command),
        Command("exit", "Exit SecondBIN", exit_command),
    ):
        registry.register(command)

    return registry
