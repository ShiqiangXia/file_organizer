# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(666, 443)
        font = QtGui.QFont()
        font.setPointSize(14)
        Window.setFont(font)
        self.moveFolderList = QtWidgets.QListWidget(Window)
        self.moveFolderList.setGeometry(QtCore.QRect(350, 190, 231, 231))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.moveFolderList.setFont(font)
        self.moveFolderList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.moveFolderList.setObjectName("moveFolderList")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(185, 212, 195))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.moveFolderList.addItem(item)
        self.infoText = QtWidgets.QPlainTextEdit(Window)
        self.infoText.setGeometry(QtCore.QRect(110, 70, 221, 61))
        self.infoText.setReadOnly(True)
        self.infoText.setObjectName("infoText")
        self.layoutWidget = QtWidgets.QWidget(Window)
        self.layoutWidget.setGeometry(QtCore.QRect(69, 20, 531, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.openBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.openBtn.setObjectName("openBtn")
        self.horizontalLayout_3.addWidget(self.openBtn)
        self.dirEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.dirEdit.setReadOnly(True)
        self.dirEdit.setPlaceholderText("")
        self.dirEdit.setObjectName("dirEdit")
        self.horizontalLayout_3.addWidget(self.dirEdit)
        self.layoutWidget1 = QtWidgets.QWidget(Window)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 390, 211, 33))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.renameBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.renameBtn.setObjectName("renameBtn")
        self.horizontalLayout_4.addWidget(self.renameBtn)
        self.renameEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.renameEdit.setPlaceholderText("")
        self.renameEdit.setObjectName("renameEdit")
        self.horizontalLayout_4.addWidget(self.renameEdit)
        self.picView = QtWidgets.QLabel(Window)
        self.picView.setGeometry(QtCore.QRect(130, 190, 171, 161))
        self.picView.setText("")
        self.picView.setPixmap(QtGui.QPixmap("images/txt_icon2.png"))
        self.picView.setScaledContents(True)
        self.picView.setObjectName("picView")
        self.layoutWidget2 = QtWidgets.QWidget(Window)
        self.layoutWidget2.setGeometry(QtCore.QRect(360, 140, 211, 33))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout_2.addWidget(self.deleteBtn)
        self.undoBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.undoBtn.setObjectName("undoBtn")
        self.horizontalLayout_2.addWidget(self.undoBtn)
        self.layoutWidget3 = QtWidgets.QWidget(Window)
        self.layoutWidget3.setGeometry(QtCore.QRect(120, 140, 221, 33))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.skipLeftBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.skipLeftBtn.setObjectName("skipLeftBtn")
        self.horizontalLayout_5.addWidget(self.skipLeftBtn)
        self.skipBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.skipBtn.setObjectName("skipBtn")
        self.horizontalLayout_5.addWidget(self.skipBtn)
        self.layoutWidget4 = QtWidgets.QWidget(Window)
        self.layoutWidget4.setGeometry(QtCore.QRect(360, 80, 211, 33))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startBtn = QtWidgets.QPushButton(self.layoutWidget4)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        self.doneBtn = QtWidgets.QPushButton(self.layoutWidget4)
        self.doneBtn.setObjectName("doneBtn")
        self.horizontalLayout.addWidget(self.doneBtn)
        self.layoutWidget5 = QtWidgets.QWidget(Window)
        self.layoutWidget5.setGeometry(QtCore.QRect(100, 350, 211, 33))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.previewBtn = QtWidgets.QPushButton(self.layoutWidget5)
        self.previewBtn.setObjectName("previewBtn")
        self.horizontalLayout_6.addWidget(self.previewBtn)
        self.fileNameLabel = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setWordWrap(True)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.horizontalLayout_6.addWidget(self.fileNameLabel)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Form"))
        __sortingEnabled = self.moveFolderList.isSortingEnabled()
        self.moveFolderList.setSortingEnabled(False)
        item = self.moveFolderList.item(0)
        item.setText(_translate("Window", "+ Add folder (double click)"))
        self.moveFolderList.setSortingEnabled(__sortingEnabled)
        self.infoText.setPlainText(_translate("Window", "Please [Open] folder.\n"
"Next click [Start]."))
        self.openBtn.setText(_translate("Window", "Open"))
        self.renameBtn.setText(_translate("Window", "Rename"))
        self.deleteBtn.setText(_translate("Window", "Delete"))
        self.undoBtn.setText(_translate("Window", "Undo"))
        self.skipLeftBtn.setText(_translate("Window", "<<"))
        self.skipBtn.setText(_translate("Window", ">>"))
        self.startBtn.setText(_translate("Window", "Start"))
        self.doneBtn.setText(_translate("Window", "Done"))
        self.previewBtn.setText(_translate("Window", "Preview"))
        self.fileNameLabel.setText(_translate("Window", "sample file.txt"))
