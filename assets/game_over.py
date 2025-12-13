from .colors import *
def game_over_screen():
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