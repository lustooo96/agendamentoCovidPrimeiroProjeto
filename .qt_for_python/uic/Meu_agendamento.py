# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\renne\Desktop\Python\Meu_agendamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 759)
        MainWindow.setStyleSheet("background-image: url(teste.jpg);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(450, 210, 411, 81))
        self.frame.setStyleSheet("\n"
"QFrame{\n"
"background:#333;\n"
"border-radius-left:15px;\n"
"border-bottom:5px solid white;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 30, 321, 31))
        self.label.setStyleSheet("QLabel{\n"
"\n"
"color:white;\n"
"border:none;\n"
" font-size:22px;\n"
" font-family:century gothic;\n"
"}")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(450, 290, 411, 371))
        self.frame_2.setStyleSheet("\n"
"QFrame{\n"
"background:#333;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_logout_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_logout_2.setGeometry(QtCore.QRect(60, 320, 75, 31))
        self.pushButton_logout_2.setStyleSheet("QPushButton{\n"
"background:#333;\n"
"border:3px;\n"
"font-size:13px;\n"
"font-family:century gothic;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:1px solid rgb(93, 93, 93)\n"
"\n"
"}")
        self.pushButton_logout_2.setObjectName("pushButton_logout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(200, 320, 61, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 56, 17)\n"
"font: 8pt \"MS Sans Serif\";\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:1px solid rgb(229, 231, 66);\n"
"\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 421, 121))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MEU AGENDAMENTO"))
        self.pushButton_logout_2.setText(_translate("MainWindow", "VOLTAR"))
        self.pushButton.setText(_translate("MainWindow", "EXCLUIR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Estado"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cidade"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Endereço"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dia/Hora"))
