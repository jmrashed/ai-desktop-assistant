import unittest
from unittest.mock import patch, mock_open
import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.utils.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='{"wake_word": "test"}')
    def test_load_existing_config(self, mock_file, mock_exists):
        mock_exists.return_value = True
        config = ConfigManager('test_config.json')
        self.assertEqual(config.get('wake_word'), 'test')
    
    @patch('os.path.exists')
    def test_load_default_config(self, mock_exists):
        mock_exists.return_value = False
        config = ConfigManager('nonexistent.json')
        self.assertEqual(config.get('wake_word'), 'assistant')
    
    def test_get_with_default(self):
        config = ConfigManager()
        result = config.get('nonexistent_key', 'default_value')
        self.assertEqual(result, 'default_value')
    
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_save_config(self, mock_exists, mock_file, mock_makedirs):
        mock_exists.return_value = False
        config = ConfigManager('test_config.json')
        config.set('test_key', 'test_value')
        mock_file.assert_called()

if __name__ == '__main__':
    unittest.main()