from .colors import *
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
    print(GREEN+
          r"""      
          ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
          ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
          ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ 
          ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  
           ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   
            ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    """)
    print("\n")
    print("                   You stand victorious in the ruins!")
    print("                 The deeper paths now whisper your name.\n"+RESET)
    print(f"{YELLOW}               Relics & Ruins is still in early development.")
    print("                 Stronger enemies and relics coming soon.\n"+RESET)
    input(f"{GREY}                    Press Enter to continue..."+RESET)