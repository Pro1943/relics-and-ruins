#Enemy Functions
import random

def enemy_logic():
    turn = random.randint(1,100)
    if turn in range(1,51): #50% chance
        print("Enemy attack!")
    elif turn in range(51,58): #6% chance
        print("Enemy defend")
    elif turn in range(58,70): #11% chance
        print("Enemy miss")
    elif turn in range(70,101):  #30% chance
        print("Enemy special")