# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Transform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import re
import math
import P_C
from PyQt5 import QtCore, QtGui, QtWidgets

class Tra_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(537, 352)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 160, 171, 21))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 190, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 80, 181, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 220, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 300, 151, 21))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(250, 300, 21, 21))
        self.label_11.setObjectName("label_11")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(190, 300, 51, 21))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(450, 300, 21, 21))
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(280, 300, 61, 21))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(220, 80, 131, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("大地坐标系")
        self.comboBox.addItem("空间直角坐标系")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 491, 21))
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 190, 171, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(340, 160, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(381, 300, 61, 21))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(350, 300, 21, 21))
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 220, 171, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 120, 201, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("克拉索夫斯基椭球参数")
        self.comboBox_2.addItem("IUGG_1975椭球参数")
        self.comboBox_2.addItem("CGCS_2000椭球参数")
        self.comboBox_2.addItem("自定义椭球参数")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(30, 120, 181, 21))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 110, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox.activated.connect(self.choose)
        self.comboBox_2.activated.connect(self.choose_1)
        self.pushButton.clicked.connect(self.Transform)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "坐标系转换"))
        self.label.setText(_translate("Dialog", "X"))
        self.pushButton.setText(_translate("Dialog", "转换"))
        self.label_7.setText(_translate("Dialog", "选择需要转换的坐标系："))
        self.label_9.setText(_translate("Dialog", "转换后结果为：    （"))
        self.label_11.setText(_translate("Dialog", "，"))
        self.label_10.setText(_translate("Dialog", "）"))
        self.comboBox.setItemText(0, _translate("Dialog", "大地坐标系"))
        self.comboBox.setItemText(1, _translate("Dialog", "空间直角坐标系"))
        self.label_8.setText(_translate("Dialog", "请选择需要转换的坐标系，并输入已知信息"))
        self.label_2.setText(_translate("Dialog", "Y"))
        self.label_12.setText(_translate("Dialog", "，"))
        self.label_3.setText(_translate("Dialog", "Z"))
        self.pushButton_2.setText(_translate("Dialog", "自定义参数"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "克拉索夫斯基椭球参数"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "IUGG_1975椭球参数"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "CGCS_2000椭球参数"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "自定义椭球参数"))
        self.label_13.setText(_translate("Dialog", "选择使用的椭球参数："))

    def RAD(self, d, f, m):
        PI = 3.1415926
        if d < 0.0:
            sign = -1.0
        else:
            sign = 1.0
        print(sign)
        if d < 0:
            d = d * (-1.0)
            print(d)
        if f < 0:
            f = f * (-1.0)
            print(f)
        if m < 0:
            m = m * (-1.0)
            print(m)
        e = sign * (d * 3600 + f * 60 + m) * PI / (3600 * 180)
        print(e)
        return e

    def RBD(self, hd):
        PI = 3.1415926
        if hd < 0.0:
            sign = -1.0
        else:
            sign = 1.0
        if hd < 0:
            hd = math.fabs(hd)
        hd = hd * 3600 * 180 / PI
        t = int(hd / 3600)
        d = sign * t
        hd = hd - t * 3600
        f = int(hd / 60)
        m = hd - f * 60
        return "{}'{}'{}'".format(d, f, m)

    def choose(self):
        a = self.comboBox.currentText()
        if a == "大地坐标系":
            self.label.setText("X")
            self.label_2.setText("Y")
            self.label_3.setText("Z")
        elif a == "空间直角坐标系":
            self.label.setText("L(输入格式为xx'xx'xx')")
            self.label_2.setText("B(输入格式为xx'xx'xx')")
            self.label_3.setText("H")

    def choose_1(self):
        a = self.comboBox_2.currentText()
        arr = []
        if a == "克拉索夫斯基椭球参数":
            return 6378245.0, 6356863.0188, 6399698.9018, 0.00669342162297, 0.00673852541468
        elif a == "IUGG_1975椭球参数":
            return 6378140.0, 6356755.2882, 6399596.6520, 0.00669438499959, 0.00673950181947
        elif a == "CGCS_2000椭球参数":
            return 6378137.0, 6356752.3141, 6399593.6259, 0.00669438002290, 0.00673949677547
        elif a == "自定义椭球参数":
            with open("save.txt") as f:
                a = f.read()
                arr = re.compile(r"\d+").findall(a)
                a = float(str(arr[0]).replace('\"', ''))
                b = float(str(arr[1]).replace('\"', ''))
                c = float(str(arr[2]).replace('\"', ''))
                e = float(str(arr[3]).replace('\"', ''))
                ep = float(str(arr[4]).replace('\"', ''))
            return a, b, c, e, ep





    def Transform(self):
        text = self.comboBox.currentText()
        if text == "大地坐标系":
            arr = self.choose_1()
            a = arr[0]
            e2 = arr[3]
            X = int(self.lineEdit.text())
            Y = int(self.lineEdit_2.text())
            Z = int(self.lineEdit_3.text())
            L = math.atan(Y/X)
            L1 = self.RBD(L)
            tgB0 = Z / math.sqrt(X * X + Y * Y)
            tgB1 = (1 / math.sqrt(X * X + Y * Y)) * (Z + a * e2 * tgB0 / math.sqrt(1 + tgB0 * tgB0 - e2 * tgB0 * tgB0))
            while (math.fabs(tgB0 - tgB1) > 5 * pow(10, -10)):
                tgB0 = tgB1
                tgB1 = (1 / math.sqrt(X * X + Y * Y)) * (Z + a * e2 * tgB0 / math.sqrt(1 + tgB0 * tgB0 - e2 * tgB0 * tgB0))
            B = math.atan(tgB1)
            B1 = self.RBD(B)
            W = math.sqrt(1 - e2 * math.sin(B) * math.sin(B))
            N = a / W
            H = math.sqrt(X * X + Y * Y) / math.cos(B) - N
            self.label_4.setText("{}".format(H))
            self.label_5.setText("{}".format(B1))
            self.label_6.setText("{}".format(L1))
        elif text == "空间直角坐标系":
            arr = self.choose_1()
            a = float(arr[0])
            e2 = float(arr[3])
            L = re.compile(r"\d+").findall(self.lineEdit.text())
            L1 = self.RAD(float(L[0]), float(L[1]), float(L[2]))
            B = re.compile(r"\d+").findall(self.lineEdit_2.text())
            B1 = self.RAD(float(B[0]), float(B[1]), float(B[2]))
            W = math.sqrt(1 - e2 * math.sin(B1) * math.sin(B1))
            N = a / W
            H = self.lineEdit_3.text()
            X = (N + float(H)) * math.cos(B1) * math.cos(L1)
            Y = (N + float(H)) * math.cos(B1) * math.sin(L1)
            Z = (N * (1 - e2) + float(H)) * math.sin(B1)
            self.label_6.setText("{}".format(X))
            self.label_5.setText("{}".format(Y))
            self.label_4.setText("{}".format(Z))


