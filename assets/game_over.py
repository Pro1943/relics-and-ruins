from colors import *
from colorama import Fore, Style, init
init(autoreset=True)

def game_over_screen():
    RED = Fore.RED
    DARK_RED = Fore.LIGHTRED_EX
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    BRIGHT = Style.BRIGHT
    RESET = Style.RESET_ALL

    print("\n" * 2)
    print(RED+
          r" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
    print(r"██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print(r"██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
    print(r"██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print(r"╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print(r" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
    print("\n")
    print("             The ruins have claimed you.")
    print("             Your journey ends… for now.\n"+RESET)
    print(f"{YELLOW}{BOLD}           Relics & Ruins is still in development.")
    print("         More chapters and bosses arriving soon.\n"+RESET)
    input(f"{GREY}               Press Enter to exit..."+RESET)
    print(DARK_RED + BRIGHT + r" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
    print(DARK_RED + BRIGHT + r"██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print(DARK_RED + BRIGHT + r"██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
    print(DARK_RED + BRIGHT + r"██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print(DARK_RED + BRIGHT + r"╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print(DARK_RED + BRIGHT + r" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")

    print("\n")
    print(RED + BRIGHT + "             The ruins have claimed you.")
    print(CYAN + "             Your journey ends… for now.\n")
    print(WHITE + "           Relics & Ruins is still in development.")
    print(WHITE + "           More chapters and bosses arriving soon.\n")

    input(BRIGHT + WHITE + "               Press Enter to exit..." + RESET)
