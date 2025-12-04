import random

def enemy_logic():
    damage = 0
    defence_gain = 0
    
    turn = random.randint(1,100)
    
    if turn in range(1, 51): #Attack
        damage = random.randint(1, 19)
        print(f"Enemy used simple slash for {damage} damage!")
    elif turn in range(51, 58): #Defend
        defence_gain = random.randint(1, 3)
        print(f"Enemy defends, gaining {defence_gain} defence!")
    elif turn in range(58, 70): #Miss
        damage = 0
        print("Enemy miss!")
    elif turn in range(70, 101): #Special
        damage = random.randint(20, 40)
        print(f"Enemy uses a special attack for {damage} damage!")
        
    return damage, defence_gain