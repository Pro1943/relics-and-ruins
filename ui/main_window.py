from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
    QHBoxLayout,
)
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from .pages.start_page import StartPage
from .pages.intro_page import IntroPage
from .pages.combat_page import CombatPage
from .pages.inventory_page import InventoryPage
from .pages.victory_page import VictoryPage
from .pages.gameover_page import GameOverPage
from core.game_state import create_default_state
from .styles import apply_styles


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relics & Ruins - Dark Fantasy Adventure")
        self.showFullScreen()

        self.state = create_default_state()

        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # pages
        self.start_page = StartPage(self)
        self.intro_page = IntroPage(self)
        self.combat_page = CombatPage(self)
        self.inventory_page = InventoryPage(self)
        self.victory_page = VictoryPage(self)
        self.gameover_page = GameOverPage(self)

        self.stack.addWidget(self.start_page)
        self.stack.addWidget(self.intro_page)
        self.stack.addWidget(self.combat_page)
        self.stack.addWidget(self.inventory_page)
        self.stack.addWidget(self.victory_page)
        self.stack.addWidget(self.gameover_page)

        # connect signals
        self.start_page.start_requested.connect(self.show_intro)
        self.intro_page.combat_requested.connect(self.show_combat)
        self.intro_page.back_requested.connect(self.show_start)
        self.combat_page.combat_ended.connect(self._check_combat_end)
        self.combat_page.inv_btn.clicked.connect(self.show_inventory_from_combat)
        self.inventory_page.back_requested.connect(self.show_combat)
        self.victory_page.restart_requested.connect(self.reset_and_show_start)
        self.gameover_page.restart_requested.connect(self.reset_and_show_start)

    def show_combat(self):
        self.state.reset_combat()
        self.combat_page.set_state(self.state)
        self.stack.setCurrentWidget(self.combat_page)

    def show_intro(self):
        self.intro_page.reset()
        self.stack.setCurrentWidget(self.intro_page)

    def show_start(self):
        self.stack.setCurrentWidget(self.start_page)

    def show_inventory_from_combat(self):
        self.inventory_page.show_inventory(self.state.inv)
        self.stack.setCurrentWidget(self.inventory_page)

    def _check_combat_end(self):
        """Check if combat has ended and show appropriate screen."""
        if self.state.player_hp <= 0:
            self.gameover_page.show()
            self.stack.setCurrentWidget(self.gameover_page)
        elif self.state.enemy_hp <= 0:
            self.victory_page.show()
            self.stack.setCurrentWidget(self.victory_page)

    def reset_and_show_start(self):
        self.state = create_default_state()
        self.show_start()
