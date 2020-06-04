import sys, os, shutil
import openpyxl, datetime
from typing import Dict, List, Tuple
from pathlib import Path
from PyQt5 import QtWidgets, QtGui, QtCore

import UI.File_Manager.file_manager as file_manager
import UI.Main_Window.main_window as main_window


class ListItem(QtWidgets.QListWidgetItem):
    def __init__(self, visible_text: str):
        super().__init__(visible_text)


class FileManager(QtWidgets.QMainWindow, file_manager.Ui_Form):
    def __init__(self):

        super().__init__()

        # Переменные
        self.directory: str = Path.home().__str__()
        self.selected_files: list = []

        # Запуск
        self.setupUi(self)
        self.browse_folder()

        # Действия
        self.Folder_Change.clicked.connect(self.browse_folder)
        self.Folder_Refresh.clicked.connect(self.fill_list)
        self.Folder_Back.clicked.connect(self.browse_folder_down)
        self.Folder_Path_Go.clicked.connect(self.browse_folder_by_path)
        self.Folder_List.itemDoubleClicked['QListWidgetItem*'].connect(self.folder_double_click_event)

    def fill_list(self):
        self.Folder_List.clear()
        item_counter = 0
        for file_name in os.listdir(self.directory):
            self.Folder_List.addItem(file_name)
            if os.path.join(self.directory, file_name) in self.selected_files:
                self.Folder_List.item(item_counter).setBackground(QtGui.QColor("#7fc97f"))
            item_counter += 1

    def browse_folder(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите рабочую директорию")
        self.fill_list()

    def browse_folder_by_path(self):
        temp_old_directory = self.directory
        self.directory = self.Folder_Path.text()

        try:
            self.fill_list()
        except OSError:
            self.Folder_Path.setText("")
            self.directory = temp_old_directory
            self.fill_list()

    def browse_folder_down(self):
        self.directory = Path(self.directory).parent
        self.fill_list()

    def folder_double_click_event(self):
        current_item = ListItem(self.Folder_List.currentItem())
        item_path = os.path.join(self.directory, current_item.text())
        if os.path.isdir(item_path):
            self.directory = item_path
            self.fill_list()
        elif Path(item_path).suffix in [".xlsx", "xls"]:
            if item_path not in self.selected_files:
                self.selected_files.append(item_path)
                self.Folder_List.currentItem().setBackground(QtGui.QColor("#7fc97f"))
            else:
                self.selected_files.remove(item_path)
                self.Folder_List.currentItem().setBackground(QtGui.QColor("#ffffff"))


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Инициализация
        self.setupUi(self)

        # Переменные
        self.work_dir = os.getcwd()
        self.temp_dir = os.path.join(self.work_dir, "temp")
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)
        self.LoadTabs.addTab(None, "Test Tab")

        # selected List[Tuple[str, str]] - Path To File AND Filename to View
        self.selected_load: List[Tuple[str, str]] = []
        self.selected_teachers = []

        self.opened_load: Dict[str, openpyxl.Workbook] = {}
        self.opened_teachers: Dict[str, openpyxl.Workbook] = {}

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
            data_list=self.selected_load, opened_files=self.opened_load, table=self.tableWidget
        ))
        self.AddLoadRow.clicked.connect(lambda: self.tableWidget.insertRow(self.tableWidget.rowCount()))
        self.AddLoadColumn.clicked.connect(lambda: self.tableWidget.insertColumn(self.tableWidget.columnCount()))
        self.LoadTabs.addTab(widget=QtWidgets.QTabWidget())

        self.TeachersSelection.clicked.connect(lambda: self.selection_button(
            qlist=self.SelectedTeachers,
            data_list=self.selected_teachers
        ))
        self.SelectedTeachers.itemClicked['QListWidgetItem*'].connect(lambda: self.deletion_menu(
            data_list=self.selected_teachers,
            qlist=self.SelectedTeachers,
        ))
        self.RefreshTeachers.clicked.connect(lambda: self.refresh(
            data_list=self.selected_teachers, opened_files=self.opened_teachers, table=self.tableWidget_2
        ))
        self.AddTeachersRow.clicked.connect(lambda: self.tableWidget_2.insertRow(self.tableWidget_2.rowCount()))
        self.AddTeachersColumn.clicked.connect(lambda: self.tableWidget_2.insertColumn(self.tableWidget_2.columnCount()))

    def refresh(self, data_list: list, opened_files: Dict[str, openpyxl.Workbook], table: QtWidgets.QTableWidget):
        for load_file in data_list:
            file_name = load_file[0]
            target_temp_file = os.path.join(self.temp_dir, file_name)
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

    def deletion_from_list(self, data_list: list, qlist: QtWidgets.QListWidget):
        data_list.pop(qlist.indexFromItem(qlist.currentItem()).row())
        qlist.removeItemWidget(qlist.currentItem())
        self.fill_list(qlist=qlist, selected_files=data_list)

    def selection_button(self, data_list: list, qlist: QtWidgets.QListWidget):
        for selected_file in QtWidgets.QFileDialog.getOpenFileNames(
                self, "Выберите файлы", filter="Excel Files (*.xls *.xlsx)"
        )[0]:
            selected = (os.path.basename(selected_file), selected_file)
            if Path(selected_file).suffix in [".xlsx", ".xls"] and selected not in data_list:
                data_list.append(selected)

        self.fill_list(qlist=qlist, selected_files=data_list)

    def deletion_menu(self, data_list: list, qlist: QtWidgets.QListWidget):
        menu = QtWidgets.QMenu(qlist)
        menu.addAction("Удалить файл из списка")
        menu.triggered.connect(lambda: self.deletion_from_list(data_list=data_list, qlist=qlist))
        menu.exec_(QtGui.QCursor.pos())

    def fill_list(self, qlist: QtWidgets.QListWidget, selected_files):
        qlist.clear()
        for selected in selected_files:
            qlist.addItem(selected[0])


def main():
    app = QtWidgets.QApplication(sys.argv)
    # file_manager = FileManager()
    # file_manager.show()
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
