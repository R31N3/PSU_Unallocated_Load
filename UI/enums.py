from enum import Enum

__all__ = ["TabWidgetType", "ListWidgetType"]


class TabWidgetType(Enum):
    xlsx_tab_widget = "xlsx_tab_widget"


class ListWidgetType(Enum):
    files_list = "files_list"

