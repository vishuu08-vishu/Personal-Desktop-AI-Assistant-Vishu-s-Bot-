"""Fix all legacy un-prefixed imports across the vishus_bot package."""

import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent / "vishus_bot"

REPLACEMENTS = [
    (r'\bfrom config import\b', 'from vishus_bot.config import'),
    (r'\bimport config\b', 'from vishus_bot import config'),
    (r'\bfrom agent\.', 'from vishus_bot.agent.'),
    (r'\bimport agent\.', 'import vishus_bot.agent.'),
    (r'\bfrom memory\.', 'from vishus_bot.memory.'),
    (r'\bimport memory\.', 'import vishus_bot.memory.'),
    (r'\bfrom actions\.', 'from vishus_bot.actions.'),
    (r'\bimport actions\.', 'import vishus_bot.actions.'),
    (r'\bfrom or_client import\b', 'from vishus_bot.or_client import'),
    (r'\bimport or_client\b', 'from vishus_bot import or_client'),
]

fixed_count = 0
for py_file in ROOT_DIR.rglob("*.py"):
    content = py_file.read_text(encoding="utf-8")
    new_content = content
    for pattern, repl in REPLACEMENTS:
        new_content = re.sub(pattern, repl, new_content)
    
    if new_content != content:
        py_file.write_text(new_content, encoding="utf-8")
        print(f"Fixed imports in: {py_file.relative_to(ROOT_DIR.parent)}")
        fixed_count += 1

print(f"Total files updated: {fixed_count}")
