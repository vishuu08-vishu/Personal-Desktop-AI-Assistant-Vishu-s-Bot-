# VISHU'S BOT — Advanced Desktop AI Assistant

**VISHU'S BOT** is a Windows-based desktop AI assistant designed to make everyday computer tasks easier through voice interaction, automation, intelligent planning, and remote control. It combines real-time voice communication, a modern PyQt6 interface, AI-powered task execution, system automation, and a web/mobile control console into a single application.

## 🌟 Key Features

* **Real-Time Voice Interaction:** Uses the Gemini Live API to provide two-way, real-time voice communication with high-quality audio input and output. The assistant is configured to use the **Puck** voice.

* **Modern PyQt6 Interface:** Features a dark-themed interface with an animated visualizer, live system information such as CPU, RAM, GPU, and network usage, along with a real-time diagnostic log.

* **AI Agent & Task Automation:** The assistant can understand requests, plan multiple steps, and execute tasks using a collection of built-in tools, including:

  * **Web & Browser Automation:** Web searches, price comparisons, website navigation, and browser interaction using Playwright.
  * **Desktop Automation:** Launching applications, managing the desktop, controlling volume, and changing system settings.
  * **File & Media Processing:** Reading files, generating code, and summarizing YouTube transcripts.
  * **Flight Search & Scheduled Tasks:** Searching flight routes and handling automated background updates through Windows Task Scheduler.
  * **Messaging:** Sending messages through WhatsApp and Telegram using voice or automated commands.

* **Persistent Memory:** Maintains useful user context across sessions through an automatic memory system stored in `pet_memory.json`.

* **Remote Web & Mobile Control:** Includes a Supabase-powered remote console that allows the assistant to be accessed and controlled from other devices through the `mobile_ui/` interface.

---

## 🚀 Getting Started

### 1. Requirements

Before running the project, make sure you have:

* Windows 10 or Windows 11
* Python 3.10 or newer

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

### 2. Configure the API Key

Add your Gemini API key to `config/api_keys.json`:

```json
{
  "gemini_api_key": "YOUR_GEMINI_API_KEY_HERE"
}
```

You can also configure the assistant through environment variables:

```bash
set VISHUS_BOT_API_KEY=YOUR_GEMINI_API_KEY
set VISHUS_BOT_VOICE=Puck
```

### 3. Run the Assistant

Start the application directly using Python:

```bash
python -m vishus_bot.main
```

---

## 🛠️ Creating the Windows Executable

The project can also be packaged as a standalone Windows application using PyInstaller.

Run:

```cmd
build.bat
```

Or build it directly with:

```cmd
pyinstaller --noconfirm VishusBot.spec
```

After the build is completed, the executable will be available at:

```text
dist/VishusBot.exe
```

---

## 🧪 Testing

The project includes automated tests and a branding audit to help verify that the application is working correctly and that the updated project name is used consistently.

Run the test suite with:

```bash
pytest tests/
```

To manually check the project for naming and branding issues:

```bash
python scripts/audit_rename.py
```

---

## 📱 Remote Mobile Console

The project also includes a web-based interface for remotely interacting with **VISHU'S BOT**.

1. Open the `mobile_ui/` directory.
2. Copy `mobile_ui/js/config.example.js` and rename it to `config.js`.
3. Add your Supabase URL and API key to the configuration.
4. Open `mobile_ui/index.html` in a browser, or host the interface on a local server.
5. Access the interface from a mobile device or another computer on the network.

The remote console provides a convenient way to interact with the assistant without directly using the desktop application.
