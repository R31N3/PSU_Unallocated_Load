from enum import Enum

__all__ = ["TabWidgetType", "ListWidgetType", "ButtonWidgetType"]


class TabWidgetType(Enum):
    xlsx_tab_widget = "xlsx_tab_widget"


class ListWidgetType(Enum):
    files_list = "files_list"


class ButtonWidgetType(Enum):
    add_row_button = "add_row_button"
    add_col_button = "add_col_button"
