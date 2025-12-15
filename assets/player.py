"""Player helpers returning structured results for GUI."""
import random

def player_attack():
    damage = random.randint(1, 19)
    return {"action": "attack", "damage": damage, "message": f"You dealt {damage} damage."}

def player_defend():
    defence_boost = 5
    return {"action": "defend", "defence_boost": defence_boost, "message": "You prepare to defend."}

def player_special():
    damage = random.randint(20, 40)
    return {"action": "special", "damage": damage, "message": f"Player uses a Special Attack for {damage} damage!"}

def player_inventory(inv_list):
    return {"action": "inventory", "inventory": inv_list}