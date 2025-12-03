from clear_terminal import clear_terminal as ct
from interactions import intro, introhouse, forest_start, the_house

def main():
    #Start screen
    print("Centuries ago, a powerful civilization fell after misusing ancient relics.")
    print("Now, the Ruin Warden — a corrupted guardian — controls the heart of the old kingdom.")
    print("You're a scavenger trying to uncover relics, survive the ruins, and eventually confront the Warden before the corruption spreads.\n")

    #Intro
    village_key = False
    while True:
        print("You stumbled upon a random old house in the woods...")
        print("\nWhat will you do?")
        intro()
        print("[Enter the dedicated number]")

        introchoice = int(input(">"))
        if introchoice == 1:
            ct()
            print("You decided to explore the house.")
            introhouse()
            introchoice2 = int(input(">"))
            if introchoice2 == 1:
                ct()
                print("You raise your hand and knock\n" \
                "For a moment, nothing but wind through the trees." \
                "\nThen — a slow, deliberate creaking from inside." \
                "\nA voice, old and weary, answers:\n'No one’s lived here in decades" \
                " Why disturb the dead?'\nThe door remains shut.\nYou feel the air grow cold.")
                the_house()
                enter = int(input(">"))
                if enter == 1:
                    print("You knocked again...")
                elif enter ==2:
                    print("You tired to push the door open.")

            else:
                print("You decided to go back")
                ct()
                continue
        else:
            ct()
            print("You stumdled upon a dense forest. \nWho knows what this is hiding?")
            forest_start()
            forestchoice = int(input(">"))
            if forestchoice == 1 and village_key == True:
                ct()
                print("You entered the forest!")
                break
            elif forestchoice == 1 and village_key == False:
               ct()
               print("There seems to be a miserious barrier that is stoping you from entering!")
               break
            else:
                print("You decided to go back.")
                ct()
                continue



if __name__ == "__main__":
    main()