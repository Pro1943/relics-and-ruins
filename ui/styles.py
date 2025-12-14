"""Professional dark fantasy theme for Relics & Ruins."""

DARK_STYLE = """
    QMainWindow {
        background-color: #0a0e27;
    }
    
    QWidget {
        background-color: #0a0e27;
        color: #e8dcc4;
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    
    /* Text Edits */
    QTextEdit {
        background-color: #1a1f3a;
        color: #e8dcc4;
        border: 2px solid #d4af37;
        border-radius: 8px;
        padding: 10px;
        font-family: 'Courier New', monospace;
        font-size: 11pt;
    }
    
    /* Progress Bars */
    QProgressBar {
        background-color: #1a1f3a;
        border: 2px solid #d4af37;
        border-radius: 5px;
        text-align: center;
        color: #e8dcc4;
        height: 30px;
        font-weight: bold;
        padding: 2px;
    }
    
    QProgressBar::chunk {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                   stop: 0 #ff6b6b,
                                   stop: 1 #ff8e8e);
        border-radius: 3px;
    }
    
    /* Buttons */
    QPushButton {
        background-color: #d4af37;
        color: #0a0e27;
        border: none;
        border-radius: 6px;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 12pt;
        min-width: 100px;
    }
    
    QPushButton:hover {
        background-color: #e8c547;
    }
    
    QPushButton:pressed {
        background-color: #b8941f;
    }
    
    QPushButton:disabled {
        background-color: #555555;
        color: #999999;
    }
    
    /* Labels */
    QLabel {
        color: #e8dcc4;
        font-size: 11pt;
    }
    
    /* Lists */
    QListWidget {
        background-color: #1a1f3a;
        color: #e8dcc4;
        border: 2px solid #d4af37;
        border-radius: 8px;
        padding: 5px;
    }
    
    QListWidget::item {
        padding: 8px;
        border-radius: 4px;
    }
    
    QListWidget::item:selected {
        background-color: #d4af37;
        color: #0a0e27;
    }
    
    QListWidget::item:hover {
        background-color: #2a2f4a;
    }
    
    /* Scrollbars */
    QScrollBar:vertical {
        background-color: #1a1f3a;
        width: 12px;
        border-radius: 6px;
    }
    
    QScrollBar::handle:vertical {
        background-color: #d4af37;
        border-radius: 6px;
        min-height: 20px;
    }
    
    QScrollBar::handle:vertical:hover {
        background-color: #e8c547;
    }
    
    QScrollBar:horizontal {
        background-color: #1a1f3a;
        height: 12px;
        border-radius: 6px;
    }
    
    QScrollBar::handle:horizontal {
        background-color: #d4af37;
        border-radius: 6px;
        min-width: 20px;
    }
"""

def apply_styles(app):
    """Apply dark fantasy theme to the entire application."""
    app.setStyle('Fusion')
    app.setStyleSheet(DARK_STYLE)

