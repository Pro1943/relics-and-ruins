from clear_terminal import clear_terminal as ct
from player import player_attack, player_defend, player_special, player_inventory
from enemy import enemy_logic

player_turn = True
enemy_turn = False

player_hp = 100
enemy_hp = 100

while True:
    if player_turn == True and enemy_turn == False:
        print("Choose an action to do: ")
        print("1. Attack⚔️                  2. Defend🛡️")
        print("3. Special Attack💫         4. Check Inventory🎒")
        player_choice = int(input(">"))
        if player_choice == 1:
            player_attack()
            
            
            player_turn = False
            enemy_turn = True
        elif player_choice == 2:
            player_defend()
            player_turn = False
            enemy_turn = True
        elif player_choice == 3:
            player_special()
            player_turn = False
            enemy_turn = True
        elif player_choice == 4:
            player_inventory()
            player_turn = False
            enemy_turn = True
    
    elif enemy_turn == True and player_turn == False:
        enemy_logic()
        player_turn = True
        enemy_turn = False