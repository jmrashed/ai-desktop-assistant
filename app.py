# app.py
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import os
import pywhatkit
import platform
import threading
import queue
import json
import requests
import random
import wolframalpha
import calendar
import pytz
import subprocess
from bs4 import BeautifulSoup
import speedtest

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app)

# Configuration
WEATHER_API_KEY = "your-openweathermap-api-key"
WOLFRAM_API_KEY = "VVV7A3-T5HXTWTGPL"
NEWS_API_KEY = "your-newsapi-key"

class VoiceAssistant:
    def __init__(self):
        self.message_queue = queue.Queue()
        self.speak = self.initialize_tts()
        self.recognizer = sr.Recognizer()
        self.user_name = "User"
        self.assistant_name = "Assistant"
        self.commands = {
            'wikipedia': self.search_wikipedia,
            'weather': self.get_weather,
            'time': self.get_time,
            'date': self.get_date,
            'news': self.get_news,
            'joke': self.tell_joke,
            'calculate': self.calculate,
            'google': self.search_google,
            'system': self.system_stats,
            'speed test': self.internet_speed,
            'reminder': self.set_reminder,
            'music': self.play_music,
            # 'email': self.send_email
        }

    def initialize_tts(self):
        """Initialize text-to-speech based on platform"""
        system = platform.system().lower()
        
        if system == 'darwin':  # macOS
            def speak(text):
                os.system(f'say "{text}"')
                socketio.emit('response', {'text': text})
            return speak
                
        elif system == 'windows':  # Windows
            import pyttsx3
            engine = pyttsx3.init()
            engine.setProperty('rate', 175)
            def speak(text):
                engine.say(text)
                engine.runAndWait()
                socketio.emit('response', {'text': text})
            return speak
                
        else:  # Linux or other systems
            import gtts
            from playsound import playsound
            import tempfile
            
            def speak(text):
                with tempfile.NamedTemporaryFile(delete=True) as fp:
                    tts = gtts.gTTS(text=text, lang='en')
                    temp_file = f"{fp.name}.mp3"
                    tts.save(temp_file)
                    playsound(temp_file)
                    os.remove(temp_file)
                    socketio.emit('response', {'text': text})
            return speak

    def search_wikipedia(self, query):
        """Search Wikipedia for information"""
        try:
            self.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            self.speak("According to Wikipedia")
            return results
        except Exception as e:
            return f"Error searching Wikipedia: {str(e)}"

    def get_weather(self, city):
        """Get weather information for a city"""
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if data["cod"] != "404":
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                return f"The temperature in {city} is {temp}°C with {desc}"
            else:
                return "City not found"
        except Exception as e:
            return f"Error getting weather: {str(e)}"

    def get_time(self):
        """Get current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

    def get_date(self):
        """Get current date"""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {current_date}"

    def get_news(self):
        """Get latest news headlines"""
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
            response = requests.get(url)
            news = response.json()
            headlines = []
            
            for article in news['articles'][:5]:
                headlines.append(article['title'])
                
            return "Here are the top headlines:\n" + "\n".join(headlines)
        except Exception as e:
            return f"Error getting news: {str(e)}"

    def tell_joke(self):
        """Tell a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!"
        ]
        return random.choice(jokes)

    def calculate(self, query):
        """Calculate using WolframAlpha"""
        try:
            client = wolframalpha.Client(WOLFRAM_API_KEY)
            res = client.query(query)
            return next(res.results).text
        except Exception as e:
            return f"Error calculating: {str(e)}"

    def search_google(self, query):
        """Search Google"""
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new_tab(url)
        return f"Here are the search results for {query}"

    def system_stats(self):
        """Get system statistics"""
        try:
            cpu = subprocess.getoutput("top -l 1 | grep 'CPU usage'")
            memory = subprocess.getoutput("top -l 1 | grep 'PhysMem'")
            return f"System Stats:\n{cpu}\n{memory}"
        except Exception as e:
            return f"Error getting system stats: {str(e)}"

    def internet_speed(self):
        """Test internet speed"""
        try:
            st = speedtest.Speedtest()
            self.speak("Testing download speed...")
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            self.speak("Testing upload speed...")
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            return f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps"
        except Exception as e:
            return f"Error testing internet speed: {str(e)}"

    def set_reminder(self, reminder_text, time_str):
        """Set a reminder"""
        try:
            # This is a simple implementation. In a real app, you'd want to use a proper scheduler
            reminder_time = datetime.datetime.strptime(time_str, "%H:%M")
            current_time = datetime.datetime.now()
            
            if reminder_time.time() < current_time.time():
                reminder_time = reminder_time + datetime.timedelta(days=1)
                
            time_diff = reminder_time - current_time
            
            def remind():
                time.sleep(time_diff.total_seconds())
                self.speak(f"Reminder: {reminder_text}")
                
            threading.Thread(target=remind).start()
            return f"Reminder set for {time_str}"
        except Exception as e:
            return f"Error setting reminder: {str(e)}"

    def play_music(self, query):
        """Play music using YouTube"""
        try:
            pywhatkit.playonyt(query)
            return f"Playing {query} on YouTube Music"
        except Exception as e:
            return f"Error playing music: {str(e)}"

    def process_command(self, statement):
        """Process voice commands"""
        try:
            statement = statement.lower()
            
            # Check for wake word
            if self.assistant_name.lower() not in statement:
                return "Waiting for wake word..."
                
            # Remove wake word from statement
            statement = statement.replace(self.assistant_name.lower(), "").strip()
            
            # Process different commands
            for key, func in self.commands.items():
                if key in statement:
                    if key == 'wikipedia':
                        return func(statement)
                    elif key == 'weather':
                        city = statement.replace('weather', '').replace('in', '').strip()
                        return func(city)
                    elif key == 'calculate':
                        query = statement.replace('calculate', '').strip()
                        return func(query)
                    elif key == 'google':
                        query = statement.replace('google', '').strip()
                        return func(query)
                    elif key == 'reminder':
                        # Extract time and reminder text
                        # Example command: "set reminder at 14:30 to take medicine"
                        parts = statement.split('at')
                        if len(parts) == 2:
                            time_str = parts[1].split('to')[0].strip()
                            reminder_text = parts[1].split('to')[1].strip()
                            return func(reminder_text, time_str)
                    elif key == 'music':
                        query = statement.replace('play', '').replace('music', '').strip()
                        return func(query)
                    else:
                        return func()
            
            return "I'm not sure how to help with that. Could you please try another command?"
            
        except Exception as e:
            return f"Error processing command: {str(e)}"

assistant = VoiceAssistant()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start_listening')
def handle_listening():
    with sr.Microphone() as source:
        socketio.emit('status', {'text': 'Listening...'})
        try:
            audio = assistant.recognizer.listen(source, timeout=5)
            statement = assistant.recognizer.recognize_google(audio, language='en-in')
            socketio.emit('command', {'text': statement})
            response = assistant.process_command(statement)
            assistant.speak(response)
        except sr.WaitTimeoutError:
            socketio.emit('error', {'text': 'No speech detected within timeout'})
        except sr.UnknownValueError:
            socketio.emit('error', {'text': "Sorry, I didn't catch that"})
        except sr.RequestError:
            socketio.emit('error', {'text': 'Sorry, there was an error with the speech recognition service'})
        except Exception as e:
            socketio.emit('error', {'text': f'Error: {str(e)}'})

if __name__ == '__main__':
    socketio.run(app, debug=True)