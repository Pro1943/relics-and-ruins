"""Loot table for GUI: returns plain data without ANSI colors."""

# Common items
def bone():
    return {
        "name": "Bone",
        "loot_type": "common",
        "saleable": True,
        "function": "selling only",
    }

def leather():
    return {
        "name": "Leather",
        "loot_type": "common",
        "saleable": True,
        "function": "armor_player",
    }

def iron_scrap():
    return {
        "name": "Iron Scrap",
        "loot_type": "common",
        "saleable": True,
        "function": "armor_player",
    }

def berry():
    return {
        "name": "Berry",
        "loot_type": "common",
        "saleable": False,
        "function": "food",
    }

# Rare items
def gold_scrap():
    return {
        "name": "Gold Scrap",
        "loot_type": "rare",
        "saleable": True,
        "function": "armor_player",
    }

def ruby():
    return {
        "name": "Ruby",
        "loot_type": "rare",
        "saleable": True,
        "function": "selling only",
    }

# Epic items
def diamond():
    return {
        "name": "Diamond",
        "loot_type": "epic",
        "saleable": True,
        "function": "selling only",
    }

def dragon_eye():
    return {
        "name": "Dragon Eye",
        "loot_type": "epic",
        "saleable": True,
        "function": "selling only",
    }
