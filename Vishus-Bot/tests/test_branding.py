import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

def test_audit_clean():
    assert subprocess.run([sys.executable, str(ROOT/"scripts/audit_rename.py")]).returncode == 0

def test_prompt_branding():
    from vishus_bot.config import load_prompt
    p = load_prompt("Vishu")
    assert "VISHU'S BOT" in p and "{user_name}" not in p

def test_config_loads():
    from vishus_bot.config import load_app_config, command_table
    assert "supabase_url" in load_app_config() and command_table() == "command_queue"

def test_mobile_ui_branding():
    html = (ROOT/"mobile_ui/index.html").read_text(encoding="utf-8")
    assert "VISHU'S" in html
    assert "VISHUS_BOT_CONFIG" in (ROOT/"mobile_ui/js/config.js").read_text(encoding="utf-8")

def test_logger_prefix(capsys):
    from vishus_bot.logging_setup import get_logger
    get_logger("t").info("x")
    assert "[VISHU'S BOT]" in capsys.readouterr().out
