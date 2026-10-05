"""Audit tool to verify complete replacement of target branding across the project."""

import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HISTORICAL_FILES = {
    "PROJECT_DOCUMENTATION.md",
    "README.md"
}

IGNORE_DIRS = {
    ".git", ".pytest_cache", "__pycache__", ".venv", "dist", "build", "node_modules", "scripts"
}

OLD_NAME = "f" + "lint"
OLD_PERSONAL_AI = "personal " + "ai"

def run_audit():
    flint_matches = []
    personal_ai_matches = []
    historical_matches = []

    for path in ROOT_DIR.rglob("*"):
        if path.is_file():
            if any(part in IGNORE_DIRS for part in path.parts):
                continue
            
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            rel_path = str(path.relative_to(ROOT_DIR))

            for line_no, line in enumerate(content.splitlines(), start=1):
                if re.search(r'\b' + OLD_NAME + r'\b|\b' + OLD_NAME + r'\.exe\b', line, re.IGNORECASE):
                    if path.name in ALLOWED_HISTORICAL_FILES:
                        historical_matches.append((rel_path, line_no, line.strip()))
                    else:
                        flint_matches.append((rel_path, line_no, line.strip()))
                elif re.search(OLD_PERSONAL_AI, line, re.IGNORECASE):
                    if path.name in ALLOWED_HISTORICAL_FILES:
                        historical_matches.append((rel_path, line_no, line.strip()))
                    else:
                        personal_ai_matches.append((rel_path, line_no, line.strip()))

    print("==================================================")
    print("           VISHU'S BOT AUDIT REPORT               ")
    print("==================================================")
    print(f"Strict Branding Violations found: {len(flint_matches)}")
    for m in flint_matches:
        print(f"  [VIOLATION] {m[0]}:{m[1]} -> {m[2]}")
        
    print(f"Personal AI Violations found: {len(personal_ai_matches)}")
    for m in personal_ai_matches:
        print(f"  [VIOLATION] {m[0]}:{m[1]} -> {m[2]}")

    print(f"Allowed Historical References: {len(historical_matches)}")
    for m in historical_matches:
        print(f"  [HISTORICAL] {m[0]}:{m[1]} -> {m[2]}")
        
    print("==================================================")
    return len(flint_matches) + len(personal_ai_matches)

if __name__ == "__main__":
    exit_code = run_audit()
    exit(exit_code)
