import unittest
from unittest.mock import MagicMock, patch
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.interfaces.cli_interface import CLIInterface

class TestCLIInterface(unittest.TestCase):
    
    def setUp(self):
        with patch('src.core.assistant_base.ConfigManager') as mock_config, \
             patch('src.core.assistant_base.SpeechEngine'), \
             patch('src.core.assistant_base.CommandProcessor'):
            mock_config.return_value.get.return_value = 'assistant'
            self.cli = CLIInterface()
            self.cli.wake_word = 'assistant'
    
    def test_initialization(self):
        self.assertIsNotNone(self.cli)
        self.assertIsNotNone(self.cli.config)
        self.assertIsNotNone(self.cli.speech)
        self.assertIsNotNone(self.cli.processor)
    
    def test_process_command_with_wake_word(self):
        self.cli.processor.process = MagicMock(return_value="Test response")
        result = self.cli.process_command("assistant test command")
        self.assertEqual(result, "Test response")
    
    def test_process_command_without_wake_word(self):
        result = self.cli.process_command("test command")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()