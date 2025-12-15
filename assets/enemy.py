import random
GHOST_ART = r""" 
                                                  
              ▒███████                             
          ▒█████     █████                         
          ██             ███                       
         ▒█                ██                      
       ▒███   ██     ███    █                      
       ▒█      █       █    █                      
     ▒▒██         ██      ███                      
    ▒▒▒██        ████     █                        
       ▒████      ██     ██                        
         ▒▒█             ███████                   
        ▒▒██                   █                   
        ▒▒█                    █                   
       ▒▒▒█                    █                   
     ▒▒▒▒▒██                   █                   
          ▒███                 ███                 
          ▒▒▒██                  ███            █  
         ▒▒▒▒▒███                   ██         █   
             ▒▒▒████                  ██████████   
               ▒▒▒▒█                      ████     
                 ▒▒█       ████     ███████        
                  ▒████████   ██████               
                                                   """                                          

def enemy_logic_state():
    """Stateless enemy decision that returns damage, defence_gain, and a message.

    Note: GameState maintains persistent counters like specials used; prefer
    using `core.game_state.GameState.enemy_action` for full behavior.
    """
    damage = 0
    defence_gain = 0

    turn = random.randint(1, 100)

    def normal_attack():
        dmg = random.randint(1, 19)
        return dmg, f"Enemy used simple slash for {dmg} damage!"

    if turn <= 50:
        dmg, msg = normal_attack()
        damage = dmg
    elif turn <= 57:
        defence_gain = random.randint(1, 3)
        msg = f"Enemy defends, gaining {defence_gain} defence!"
    elif turn <= 69:
        msg = "Enemy missed!"
    else:
        damage = random.randint(20, 40)
        msg = f"Enemy uses a SPECIAL attack for {damage} damage!"

    return {"damage": damage, "defence_gain": defence_gain, "msg": msg}
