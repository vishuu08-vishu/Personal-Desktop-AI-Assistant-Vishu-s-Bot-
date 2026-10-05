"""Port and rebrand all modules from FLINT-master to Vishus-Bot."""

import os
import re
from pathlib import Path

SRC_DIR = Path(r"c:\Users\user\Downloads\FLINT-master\FLINT-master")
DST_DIR = Path(r"c:\Users\user\Downloads\Vishus-Bot\Vishus-Bot")
VISHUS_BOT_PKG = DST_DIR / "vishus_bot"

VISHUS_BOT_PKG.mkdir(parents=True, exist_ok=True)
(VISHUS_BOT_PKG / "agent").mkdir(parents=True, exist_ok=True)
(VISHUS_BOT_PKG / "actions").mkdir(parents=True, exist_ok=True)
(VISHUS_BOT_PKG / "memory").mkdir(parents=True, exist_ok=True)

REPLACEMENTS = [
    # Class / Specific Identifiers
    ("from ui import FlintUI", "from vishus_bot.ui import VishusBotUI"),
    ("from ui import", "from vishus_bot.ui import"),
    ("import ui", "from vishus_bot import ui"),
    ("FlintUI", "VishusBotUI"),
    ("FlintLive", "VishusBotLive"),
    ("FLINTWindow", "VishusBotWindow"),
    ("FlintAssistant", "VishusBotAssistant"),
    ("flint_config", "vishus_bot_config"),
    ("FLINT_VERSION", "VISHUS_BOT_VERSION"),
    ("shutdown_flint", "shutdown_vishus_bot"),
    ("flint_speaking", "vishus_bot_speaking"),
    ("flint_text", "vishus_bot_text"),
    ("FLINT_Game_Update", "VishusBot_Game_Update"),
    ("flint_scratch", "vishus_bot_scratch"),
    ("flint_downloads", "vishus_bot_downloads"),
    ("flint_projects", "vishus_bot_projects"),
    ("FLINT_APP_NAME", "VISHUS_BOT_APP_NAME"),
    ("FLINT_HOME", "VISHUS_BOT_HOME"),
    ("FLINT_CONFIG", "VISHUS_BOT_CONFIG"),
    ("FLINT_DATA", "VISHUS_BOT_DATA"),
    ("FLINT_API", "VISHUS_BOT_API"),
    ("voice_name=\"Charon\"", "voice_name=\"Puck\""),
    ("voice_name='Charon'", "voice_name='Puck'"),
    
    # Package imports relative fixes
    ("from memory.memory_manager import", "from vishus_bot.memory.memory_manager import"),
    ("from memory.config_manager import", "from vishus_bot.memory.config_manager import"),
    ("from agent.planner import", "from vishus_bot.agent.planner import"),
    ("from agent.executor import", "from vishus_bot.agent.executor import"),
    ("from agent.task_queue import", "from vishus_bot.agent.task_queue import"),
    ("from agent.error_handler import", "from vishus_bot.agent.error_handler import"),
    ("from actions.", "from vishus_bot.actions."),
    ("import or_client", "from vishus_bot import or_client"),
    ("from or_client import", "from vishus_bot.or_client import"),
    
    # General Strings
    ("FLINT ODIN", "VISHU'S BOT"),
    ("FLINT AI", "VISHU'S BOT AI"),
    ("FLINT Assistant", "VISHU'S BOT Assistant"),
    ("FLINT Personal AI", "VISHU'S BOT Personal AI"),
    ("Welcome to FLINT", "Welcome to VISHU'S BOT"),
    ("FLINT is listening", "VISHU'S BOT is listening"),
    ("FLINT is thinking", "VISHU'S BOT is thinking"),
    ("FLINT is speaking", "VISHU'S BOT is speaking"),
    ("FLINT", "VISHU'S BOT"),
    ("Flint", "VishusBot"),
    ("flint", "vishus_bot"),
    ("Personal AI", "VISHU'S BOT AI ASSISTANT")
]

def transform_content(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text

# Port main files
file_map = {
    SRC_DIR / "main.py": VISHUS_BOT_PKG / "main.py",
    SRC_DIR / "ui.py": VISHUS_BOT_PKG / "ui.py",
    SRC_DIR / "or_client.py": VISHUS_BOT_PKG / "or_client.py",
}

# Port subdirectories
for sub in ["agent", "actions", "memory"]:
    src_sub = SRC_DIR / sub
    dst_sub = VISHUS_BOT_PKG / sub
    for f in src_sub.glob("*.py"):
        file_map[f] = dst_sub / f.name

count = 0
for src_f, dst_f in file_map.items():
    if src_f.exists():
        content = src_f.read_text(encoding="utf-8")
        transformed = transform_content(content)
        dst_f.write_text(transformed, encoding="utf-8")
        print(f"Ported: {src_f.name} -> {dst_f}")
        count += 1

print(f"Total files ported & rebranded: {count}")
