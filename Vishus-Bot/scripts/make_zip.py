"""Script to package Vishus-Bot into Vishus-Bot.zip."""

import os
import zipfile
from pathlib import Path

PROJECT_DIR = Path(r"c:\Users\user\Downloads\Vishus-Bot\Vishus-Bot")
OUTPUT_ZIP = Path(r"c:\Users\user\Downloads\Vishus-Bot.zip")

EXCLUDE_DIRS = {".git", ".pytest_cache", "__pycache__", ".venv", "build"}
EXCLUDE_EXTS = {".pyc", ".pyo"}

def create_zip():
    print(f"Creating ZIP archive: {OUTPUT_ZIP}")
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(PROJECT_DIR):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix in EXCLUDE_EXTS:
                    continue
                
                arcname = Path("Vishus-Bot") / file_path.relative_to(PROJECT_DIR)
                zf.write(file_path, arcname)
                
    size_mb = OUTPUT_ZIP.stat().st_size / (1024 * 1024)
    print(f"Successfully created {OUTPUT_ZIP} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    create_zip()
