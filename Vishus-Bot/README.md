# VISHU'S BOT — Advanced Desktop AI Assistant

**VISHU'S BOT** is a state-of-the-art Windows desktop AI assistant and automation suite featuring real-time bidirectional voice streaming, an interactive PyQt6 dark mode interface, autonomous multi-step agent planning, multi-modal vision, system automation, and a remote web/mobile control console.

---

## 🌟 Key Features

- **Real-Time Voice Streaming**: Powered by Gemini Live API with high-quality real-time audio input/output (configured with the dynamic **Puck** prebuilt voice).
- **Interactive PyQt6 Visual UI**: Neural Obsidian dark mode design with animated visualizer, system resource metrics (CPU, RAM, GPU, network), and real-time diagnostic logger.
- **Autonomous Agent & Planner**: Intelligent multi-tool execution engine equipped with 17 built-in actions:
  - **Browser & Web Control**: Web searching, price comparison, site navigation via Playwright.
  - **Computer & Desktop Automation**: App launcher, desktop management, volume and system settings.
  - **File & Media Processing**: Intelligent file reading, code generation, YouTube transcript summarization.
  - **Flight Search & Game Updating**: Flight route queries and automated Windows Task Scheduler background updates.
  - **WhatsApp & Telegram Dispatch**: Hands-free messaging dispatch.
- **Persistent Memory Engine**: Automatic user context extraction and memory storage (`pet_memory.json`).
- **Remote Web & Mobile Console**: Supabase-backed real-time remote command console (`mobile_ui/`) for cross-device control.

---

## 🚀 Quick Start

### 1. Requirements & Setup
- Windows 10/11
- Python 3.10+
- Dependencies installation:
```bash
pip install -r requirements.txt
```

### 2. Configuration
Set your Gemini API Key in `config/api_keys.json` or as an environment variable:
```json
{
  "gemini_api_key": "YOUR_GEMINI_API_KEY_HERE"
}
```
Or via environment variables:
```bash
set VISHUS_BOT_API_KEY=YOUR_GEMINI_API_KEY
set VISHUS_BOT_VOICE=Puck
```

### 3. Launching the Assistant
Run directly with Python:
```bash
python -m vishus_bot.main
```

---

## 🛠️ Building the Standalone Executable

To build the standalone Windows executable (`VishusBot.exe`):

```cmd
build.bat
```
or run PyInstaller directly:
```cmd
pyinstaller --noconfirm VishusBot.spec
```

The resulting executable will be generated at:
```text
dist/VishusBot.exe
```

---

## 🧪 Testing & Verification

Run the automated test suite and global branding audit:
```bash
pytest tests/
```

Run the audit script manually:
```bash
python scripts/audit_rename.py
```

---

## 📱 Mobile Remote Console

1. Navigate to `mobile_ui/`.
2. Copy `mobile_ui/js/config.example.js` to `mobile_ui/js/config.js` and set your Supabase URL and key.
3. Open `mobile_ui/index.html` in any browser or host it on your local server for mobile access.
