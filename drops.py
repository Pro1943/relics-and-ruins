import random
from loot_table import *

bone_drop = bone() #common
leather_drop = leather() #common
iron_scrap_drop = iron_scrap() #common
berry_drop = berry() #common

gold_scrap_drop = gold_scrap() #rare
ruby_drop = ruby() #rare

diamond_drop = diamond() #epic
dragon_eye_drop = dragon_eye() #epic

test = 0

def common_item():
    drop = random.randint(1,37)
    if drop in range(1,13):
        return"Bone"
    elif drop in range(13,25):
        return"Leather"
    elif drop in range(25,30):
        return"Berry"
    else:
        return"Iron Scrap"


def dropped():
    chance = random.randint(1,72)
    if chance in range(1,71):                                                                                               #70% chance
        print(f"You got {common_item()}")