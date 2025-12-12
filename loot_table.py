#Loot_table of the Player
''' 
Mainly, there are 3 types of loots: 
 1. Common    2. rare    3. epic 
loots : bone, leather, iron scrap, gold scrap, dragon eye, diamond, ruby, berry
'''
            
def bone():
    return {
        "name" : "Bone",
        "loot_type": "common",
        "saleable": True,
        "function": "selling only"
    }
def leather():
    return {
        "name" : "Leather",
        "loot_type": "common",
        "saleable": True,
        "function": "armor_player"
    }
def iron_scrap():
    return {
        "name" : "Iron Scrap",
        "loot_type": "common",
        "saleable": True,
        "function": "armor_player"
    }
def gold_scrap():
    return {
        "name" : "Gold Scrap",
        "loot_type": "rare",
        "saleable": True,
        "function": "armor_player"
    }
def dragon_eye():
    return {
        "name": "Dragon Eye",
        "loot_type": "epic",
        "saleable" : True,
        "function" : "selling only"
    }
def diamond():
    return {
        "name": "Diamond",
        "loot_type": "epic",
        "saleable" : True,
        "function" : "selling only"
    }
def ruby():
    return {
        "name": "Ruby",
        "loot_type": "rare",
        "saleable" : True,
        "function" : "selling only"
    } 
def berry():
    return {
        "name": "Berry",
        "loot_type": "common",
        "saleable" : False,
        "function" : "food"
    }