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