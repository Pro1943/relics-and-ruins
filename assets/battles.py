"""Battle helpers adapted for GUI."""
from .fighting import round_with_action

def intro_fight_state(state):
    """Prepare the state for an intro fight and return an initial message."""
    state.reset_combat()
    return {"msg": "A wild ghost appears!", "state": {"player_hp": state.player_hp, "enemy_hp": state.enemy_hp}}
