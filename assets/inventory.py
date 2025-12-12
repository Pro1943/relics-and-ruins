from .drops import drop_item

inv = []

def inv_add():
    item = drop_item()
    inv.append(item)

def inventory():
    print("\nYour Inventory:")
    for i, item in enumerate(inv, 1):
        print(f"{i}. {item['name']} ({item['loot_type']})")