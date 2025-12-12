from .drops import drop_item
from saveing.save import save_inventory as save_inv_file
from saveing.load import load_inventory as load_inv_file

inv = []

def inv_add():
    item = drop_item()
    inv.append(item)

def inventory():
    print("\nYour Inventory:")
    if not inv:
        print(" - Your bag is empty - ")
    for i, item in enumerate(inv, 1):
        print(f"{i}. {item['name']} ({item['loot_type']})")

def save_inv():
    save_inv_file(inv)

def load_inv():
    global inv
    inv = load_inv_file()
