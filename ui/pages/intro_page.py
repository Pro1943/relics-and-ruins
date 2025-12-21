"""Intro story page with branching narrative."""
import assets.screens 
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QTextCursor
from PySide6.QtGui import QPixmap

class IntroPage(QWidget):
    combat_requested = Signal()
    back_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Title
        title = QTextEdit()
        title.setReadOnly(True)
        title.setMaximumHeight(60)
        title.setAlignment(Qt.AlignCenter)
        title.setPlainText("📖 THE RUINS AWAIT 📖")
        title.setStyleSheet("""
            QTextEdit {
                background-color: #0a0e27;
                color: #d4af37;
                border: 2px solid #d4af37;
                border-radius: 8px;
                font-size: 14pt;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)

        # Story text
        self.story = QTextEdit()
        self.story.setReadOnly(True)
        self.story.setStyleSheet("""
            QTextEdit {
                background-color: #1a1f3a;
                color: #e8dcc4;
                border: 2px solid #d4af37;
                border-radius: 8px;
                padding: 15px;
                font-family: 'Courier New', monospace;
                font-size: 14pt;
                line-height: 1.8;
            }
        """)
        layout.addWidget(self.story)

        # Choice buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)
        btn_layout.setAlignment(Qt.AlignCenter)
        
        self.choice1_btn = QPushButton("Choice 1")
        self.choice2_btn = QPushButton("Choice 2")
        self.back_btn = QPushButton("↩️ BACK")

        button_style = """
            QPushButton {
                background-color: #d4af37;
                color: #0a0e27;
                border: 2px solid #e8c547;
                border-radius: 6px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #e8c547;
                border: 2px solid #ffd700;
            }
            QPushButton:pressed {
                background-color: #b8941f;
            }
        """
        
        self.choice1_btn.setStyleSheet(button_style)
        self.choice2_btn.setStyleSheet(button_style)
        self.back_btn.setStyleSheet(button_style)

        self.choice1_btn.clicked.connect(self._on_choice1)
        self.choice2_btn.clicked.connect(self._on_choice2)
        self.back_btn.clicked.connect(self._on_back)

        btn_layout.addWidget(self.choice1_btn)
        btn_layout.addWidget(self.choice2_btn)
        btn_layout.addWidget(self.back_btn)

        layout.addLayout(btn_layout)

        self.current_scene = "start"

    def set_story(self, text, choices=None):
        self.story.setPlainText(text)
        # Center-align text using QTextCursor
        cursor = self.story.textCursor()
        cursor.select(QTextCursor.Document)
        block_format = cursor.blockFormat()
        block_format.setAlignment(Qt.AlignCenter)
        cursor.mergeBlockFormat(block_format)
        if choices:
            self.choice1_btn.setText(choices[0] if len(choices) > 0 else "Next")
            self.choice2_btn.setText(choices[1] if len(choices) > 1 else "Back")
            self.choice1_btn.setVisible(True)
            self.choice2_btn.setVisible(True)
        else:
            self.choice1_btn.setVisible(False)
            self.choice2_btn.setVisible(False)

    def _on_choice1(self):
        if self.current_scene == "start":
            self.current_scene = "house"
            self.set_story(
                "You decided to explore the house.\n\n"
                "You raised your hand and knocked.\n"
                "For a moment, nothing but wind through the trees.\n"
                "Then — a slow, deliberate creaking from inside.\n"
                "A voice, old and weary, answers:\n"
                "'No one lived here for decades. Why disturb the dead?'\n"
                "The door remains shut. You feel the air grow cold.",
                ["Knock again", "Push the door"]
            )
        elif self.current_scene == "house":
            self.combat_requested.emit()

    def _on_choice2(self):
        if self.current_scene == "start":
            self.current_scene = "forest"
            self.set_story(
                "You decided to continue your journey, walking deeper into the wilderness.\n\n"
                "You stumbled upon a dense forest.\n"
                "Who knows what this is hiding?\n\n"
                "There seems to be a mysterious barrier stopping you from entering.\n"
                "You'll need the village key.",
                ["Back to start"]
            )
        else:
            self.current_scene = "start"
            self.reset()

    def _on_back(self):
        self.back_requested.emit()

    def reset(self):
        self.set_scene_image("assets/screens/FINAL.png")
        self.current_scene = "start"
        self.set_story(
            "Centuries ago, a powerful civilization fell after misusing ancient relics.\n"
            "Now, the Ruin Warden — a corrupted guardian — controls the heart of the old kingdom.\n"
            "You're a scavenger trying to uncover relics, survive the ruins,\n"
            "and eventually confront the Warden before the corruption spreads.\n\n"
            "You stumbled upon a random old house in the woods...",
            ["Approach the house", "Continue your journey"]
        )

