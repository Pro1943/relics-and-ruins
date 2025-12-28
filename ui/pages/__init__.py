"""UI pages package"""
from .intro_page import IntroPage
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
    QLabel,          
)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QTextCursor, QPixmap

class IntroPage(QWidget):
    combat_requested = Signal()
    back_requested = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Title (already correct)
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

        # ✅ Scene image (THIS is the correct spot)
        self.scene_image = QLabel()
        self.scene_image.setAlignment(Qt.AlignCenter)
        self.scene_image.setStyleSheet("""
            QLabel {
                background-color: #0a0e27;
                border: 2px solid #d4af37;
                border-radius: 8px;
            }
        """)
        layout.addWidget(self.scene_image)

        # Story text (already correct)
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
    def set_scene_image(self, path):
        self.scene_image.setMinimumHeight(220)
        pixmap = QPixmap(path)
        if pixmap.isNull():
            self.scene_image.clear()
            return

        self.scene_image.setPixmap(
            pixmap.scaled(
                640, 360,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

