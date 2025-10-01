import platform
import os
import speech_recognition as sr

class SpeechEngine:
    def __init__(self):
        self.speak = self._initialize_tts()
        self.recognizer = sr.Recognizer()
    
    def _initialize_tts(self):
        """Initialize text-to-speech based on platform"""
        system = platform.system().lower()
        
        if system == 'darwin':  # macOS
            def speak(text):
                os.system(f'say "{text}"')
            return speak
        elif system == 'windows':  # Windows
            try:
                import pyttsx3
                engine = pyttsx3.init()
                engine.setProperty('rate', 175)
                def speak(text):
                    engine.say(text)
                    engine.runAndWait()
                return speak
            except:
                return lambda x: print(f"Speech: {x}")
        else:  # Linux
            try:
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
                return speak
            except:
                return lambda x: print(f"Speech: {x}")
    
    def listen(self, timeout=5):
        """Listen for voice input"""
        with sr.Microphone() as source:
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                return self.recognizer.recognize_google(audio, language='en-in').lower()
            except:
                return ""