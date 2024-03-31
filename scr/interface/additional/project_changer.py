from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import QSize

from scr.interface.abstract import TransparentDialogWindow, ListChanger
from scr.interface.basic import Text, DialogButton

from scr.scripts.font import Font
from scr.scripts.tools.file import FileLoader

from scr.project.pyproject import PyProjectConfig


class ProjectChanger(ListChanger):
    def __init__(self):
        super().__init__(*PyProjectConfig.get_projects_names())

        self.setStyleSheet(
            self.styleSheet() + FileLoader.load_style("scr/interface/additional/styles/project_changer.css")
        )

        self.setFont(Font.get_system_font("CascadiaMono.ttf", 12))
        self.setIconSize(QSize(self.font().pointSize() * 2, self.font().pointSize() * 2))
        self.__set_icons()

    def __set_icons(self) -> None:
        for item, icon_path in zip(self.get_items(), PyProjectConfig.get_project_icons()):
            item.setIcon(QIcon(icon_path))


class ProjectChangerWindow(TransparentDialogWindow):
    def __init__(self, __parent):
        super().__init__(__parent, width=1000, height=600)

        self.projectChanger = ProjectChanger()
        self.add_widget(Text.label("Projects...", "CascadiaMono.ttf", 9))
        self.add_widget(self.projectChanger)

        self.openBtn = DialogButton("Choose", "accept")
        self.newBtn = DialogButton("New", "reject")
        self.cancelBtn = DialogButton("Cancel", "reject")

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.buttonsLayout.addWidget(self.openBtn)
        self.buttonsLayout.addWidget(self.newBtn)
        self.buttonsLayout.addWidget(self.cancelBtn)
        self.add_layout(self.buttonsLayout)
