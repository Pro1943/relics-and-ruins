from assets.enemy import GHOST_ART
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
    QProgressBar,
    QListWidget,
)
from PySide6.QtCore import Qt, Signal

class CombatPage(QWidget):
    combat_ended = Signal()  # Emitted when victory or defeat occurs

    def __init__(self, parent=None):
        super().__init__(parent)
        self.state = None
        self.inventory_open = False
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Title
        title = QLabel("⚔️ BATTLE ⚔️")
        title.setStyleSheet("""
            color: #d4af37;
            font-size: 16pt;
            font-weight: bold;
            text-align: center;
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # HP bars with enhanced styling
        self.player_hp_bar = QProgressBar()
        self.player_hp_bar.setMaximum(100)
        self.player_hp_bar.setFormat("Player HP: %p%")
        self.player_hp_bar.setStyleSheet("""
            QProgressBar {
                background-color: #1a1f3a;
                border: 2px solid #4CAF50;
                border-radius: 6px;
                text-align: center;
                color: #4CAF50;
                height: 32px;
                font-weight: bold;
                padding: 1px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                           stop: 0 #4CAF50,
                                           stop: 1 #81C784);
                border-radius: 4px;
            }
        """)

        self.enemy_hp_bar = QProgressBar()
        self.enemy_hp_bar.setMaximum(100)
        self.enemy_hp_bar.setFormat("Enemy HP: %p%")
        self.enemy_hp_bar.setStyleSheet("""
            QProgressBar {
                background-color: #1a1f3a;
                border: 2px solid #ff6b6b;
                border-radius: 6px;
                text-align: center;
                color: #ff6b6b;
                height: 32px;
                font-weight: bold;
                padding: 1px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                           stop: 0 #ff6b6b,
                                           stop: 1 #ff8e8e);
                border-radius: 4px;
            }
        """)

        layout.addWidget(self.player_hp_bar)
        layout.addWidget(self.enemy_hp_bar)
                # Enemy ASCII art (battle visual)
        self.enemy_art = QLabel(GHOST_ART)
        self.enemy_art.setAlignment(Qt.AlignCenter)
        self.enemy_art.setTextInteractionFlags(Qt.NoTextInteraction)

        self.enemy_art.setStyleSheet("""
            QLabel {
                color: #cfd8ff;
                background-color: #121633;
                border: 2px solid #d4af37;
                border-radius: 8px;
                padding: 12px;
                font-family: 'Courier New', monospace;
                font-size: 12pt;
            }
        """)

        layout.addWidget(self.enemy_art)

        # action buttons with icons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(8)
        btn_layout.setAlignment(Qt.AlignCenter)
        
        self.attack_btn = QPushButton("⚔️ ATTACK ⚔️")
        self.defend_btn = QPushButton("🛡️  DEFEND  🛡️")
        self.special_btn = QPushButton("🔥 SPECIAL 🔥")
        self.inv_btn = QPushButton("🎒 INVENTORY 🎒")
        self.continue_btn = QPushButton("➜ CONTINUE ➜")
        self.continue_btn.setVisible(False)

        button_style = """
            QPushButton {
                background-color: #d4af37;
                color: #0a0e27;
                border: 2px solid #e8c547;
                border-radius: 6px;
                padding: 10px 15px;
                font-weight: bold;
                font-size: 11pt;
                min-height: 25px;
            }
            QPushButton:hover {
                background-color: #e8c547;
                border: 2px solid #ffd700;
            }
            QPushButton:pressed {
                background-color: #b8941f;
            }
            QPushButton:disabled {
                background-color: #555555;
                color: #999999;
            }
        """
        
        for btn in [self.attack_btn, self.defend_btn, self.special_btn, self.inv_btn, self.continue_btn]:
            btn.setStyleSheet(button_style)

        btn_layout.addWidget(self.attack_btn)
        btn_layout.addWidget(self.defend_btn)
        btn_layout.addWidget(self.special_btn)
        btn_layout.addWidget(self.inv_btn)
        btn_layout.addWidget(self.continue_btn)

        layout.addLayout(btn_layout)

        # log area with enhanced styling
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setStyleSheet("""
            QTextEdit {
                background-color: #1a1f3a;
                color: #e8dcc4;
                border: 2px solid #d4af37;
                border-radius: 8px;
                padding: 10px;
                font-family: 'Courier New', monospace;
                font-size: 11pt;
            }
            QScrollBar:vertical {
                background-color: #0a0e27;
                width: 12px;
            }
            QScrollBar::handle:vertical {
                background-color: #d4af37;
                border-radius: 6px;
            }
        """)
        layout.addWidget(self.log)
        # connections
        self.attack_btn.clicked.connect(self.on_attack)
        self.defend_btn.clicked.connect(self.on_defend)
        self.special_btn.clicked.connect(self.on_special)
        self.inv_btn.clicked.connect(self.on_inventory)
        self.continue_btn.clicked.connect(self.on_continue)

    def set_state(self, state):
        self.state = state
        self.inventory_open = False
        self.log.clear()
        self.append_log("A wild ghost appears!")
        self.append_log("Battle start!")
        self.are_buttons_enabled(True)
        self.update_ui()

    def update_ui(self):
        if not self.state:
            return
        self.player_hp_bar.setValue(self.state.player_hp)
        self.enemy_hp_bar.setValue(self.state.enemy_hp)

    def append_log(self, text):
        self.log.append(text)

    def are_buttons_enabled(self, enabled):
        self.attack_btn.setEnabled(enabled)
        self.defend_btn.setEnabled(enabled)
        self.special_btn.setEnabled(enabled)
        self.inv_btn.setEnabled(enabled)

    def on_attack(self):
        if not self.state:
            return
        self.are_buttons_enabled(False)
        res = self.state.attack()
        self.append_log(f"You attack for {res['damage']} damage.")
        self.update_ui()
        if self.state.enemy_hp <= 0:
            self.append_log("\n🎉 Enemy defeated! You gained loot!")
            item = self.state.inv_add()
            self.append_log(f"You got: {item['name']} [{item.get('loot_type', '')}]")
            self.state.save()
            self.show_continue_button()
            return  # Wait for user to click Continue

        e = self.state.enemy_action()
        self.append_log(f"\n{e['msg']}")
        if e['actual_damage'] > 0:
            self.append_log(f"You take {e['actual_damage']} damage.")
        if self.state.player_hp <= 0:
            self.append_log("\n💀 You have been defeated!")
            self.show_continue_button()
            return  # Wait for user to click Continue
        self.update_ui()
        self.are_buttons_enabled(True)

    def on_defend(self):
        if not self.state:
            return
        self.are_buttons_enabled(False)
        res = self.state.defend()
        self.append_log(f"You brace and gain defence ({res['defence']}).")
        e = self.state.enemy_action()
        self.append_log(f"{e['msg']}")
        if e['actual_damage'] > 0:
            self.append_log(f"You take {e['actual_damage']} damage.")
        if self.state.player_hp <= 0:
            self.append_log("\n💀 You have been defeated!")
            self.combat_ended.emit()
            return
        self.update_ui()
        self.are_buttons_enabled(True)

    def on_special(self):
        if not self.state:
            return
        self.are_buttons_enabled(False)
        res = self.state.special()
        if res.get('used') is False:
            self.append_log(res.get('reason', 'Cannot use special.'))
            self.are_buttons_enabled(True)
            return
        self.append_log(f"You use special for {res.get('damage', 0)} damage.")
        self.update_ui()
        if self.state.enemy_hp <= 0:
            self.append_log("\n🎉 Enemy defeated! You gained loot!")
            item = self.state.inv_add()
            self.append_log(f"You got: {item['name']} [{item.get('loot_type', '')}]")
            self.state.save()
            self.show_continue_button()
            return
        e = self.state.enemy_action()
        self.append_log(f"{e['msg']}")
        if e['actual_damage'] > 0:
            self.append_log(f"You take {e['actual_damage']} damage.")
        if self.state.player_hp <= 0:
            self.append_log("\n💀 You have been defeated!")
            self.show_continue_button()
            return
        self.update_ui()
        self.are_buttons_enabled(True)

    def on_inventory(self):
        self.are_buttons_enabled(False)
        inv = self.state.inv if self.state else []
        if not inv:
            self.append_log("Inventory is empty.")
        else:
            self.append_log("\n--- Inventory ---")
            for i, it in enumerate(inv, 1):
                self.append_log(f"{i}. {it.get('name', 'Unknown')} - {it.get('loot_type','')}")
            self.append_log("--- End Inventory ---\n")
        self.are_buttons_enabled(True)

    def show_continue_button(self):
        """Show Continue button and hide action buttons."""
        self.attack_btn.setVisible(False)
        self.defend_btn.setVisible(False)
        self.special_btn.setVisible(False)
        self.inv_btn.setVisible(False)
        self.continue_btn.setVisible(True)

    def on_continue(self):
        """Handle Continue button click."""
        self.continue_btn.setVisible(False)
        self.attack_btn.setVisible(True)
        self.defend_btn.setVisible(True)
        self.special_btn.setVisible(True)
        self.inv_btn.setVisible(True)
        self.combat_ended.emit()
