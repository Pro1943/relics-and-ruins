import random

def enemy_logic():
    # Static variable (persists across calls)
    if not hasattr(enemy_logic, "specials_used"):
        enemy_logic.specials_used = 0

    damage = 0
    defence_gain = 0

    turn = random.randint(1, 100)

    # Normal attack
    def normal_attack():
        dmg = random.randint(1, 19)
        print(f"Enemy used simple slash for {dmg} damage!")
        return dmg

    if turn <= 50:
        damage = normal_attack()

    elif turn <= 57:
        defence_gain = random.randint(1, 3)
        print(f"Enemy defends, gaining {defence_gain} defence!")

    elif turn <= 69:
        print("Enemy missed!")

    else:
        if enemy_logic.specials_used < 3:
            damage = random.randint(20, 40)
            enemy_logic.specials_used += 1
            print(f"Enemy uses a SPECIAL attack for {damage} damage!")
        else:
            print("Enemy tried to use a special… but is exhausted!")
            damage = normal_attack()

    return damage, defence_gain
