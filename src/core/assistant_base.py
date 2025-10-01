from .speech_engine import SpeechEngine
from .command_processor import CommandProcessor
from ..utils.config_manager import ConfigManager

class AssistantBase:
    def __init__(self):
        self.config = ConfigManager()
        self.speech = SpeechEngine()
        self.processor = CommandProcessor(self.config, self.speech)
        self.wake_word = self.config.get('wake_word', 'assistant')
    
    def process_command(self, statement):
        """Process voice commands"""
        if self.wake_word not in statement.lower():
            return None
        return self.processor.process(statement)
    
    def run(self):
        """Main assistant loop"""
        self.speech.speak(f"Hello! Say '{self.wake_word}' followed by your command.")
        
        while True:
            try:
                statement = self.speech.listen()
                if not statement:
                    continue
                
                if any(cmd in statement for cmd in ["goodbye", "exit", "quit"]):
                    self.speech.speak("Goodbye!")
                    break
                
                response = self.process_command(statement)
                if response:
                    self.speech.speak(response)
                    
            except KeyboardInterrupt:
                break