from .clear_terminal import clear_terminal as ct
from .player import *
from .enemy import enemy_logic
from .inventory import *
from assets.screens.game_over import *
from assets.screens.victory import *
from assets.screens.colors import *

def get_valid_input(prompt, valid_range=None):
    while True:
        choice_input = input(prompt)
        try:
            choice = int(choice_input)
            if valid_range and choice not in valid_range:
                print("❌ Invalid input. Please select a listed option.")
                continue
            return choice
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

def fighting():
    player_turn = True
    enemy_turn = False

    player_hp = 100
    enemy_hp = 100
    defence = 0
    special_uses = 4

    load_inv()
    
    if hasattr(enemy_logic, "specials_used"):
        enemy_logic.specials_used = 0

    while player_hp > 0 and enemy_hp > 0:
        if player_turn and not enemy_turn:
            print(f"\nYour HP❤️: {player_hp} | Enemy HP🖤: {enemy_hp}")
            print(f"Special Attacks Left: {special_uses}")
            print("Choose an action to do:")
            print(f"1. {RED}Attack⚔️{RESET}                 2. {YELLOW}Defend🛡️{RESET}")
            print(f"3. {LIGHT_CYAN}Special Attack💫{RESET}        4. {LIGHT_GREEN}Check Inventory🎒{RESET}")

            player_choice = get_valid_input(">", [1, 2, 3, 4])

            damage = 0
            defence_boost = 0
            turn_end = True

            if player_choice == 1:
                ct()
                damage = player_attack()
                enemy_hp -= damage

            elif player_choice == 2:
                ct()
                defence_boost = player_defend()
                defence += defence_boost
                defence = min(defence, 5)

            elif player_choice == 3:
                ct()
                if special_uses > 0:
                    damage = player_special()
                    enemy_hp -= damage
                    special_uses -= 1
                    print(f"💫 Special attacks left: {special_uses}")
                else:
                    print("❌ You are out of special attacks!")
                    turn_end = False

            elif player_choice == 4:
                ct()
                player_inventory()
                turn_end = False

            if turn_end:
                player_turn = False
                enemy_turn = True

        elif enemy_turn and not player_turn:
            enemy_damage, enemy_defence_gain = enemy_logic()

            actual_damage = max(0, enemy_damage - defence)
            player_hp -= actual_damage

            defence += enemy_defence_gain
            defence = max(0, defence - 1)

            if actual_damage > 0:
                print(f"You took {actual_damage} damage!")

            player_turn = True
            enemy_turn = False

    if player_hp <= 0:
        ct()
        game_over_screen()

    elif enemy_hp <= 0:
        inv_add()
        save_inv()
        input("Press a key to continue...")
        ct()
        victory_screen()