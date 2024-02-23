from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtCore import Qt

from scr.scripts import FileLoader

import copy


class CodeGlanceMap(QPlainTextEdit):
    def __init__(self, __text: str, __font: QFont) -> None:
        super().__init__()

        self.setLineWrapMode(self.LineWrapMode.NoWrap)
        self.setFixedWidth(150)
        self.setReadOnly(True)
        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/code_map.css"))
        self.setObjectName("code-map")
        self.setPlainText(__text)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setTabStopDistance(1)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByKeyboard)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        font = copy.copy(__font)
        font.setPointSize(3)
        self.setTabStopDistance(QFontMetrics(font).horizontalAdvanceChar(" ") * 1.5)
        self.setFont(font)