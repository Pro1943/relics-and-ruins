"""
GUI launcher for Relics & Ruins.

This replaces the original CLI entrypoint with a PySide6 GUI.
If PySide6 is unavailable, prints guidance to install requirements.
"""
import sys

try:
    from ui.gui_main import run_gui
    HAS_QT = True
except Exception:
    HAS_QT = False


def main():
    if HAS_QT:
        run_gui()
    else:
        print("PySide6 not available. Please install requirements and run again.")
        print("To install: pip install -r requirments.txt")


if __name__ == "__main__":
    main()
