"""Configuration manager for VISHU'S BOT."""

import os
import json
import platform
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
CORE_DIR = BASE_DIR / "core"
APP_CONFIG_PATH = CONFIG_DIR / "app_config.json"
API_KEYS_PATH = CONFIG_DIR / "api_keys.json"
PROMPT_PATH = CORE_DIR / "prompt.txt"

def load_app_config() -> dict:
    if APP_CONFIG_PATH.exists():
        try:
            with open(APP_CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "app_name": "VISHU'S BOT",
        "voice": os.getenv("VISHUS_BOT_VOICE", "Puck"),
        "supabase_url": os.getenv("VISHUS_BOT_SUPABASE_URL", ""),
        "supabase_key": os.getenv("VISHUS_BOT_SUPABASE_KEY", "")
    }

def get_config() -> dict:
    if API_KEYS_PATH.exists():
        try:
            with open(API_KEYS_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return load_app_config()

def get_api_key() -> str:
    env_key = os.getenv("VISHUS_BOT_API_KEY") or os.getenv("GEMINI_API_KEY")
    if env_key:
        return env_key
    if API_KEYS_PATH.exists():
        try:
            with open(API_KEYS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("gemini_api_key", "")
        except Exception:
            pass
    return ""

def load_prompt(user_name: str = "User") -> str:
    if PROMPT_PATH.exists():
        try:
            text = PROMPT_PATH.read_text(encoding="utf-8")
            return text.replace("{user_name}", user_name)
        except Exception:
            pass
    return "You are VISHU'S BOT - a highly intelligent AI assistant."

def command_table() -> str:
    return "command_queue"

def get_os() -> str:
    """Returns: 'windows' | 'mac' | 'linux'"""
    system = platform.system().lower()
    if "win" in system:
        return "windows"
    elif "darwin" in system or "mac" in system:
        return "mac"
    return "linux"

def is_windows() -> bool:
    return get_os() == "windows"

def is_mac() -> bool:
    return get_os() == "mac"

def is_linux() -> bool:
    return get_os() == "linux"
