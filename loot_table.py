#Loot_table of the Player
# Mainly, there are 3 types of loots: 
# 1. Common
# 2. rare
# 3. epic 
            
def bone():
    loot_type = "common"
    saleable = True
    function = "selling only"
    return {
        "loot_type": "common",
        "saleable": True,
        "function": "selling only"
    }
def leather():
    loot_type = "common"
    saleable = True
    function = "armor_player"
    return {
        "loot_type": "common",
        "saleable": True,
        "function": "armor_player"
    }
def iron_scrap():
    loot_type = "common"
    function = "armor_player"
    saleable = True
    return {
        "loot_type": "common",
        "saleable": True,
        "function": "armor_player"
    }
def gold_scrap():
    loot_type = "rare"
    function = "armor_player"
    saleable = True
    return {
        "loot_type": "rare",
        "saleable": True,
        "function": "armor_player"
    }
def dragon_eye():
    loot_type = "epic"
    function = "selling only"
    saleable = True
    return {
        "loot_type": "epic",
        "saleable" : True,
        "function" : "selling only"
    }
def diamond():
    loot_type = "epic"
    function = "selling only"
    saleable = True
    return {
        "loot_type": "epic",
        "saleable" : True,
        "function" : "selling only"
    }
def ruby():
    loot_type = "rare"
    function = "selling only"
    saleable = True
    return {
        "loot_type": "rare",
        "saleable" : True,
        "function" : "selling only"
    }
