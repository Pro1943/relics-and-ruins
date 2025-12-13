#Loot_table of the Player
''' 
Mainly, there are 3 types of loots: 
 1. Common    2. rare    3. epic 
loots : bone, leather, iron scrap, gold scrap, dragon eye, diamond, ruby, berry
'''
from assets.screens.colors import *

# Common items
def bone():
    return {
        "name": "Bone",
        "loot_type": f"{GREY}common"+RESET,
        "saleable": True,
        "function": "selling only"
    }

def leather():
    return {
        "name": "Leather",
        "loot_type": f"{GREY}common"+RESET,
        "saleable": True,
        "function": "armor_player"
    }

def iron_scrap():
    return {
        "name": "Iron Scrap",
        "loot_type": f"{GREY}common"+RESET,
        "saleable": True,
        "function": "armor_player"
    }

def berry():
    return {
        "name": "Berry",
        "loot_type": f"{GREY}common"+RESET,
        "saleable": False,
        "function": "food"
    }

# Rare items
def gold_scrap():
    return {
        "name": "Gold Scrap",
        "loot_type": f"{YELLOW}{BOLD}rare"+RESET,
        "saleable": True,
        "function": "armor_player"
    }

def ruby():
    return {
        "name": "Ruby",
        "loot_type": f"{YELLOW}{BOLD}rare"+RESET,
        "saleable": True,
        "function": "selling only"
    }

# Epic items
def diamond():
    return {
        "name": "Diamond",
        "loot_type": f"{MAGENTA}{BOLD}epic"+RESET,
        "saleable": True,
        "function": "selling only"
    }

def dragon_eye():
    return {
        "name": "Dragon Eye",
        "loot_type": f"{MAGENTA}{BOLD}epic"+RESET,
        "saleable": True,
        "function": "selling only"
    }
