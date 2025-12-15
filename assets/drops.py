import random
from .loot_table import *

# Preload all items
COMMON_LOOT = [bone(), leather(), iron_scrap(), berry()]
RARE_LOOT = [gold_scrap(), ruby()]
EPIC_LOOT = [diamond(), dragon_eye()]

# Get a random item from each tier
def get_common():
    return random.choice(COMMON_LOOT)

def get_rare():
    return random.choice(RARE_LOOT)

def get_epic():
    return random.choice(EPIC_LOOT)

# Main drop function
def drop_item():
    roll = random.randint(1, 100)

    # Rarity chances
    if roll <= 70:          # 70% Common
        item = get_common()
    elif roll <= 90:        # 20% Rare
        item = get_rare()
    else:                   # 10% Epic
        item = get_epic()
    return item
