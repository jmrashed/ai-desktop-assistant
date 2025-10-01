import unittest
from unittest.mock import MagicMock, patch
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.features.weather_service import WeatherService

class TestWeatherService(unittest.TestCase):
    
    def setUp(self):
        self.mock_config = MagicMock()
        self.mock_config.get.return_value = 'test_api_key'
        self.weather_service = WeatherService(self.mock_config)
    
    def test_no_api_key(self):
        config = MagicMock()
        config.get.return_value = ''
        service = WeatherService(config)
        result = service.get_weather('London')
        self.assertEqual(result, "Weather API key not configured")
    
    @patch('requests.get')
    def test_successful_weather_request(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": "200",
            "main": {"temp": 20},
            "weather": [{"description": "sunny"}]
        }
        mock_get.return_value = mock_response
        
        result = self.weather_service.get_weather('London')
        self.assertIn("Weather in London: 20°C, sunny", result)
    
    @patch('requests.get')
    def test_city_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"cod": "404"}
        mock_get.return_value = mock_response
        
        result = self.weather_service.get_weather('InvalidCity')
        self.assertEqual(result, "City not found")
    
    @patch('requests.get')
    def test_api_error(self, mock_get):
        mock_get.side_effect = Exception("API Error")
        
        result = self.weather_service.get_weather('London')
        self.assertIn("Error getting weather", result)

if __name__ == '__main__':
    unittest.main()