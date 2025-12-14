import json
import os

SAVE_DIR = os.path.join("saveing", "save_files")
SAVE_FILE = os.path.join(SAVE_DIR, "inventory.json")

def save_inventory(inv_list):
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(inv_list, f, indent=4)
    print("💾 Inventory saved!")
