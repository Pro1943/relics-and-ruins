"""Non-blocking combat helpers for GUI.

Provides a single-step combat adapter that takes a GameState-like
object (see `core/game_state.GameState`) and applies the requested action,
then resolves enemy action and returns a structured event dict.
"""

def round_with_action(state, action):
    """Apply a player action ('attack','defend','special','inventory') to the
    provided `state` and resolve an enemy turn. Returns a dict with event
    messages and updated hp/defence values."""
    events = []

    if action == "attack":
        res = state.attack()
        events.append({"type": "player_attack", "damage": res["damage"], "enemy_hp": res["enemy_hp"]})

    elif action == "defend":
        res = state.defend()
        events.append({"type": "player_defend", "defence": res["defence"]})

    elif action == "special":
        res = state.special()
        if res.get("used") is False:
            events.append({"type": "player_special_failed", "reason": res.get("reason")})
        else:
            events.append({"type": "player_special", "damage": res.get("damage", 0), "enemy_hp": res.get("enemy_hp")})

    elif action == "inventory":
        # Inventory handled by UI directly via state.inv
        events.append({"type": "inventory_opened", "inventory": list(state.inv)})

    # resolve enemy turn if enemy still alive
    if state.enemy_hp > 0 and state.player_hp > 0:
        e = state.enemy_action()
        events.append({"type": "enemy_action", "msg": e.get("msg"), "actual_damage": e.get("actual_damage"), "player_hp": e.get("player_hp")})

    # determine end conditions
    if state.player_hp <= 0:
        events.append({"type": "player_defeated"})
    if state.enemy_hp <= 0:
        # auto-loot: add randomly via inv_add helper if desired (UI can call inv_add)
        events.append({"type": "enemy_defeated"})

    return {"events": events, "state": {"player_hp": state.player_hp, "enemy_hp": state.enemy_hp, "defence": state.defence}}