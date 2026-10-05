# VISHU'S BOT — Comprehensive Project Documentation

## 1. Executive Overview
**VISHU'S BOT** is a fully feature-complete, standalone desktop AI assistant and system automation suite. Re-architected with a modular Python package structure (`vishus_bot/`), the application integrates real-time voice interaction, multi-tool autonomous planning, PyQt6 graphical user interface, persistent memory, and remote cloud connectivity.

---

## 2. Architecture & Directory Structure

```text
Vishus-Bot/
├── vishus_bot/                # Core Python Package
│   ├── __init__.py            # Application branding and package metadata
│   ├── main.py                # Live assistant loop & Gemini Live API handler
│   ├── ui.py                  # PyQt6 Neural Obsidian dark theme interface
│   ├── or_client.py           # OpenRouter API client integration
│   ├── config.py              # Configuration loader & VISHUS_BOT_* env overrides
│   ├── logging_setup.py       # Standardized [VISHU'S BOT] logging engine
│   ├── agent/                 # Autonomous Agent & Planning Engine
│   │   ├── planner.py         # Multi-step action decomposition module
│   │   ├── executor.py        # Action execution dispatcher
│   │   ├── task_queue.py      # Async task queue manager
│   │   └── error_handler.py   # Diagnostics and recovery handler
│   ├── actions/               # 17 Built-In Action Handlers
│   │   ├── browser_control.py # Web search & Playwright browser control
│   │   ├── code_helper.py     # Code execution & file generation
│   │   ├── computer_control.py# System navigation & downloads manager
│   │   ├── computer_settings.py# Volume, screen, system settings
│   │   ├── desktop.py         # Desktop screenshot & window management
│   │   ├── dev_agent.py       # Autonomous dev agent workspace
│   │   ├── file_controller.py # File I/O manager
│   │   ├── file_processor.py  # Unified file parser
│   │   ├── flight_finder.py   # Flight search integration
│   │   ├── game_updater.py    # Automated task scheduler manager
│   │   ├── open_app.py        # Windows application launcher
│   │   ├── reminder.py        # Task scheduler reminders
│   │   ├── screen_processor.py# Visual screen processor
│   │   ├── send_message.py    # Messaging dispatcher (WhatsApp/Telegram)
│   │   ├── weather_report.py  # Live weather reporter
│   │   ├── web_search.py     # Search engine queries
│   │   └── youtube_video.py   # YouTube transcript summarizer
│   └── memory/                # Context & Memory Manager
│       ├── memory_manager.py  # Automatic memory extraction & storage
│       └── config_manager.py  # Dynamic configuration manager
├── core/                      # Core System Resources
│   └── prompt.txt             # VISHU'S BOT persona and instruction prompt
├── config/                    # Config Files
│   ├── app_config.json        # Supabase and app configuration
│   ├── api_keys.example.json  # API key template
│   └── pet_memory.json        # Saved persistent user memory
├── mobile_ui/                 # Web & Mobile Remote Console
│   ├── index.html             # Responsive remote control dashboard
│   ├── css/styles.css         # Visual styles and animations
│   └── js/                    # Supabase command client scripts
├── scripts/                   # Development & Audit Scripts
│   ├── audit_rename.py        # Automated global branding compliance audit
│   └── port_modules.py        # Rebranding module porting utility
├── tests/                     # Test Suite
│   └── test_branding.py       # Pytest unit and branding tests
├── VishusBot.spec             # PyInstaller build specification
├── build.bat                  # Executable compilation script
├── requirements.txt           # Environment dependencies
└── .env.example               # Environment variables template
```

---

## 3. Source Analysis & Historical Origin

> [!NOTE]
> **Source Analysis**: The project was developed by analyzing the provided FLINT packaged application.
> The architecture was fully re-engineered, rebranded, and ported into the modular `vishus_bot` package structure.
> All application identities, window titles, executable names, logger headers, environment variables, PyInstaller build specs, UI strings, prompt definitions, and action handlers have been transformed to **VISHU'S BOT**.

---

## 4. Environment Variables & Configuration Keys

| Config Key / Env Variable | Description | Default / Example |
| :--- | :--- | :--- |
| `VISHUS_BOT_API_KEY` | Gemini API Key for Live Voice & AI | `AIzaSy...` |
| `VISHUS_BOT_VOICE` | Prebuilt voice name for Live Audio | `Puck` |
| `VISHUS_BOT_APP_NAME` | Executable and Window Title | `VISHU'S BOT` |
| `VISHUS_BOT_SUPABASE_URL` | Remote console database URL | `https://...supabase.co` |
| `VISHUS_BOT_SUPABASE_KEY` | Remote console database anon key | `eyJhbG...` |

---

## 5. Build and Distribution Specifications

- **Executable Target**: `VishusBot.exe`
- **Output Directory**: `dist/VishusBot.exe`
- **Build Command**: `pyinstaller --noconfirm VishusBot.spec`
- **Distributable Package**: `Vishus-Bot.zip`
