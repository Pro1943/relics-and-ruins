from .clear_terminal import clear_terminal as ct
from .player import *
from .enemy import enemy_logic
from .inventory import *
from .game_over import *
from .victory import *
from .colors import *

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
    load_inv()
    while player_hp > 0 and enemy_hp > 0:
        if player_turn == True and enemy_turn == False:
            print(f"\nYour HP: {player_hp} | Enemy HP: {enemy_hp}")
            print(f"{GREY}Choose an action to do: "+RESET)
            print(f"1. {RED}Attack⚔️{RESET}               2. {YELLOW}Defend🛡️{RESET}")
            print(f"3. {LIGHT_CYAN}Special Attack💫{RESET}      4. {LIGHT_GREEN}Check Inventory🎒{RESET}")
        
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
                damage = player_special()
                enemy_hp -= damage
            
            elif player_choice == 4:
                ct()
                player_inventory()
                turn_end = False
        
            if turn_end == True:
                player_turn = False
                enemy_turn = True
            
        elif enemy_turn == True and player_turn == False:
        
            enemy_damage, enemy_defence_gain = enemy_logic()
        
            actual_damage = max(0, enemy_damage - defence)
            player_hp -= actual_damage
            defence += enemy_defence_gain
            defence = max(0, defence - 1)
        
            if enemy_damage > 0 and actual_damage > 0:
                print(f"You took {actual_damage} damage!")
            player_turn = True
            enemy_turn = False

    if player_hp <= 0:
        game_over_screen()
    elif enemy_hp <= 0:
        inv_add()
        save_inv()
        input("Press a key to continue...")
        ct()
        victory_screen()