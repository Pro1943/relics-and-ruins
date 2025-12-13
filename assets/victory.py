from colorama import Fore, Style, init
init(autoreset=True)

def victory_screen():
    GOLD = Fore.YELLOW
    GREEN = Fore.GREEN
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    BRIGHT = Style.BRIGHT
    RESET = Style.RESET_ALL

    print("\n" * 2)
    print(GOLD + BRIGHT + r"██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗")
    print(GOLD + BRIGHT + r"██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝")
    print(GOLD + BRIGHT + r"██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ ")
    print(GOLD + BRIGHT + r"╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  ")
    print(GOLD + BRIGHT + r" ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   ")
    print(GOLD + BRIGHT + r"  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ")

    print("\n")
    print(GREEN + BRIGHT + "           You stand victorious in the ruins!")
    print(CYAN + "         The deeper paths now whisper your name.\n")
    print(WHITE + "       Relics & Ruins is still in early development.")
    print(WHITE + "         Stronger enemies and relics coming soon.\n")

    input(BRIGHT + WHITE + "             Press Enter to quit..." + RESET)