"""Test script to import every single module in the vishus_bot package to verify 100% clean imports."""

import sys
import importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

def import_all():
    print("Testing recursive import of all vishus_bot modules...")
    vishus_bot_dir = ROOT / "vishus_bot"
    
    success_count = 0
    fail_count = 0
    
    for path in vishus_bot_dir.rglob("*.py"):
        rel = path.relative_to(ROOT)
        mod_name = str(rel.with_suffix("")).replace("\\", ".").replace("/", ".")
        
        try:
            importlib.import_module(mod_name)
            print(f"  [OK] {mod_name}")
            success_count += 1
        except Exception as e:
            print(f"  [FAIL] {mod_name}: {e}")
            fail_count += 1
            
    print("==================================================")
    print(f"Import Test Results: {success_count} Passed, {fail_count} Failed")
    print("==================================================")
    return fail_count

if __name__ == "__main__":
    exit(import_all())
