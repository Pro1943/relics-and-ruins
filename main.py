from assets.screens.colors import *
'''
      ▄▄▄▄▄▄         ▄▄                                        ▄▄▄▄▄▄                        
     █▀██▀▀▀█▄        ██                                 █▄   █▀██▀▀▀█▄                      
       ██▄▄▄█▀        ██ ▀▀                     ▄        ██     ██▄▄▄█▀        ▀▀ ▄          
       ██▀▀█▄   ▄█▀█▄ ██ ██ ▄███▀ ▄██▀█   ▄▀▀█▄ ████▄ ▄████     ██▀▀█▄   ██ ██ ██ ████▄ ▄██▀█
     ▄ ██  ██   ██▄█▀ ██ ██ ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ▄ ██  ██   ██ ██ ██ ██ ██ ▀███▄
     ▀██▀  ▀██▀▄▀█▄▄▄▄██▄██▄▀███▄█▄▄██▀  ▄▀█▄██▄██ ▀█▄█▀███   ▀██▀  ▀██▀▄▀██▀█▄██▄██ ▀██▄▄██▀
'''
import sys

try:
    from ui.gui_main import run_gui
    HAS_QT = True
except Exception:
    HAS_QT = False


def main():
    if HAS_QT:
        run_gui()
    else:
        print(f"{RED}ERROR:PySide6 not available. Please install requirements and run again.{RESET}")
        print(fr"{CYAN}{BOLD}To install: pip install -r requirments.txt{RESET}")


if __name__ == "__main__":
    main()
