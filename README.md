# 🎙️ Jarvis Virtual Assistant

Jarvis is a smart voice-activated virtual assistant built with Python. It can open websites, play your favorite music, and answer complex questions using the **Cohere AI** engine.

---

## ✨ Features

- **Voice Activation**: Responds to the wake word "Jarvis".
- **AI-Powered Chat**: Integrated with Cohere API for intelligent and concise answers.
- **Web Automation**: Opens Google, YouTube, WhatsApp, Facebook, and News with voice commands.
- **Music Player**: Plays specific songs from a pre-defined library via YouTube.
- **Text-to-Speech (TTS)**: Jarvis talks back to you using the `pyttsx3` engine.
- **Environment Security**: API keys are securely managed using `.env` files.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.x
- A working Microphone.
- A **Cohere API Key**.

### 2. Installation
Install the necessary libraries:
```bash
pip install speechrecognition pyttsx3 cohere python-dotenv
Use code with caution.

Note: If you face issues with PyAudio, install it separately using your OS package manager.
3. Setup API Key
Create a .env file in the project folder:
text
MY_API_KEY=your_cohere_api_key_here
Use code with caution.

4. Running Jarvis
Start the assistant by running:
python main.py
🛠️ Commands to Try
Activation: Say "Jarvis" and wait for the response.
Websites: "Open Google", "Open Youtube", "Open News".
Music: "Play flight", "Play purple", "Play mirror". You can add your favorite songs in music dictionary.
AI Questions: Ask anything else, and Jarvis will use AI to answer!
📂 Project Structure
main.py: The core logic and voice processing.
.env: (Ignored by Git) Stores your sensitive API keys.
.gitignore: Prevents .env and .venv from being uploaded.
📜 License
Distributed under the MIT License.
Created with ❤️ by Ayyaan