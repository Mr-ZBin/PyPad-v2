import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QAbstractItemView, QFileSystemModel, QTreeView

from scr.project import ProjectConfig
from scr.scripts.font import Font, WorkbenchFontManager
from scr.scripts.tools.file import FileLoader
from scr.scripts.utils import IconProvider


class FileTree(QTreeView):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/file_tree.css"))
        self.setObjectName("file-tree")
        self.setMinimumWidth(300)

        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.setIndentation(20)
        self.setSelectionBehavior(QTreeView.SelectionBehavior.SelectRows)
        self.setEditTriggers(QTreeView.EditTrigger.NoEditTriggers)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.__directory = ProjectConfig.get_directory()

        # font & icon size
        self.update_font()

        self.model = QFileSystemModel()
        self.model.setRootPath(self.__directory)
        self.setModel(self.model)
        self.setRootIndex(self.model.index(self.__directory))
        self.setHeaderHidden(True)
        self.model.setIconProvider(IconProvider())

        for i in range(1, 4):
            self.header().setSectionHidden(i, True)

        self.__changed_directory_event = None

    def update_font(self):
        self.__main_font = Font.get_system_font(
            WorkbenchFontManager.get_current_family(),
            WorkbenchFontManager.get_current_font_size(),
        )
        self.setFont(self.__main_font)

        icon_size = WorkbenchFontManager.get_current_font_size() * 1.5
        self.setIconSize(QSize(icon_size, icon_size))

    def get_path_by_index(self, __index) -> str:
        return self.model.filePath(__index)

    def get_index_by_path(self, __path: str):
        return self.model.index(__path, 0)

    def get_file_icon(self, __index):
        return self.model.fileIcon(__index)

    def open_file(self, __path: str):
        """returns the index of this path to open it in the editor"""
        try:
            self.open_directory(os.path.dirname(__path))

        except TypeError:
            ...

        return self.get_index_by_path(__path)

    def directory_changed_connect(self, __command) -> None:
        self.__changed_directory_event = __command

    def open_directory(self, __path: str) -> None:
        ProjectConfig.set_directory(__path)

        if self.__changed_directory_event is not None:
            self.__changed_directory_event()

        self.__directory = __path
        self.model.setRootPath(__path)
        self.setRootIndex(self.model.index(__path))

    def get_current_directory(self) -> str:
        return self.__directory

    def show_hide_file_tree(self) -> None:
        if self.isVisible():
            self.setVisible(False)
        else:
            self.setVisible(True)
