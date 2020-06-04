# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_manager_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(690, 620)
        self.Folder_List = QtWidgets.QListWidget(Form)
        self.Folder_List.setGeometry(QtCore.QRect(20, 70, 651, 521))
        self.Folder_List.setObjectName("Folder_List_2")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 651, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Folder_Choose_Lay = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Folder_Choose_Lay.setContentsMargins(0, 0, 0, 0)
        self.Folder_Choose_Lay.setObjectName("Folder_Choose_Lay")
        self.Folder_Back = QtWidgets.QToolButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../.designer/backup/Icons/Folder_Back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Folder_Back.setIcon(icon)
        self.Folder_Back.setObjectName("Folder_Back")
        self.Folder_Choose_Lay.addWidget(self.Folder_Back)
        self.Folder_Change = QtWidgets.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../.designer/backup/Icons/Folder_Change.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Folder_Change.setIcon(icon1)
        self.Folder_Change.setObjectName("Folder_Change")
        self.Folder_Choose_Lay.addWidget(self.Folder_Change)
        self.Folder_Refresh = QtWidgets.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../.designer/backup/Icons/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Folder_Refresh.setIcon(icon2)
        self.Folder_Refresh.setObjectName("Folder_Refresh")
        self.Folder_Choose_Lay.addWidget(self.Folder_Refresh)
        self.Folder_Path = QtWidgets.QLineEdit(self.layoutWidget)
        self.Folder_Path.setText("")
        self.Folder_Path.setObjectName("Folder_Path")
        self.Folder_Choose_Lay.addWidget(self.Folder_Path)
        self.Folder_Path_Go = QtWidgets.QToolButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../.designer/backup/Icons/Folder_Go.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Folder_Path_Go.setIcon(icon3)
        self.Folder_Path_Go.setObjectName("Folder_Path_Go")
        self.Folder_Choose_Lay.addWidget(self.Folder_Path_Go)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Folder_Back.setText(_translate("Form", "..."))
        self.Folder_Change.setText(_translate("Form", "..."))
        self.Folder_Refresh.setText(_translate("Form", "..."))
        self.Folder_Path_Go.setText(_translate("Form", "..."))
