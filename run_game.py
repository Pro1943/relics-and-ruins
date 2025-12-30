"""
RPG Game Launcher - Entry point for the new grid-based RPG game
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ui.game_window import run_game

if __name__ == "__main__":
    run_game()
