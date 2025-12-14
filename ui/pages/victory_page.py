"""Victory screen."""
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
)
from PySide6.QtCore import Signal, Qt


VICTORY_ART = r"""
                                    ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
                                    ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
                                    ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ 
                                    ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  
                                     ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   
                                      ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝
"""


class VictoryPage(QWidget):
    restart_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 30, 20, 30)
        layout.setSpacing(20)

        # Title
        title = QTextEdit()
        title.setReadOnly(True)
        title.setMaximumHeight(150)
        title.setAlignment(Qt.AlignCenter)
        title.setPlainText(VICTORY_ART)
        title.setStyleSheet("""
            QTextEdit {
                background-color: #0a0e27;
                color: #4CAF50;
                border: 3px solid #4CAF50;
                border-radius: 10px;
                font-family: 'Courier New', monospace;
                font-size: 10pt;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)

        # Message display
        self.display = QTextEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            QTextEdit {
                background-color: #1a1f3a;
                color: #e8dcc4;
                border: 2px solid #d4af37;
                border-radius: 8px;
                padding: 15px;
                font-size: 12pt;
                line-height: 1.5;
            }
        """)
        layout.addWidget(self.display)

        # Restart button
        btn_layout = QHBoxLayout()
        btn_layout.setAlignment(Qt.AlignCenter)
        restart_btn = QPushButton("🔄 RESTART GAME 🔄")
        quit_btn = QPushButton("❌ QUIT ❌")
        
        button_style = """
            QPushButton {
                background-color: #d4af37;
                color: #0a0e27;
                border: 2px solid #e8c547;
                border-radius: 8px;
                padding: 15px 30px;
                font-weight: bold;
                font-size: 13pt;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #e8c547;
                border: 2px solid #ffd700;
            }
            QPushButton:pressed {
                background-color: #b8941f;
            }
        """
        
        restart_btn.setStyleSheet(button_style)
        quit_btn.setStyleSheet(button_style)
        restart_btn.clicked.connect(self._on_restart)
        quit_btn.clicked.connect(self._on_quit)
        btn_layout.addStretch()
        btn_layout.addWidget(restart_btn)
        btn_layout.addWidget(quit_btn)
        btn_layout.addStretch()

        layout.addLayout(btn_layout)

    def show(self):
        text = "You stand victorious in the ruins!\n\n"
        text += "✨ The deeper paths now whisper your name. ✨\n\n"
        text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        text += "Relics & Ruins is in active development.\n"
        text += "Stronger enemies, new relics, and epic treasures coming soon!\n"
        text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        self.display.setPlainText(text)

    def _on_restart(self):
        self.restart_requested.emit()

    def _on_quit(self):
        import sys
        sys.exit()

