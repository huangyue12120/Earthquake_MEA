# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newTQCS.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class New_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(327, 261)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 72, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 72, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 72, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 72, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 72, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 70, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 100, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 130, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 160, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "    a"))
        self.label_2.setText(_translate("Dialog", "    b"))
        self.label_3.setText(_translate("Dialog", "    c"))
        self.label_4.setText(_translate("Dialog", "    e"))
        self.label_5.setText(_translate("Dialog", "    e\""))
        self.pushButton.setText(_translate("Dialog", "保存"))

    def save(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        e = self.lineEdit_4.text()
        ep = self.lineEdit_5.text()
        arr = []
        arr.append(a)
        arr.append(b)
        arr.append(c)
        arr.append(e)
        arr.append(ep)
        with open("save.txt", mode="w") as f:
            f.write(str(arr))
