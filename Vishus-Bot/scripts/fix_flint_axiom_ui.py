"""Fix F.L.I.N.T. and AXIOM branding in UI and action files."""

import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent / "vishus_bot"

REPLACEMENTS = [
    ("F.L.I.N.T - AXIOM", "VISHU'S BOT"),
    ("F.L.I.N.T.", "VISHU'S BOT"),
    ("F.L.I.N.T", "VISHU'S BOT"),
    ("AXIOM", "VISHU'S BOT"),
    ("Rishi Industries", "Vishu Industries"),
]

fixed_count = 0
for py_file in ROOT_DIR.rglob("*.py"):
    content = py_file.read_text(encoding="utf-8")
    new_content = content
    for old, new in REPLACEMENTS:
        new_content = new_content.replace(old, new)
        
    if new_content != content:
        py_file.write_text(new_content, encoding="utf-8")
        print(f"Rebranded F.L.I.N.T/AXIOM in: {py_file.relative_to(ROOT_DIR.parent)}")
        fixed_count += 1

print(f"Total files updated: {fixed_count}")
