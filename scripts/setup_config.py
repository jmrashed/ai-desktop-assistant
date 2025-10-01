import json
import os

def setup_configuration():
    """Setup configuration for the enhanced assistant"""
    print("=== Enhanced AI Assistant Configuration ===\n")
    
    config = {}
    
    # Wake word setup
    wake_word = input("Enter your preferred wake word (default: 'assistant'): ").strip()
    config['wake_word'] = wake_word if wake_word else 'assistant'
    
    # Weather API setup
    print("\nFor weather features, you need an OpenWeatherMap API key.")
    print("Get one free at: https://openweathermap.org/api")
    weather_api = input("Enter your OpenWeatherMap API key (optional): ").strip()
    config['weather_api_key'] = weather_api
    
    # Security PIN
    pin = input("Set a 4-digit PIN for secure commands (default: '1234'): ").strip()
    config['user_pin'] = pin if pin and pin.isdigit() and len(pin) == 4 else '1234'
    
    # Save configuration
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\nConfiguration saved!")
    print(f"Wake word: {config['wake_word']}")
    print(f"Weather API: {'Configured' if config['weather_api_key'] else 'Not configured'}")
    print(f"Security PIN: Set")
    
    print("\nYou can now run the enhanced assistant with: python enhanced_assistant.py")

if __name__ == '__main__':
    setup_configuration()