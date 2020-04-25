# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_manager.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 796)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 796))
        MainWindow.setMaximumSize(QtCore.QSize(700, 796))
        self.File_Manager_Widget = QtWidgets.QWidget(MainWindow)
        self.File_Manager_Widget.setObjectName("File_Manager_Widget")
        self.layoutWidget = QtWidgets.QWidget(self.File_Manager_Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 651, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Folder_Choose_Lay = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Folder_Choose_Lay.setContentsMargins(0, 0, 0, 0)
        self.Folder_Choose_Lay.setObjectName("Folder_Choose_Lay")
        self.Folder_Back = QtWidgets.QToolButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/r31n3/Рабочий стол/PSU_Unallocated_Load/UI/File_Manager/Icons/Folder_Back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Folder_Back.setIcon(icon)
        self.Folder_Back.setObjectName("Folder_Back")
        self.Folder_Choose_Lay.addWidget(self.Folder_Back)
        self.Folder_Change = QtWidgets.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/r31n3/Рабочий стол/PSU_Unallocated_Load/UI/File_Manager/Icons/Folder_Change.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Folder_Change.setIcon(icon1)
        self.Folder_Change.setObjectName("Folder_Change")
        self.Folder_Choose_Lay.addWidget(self.Folder_Change)
        self.Folder_Refresh = QtWidgets.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/r31n3/Рабочий стол/PSU_Unallocated_Load/UI/File_Manager/Icons/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Folder_Refresh.setIcon(icon2)
        self.Folder_Refresh.setObjectName("Folder_Refresh")
        self.Folder_Choose_Lay.addWidget(self.Folder_Refresh)
        self.Folder_Path = QtWidgets.QLineEdit(self.layoutWidget)
        self.Folder_Path.setText("")
        self.Folder_Path.setObjectName("Folder_Path")
        self.Folder_Choose_Lay.addWidget(self.Folder_Path)
        self.Folder_Path_Go = QtWidgets.QToolButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/r31n3/Рабочий стол/PSU_Unallocated_Load/UI/File_Manager/Icons/Folder_Go.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Folder_Path_Go.setIcon(icon3)
        self.Folder_Path_Go.setObjectName("Folder_Path_Go")
        self.Folder_Choose_Lay.addWidget(self.Folder_Path_Go)
        self.layoutWidget1 = QtWidgets.QWidget(self.File_Manager_Widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(21, 70, 651, 701))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Folder_List_Lay = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.Folder_List_Lay.setContentsMargins(0, 0, 0, 0)
        self.Folder_List_Lay.setObjectName("Folder_List_Lay")
        self.Folder_List = QtWidgets.QListWidget(self.layoutWidget1)
        self.Folder_List.setObjectName("Folder_List")
        self.Folder_List_Lay.addWidget(self.Folder_List)
        self.Folder_Scroll = QtWidgets.QScrollBar(self.layoutWidget1)
        self.Folder_Scroll.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Folder_Scroll.setOrientation(QtCore.Qt.Vertical)
        self.Folder_Scroll.setObjectName("Folder_Scroll")
        self.Folder_List_Lay.addWidget(self.Folder_Scroll)
        MainWindow.setCentralWidget(self.File_Manager_Widget)

        self.retranslateUi(MainWindow)
        self.Folder_Scroll.sliderMoved['int'].connect(self.Folder_List.scrollToTop)
        self.Folder_Scroll.sliderMoved['int'].connect(self.Folder_List.scrollToBottom)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Folder_Back.setText(_translate("MainWindow", "..."))
        self.Folder_Change.setText(_translate("MainWindow", "..."))
        self.Folder_Refresh.setText(_translate("MainWindow", "..."))
        self.Folder_Path_Go.setText(_translate("MainWindow", "..."))
