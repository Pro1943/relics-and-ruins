"""Inventory display page."""
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QTextCursor


class InventoryPage(QWidget):
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
        title.setPlainText("🎒 YOUR TREASURES 🎒")
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

        # Inventory display
        self.inv_display = QTextEdit()
        self.inv_display.setReadOnly(True)
        self.inv_display.setStyleSheet("""
            QTextEdit {
                background-color: #1a1f3a;
                color: #e8dcc4;
                border: 2px solid #d4af37;
                border-radius: 8px;
                padding: 15px;
                font-family: 'Courier New', monospace;
                font-size: 13pt;
            }
        """)
        layout.addWidget(self.inv_display)

        # Back button
        btn_layout = QHBoxLayout()
        btn_layout.setAlignment(Qt.AlignCenter)
        back_btn = QPushButton("↩️ BACK TO COMBAT ↩️")
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #d4af37;
                color: #0a0e27;
                border: 2px solid #e8c547;
                border-radius: 8px;
                padding: 12px 25px;
                font-weight: bold;
                font-size: 12pt;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #e8c547;
                border: 2px solid #ffd700;
            }
            QPushButton:pressed {
                background-color: #b8941f;
            }
        """)
        back_btn.clicked.connect(self._on_back)
        btn_layout.addStretch()
        btn_layout.addWidget(back_btn)
        btn_layout.addStretch()

        layout.addLayout(btn_layout)

    def show_inventory(self, inv_list):
        if not inv_list:
            text = "🎒 Your Inventory:\n\n✨ Your bag is empty ✨"
        else:
            lines = ["🎒 Your Treasures:\n", "━" * 40]
            for i, item in enumerate(inv_list, 1):
                rarity = item.get('loot_type', '')
                icon = self._get_rarity_icon(rarity)
                lines.append(f"{i}. {icon} {item.get('name', 'Unknown')} [{rarity}]")
            lines.append("━" * 40)
            text = "\n".join(lines)
        self.inv_display.setPlainText(text)
        # Center-align text using QTextCursor
        cursor = self.inv_display.textCursor()
        cursor.select(QTextCursor.Document)
        block_format = cursor.blockFormat()
        block_format.setAlignment(Qt.AlignCenter)
        cursor.mergeBlockFormat(block_format)

    def _get_rarity_icon(self, rarity):
        """Return icon for item rarity."""
        icons = {
            "common": "⚪",
            "rare": "🔵",
            "epic": "🟣",
        }
        return icons.get(rarity, "⭐")

    def _on_back(self):
        self.back_requested.emit()

