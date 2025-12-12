import json
import os

SAVE_FILE = "saveing/save_files/inventory.json"

def save_inventory(inv_list):
    os.makedirs("saves", exist_ok=True)
    with open(SAVE_FILE, "w") as f:
        json.dump(inv_list, f, indent=4)
    print("💾 Inventory saved!")
