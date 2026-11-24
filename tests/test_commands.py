import unittest
from unittest.mock import patch

from secondbin.commands import Command, CommandRegistry, create_default_registry


class CommandRegistryTests(unittest.TestCase):
    def test_builtin_commands_are_registered(self):
        registry = create_default_registry()
        names = {command.name for command in registry.all()}
        self.assertTrue({"help", "clear", "echo", "version", "date", "time", "pwd", "ls", "cd", "exit"} <= names)

    def test_unknown_command_does_not_exit(self):
        registry = create_default_registry()
        with patch("builtins.print") as output:
            self.assertTrue(registry.execute("not-a-command"))
        self.assertIn("unknown command", str(output.call_args_list).lower())

    def test_exit_returns_false(self):
        registry = create_default_registry()
        self.assertFalse(registry.execute("exit"))

    def test_custom_command_can_be_registered(self):
        registry = CommandRegistry()
        seen = []
        registry.register(Command("hello", "Test command", lambda args: seen.append(args) or True))
        self.assertTrue(registry.execute('hello "two words"'))
        self.assertEqual(seen, [["two words"]])

    def test_duplicate_command_is_rejected(self):
        registry = CommandRegistry()
        handler = lambda args: True
        registry.register(Command("hello", "First", handler))
        with self.assertRaises(ValueError):
            registry.register(Command("HELLO", "Duplicate", handler))


if __name__ == "__main__":
    unittest.main()
