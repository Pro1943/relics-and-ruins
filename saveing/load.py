import json
import os

SAVE_DIR = os.path.join("saveing", "save_files")
SAVE_FILE = os.path.join(SAVE_DIR, "inventory.json")

def load_inventory():
    if not os.path.exists(SAVE_FILE):
        print("       ❌ No save file found.")
        return []
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
