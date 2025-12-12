import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')                                                                                            #for windows
    else:
        os.system('clear')                                                                                          #for mac_os