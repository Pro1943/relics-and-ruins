#Player functions
import random

def player_attack():
    damage = random.randint(1, 19)
    print(f"You delt attacks for {damage} damage!")
    return damage
def player_defend():
    print("You prepare to defend...")
    defence_boost = 1
    return defence_boost
def player_special():
    damage = random.randint(20, 40)
    print(f"Player uses a Special Attack for {damage} damage!")
    return damage
def player_inventory():
    print("Player_Inventory")
    #To_Be_Added_Later
    return 0