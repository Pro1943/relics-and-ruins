import json
import os

SAVE_FILE = "saving/save_files/inventory.json"

def load_inventory():
    if not os.path.exists(SAVE_FILE):
        print("       ❌ No save file found.")
        return []
    with open(SAVE_FILE, "r") as f:
        return json.load(f)
