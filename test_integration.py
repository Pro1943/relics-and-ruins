"""
Integration test for Relics & Ruins GUI.

This script validates all core components without requiring a display.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Verify all modules import successfully."""
    print("Testing imports...")
    try:
        from ui.gui_main import run_gui
        from ui.main_window import MainWindow
        from ui.pages.start_page import StartPage
        from ui.pages.intro_page import IntroPage
        from ui.pages.combat_page import CombatPage
        from ui.pages.inventory_page import InventoryPage
        from ui.pages.victory_page import VictoryPage
        from ui.pages.gameover_page import GameOverPage
        from core.game_state import create_default_state
        from assets.drops import drop_item
        from assets.inventory import inv_add, inventory_list
        from assets.start_screen import get_start_art
        print("✅ All imports successful!")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False


def test_game_state():
    """Test core game logic."""
    print("\nTesting GameState...")
    try:
        from core.game_state import create_default_state
        
        state = create_default_state()
        assert state.player_hp == 100, "Initial HP should be 100"
        assert state.enemy_hp == 100, "Initial enemy HP should be 100"
        
        # Test attack
        res = state.attack()
        assert res["damage"] > 0, "Attack should deal damage"
        assert state.enemy_hp < 100, "Enemy HP should decrease"
        print(f"  Attack test: dealt {res['damage']} damage")
        
        # Test defend
        initial_def = state.defence
        res = state.defend()
        assert state.defence > initial_def, "Defense should increase"
        print(f"  Defend test: defense now {res['defence']}")
        
        # Test special
        state.special_uses = 1
        res = state.special()
        assert res["damage"] > 0, "Special should deal damage"
        assert state.special_uses == 0, "Special uses should decrease"
        print(f"  Special test: dealt {res['damage']} damage, {res['remaining']} remaining")
        
        # Test inventory
        state.reset_combat()
        item = state.inv_add()
        assert item in state.inv, "Item should be in inventory"
        assert "name" in item, "Item should have a name"
        print(f"  Inventory test: added {item['name']} ({item.get('loot_type', 'unknown')})")
        
        print("✅ GameState tests passed!")
        return True
    except Exception as e:
        print(f"❌ GameState test failed: {e}")
        return False


def test_assets():
    """Test refactored asset functions."""
    print("\nTesting Assets...")
    try:
        from assets.drops import drop_item
        from assets.start_screen import get_start_art, get_start_options
        from assets.interactions import intro, introhouse
        
        # Test drop
        item = drop_item()
        assert "name" in item, "Dropped item should have name"
        assert "loot_type" in item, "Dropped item should have type"
        print(f"  Drop test: {item['name']} ({item['loot_type']})")
        
        # Test start screen
        art = get_start_art()
        assert len(art) > 0, "ASCII art should exist"
        assert "██" in art or "╔" in art, "ASCII art should have box-drawing chars"
        print(f"  Start screen has {len(art)} chars of ASCII art")
        
        opts = get_start_options()
        assert len(opts) == 3, "Should have 3 start options"
        print(f"  Start options: {', '.join(opts)}")
        
        # Test interactions
        choices = intro()
        assert len(choices) == 2, "Intro should have 2 choices"
        print(f"  Intro choices: {choices}")
        
        print("✅ Asset tests passed!")
        return True
    except Exception as e:
        print(f"❌ Asset test failed: {e}")
        return False


def test_save_load():
    """Test save/load functionality."""
    print("\nTesting Save/Load...")
    try:
        from saveing.save import save_inventory
        from saveing.load import load_inventory
        import json
        import os
        
        # Test save
        test_inv = [
            {"name": "Test Item", "loot_type": "common", "saleable": True},
            {"name": "Epic Item", "loot_type": "epic", "saleable": True},
        ]
        save_inventory(test_inv)
        print(f"  Saved {len(test_inv)} items")
        
        # Test load
        loaded = load_inventory()
        assert len(loaded) == len(test_inv), "Should load same number of items"
        assert loaded[0]["name"] == "Test Item", "Should load correct item name"
        print(f"  Loaded {len(loaded)} items")
        
        print("✅ Save/Load tests passed!")
        return True
    except Exception as e:
        print(f"❌ Save/Load test failed: {e}")
        return False


def main():
    print("=" * 60)
    print("Relics & Ruins — Integration Test Suite")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_game_state,
        test_assets,
        test_save_load,
    ]
    
    results = [test() for test in tests]
    
    print("\n" + "=" * 60)
    if all(results):
        print(f"✅ ALL TESTS PASSED ({sum(results)}/{len(results)})")
        print("\nThe GUI is ready to run:")
        print("  python main.py")
    else:
        print(f"❌ Some tests failed ({sum(results)}/{len(results)})")
        sys.exit(1)
    print("=" * 60)


if __name__ == "__main__":
    main()

