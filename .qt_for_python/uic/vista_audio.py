# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Dorian\Desktop\audio\vista_audio.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Adelante = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Adelante.setGeometry(QtCore.QRect(20, 70, 131, 51))
        self.pushButton_Adelante.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Adelante.setObjectName("pushButton_Adelante")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 531, 31))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton_Atras = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Atras.setGeometry(QtCore.QRect(170, 70, 131, 51))
        self.pushButton_Atras.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Atras.setObjectName("pushButton_Atras")
        self.pushButton_Izquierda = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Izquierda.setGeometry(QtCore.QRect(320, 70, 131, 51))
        self.pushButton_Izquierda.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Izquierda.setObjectName("pushButton_Izquierda")
        self.pushButton_Alto = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Alto.setGeometry(QtCore.QRect(420, 150, 131, 51))
        self.pushButton_Alto.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Alto.setObjectName("pushButton_Alto")
        self.pushButton_Derecha = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Derecha.setGeometry(QtCore.QRect(470, 70, 131, 51))
        self.pushButton_Derecha.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Derecha.setObjectName("pushButton_Derecha")
        self.pushButton_Acelera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Acelera.setGeometry(QtCore.QRect(60, 150, 131, 51))
        self.pushButton_Acelera.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Acelera.setObjectName("pushButton_Acelera")
        self.pushButton_Disminuye = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Disminuye.setGeometry(QtCore.QRect(230, 150, 151, 51))
        self.pushButton_Disminuye.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Disminuye.setObjectName("pushButton_Disminuye")
        self.pushButton_Intermitentes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Intermitentes.setGeometry(QtCore.QRect(230, 230, 171, 51))
        self.pushButton_Intermitentes.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Intermitentes.setObjectName("pushButton_Intermitentes")
        self.pushButton_Luz_Alta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Luz_Alta.setGeometry(QtCore.QRect(20, 230, 191, 51))
        self.pushButton_Luz_Alta.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Luz_Alta.setObjectName("pushButton_Luz_Alta")
        self.pushButton_Luz_Baja = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Luz_Baja.setGeometry(QtCore.QRect(410, 230, 191, 51))
        self.pushButton_Luz_Baja.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Luz_Baja.setObjectName("pushButton_Luz_Baja")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 311, 41))
        self.label_2.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_Iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Iniciar.setGeometry(QtCore.QRect(440, 320, 161, 41))
        self.pushButton_Iniciar.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_Iniciar.setObjectName("pushButton_Iniciar")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 320, 81, 41))
        self.lineEdit.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
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
        self.pushButton_Adelante.setText(_translate("MainWindow", "Adelante"))
        self.label.setText(_translate("MainWindow", "Grabar Audio para los siguientes comandos:"))
        self.pushButton_Atras.setText(_translate("MainWindow", "Atras"))
        self.pushButton_Izquierda.setText(_translate("MainWindow", "Izquierda"))
        self.pushButton_Alto.setText(_translate("MainWindow", "Alto"))
        self.pushButton_Derecha.setText(_translate("MainWindow", "Derecha"))
        self.pushButton_Acelera.setText(_translate("MainWindow", "Acelera"))
        self.pushButton_Disminuye.setText(_translate("MainWindow", "Disminuye"))
        self.pushButton_Intermitentes.setText(_translate("MainWindow", "Intermitentes"))
        self.pushButton_Luz_Alta.setText(_translate("MainWindow", "Luz Alta"))
        self.pushButton_Luz_Baja.setText(_translate("MainWindow", "Luz Baja"))
        self.label_2.setText(_translate("MainWindow", "No. de Iteraciones de NN:"))
        self.pushButton_Iniciar.setText(_translate("MainWindow", "Iniciar NN"))
        self.lineEdit.setText(_translate("MainWindow", "20"))