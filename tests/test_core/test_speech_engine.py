import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core.speech_engine import SpeechEngine

class TestSpeechEngine(unittest.TestCase):
    
    def setUp(self):
        self.engine = SpeechEngine()
    
    @patch('platform.system')
    def test_initialize_tts_windows(self, mock_system):
        mock_system.return_value = 'Windows'
        with patch('pyttsx3.init') as mock_init:
            mock_engine = MagicMock()
            mock_init.return_value = mock_engine
            engine = SpeechEngine()
            self.assertIsNotNone(engine.speak)
    
    @patch('platform.system')
    def test_initialize_tts_macos(self, mock_system):
        mock_system.return_value = 'Darwin'
        with patch('os.system') as mock_os:
            engine = SpeechEngine()
            engine.speak("test")
            mock_os.assert_called_once()
    
    @patch('speech_recognition.Recognizer')
    @patch('speech_recognition.Microphone')
    def test_listen_success(self, mock_mic, mock_recognizer):
        mock_recognizer_instance = MagicMock()
        mock_recognizer.return_value = mock_recognizer_instance
        mock_recognizer_instance.recognize_google.return_value = "Hello Assistant"
        
        engine = SpeechEngine()
        result = engine.listen()
        self.assertEqual(result, "hello assistant")
    
    @patch('speech_recognition.Recognizer')
    @patch('speech_recognition.Microphone')
    def test_listen_timeout(self, mock_mic, mock_recognizer):
        mock_recognizer_instance = MagicMock()
        mock_recognizer.return_value = mock_recognizer_instance
        mock_recognizer_instance.listen.side_effect = Exception("Timeout")
        
        engine = SpeechEngine()
        result = engine.listen()
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()