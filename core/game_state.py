"""Core game state and non-UI game logic.

This module centralizes player/enemy/inventory state and provides methods
that return structured results (instead of printing or reading input).
"""
import random
from pathlib import Path
from assets.drops import drop_item
from saveing.save import save_inventory as _save_inventory
from saveing.load import load_inventory as _load_inventory


class GameState:
    def __init__(self):
        self.player_hp = 100
        self.enemy_hp = 100
        self.defence = 0
        self.special_uses = 3
        self.inv = _load_inventory() or []
        self.enemy_specials_used = 0

    # Inventory
    def add_loot(self, item):
        self.inv.append(item)

    def inv_add(self):
        """Add a randomly dropped item to inventory and return it."""
        item = drop_item()
        self.inv.append(item)
        return item

    def save(self):
        _save_inventory(self.inv)

    # Player actions
    def attack(self):
        dmg = random.randint(1, 19)
        self.enemy_hp = max(0, self.enemy_hp - dmg)
        return {"action": "attack", "damage": dmg, "enemy_hp": self.enemy_hp}

    def defend(self):
        boost = 5
        self.defence = min(5, self.defence + boost)
        return {"action": "defend", "defence": self.defence}

    def special(self):
        if self.special_uses <= 0:
            return {"action": "special", "used": False, "reason": "No specials left"}
        dmg = random.randint(20, 40)
        self.enemy_hp = max(0, self.enemy_hp - dmg)
        self.special_uses -= 1
        return {"action": "special", "damage": dmg, "enemy_hp": self.enemy_hp, "remaining": self.special_uses}

    # Enemy turn logic
    def enemy_action(self):
        damage = 0
        defence_gain = 0
        turn = random.randint(1, 100)

        def normal_attack():
            return random.randint(1, 19)

        if turn <= 50:
            damage = normal_attack()
            msg = f"Enemy used simple slash for {damage} damage!"
        elif turn <= 57:
            defence_gain = random.randint(1, 3)
            self.defence += defence_gain
            msg = f"Enemy defends, gaining {defence_gain} defence!"
        elif turn <= 69:
            msg = "Enemy missed!"
        else:
            if self.enemy_specials_used < 3:
                damage = random.randint(20, 40)
                self.enemy_specials_used += 1
                msg = f"Enemy uses a SPECIAL attack for {damage} damage!"
            else:
                damage = normal_attack()
                msg = "Enemy tried to use a special… but is exhausted!"

        actual_damage = max(0, damage - self.defence)
        self.player_hp = max(0, self.player_hp - actual_damage)
        # decay player's defence by 1 after enemy turn
        self.defence = max(0, self.defence - 1)

        return {
            "msg": msg,
            "damage": damage,
            "actual_damage": actual_damage,
            "player_hp": self.player_hp,
            "defence": self.defence,
        }

    def reset_combat(self):
        self.player_hp = 100
        self.enemy_hp = 100
        self.defence = 0
        self.special_uses = 3
        self.enemy_specials_used = 0


def create_default_state():
    return GameState()
