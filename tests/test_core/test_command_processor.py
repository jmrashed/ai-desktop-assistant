import unittest
from unittest.mock import MagicMock, patch
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core.command_processor import CommandProcessor

class TestCommandProcessor(unittest.TestCase):
    
    def setUp(self):
        self.mock_config = MagicMock()
        self.mock_config.get.return_value = 'assistant'
        self.mock_speech = MagicMock()
        self.processor = CommandProcessor(self.mock_config, self.mock_speech)
    
    def test_time_command(self):
        result = self.processor.process("assistant what time is it")
        self.assertIn("The time is", result)
    
    @patch('wikipedia.summary')
    def test_wikipedia_command(self, mock_wikipedia):
        mock_wikipedia.return_value = "Test summary"
        result = self.processor.process("assistant who is Einstein")
        self.assertIn("According to Wikipedia", result)
    
    @patch('webbrowser.open_new_tab')
    def test_website_command(self, mock_browser):
        result = self.processor.process("assistant open youtube")
        mock_browser.assert_called_once()
        self.assertIn("Opening youtube", result)
    
    @patch('pywhatkit.playonyt')
    def test_music_command(self, mock_play):
        result = self.processor.process("assistant play despacito")
        mock_play.assert_called_with("despacito")
        self.assertIn("Playing despacito", result)
    
    def test_weather_command(self):
        result = self.processor.process("assistant weather in London")
        self.assertIsNotNone(result)
    
    def test_system_info_command(self):
        result = self.processor.process("assistant system info")
        self.assertIsNotNone(result)
    
    def test_file_search_command(self):
        result = self.processor.process("assistant search file test.txt")
        self.assertIsNotNone(result)
    
    def test_create_folder_command(self):
        result = self.processor.process("assistant create folder TestFolder")
        self.assertIsNotNone(result)
    
    def test_unknown_command(self):
        result = self.processor.process("assistant unknown command")
        self.assertEqual(result, "I'm not sure how to help with that")

if __name__ == '__main__':
    unittest.main()