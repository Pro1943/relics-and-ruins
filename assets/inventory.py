from .drops import drop_item
from saveing.save import save_inventory as save_inv_file
from saveing.load import load_inventory as load_inv_file

def inv_add(inv_list):
    item = drop_item()
    inv_list.append(item)
    return item

def inventory_list(inv_list):
    """Return a list of inventory display strings."""
    if not inv_list:
        return ["- Your bag is empty -"]
    return [f"{i}. {item['name']} ({item.get('loot_type', '')})" for i, item in enumerate(inv_list, 1)]

def save_inv(inv_list):
    save_inv_file(inv_list)

def load_inv():
    return load_inv_file()
