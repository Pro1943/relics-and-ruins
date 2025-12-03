#Enemy Functions
import random

def enemy_logic():
    turn = random.randint(1,100)
    if turn in range(1,51): #50% chance
        print("Enemy attack!")
        damage = random.randint(1, 19)
    elif turn in range(51,58): #6% chance
        print("Enemy defend")
        defence = random.randint(1,3)
    elif turn in range(58,70): #11% chance
        print("Enemy miss")
        damage = 0
    elif turn in range(70,101):  #30% chance
        print("Enemy special")
        damage = random.randint(20,40)