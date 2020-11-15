from typing import Optional, List, Tuple, Dict

from openpyxl import Workbook

from PyQt5.QtCore import (
    QRect,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QFont
)
from PyQt5.QtWidgets import (
    QSizePolicy,
    QWidget,
    QTabWidget,
    QListWidget,
    QPushButton,
    QLabel,
    QTableWidget
)

from UI.enums import ListWidgetType, TabWidgetType

__all__ = [
    "QTabWidgetExtended",
    "QTabWidgetTabExtended",
    "QTableWidgetExtended",
    "QListWidgetExtended",
    "QPushButtonExtended",
    "QLabelExtended"
]


class QTabWidgetExtended(QTabWidget):
    def __init__(
            self,
            geometry: QRect,
            object_name: str,
            size_policy: Optional[QSizePolicy] = None,
            font: Optional[QFont] = None,
            font_size: Optional[int] = None,
            tab_widget_type: Optional[TabWidgetType] = None,
            parent=None,
    ):
        super(QTabWidgetExtended, self).__init__(parent=parent)
        # Setup Default Values
        self.setEnabled(True)
        self.setMouseTracking(True)
        self.setTabPosition(QTabWidget.North)
        self.setTabShape(QTabWidget.Rounded)
        # Setup Variable Values
        self._setup_variable_values(
            geometry=geometry,
            size_policy=size_policy,
            font=font,
            font_size=font_size,
            object_name=object_name
        )
        # Setup Extension Values
        if tab_widget_type == TabWidgetType.xlsx_tab_widget:
            self.opened_files: Dict[str, Workbook] = {}
            self.opened_files_tables: Dict[str, QTableWidgetExtended] = {}

    def _setup_variable_values(
            self,
            geometry: QRect,
            size_policy: QSizePolicy,
            font: QFont,
            font_size: int,
            object_name: str,
    ):
        self.setGeometry(geometry)
        self.setObjectName(object_name)

        if size_policy is not None:
            self.setSizePolicy(size_policy)

        if font is not None and font_size is not None:
            font.setPointSize(font_size)
            self.setFont(font)


class QTabWidgetTabExtended(QWidget):
    def __init__(self, object_name: str = None):
        super(QTabWidgetTabExtended, self).__init__()
        # Setup Variable Values
        if object_name is not None:
            self._setup_variable_values(object_name=object_name)

    def _setup_variable_values(self, object_name: str):
        self.setObjectName(object_name)


class QTableWidgetExtended(QTableWidget):
    def __init__(
            self,
            geometry: QRect,
            object_name: str,
            column_count: int = 0,
            row_count: int = 0,
            parent=None
    ):
        super(QTableWidgetExtended, self).__init__(parent=parent)
        # Setup Variable Values
        self._setup_variable_values(
            geometry=geometry, object_name=object_name, column_count=column_count, row_count=row_count
        )

    def _setup_variable_values(
            self,
            geometry: QRect,
            object_name: str,
            column_count: int,
            row_count: int
    ):
        self.setGeometry(geometry)
        self.setObjectName(object_name)
        self.setColumnCount(column_count)
        self.setRowCount(row_count)


class QListWidgetExtended(QListWidget):
    def __init__(
            self,
            geometry: QRect,
            object_name: str,
            list_widget_type: Optional[ListWidgetType] = None,
            parent=None
    ):
        super(QListWidgetExtended, self).__init__(parent=parent)
        # Setup Default Values
        self.setContextMenuPolicy(Qt.DefaultContextMenu)
        # Setup Variable Values
        self._setup_variable_values(geometry=geometry, object_name=object_name)
        # Setup Extension Values
        if list_widget_type == ListWidgetType.files_list:
            self.selected_files: List[Tuple[str, str]] = []

    def _setup_variable_values(
            self,
            geometry: QRect,
            object_name: str,
    ):
        self.setGeometry(geometry)
        self.setObjectName(object_name)


class QPushButtonExtended(QPushButton):
    def __init__(
            self,
            geometry: QRect,
            font: QFont,
            font_size: int,
            object_name: str,
            parent=None
    ):
        super(QPushButtonExtended, self).__init__(parent=parent)
        # Setup Default Values
        # Setup Variable Values
        self._setup_variable_values(
            geometry=geometry,
            font=font,
            font_size=font_size,
            object_name=object_name
        )

    def _setup_variable_values(
            self,
            geometry: QRect,
            font: QFont,
            font_size: int,
            object_name: str,
    ):
        self.setGeometry(geometry)
        font.setPointSize(font_size)
        self.setFont(font)
        self.setObjectName(object_name)


class QLabelExtended(QLabel):
    def __init__(
            self,
            geometry: QRect,
            font: QFont,
            font_size: int,
            object_name: str,
            parent=None
    ):
        super(QLabelExtended, self).__init__(parent=parent)
        # Setup Default Values
        # Setup Variable Values
        self._setup_variable_values(geometry=geometry, font=font, font_size=font_size, object_name=object_name)

    def _setup_variable_values(
            self,
            geometry: QRect,
            font: QFont,
            font_size: int,
            object_name: str,
    ):
        self.setGeometry(geometry)
        font.setPointSize(font_size)
        self.setFont(font)
        self.setObjectName(object_name)
