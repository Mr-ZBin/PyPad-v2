from PySide6.QtWidgets import QFrame, QVBoxLayout, QComboBox, QSpinBox, QPushButton
from PySide6.QtCore import Qt

from .frame_titles import FrameTitles

from typing import Optional

from scr.interface.basic import DropDownMenu, DigitalEntry


class AbstractSettingFrame(QFrame):
    def __init__(self, __title: Optional[str], __description: Optional[str]) -> None:
        super().__init__()

        self.setObjectName("setting-frame")
        self.mainLayout = QVBoxLayout()
        self.setMinimumHeight(100)
        self.setContentsMargins(10, 0, 0, 0)

        if __title is not None: self.add_subtitle(__title)
        if __description is not None: self.add_description(__description)

        self.setLayout(self.mainLayout)

    def __add_widget(self, __widget) -> None:
        self.mainLayout.addWidget(__widget)

    def add_subtitle(self, __text: str) -> None:
        self.__add_widget(FrameTitles.subtitle(__text))

    def add_description(self, __text: str) -> None:
        self.__add_widget(FrameTitles.description(__text))

    def add_combobox(self, __values: list, __width: int = 200) -> QComboBox:
        combobox = DropDownMenu(*__values, width=__width)
        combobox.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.__add_widget(combobox)

        return combobox

    def add_spinbox(self, __range: tuple[int, int], __width: int = 30) -> QSpinBox:
        spinbox = DigitalEntry(__range, __width)
        self.mainLayout.addWidget(spinbox)

        return spinbox

    def add_button(self, __text: str, __width: int = 200, is_highlighted: bool = False):
        btn = QPushButton(__text)
        btn.setFixedWidth(__width)
        btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        if is_highlighted: btn.setObjectName("highlighted-btn")

        self.mainLayout.addWidget(btn)

        return btn
