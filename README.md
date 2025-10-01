# AI Desktop Assistant

A Python-based AI desktop assistant designed to perform various tasks like opening websites, searching Wikipedia, playing music, retrieving the current time, and more. The assistant uses speech recognition and text-to-speech to interact with the user in a conversational manner.

 

## Features

### Core Features
- **Wikipedia Search**: Ask questions like "Who is Elon Musk?" or "What is Python?"
- **Website Commands**: Open popular websites such as YouTube, Google, Gmail, and LeetCode.
- **Music Playback**: Play songs directly from YouTube with a simple command.
- **Time Queries**: Get the current time instantly.
- **News Updates**: Access the latest news headlines from Google News.
- **Search the Web**: Perform Google searches directly from your voice commands.
- **Platform-Specific TTS**: Text-to-Speech support for macOS, Windows, and Linux.

### Enhanced Features ✨
- **Weather Updates**: Get real-time weather information for any city
- **File Management**: Search, create folders, and manage files with voice commands
- **Task Automation**: Open applications and control desktop tasks
- **Customizable Wake Word**: Set your own wake word for activation
- **Security Features**: PIN authentication for sensitive commands
- **System Information**: Get CPU, memory, and disk usage statistics
- **Smart Reminders**: Set voice-activated reminders
- **GUI Interface**: Optional graphical user interface for easier interaction

## Prerequisites

Make sure you have the following installed:

- Python 3.7 or later
- Required Python libraries (see below for installation)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jmrashed/ai-desktop-assistant.git
   cd ai-desktop-assistant
   ```

2. **Install dependencies**:
   Install the required Python libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   **Original Version Libraries:**
   - `SpeechRecognition`
   - `pyttsx3` (for Windows)
   - `gTTS` (for Linux)
   - `playsound` (for Linux)
   - `pywhatkit`
   - `wikipedia-api`
   - `platform`
   - `datetime`
   
   **Enhanced Version Additional Libraries:**
   - `requests` (for weather API)
   - `psutil` (for system information)
   - `pathlib` (for file operations)

3. **Choose your version**:
   
   **Original Version:**
   ```bash
   python assistant.py
   ```
   
   **Enhanced Version (Recommended):**
   ```bash
   # First, install enhanced dependencies
   pip install -r enhanced_requirements.txt
   
   # Setup configuration
   python setup_config.py
   
   # Run enhanced assistant
   python enhanced_assistant.py
   ```
   
   **GUI Version:**
   ```bash
   python gui_assistant.py
   ```
   
   **Web Version:**
   ```bash
   python app.py
   ```

## Usage

### Basic Commands
1. Start the assistant by running your chosen version.
2. The assistant will greet you based on the time of day.
3. Say your wake word (default: "assistant") followed by commands:

**Original Commands:**
- **"Assistant, who is Albert Einstein?"**: Wikipedia search
- **"Assistant, open YouTube"**: Opens websites
- **"Assistant, play Despacito"**: Plays music on YouTube
- **"Assistant, what time is it?"**: Current time
- **"Assistant, goodbye"**: Shuts down

### Enhanced Commands ✨
**Weather:**
- **"Assistant, weather in London"**: Get weather information

**File Management:**
- **"Assistant, search file document.pdf"**: Find files
- **"Assistant, create folder MyFolder"**: Create directories
- **"Assistant, delete file oldfile.txt"**: Delete files (requires PIN)

**System Control:**
- **"Assistant, open notepad"**: Launch applications
- **"Assistant, system info"**: Get system statistics

**Customization:**
- **"Assistant, change wake word"**: Set custom wake word
- **"Assistant, remind me to call mom in 30 minutes"**: Set reminders

## Project Structure

```
ai-desktop-assistant/
├── assistant.py              # Original assistant script
├── enhanced_assistant.py     # Enhanced version with new features
├── gui_assistant.py          # GUI version using tkinter
├── setup_config.py           # Configuration setup script
├── app.py                    # Flask web version
├── requirements.txt          # Original dependencies
├── enhanced_requirements.txt # Enhanced version dependencies
├── config.json              # Configuration file (auto-generated)
├── templates/               # Web templates
└── README.md                # Documentation
```

## Platform-Specific Text-to-Speech

- **macOS**: Uses the built-in `say` command for text-to-speech.
- **Windows**: Uses the `pyttsx3` library.
- **Linux**: Uses `gTTS` and `playsound`.

If TTS is unavailable for a platform, the assistant will fall back to printing the output to the terminal.

## Configuration

The enhanced version supports configuration through `config.json`:

```json
{
  "wake_word": "assistant",
  "weather_api_key": "your-openweathermap-api-key",
  "user_pin": "1234"
}
```

**To get a weather API key:**
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key
4. Run `python setup_config.py` to configure

## Security Features

The enhanced version includes basic security:
- **PIN Authentication**: Required for file deletion and sensitive operations
- **Configurable Access**: Customize which commands require authentication
- **Safe Defaults**: Secure settings by default

## Available Versions

1. **assistant.py** - Original lightweight version
2. **enhanced_assistant.py** - Feature-rich command-line version
3. **gui_assistant.py** - User-friendly GUI version
4. **app.py** - Web-based version with Flask

## Contributing

Feel free to contribute to the project! Here's how:

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

### Suggested Improvements
- Calendar integration (Google Calendar, Outlook)
- Smart home device control
- Email and messaging capabilities
- Multi-language support
- Voice authentication
- Plugin system for custom commands

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Troubleshooting

**Common Issues:**

1. **Microphone not working**: Check system permissions and microphone access
2. **TTS not working**: Install platform-specific TTS libraries
3. **Weather not working**: Ensure you have a valid OpenWeatherMap API key
4. **File operations failing**: Check file permissions and paths

**Performance Tips:**
- Use the GUI version for better user experience
- Configure a shorter wake word for faster activation
- Close other audio applications for better speech recognition

## Contact

If you have any questions or feedback, feel free to reach out:

- **Author**: Md Rasheduzzaman
- **Email**: jmrashed@gmail.com
- **GitHub**: [jmrashed](https://github.com/jmrashed)

---

**Enhanced by AI Assistant** - Added weather updates, file management, task automation, customizable wake words, security features, and GUI interface.
 