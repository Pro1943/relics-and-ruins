from assets.clear_terminal import clear_terminal as ct
from assets.interactions import *
from assets.battles import *
from assets.start_screen import start_screen
import os

required_folders = [
    "saveing/save_files",
]

for folder in required_folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

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

def game_intro():
    print("Centuries ago, a powerful civilization fell after misusing ancient relics.")
    print("Now, the Ruin Warden — a corrupted guardian — controls the heart of the old kingdom.")
    print("You're a scavenger trying to uncover relics, survive the ruins, and eventually confront the Warden before the corruption spreads.\n")

    village_key = False
    print("You stumbled upon a random old house in the woods...") 
    while True:
        print("\nWhat will you do?")
        
        intro() 
        
        print("[Enter the dedicated number]")

        introchoice = get_valid_input(">", [1, 2])
        
        if introchoice == 1:
            ct()
            print("You decided to explore the house.")
            introhouse() 
            
            introchoice2 = get_valid_input(">", [1, 2])
            
            if introchoice2 == 1:
                ct()
                print("You raised your hand and knocked\nFor a moment, nothing but wind through the trees."
                      "\nThen — a slow, deliberate creaking from inside."
                      "\nA voice, old and weary, answers:\n'No one’s lived here for decades"
                      " Why disturb the dead?'\nThe door remains shut.\nYou feel the air grow cold.")
                the_house()
                
                enter = get_valid_input(">", [1, 2])
                
                if enter == 1:
                    ct()
                    print("You knocked again...")
                    intro_fight()
                    return
                    
                elif enter == 2:
                    ct()
                    print("You tried to push the door open.")
                    intro_fight()
                    return
                
            elif introchoice2 == 2:
                ct() 
                print("You decided to step away from the house.")
                continue 
        
        elif introchoice == 2: 
            ct()
            print("You decided to continue your journey, walking deeper into the wilderness.")
            print("You stumbled upon a dense forest.\nWho knows what this is hiding?")
            forest_start()
            
            forestchoice = get_valid_input(">", [1, 2])
            
            if forestchoice == 1 and village_key == True:
                ct()
                print("You entered the forest!")
                return

            elif forestchoice == 1 and village_key == False:
                ct()
                print("There seems to be a mysterious barrier that is stopping you from entering!")
                return

            elif forestchoice == 2:
                print("You decided to go back.")
                ct()
                continue 

def main():
    while True:
        choice = start_screen()
        if choice == "1":
            ct()
            game_intro()
            break
        elif choice == "2":
            ct()
            print("Load system coming soon.")
            break
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
