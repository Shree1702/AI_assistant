# AI_assistant
Welcome to AI Assistant, a voice-controlled assistant built using Python and Tkinter, designed to perform various tasks such as playing music, telling jokes, searching the web, and much more. This assistant can recognize and respond to voice commands, making it a versatile tool for personal and productivity use.

# Features
Voice Recognition: Uses speech_recognition to interpret voice commands.
Text-to-Speech: Uses pyttsx3 to convert text responses into speech.
Task Automation: Can open websites, tell the time, play songs on YouTube, tell jokes, etc.
Graphical Interface: Built with Tkinter for an interactive UI.
GIF Support: Displays an animated GIF while listening and processing commands.
# Setup and Installation
# Prerequisites
Python 3.x: Ensure Python is installed on your system.
pip: Python's package installer should be available.
# Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Shree1702/ai_assistant.git
cd ai_assistant
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Make sure you have the following external dependencies installed:

PyAudio (for microphone access)
Pillow (for handling images and GIFs)
If not installed, you can add them manually using pip:

bash
Copy code
pip install pyaudio pillow
# Running the Assistant
Run the AI Assistant using the following command:

bash
Copy code
python main.py
This will start the application and the assistant will be ready to take commands.

# Usage
Greeting: The assistant will greet you based on the time of day.
Playing Music: Say play [song name] to play a song on YouTube.
Telling Time: Ask what time is it? to get the current time.
Wikipedia Search: Use who is [person] or wikipedia [topic] to get a summary from Wikipedia.
Jokes: Say tell me a joke for a quick laugh.
Web Search: Say search [query] to search on Google.
Open Applications/Websites: Commands like open YouTube, open Gmail, etc., will open the respective websites.
Shutdown/Restart: You can instruct the assistant to shut down or restart your PC with commands like shut down or restart.
# Contributing
Contributions are welcome! Please fork this repository, create a new branch, make your changes, and submit a pull request. Please ensure that your contributions align with the existing code style and functionality.

# Acknowledgments
Special thanks to the open-source community for their contributions and libraries.
Credits to the developers of the libraries used: speech_recognition, pyttsx3, Pillow, wikipedia-api, pyjokes, etc.
