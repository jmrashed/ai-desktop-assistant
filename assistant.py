import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import os
import pywhatkit
import platform

# Initialize text-to-speech based on platform
def initialize_tts():
    system = platform.system().lower()
    
    if system == 'darwin':  # macOS
        try:
            import os
            def speak(text):
                os.system(f'say "{text}"')
            return speak
        except Exception as e:
            print(f"Error initializing macOS speech: {e}")
            
    elif system == 'windows':  # Windows
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.setProperty('rate', 175)
            def speak(text):
                engine.say(text)
                engine.runAndWait()
            return speak
        except Exception as e:
            print(f"Error initializing Windows speech: {e}")
            
    else:  # Linux or other systems
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
        except Exception as e:
            print(f"Error initializing Linux speech: {e}")
    
    # Fallback to print-only if all TTS methods fail
    return lambda x: print(f"Speech output (TTS not available): {x}")

# Initialize the speech function
speak = initialize_tts()

def wish_on_startup():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    message = f"Hello, {greeting}"
    print(message)
    speak(message)

def get_instructions():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening now...")
        try:
            audio = r.listen(source, timeout=5)
            statement = r.recognize_google(audio, language='en-in')
            print(f"You asked: {statement}\n")
            return statement.lower()
        except sr.WaitTimeoutError:
            print("No speech detected within timeout")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

def main():
    wish_on_startup()
    
    while True:
        speak("How can I help you?")
        statement = get_instructions()
        
        if not statement:
            continue
            
        # Wikipedia queries
        if 'what is' in statement or 'who is' in statement:
            query = statement.replace("what is", "").replace("who is", "").strip()
            if query:
                speak('Searching Wikipedia...')
                try:
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("Sorry, I couldn't find that information on Wikipedia")
        
        # Social media commands
        elif 'open facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Facebook is opened")
            
        elif 'open instagram' in statement:
            webbrowser.open_new_tab("https://www.instagram.com")
            speak("Instagram is opened")
        
        elif 'open twitter' in statement:
            webbrowser.open_new_tab("https://www.twitter.com")
            speak("Twitter is opened")
        
        elif 'open linkedin' in statement:
            webbrowser.open_new_tab("https://www.linkedin.com")
            speak("LinkedIn is opened")
        
        elif 'open tiktok' in statement:
            webbrowser.open_new_tab("https://www.tiktok.com")
            speak("TikTok is opened")
        
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is opened")
        
        elif 'open snapchat' in statement:
            webbrowser.open_new_tab("https://www.snapchat.com")
            speak("Snapchat is opened")
        
        elif 'open pinterest' in statement:
            webbrowser.open_new_tab("https://www.pinterest.com")
            speak("Pinterest is opened")
        
        elif 'open reddit' in statement:
            webbrowser.open_new_tab("https://www.reddit.com")
            speak("Reddit is opened")
        
        elif 'open whatsapp' in statement:
            webbrowser.open_new_tab("https://web.whatsapp.com")
            speak("WhatsApp is opened")
        
        elif 'open telegram' in statement:
            webbrowser.open_new_tab("https://web.telegram.org")
            speak("Telegram is opened")
            
        # Play music (YouTube)
        elif 'play' in statement:
            song = statement.replace('play', '').strip()
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        
        # Website commands
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is opened")
            
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://gmail.com")
            speak("Google Mail is opened")
            
        # Time query
        elif 'time' in statement:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")
            
        # Additional features
        elif "open leetcode" in statement:
            webbrowser.open_new_tab("https://leetcode.com/problemset/all/")
            speak("Here is leetcode, Have a great time solving problems!")
            
        elif 'news' in statement:
            webbrowser.open_new_tab("https://news.google.com")
            speak('Here are some headlines from Google News. Happy reading')
            
        elif 'search' in statement:
            query = statement.replace("search", "").strip()
            if query:
                url = f"https://www.google.com/search?q={query}"
                webbrowser.open_new_tab(url)
                speak(f"Here are the search results for {query}")
            
        # Assistant information
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your personal assistant. I can help you with tasks like opening websites, searching information, telling time, and playing music.')
            
        # Exit commands
        elif any(cmd in statement for cmd in ["goodbye", "ok bye", "shut down", "exit", "quit"]):
            speak('Assistant shutting down. Goodbye!')
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")
