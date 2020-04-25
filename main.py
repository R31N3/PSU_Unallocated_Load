import sys, os
from pathlib import Path
from PyQt5 import QtWidgets

import UI.File_Manager.file_manager as file_manager


class FileManager(QtWidgets.QMainWindow, file_manager.Ui_MainWindow):
    def __init__(self):

        super().__init__()

        # Переменные
        self.directory = None

        # Запуск
        self.setupUi(self)
        self.browse_folder()

        # Действия
        self.Folder_Change.clicked.connect(self.browse_folder)
        self.Folder_Refresh.clicked.connect(self.fill_list)
        self.Folder_Back.clicked.connect(self.browse_folder_down)
        self.Folder_Path_Go.clicked.connect(self.browse_folder_by_path)

    def fill_list(self):
        self.Folder_List.clear()
        for file_name in os.listdir(self.directory):
            self.Folder_List.addItem(file_name)

    def browse_folder(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите рабочую директорию")
        self.fill_list()

    def browse_folder_by_path(self):
        temp_old_directory = self.directory
        self.directory = self.Folder_Path.text()

        try:
            self.fill_list()
        except:
            self.directory = temp_old_directory
            self.fill_list()

    def browse_folder_down(self):
        directory_path = Path(self.directory)

        self.directory = directory_path.parent
        self.fill_list()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FileManager()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()