from PySide6.QtWidgets import QApplication
import sys
from .main_window import MainWindow
from .styles import apply_styles


def run_gui():
    app = QApplication(sys.argv)
    apply_styles(app)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui()
