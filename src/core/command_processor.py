import datetime
import wikipedia
import webbrowser
import pywhatkit
from ..features.weather_service import WeatherService
from ..features.file_manager import FileManager
from ..features.system_monitor import SystemMonitor

class CommandProcessor:
    def __init__(self, config, speech_engine):
        self.config = config
        self.speech = speech_engine
        self.weather = WeatherService(config)
        self.file_manager = FileManager()
        self.system_monitor = SystemMonitor()
    
    def process(self, statement):
        """Process and route commands"""
        statement = statement.lower().replace(self.config.get('wake_word', 'assistant'), '').strip()
        
        # Weather commands
        if 'weather' in statement:
            city = statement.split('in')[-1].strip() if 'in' in statement else 'London'
            return self.weather.get_weather(city)
        
        # File management
        elif 'search file' in statement:
            filename = statement.replace('search file', '').strip()
            return self.file_manager.search_files(filename)
        
        elif 'create folder' in statement:
            folder_name = statement.replace('create folder', '').strip()
            return self.file_manager.create_folder(folder_name)
        
        # System info
        elif 'system info' in statement:
            return self.system_monitor.get_system_info()
        
        # Time
        elif 'time' in statement:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The time is {current_time}"
        
        # Wikipedia
        elif any(word in statement for word in ['what is', 'who is', 'wikipedia']):
            query = statement.replace('what is', '').replace('who is', '').replace('wikipedia', '').strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                return f"According to Wikipedia: {results}"
            except:
                return "Sorry, I couldn't find that information"
        
        # Music
        elif 'play' in statement:
            song = statement.replace('play', '').strip()
            pywhatkit.playonyt(song)
            return f"Playing {song}"
        
        # Websites
        elif any(site in statement for site in ['youtube', 'google', 'gmail']):
            sites = {
                'youtube': 'https://www.youtube.com',
                'google': 'https://www.google.com',
                'gmail': 'https://gmail.com'
            }
            for site, url in sites.items():
                if site in statement:
                    webbrowser.open_new_tab(url)
                    return f"Opening {site}"
        
        return "I'm not sure how to help with that"