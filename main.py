from clear_terminal import clear_terminal as ct
from interactions import intro, introhouse, forest_start

def main():
    #Start screen
    print("Centuries ago, a powerful civilization fell after misusing ancient relics.")
    print("Now, the Ruin Warden — a corrupted guardian — controls the heart of the old kingdom.")
    print("You're a scavenger trying to uncover relics, survive the ruins, and eventually confront the Warden before the corruption spreads.")

    #Intro
    while True:
        print("\nYou stumble upon a random old house in the woods...")
        print("\nWhat will you do?")
        intro()
        print("[Enter the dedicated number]")

        village_key = False
        introchoice = int(input(">"))
        if introchoice == 1:
            ct()
            print("You decided to explore the house.")
            introhouse()
            introchoice2 = int(input(">"))
            if introchoice2 == 1:
                ct()
                print("You decided to knock on the door...")
                break
            else:
                print("You decided to go back")
                ct()
                continue
        else:
            ct()
            print("You decided to go the the forest.")
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
            elif forestchoice == 2:
                print("You decided to go back.")
                ct()
                continue



if __name__ == "__main__":
    main()