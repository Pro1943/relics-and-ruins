from .colors import *
def victory_screen():
    print("\n" * 2)
    print(GREEN+
          r"      ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗ ")
    print(r"      ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝ ")
    print(r"      ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝  ")
    print(r"      ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝   ")
    print(r"       ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║    ")
    print(r"        ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ")
    print("\n")
    print("           You stand victorious in the ruins!")
    print("         The deeper paths now whisper your name.\n"+RESET)
    print(f"{YELLOW}       Relics & Ruins is still in early development.")
    print("         Stronger enemies and relics coming soon.\n"+RESET)
    input(f"{GREY}             Press Enter to continue..."+RESET)
