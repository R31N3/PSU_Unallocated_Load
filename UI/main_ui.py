import sys

from PyQt5.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QSizePolicy,
    QWidget,
)

from UI.extended_widgets import *
from enums import ListWidgetType, TabWidgetType, ButtonWidgetType

__all__ = ["MainWindowRefactored"]


class MainWindowRefactored(QMainWindow):
    def __init__(self):
        super(MainWindowRefactored, self).__init__()
        # Default Values
        self.default_size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.default_size_policy.setHorizontalStretch(0)
        self.default_size_policy.setVerticalStretch(0)
        self.default_font = QFont()
        self.default_font.setFamily("MS Shell Dlg 2")
        self.default_size = QSize(1280, 720)
        # Setup UI
        self._setup_ui()
        # Retranslate UI
        self._retranslate_ui()

    def _setup_ui(self):
        # Main Window Section
        self.setObjectName("MainWindow")
        self.resize(self.default_size)

        # Main Widget Section
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("MainWidget")

        # Main Tab Section
        self.main_tab = QTabWidgetExtended(
            geometry=QRect(5, 0, 1270, 720),
            size_policy=self.default_size_policy,
            font=self.default_font,
            font_size=16,
            object_name="MainTab",
            parent=self.central_widget,
        )

        # File Selection Tab Section
        self._setup_files_selection_tab()
        self.main_tab.addTab(self.files_selection_tab, "")

        # Work With Files Tab Section
        self._setup_work_with_files_tab()
        self.main_tab.addTab(self.work_with_files_tab, "")

        # Final Section
        self.setCentralWidget(self.central_widget)
        QMetaObject.connectSlotsByName(self)

    def _setup_files_selection_tab(self):
        self.files_selection_tab = QTabWidgetTabExtended()
        self.files_selection_tab.setObjectName("FilesSelectionTab")

        # Load Files Section
        self.load_files_list = QListWidgetExtended(
            geometry=QRect(10, 60, 610, 520),
            object_name="LoadFilesList",
            list_widget_type=ListWidgetType.files_list,
            parent=self.files_selection_tab,
        )
        self.load_files_selection_button = QPushButtonExtended(
            geometry=QRect(80, 590, 470, 60),
            font=self.default_font,
            font_size=12,
            object_name="LoadFilesSelectionButton",
            parent=self.files_selection_tab,
        )

        # Teachers Files Section
        self.teachers_files_list = QListWidgetExtended(
            geometry=QRect(640, 60, 610, 520),
            object_name="TeachersFilesList",
            list_widget_type=ListWidgetType.files_list,
            parent=self.files_selection_tab,
        )
        self.teachers_files_selection_button = QPushButtonExtended(
            geometry=QRect(710, 590, 470, 60),
            font=self.default_font,
            font_size=12,
            object_name="TeachersFilesSelectionButton",
            parent=self.files_selection_tab,
        )

        # Labels Section
        self.load_label = QLabelExtended(
            geometry=QRect(120, 20, 400, 20),
            font=self.default_font,
            font_size=14,
            object_name="LoadLabel",
            parent=self.files_selection_tab,
        )
        self.teachers_label = QLabelExtended(
            geometry=QRect(710, 20, 480, 20),
            font=self.default_font,
            font_size=14,
            object_name="TeachersLabel",
            parent=self.files_selection_tab,
        )

    def _setup_work_with_files_tab(self):
        self.work_with_files_tab = QTabWidgetTabExtended()
        self.work_with_files_tab.setObjectName("WorkWithFilesTab")

        # Load Tab Section
        self.load_tab = QTabWidgetExtended(
            geometry=QRect(10, 50, 610, 520),
            object_name="LoadTab",
            parent=self.work_with_files_tab,
            tab_widget_type=TabWidgetType.xlsx_tab_widget,
        )
        self.refresh_load_button = QPushButtonExtended(
            geometry=QRect(50, 10, 530, 30),
            font=self.default_font,
            font_size=14,
            object_name="RefreshLoadButton",
            parent=self.work_with_files_tab,
        )
        self.add_load_row_button = QPushButtonExtended(
            geometry=QRect(10, 580, 290, 40),
            font=self.default_font,
            font_size=14,
            object_name="AddLoadRowButton",
            button_widget_type=ButtonWidgetType.add_row_button,
            parent=self.work_with_files_tab,
        )
        self.add_load_column_button = QPushButtonExtended(
            geometry=QRect(330, 580, 290, 40),
            font=self.default_font,
            font_size=14,
            object_name="AddLoadColumnButton",
            button_widget_type=ButtonWidgetType.add_col_button,
            parent=self.work_with_files_tab,
        )
        self.add_load_sheet_button = QPushButtonExtended(
            geometry=QRect(10, 630, 320, 40),
            font=self.default_font,
            font_size=14,
            object_name="AddLoadSheetButton",
            parent=self.work_with_files_tab,
        )

        # Teachers Tab Section
        self.teachers_tab = QTabWidgetExtended(
            geometry=QRect(640, 50, 610, 520),
            object_name="TeachersTab",
            parent=self.work_with_files_tab,
            tab_widget_type=TabWidgetType.xlsx_tab_widget,
        )
        self.refresh_teachers_button = QPushButtonExtended(
            geometry=QRect(680, 10, 530, 30),
            font=self.default_font,
            font_size=14,
            object_name="RefreshTeachersButton",
            parent=self.work_with_files_tab,
        )
        self.add_teachers_row_button = QPushButtonExtended(
            geometry=QRect(640, 580, 290, 40),
            font=self.default_font,
            font_size=14,
            object_name="AddTeachersRowButton",
            button_widget_type=ButtonWidgetType.add_row_button,
            parent=self.work_with_files_tab,
        )
        self.add_teachers_column_button = QPushButtonExtended(
            geometry=QRect(960, 580, 290, 40),
            font=self.default_font,
            font_size=14,
            object_name="AddTeachersColumnButton",
            button_widget_type=ButtonWidgetType.add_col_button,
            parent=self.work_with_files_tab,
        )
        self.add_teachers_sheet_button = QPushButtonExtended(
            geometry=QRect(930, 630, 320, 40),
            font=self.default_font,
            font_size=14,
            object_name="AddTeachersSheetButton",
            parent=self.work_with_files_tab,
        )

        # End Work Button
        self.end_work_button = QPushButtonExtended(
            geometry=QRect(460, 630, 340, 40),
            font=self.default_font,
            font_size=14,
            object_name="EndWorkButton",
            parent=self.work_with_files_tab,
        )

    def _retranslate_ui(self):
        _translate = QCoreApplication.translate
        main_window_title = "MainWindow"
        self.setWindowTitle(_translate(main_window_title, "Программа распределения нагрузки"))

        self.main_tab.setTabText(
            self.main_tab.indexOf(self.files_selection_tab), _translate(main_window_title, "Выбор файлов")
        )
        self.load_label.setText(_translate(main_window_title, "Файлы с нераспределенной нагрузкой"))
        self.load_files_selection_button.setText(
            _translate(main_window_title, "Выберите файлы с нераспределенной нагрузкой")
        )
        self.teachers_label.setText(_translate(main_window_title, "Файлы с преподавателями для распределения"))
        self.teachers_files_selection_button.setText(
            _translate(main_window_title, "Выберите файлы преподавателей для распределения")
        )

        self.main_tab.setTabText(
            self.main_tab.indexOf(self.work_with_files_tab),
            _translate(main_window_title, "Распределение нагрузки по преподавателям"),
        )

        self.refresh_load_button.setText(_translate(main_window_title, "Обновить нераспределенную нагрузку"))
        self.add_load_row_button.setText(_translate(main_window_title, "Добавить строку"))
        self.add_load_column_button.setText(_translate(main_window_title, "Добавить столбец"))
        self.add_load_sheet_button.setText(_translate(main_window_title, "Добавить лист с нагрузкой"))

        self.refresh_teachers_button.setText(_translate(main_window_title, "Обновить список для распределения"))
        self.add_teachers_row_button.setText(_translate(main_window_title, "Добавить строку"))
        self.add_teachers_column_button.setText(_translate(main_window_title, "Добавить столбец"))
        self.add_teachers_sheet_button.setText(_translate(main_window_title, "Добавить лист распределения"))

        self.end_work_button.setText(_translate(main_window_title, "Завершить распределение"))


def main():
    app = QApplication(sys.argv)
    application_window = MainWindowRefactored()
    application_window.show()
    app.exec_()


if __name__ == "__main__":
    main()
