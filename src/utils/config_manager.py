import json
import os

class ConfigManager:
    def __init__(self, config_path='config/user_config.json'):
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration from file"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return self._load_default_config()
    
    def _load_default_config(self):
        """Load default configuration"""
        default_path = 'config/default_config.json'
        if os.path.exists(default_path):
            with open(default_path, 'r') as f:
                return json.load(f)
        return {
            'wake_word': 'assistant',
            'weather_api_key': '',
            'user_pin': '1234'
        }
    
    def get(self, key, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Set configuration value"""
        self.config[key] = value
        self.save()
    
    def save(self):
        """Save configuration to file"""
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)