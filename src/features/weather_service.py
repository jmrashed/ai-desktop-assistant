import requests

class WeatherService:
    def __init__(self, config):
        self.api_key = config.get('weather_api_key', '')
    
    def get_weather(self, city):
        """Get weather information for a city"""
        if not self.api_key:
            return "Weather API key not configured"
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if data["cod"] != "404":
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                return f"Weather in {city}: {temp}°C, {desc}"
            else:
                return "City not found"
        except Exception as e:
            return f"Error getting weather: {str(e)}"