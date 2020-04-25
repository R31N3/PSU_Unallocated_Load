import sys, os
from typing import Dict
from pathlib import Path
from PyQt5 import QtWidgets, QtGui

import UI.File_Manager.file_manager as file_manager


class ListItem(QtWidgets.QListWidgetItem):
    def __init__(self, visible_text: str):
        super().__init__(visible_text)


class FileManager(QtWidgets.QMainWindow, file_manager.Ui_MainWindow):
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    file_manager = FileManager()
    file_manager.show()
    app.exec_()


if __name__ == '__main__':
    main()
