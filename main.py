import sys

from PyQt5.QtWidgets import QApplication

from main_functionality import UnallocatedLoadApplication


def main():
    app = QApplication(sys.argv)
    application_window = UnallocatedLoadApplication()
    application_window.show()
    app.exec_()


if __name__ == "__main__":
    main()
