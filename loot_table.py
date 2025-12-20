#Loot_table of the Player
''' 
Mainly, there are 3 types of loots: 
 1. Common    2. rare    3. epic 
loots : bone, leather, iron scrap, gold scrap, dragon eye, diamond, ruby, berry
  '''
            
def bone():
    return {
        "loot_type": "common",
        "saleable": True,
        "function": "selling only"
    }
def leather():
    return {
        "loot_type": "common",
        "saleable": True,
        "function": "armor_player"
    }
def iron_scrap():
    return {
        "loot_type": "common",
        "saleable": True,
        "function": "armor_player"
    }
def gold_scrap():
    return {
        "loot_type": "rare",
        "saleable": True,
        "function": "armor_player"
    }
def dragon_eye():
    return {
        "loot_type": "epic",
        "saleable" : True,
        "function" : "selling only"
    }
def diamond():
    return {
        "loot_type": "epic",
        "saleable" : True,
        "function" : "selling only"
    }
def ruby():
    return {
        "loot_type": "rare",
        "saleable" : True,
        "function" : "selling only"
    } 
def berry():
    return {
        "loot_type": "common",
        "saleable" : False,
        "function" : "food"
    }
def defence_potion():
    return {
        "loot_type": "rare",
        "saleable" : False,
        "function" : "defence"
    }
def regenerate_potion():
    return {
         "loot_type": "common",
        "saleable" : True,
        "function" : "regenerate"
    }
def Relic_of_Eternal_Spark():
    return {
         "loot_type": "epic",
        "saleable" : False,
        "function" : "revive"
    }