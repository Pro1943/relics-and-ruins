import os
import time
from .colors import *
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def start_screen():
    clear()
    print(YELLOW+r"""
██████╗ ███████╗██╗     ██╗ ██████╗███████╗███████╗
██╔══██╗██╔════╝██║     ██║██╔════╝██╔════╝██╔════╝
██████╔╝█████╗  ██║     ██║██║     █████╗  ███████╗
██╔══██╗██╔══╝  ██║     ██║██║     ██╔══╝  ╚════██║
██║  ██║███████╗███████╗██║╚██████╗███████╗███████║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝╚══════╝╚══════╝
                Relics and Ruins
    """+RESET)
    print("----------------------------------------------------")
    print(f"{BOLD}{GREEN}1. Start Game"+RESET)
    print(f"{BOLD}{BLUE}2. Load Game"+RESET)
    print(f"{BOLD}{RED}3. Quit"+RESET)
    print("----------------------------------------------------")

    choice = input("Enter choice: ").strip()
    return choice
