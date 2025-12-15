from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
)
from PySide6.QtCore import Signal, Qt


ASCII_TITLE = r"""




                                                     ▄▄▄▄▄▄         ▄▄                                        ▄▄▄▄▄▄                        
                                                    █▀██▀▀▀█▄        ██                                 █▄   █▀██▀▀▀█▄                      
                                                      ██▄▄▄█▀        ██ ▀▀                     ▄        ██     ██▄▄▄█▀        ▀▀ ▄          
                                                      ██▀▀█▄   ▄█▀█▄ ██ ██ ▄███▀ ▄██▀█   ▄▀▀█▄ ████▄ ▄████     ██▀▀█▄   ██ ██ ██ ████▄ ▄██▀█
                                                    ▄ ██  ██   ██▄█▀ ██ ██ ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ▄ ██  ██   ██ ██ ██ ██ ██ ▀███▄
                                                    ▀██▀  ▀██▀▄▀█▄▄▄▄██▄██▄▀███▄█▄▄██▀  ▄▀█▄██▄██ ▀█▄█▀███   ▀██▀  ▀██▀▄▀██▀█▄██▄██ ▀██▄▄██▀
"""


class StartPage(QWidget):
    start_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 40, 20, 40)
        layout.setSpacing(30)
        layout.setAlignment(Qt.AlignCenter)

        # ASCII art in a read-only text area to preserve monospace
        art = QTextEdit()
        art.setReadOnly(True)
        art.setPlainText(ASCII_TITLE)
        art.setAlignment(Qt.AlignCenter)
        art.setStyleSheet("""
            QTextEdit {
                background-color: #0a0e27;
                color: #d4af37;
                border: 3px solid #d4af37;
                border-radius: 10px;
                padding: 20px;
                font-family: 'Courier New', monospace;
                font-size: 9pt;
                font-weight: bold;
            }
        """)
        art.setMinimumHeight(200)
        layout.addWidget(art)

        # Tagline
        tagline = QLabel("Explore ancient ruins. Fight mysterious ghosts. Claim legendary treasures.")
        tagline.setStyleSheet("""
            color: #d4af37;
            font-size: 14pt;
            font-weight: bold;
            text-align: center;
        """)
        tagline.setAlignment(Qt.AlignCenter)
        layout.addWidget(tagline)

        # Button layout
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(15)
        btn_layout.setAlignment(Qt.AlignCenter)
        
        start_btn = QPushButton("⚔️  START ADVENTURE  ⚔️")
        load_btn = QPushButton("📖  LOAD GAME  📖")
        quit_btn = QPushButton("❌  QUIT  ❌")

        # Enhanced button styling
        button_style = """
            QPushButton {
                background-color: #d4af37;
                color: #0a0e27;
                border: 2px solid #e8c547;
                border-radius: 8px;
                padding: 15px 30px;
                font-weight: bold;
                font-size: 13pt;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #e8c547;
                border: 2px solid #ffd700;
            }
            QPushButton:pressed {
                background-color: #b8941f;
            }
        """
        start_btn.setStyleSheet(button_style)
        load_btn.setStyleSheet(button_style)
        quit_btn.setStyleSheet(button_style)

        start_btn.clicked.connect(self._on_start)
        load_btn.clicked.connect(self._on_load)
        quit_btn.clicked.connect(self._on_quit)

        btn_layout.addWidget(start_btn)
        btn_layout.addWidget(load_btn)
        btn_layout.addWidget(quit_btn)

        layout.addLayout(btn_layout)
        layout.addStretch()

    def _on_start(self):
        self.start_requested.emit()

    def _on_load(self):
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.information(self, "Load Game", "Save/Load feature coming soon!")

    def _on_quit(self):
        from PySide6.QtWidgets import QApplication

        QApplication.instance().quit()
