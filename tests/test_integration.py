import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestIntegration(unittest.TestCase):
    """Integration tests for complete workflows"""
    
    @patch('src.core.speech_engine.SpeechEngine')
    @patch('src.utils.config_manager.ConfigManager')
    def test_full_command_workflow(self, mock_config, mock_speech):
        """Test complete command processing workflow"""
        from src.core.assistant_base import AssistantBase
        
        # Setup mocks
        mock_config_instance = MagicMock()
        mock_config_instance.get.return_value = 'assistant'
        mock_config.return_value = mock_config_instance
        
        mock_speech_instance = MagicMock()
        mock_speech.return_value = mock_speech_instance
        
        # Test assistant initialization
        assistant = AssistantBase()
        self.assertIsNotNone(assistant)
        
        # Test command processing
        result = assistant.process_command("assistant what time is it")
        self.assertIsNotNone(result)
    
    @patch('requests.get')
    def test_weather_integration(self, mock_get):
        """Test weather service integration"""
        from src.features.weather_service import WeatherService
        from src.utils.config_manager import ConfigManager
        
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": "200",
            "main": {"temp": 25},
            "weather": [{"description": "clear sky"}]
        }
        mock_get.return_value = mock_response
        
        config = ConfigManager()
        config.config = {"weather_api_key": "test_key"}
        weather = WeatherService(config)
        
        result = weather.get_weather("London")
        self.assertIn("Weather in London", result)
        self.assertIn("25°C", result)
    
    def test_file_operations_integration(self):
        """Test file management integration"""
        from src.features.file_manager import FileManager
        
        file_manager = FileManager()
        
        # Test with mock data
        with patch('os.walk') as mock_walk:
            mock_walk.return_value = [('/test', [], ['test.txt'])]
            result = file_manager.search_files('test')
            self.assertIn("Found 1 files", result)

if __name__ == '__main__':
    unittest.main()