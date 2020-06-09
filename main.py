import sys, os, shutil, datetime
import openpyxl, sympy
from typing import Dict, List, Tuple, Optional
from pathlib import Path
from PyQt5 import QtWidgets, QtGui, QtCore

import UI.Main_Window.main_window as main_window


class ListItem(QtWidgets.QListWidgetItem):
    def __init__(self, visible_text: str):
        super().__init__(visible_text)


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Переменные
        self.root_dir = os.getcwd()

        # selected List[Tuple[str, str]] - Path To File AND Filename to View
        self.selected_load: List[Tuple[str, str]] = []
        self.selected_teachers: List[Tuple[str, str]] = []

        # opened Dict[str, openpyxl.Workbook] - Dict of Opened Files
        self.opened_load: Dict[str, openpyxl.Workbook] = {}
        self.opened_teachers: Dict[str, openpyxl.Workbook] = {}

        # tables Dict[str, QtWidgets.QTableWidget] - Loaded Tables From Excel or Created by User
        self.load_tables: Dict[str, QtWidgets.QTableWidget] = {}
        self.teachers_tables: Dict[str, QtWidgets.QTableWidget] = {}

        # Инициализация
        self.setupUi(self)
        self.source_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите директорию с файлами для работы", directory=self.root_dir) or self.root_dir
        self.work_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите рабочую директорию", directory=self.root_dir) or self.root_dir
        self.result_dir = os.path.join(self.work_dir, "Результат")
        if os.path.exists(self.result_dir):
            os.rmdir(self.result_dir)
        os.mkdir(self.result_dir)

        # Действия
        self.LoadSelection.clicked.connect(lambda: self.selection_button(
            qlist=self.SelectedLoad,
            data_list=self.selected_load
        ))
        self.SelectedLoad.itemClicked['QListWidgetItem*'].connect(lambda: self.deletion_menu(
            data_list=self.selected_load,
            qlist=self.SelectedLoad,
        ))
        self.RefreshLoad.clicked.connect(lambda: self.refresh(
            data_list=self.selected_load, opened_files=self.opened_load, tables=self.load_tables, tab_widget=self.LoadTabs
        ))
        self.AddLoadRow.clicked.connect(lambda: self.add_row_button(tab_widget=self.LoadTabs, tables=self.load_tables))
        self.AddLoadColumn.clicked.connect(lambda: self.add_column_button(tab_widget=self.LoadTabs, tables=self.load_tables))
        self.AddLoadTab.clicked.connect(lambda: self.add_tab_button(tab_widget=self.LoadTabs, tables=self.load_tables))

        self.TeachersSelection.clicked.connect(lambda: self.selection_button(
            qlist=self.SelectedTeachers,
            data_list=self.selected_teachers
        ))
        self.SelectedTeachers.itemClicked['QListWidgetItem*'].connect(lambda: self.deletion_menu(
            data_list=self.selected_teachers,
            qlist=self.SelectedTeachers,
        ))
        self.RefreshTeachers.clicked.connect(lambda: self.refresh(
            data_list=self.selected_teachers, opened_files=self.opened_teachers, tables=self.teachers_tables, tab_widget=self.TeachersTabs
        ))
        self.AddTeachersRow.clicked.connect(
            lambda: self.add_row_button(tab_widget=self.TeachersTabs, tables=self.teachers_tables)
        )
        self.AddTeachersColumn.clicked.connect(
            lambda: self.add_column_button(tab_widget=self.TeachersTabs, tables=self.teachers_tables)
        )
        self.AddTeachersTab.clicked.connect(
            lambda: self.add_tab_button(tab_widget=self.TeachersTabs, tables=self.teachers_tables)
        )

    def fill_list(self, qlist: QtWidgets.QListWidget, selected_files):
        qlist.clear()
        for selected in selected_files:
            qlist.addItem(selected[0])

    def selection_button(self, data_list: list, qlist: QtWidgets.QListWidget):
        for selected_file in QtWidgets.QFileDialog.getOpenFileNames(
                self, "Выберите файлы", filter="Excel Files (*.xls *.xlsx)", directory=self.source_dir
        )[0]:
            selected = (os.path.basename(selected_file), selected_file)
            if Path(selected_file).suffix in [".xlsx", ".xls"] and selected not in data_list:
                data_list.append(selected)

        self.fill_list(qlist=qlist, selected_files=data_list)

    def deletion_from_list(self, data_list: list, qlist: QtWidgets.QListWidget):
        data_list.pop(qlist.indexFromItem(qlist.currentItem()).row())
        qlist.removeItemWidget(qlist.currentItem())
        self.fill_list(qlist=qlist, selected_files=data_list)

    def deletion_menu(self, data_list: list, qlist: QtWidgets.QListWidget):
        menu = QtWidgets.QMenu(qlist)
        menu.addAction("Удалить файл из списка")
        menu.triggered.connect(lambda: self.deletion_from_list(data_list=data_list, qlist=qlist))
        menu.exec_(QtGui.QCursor.pos())

    def refresh(self, data_list: list, opened_files: Dict[str, openpyxl.Workbook], tab_widget: QtWidgets.QTabWidget, tables: Dict[str, QtWidgets.QTableWidget]):
        for load_file in data_list:
            file_name = load_file[0]
            target_temp_file = os.path.join(self.work_dir, file_name)
            if not os.path.exists(target_temp_file):
                shutil.copyfile(load_file[1], target_temp_file)
                opened_file = openpyxl.load_workbook(filename=target_temp_file)
                opened_files[target_temp_file] = opened_file
            elif not opened_files.get(target_temp_file):
                opened_file = openpyxl.load_workbook(filename=target_temp_file)
                opened_files[target_temp_file] = opened_file
            else:
                opened_file = openpyxl.load_workbook(filename=target_temp_file)

            for sheet_name in opened_file.sheetnames:
                tab_name = f"{file_name} -> {sheet_name}"
                if not tables.get(tab_name):
                    tab = QtWidgets.QWidget()
                    tab.setObjectName(tab_name)
                    tables[tab_name] = QtWidgets.QTableWidget(tab)
                    tables[tab_name].setGeometry(QtCore.QRect(-10, -10, 861, 901))
                    tables[tab_name].setObjectName(tab_name)
                    tables[tab_name].setColumnCount(0)
                    tables[tab_name].setRowCount(0)
                    tab_widget.addTab(tab, tab_name)

                table = tables[tab_name]

                ws = opened_file[sheet_name]
                headers = [item.value for item in ws[8] if item.value is not None]
                row = 9
                rows = []
                table.setColumnCount(len(headers))
                table.setHorizontalHeaderLabels(headers)
                while ws[row][0].value is not None:
                    row_values = []
                    table.insertRow(table.rowCount())
                    for col in range(len(headers)):
                        row_values.append(QtWidgets.QTableWidgetItem(str(ws[row][col].value or "")))
                    rows.append(row_values)
                    row += 1

                row = 0
                for row_values in rows:
                    for col in range(len(headers)):
                        table.setItem(row, col, row_values[col])
                    row += 1

                table.resizeColumnsToContents()
                table.itemChanged.connect(lambda: self.change_table_cell_value(active_table=table, tab_widget=tab))
                table.itemChanged.connect(table.resizeColumnsToContents)
                table.itemChanged.connect(table.resizeRowsToContents)

    def show_warning(self, title: str, text: str):
        warning = QtWidgets.QMessageBox()
        warning.setWindowTitle(title)
        warning.setText(text)
        warning.setIcon(warning.Warning)
        warning.setStandardButtons(warning.Ok)
        warning.exec()

    def add_tab_button(self, tab_widget: QtWidgets.QTabWidget, tables: Dict[str, QtWidgets.QTableWidget]):
        text, result = QtWidgets.QInputDialog.getText(self, "Добавление листа", "Введите название листа")
        while not text or tables.get(text):
            if not result:
                return
            self.show_warning(title="Ошибка добавления листа", text="Название листа пустое или существует!")
            text, result = QtWidgets.QInputDialog.getText(self, "Добавление листа", "Введите название листа")

        tab_to_create = QtWidgets.QWidget()
        tab_to_create.setObjectName(text)
        tables[text] = QtWidgets.QTableWidget(tab_to_create)
        tables[text].setGeometry(QtCore.QRect(-10, -10, 861, 901))
        tables[text].setObjectName(text)
        tables[text].setColumnCount(0)
        tables[text].setRowCount(0)
        tab_widget.addTab(tab_to_create, text)
        tab_widget.setCurrentWidget(tab_to_create)
        table = tables[text]
        table.itemChanged.connect(lambda: self.change_table_cell_value(active_table=table, tab_widget=tab_to_create))
        table.itemChanged.connect(table.resizeColumnsToContents)
        table.itemChanged.connect(table.resizeRowsToContents)

    def add_row_button(self, tab_widget: QtWidgets.QTabWidget, tables: Dict[str, QtWidgets.QTableWidget]):
        active_tab = tab_widget.currentWidget()
        if not active_tab:
            self.show_warning(title="Ошибка добавления ячеек", text="Сначала добавьте лист!")
            return

        table_name = active_tab.objectName()
        current_table = tables[table_name]
        current_table.insertRow(current_table.rowCount())

    def add_column_button(self, tab_widget: QtWidgets.QTabWidget, tables: Dict[str, QtWidgets.QTableWidget]):
        active_tab = tab_widget.currentWidget()
        if not active_tab:
            self.show_warning(title="Ошибка добавления ячеек", text="Сначала добавьте лист!")
            return

        table_name = active_tab.objectName()
        current_table = tables[table_name]
        current_table.insertColumn(current_table.columnCount())

    def change_table_cell_value(self, active_table: QtWidgets.QTableWidget, tab_widget: QtWidgets.QWidget, ):
        opened_files: Dict[str, openpyxl.Workbook] = (
            self.opened_load if tab_widget.parent().objectName() == self.LoadTabs.objectName() else self.opened_teachers
        )
        current_item = active_table.currentItem()
        if " -> " in active_table.objectName():
            file_name, sheet_name = active_table.objectName().split(" -> ")
            current_temp_file_path = os.path.join(self.work_dir, file_name)
            current_workbook = opened_files[current_temp_file_path]

        try:
            if current_item.text() != sympy.sympify(current_item.text()):
                current_item.setText(str(sympy.sympify(current_item.text())))
        except:
            pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
