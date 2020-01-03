# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gaussian.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import math
import re
from PyQt5 import QtCore, QtGui, QtWidgets

class Gau_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 407)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 300, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(220, 80, 131, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 150, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 160, 201, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 491, 21))
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 181, 21))
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 80, 181, 21))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 340, 2000, 21))
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(30, 120, 181, 21))
        self.label_12.setObjectName("label_12")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(220, 120, 131, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 260, 171, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 230, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 260, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(340, 200, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 200, 171, 21))
        self.label.setObjectName("label")
        self.comboBox.activated.connect(self.choose_2)
        self.comboBox_2.activated.connect(self.choose_3)
        self.pushButton.clicked.connect(self.calculate)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "高斯投影正反算"))
        self.pushButton.setText(_translate("Dialog", "计算"))
        self.comboBox.setItemText(0, _translate("Dialog", "高斯投影正算"))
        self.comboBox.setItemText(1, _translate("Dialog", "高斯投影反算"))
        self.pushButton_2.setText(_translate("Dialog", "自定义参数"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "克拉索夫斯基椭球参数"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "IUGG_1975椭球参数"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "CGCS_2000椭球参数"))
        self.label_8.setText(_translate("Dialog", "请选择需要转换的坐标系，并输入已知信息"))
        self.label_13.setText(_translate("Dialog", "选择使用的椭球参数："))
        self.label_7.setText(_translate("Dialog", "计算方法："))
        self.label_9.setText(_translate("Dialog", "转换后结果为："))
        self.label_12.setText(_translate("Dialog", "高斯分带度数："))
        self.comboBox_3.setItemText(0, _translate("Dialog", "3°"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "6°"))
        self.label_3.setText(_translate("Dialog", "在此处输入无效！"))
        self.label_2.setText(_translate("Dialog", "B(输入格式为xx'xx'xx')"))
        self.label.setText(_translate("Dialog", "L(输入格式为xx'xx'xx')"))

    def choose_2(self):
        text = self.comboBox.currentText()
        if text == "高斯投影正算":
            self.label.setText("L(输入格式为xx'xx'xx')")
            self.label_2.setText("B(输入格式为xx'xx'xx')")
        elif text == "高斯投影反算":
            self.label.setText("x")
            self.label_2.setText("y")
            self.label_3.setText("Y")



    def choose_3(self):
        text = self.comboBox_2.currentText()
        if text == "克拉索夫斯基椭球参数":
            return 6378245.0, 6356863.0188, 6399698.9018, 0.00669342162297, 0.00673852541468
        elif text == "IUGG_1975椭球参数":
            return 6378140.0, 6356755.2882, 6399596.6520, 0.00669438499959, 0.00673950181947
        elif text == "CGCS_2000椭球参数":
            return 6378137.0, 6356752.3141, 6399593.6259, 0.00669438002290, 0.00673949677547
        elif text == "自定义椭球参数":
            with open("save.txt") as f:
                a = f.read()
                arr = re.compile(r"\d+").findall(a)
                a = float(str(arr[0]).replace('\"', ''))
                b = float(str(arr[1]).replace('\"', ''))
                c = float(str(arr[2]).replace('\"', ''))
                e = float(str(arr[3]).replace('\"', ''))
                ep = float(str(arr[4]).replace('\"', ''))
            return a, b, c, e, ep

    def RAD(self, d, f, m):
        PI = 3.1415926
        if d < 0.0:
            sign = -1.0
        else:
            sign = 1.0
        print(sign)
        if d < 0:
            d = d * (-1.0)
        if f < 0:
            f = f * (-1.0)
        if m < 0:
            m = m * (-1.0)
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

    def ZS_3(self, a, e, ep):
        PI = 3.1415926
        L = re.compile(r"\d+").findall(self.lineEdit.text())
        L1 = self.RAD(float(L[0]), float(L[1]), float(L[2]))
        B = re.compile(r"\d+").findall(self.lineEdit_2.text())
        B1 = self.RAD(float(B[0]), float(B[1]), float(B[2]))
        At =float(1 + 3 * e / 4 + 45 * e * e / 64 + 175 * e * e * e / 256)
        Bt =float(3 * e / 4 + 15 * e * e / 16 + 525 * e * e * e / 512)
        Ct =float(15 * e * e / 64 + 105 * e * e * e / 256)
        Dt =float(35 * e * e * e / 512)
        X = float(a * (1 - e) * (At * B1 - Bt * math.sin(2 * B1) / 2 + Ct * math.sin(4 * B1) / 4 - Dt * math.sin(6 * B1) / 6))
        W = float(math.sqrt(1 - e * math.sin(B1) * math.sin(B1)))
        N = float(a / W)
        n = float(math.sqrt(ep) * math.cos(B1))
        t = float(math.tan(B1))
        DH3 = (L1 - (1.5 * PI / 180)) / (3 * PI / 180) + 1
        L03 = DH3 * (3 * PI / 180)
        l3 = L1 - L03
        m3 = math.cos(B1) * l3
        x3 = X + N * t * (m3 * m3 / 2 + (5 - t * t + 9 * n * n + 4 * n * n * n * n) * m3 * m3 * m3 * m3 / 24 + (
                    61 - 58 * t * t + t * t * t * t) * m3 * m3 * m3 * m3 * m3 * m3 / 720)
        y3 = N * (m3 + (1 - t * t + n * n) * m3 * m3 * m3 / 6 + (
                    5 - 18 * t * t + t * t * t * t + 14 * n * n - 58 * n * n * t * t) * m3 * m3 * m3 * m3 * m3 / 120)
        Y3 = DH3 * 1000000 + 500000 + y3
        self.label_9.setText("转换后结果为：纵坐标x={}, 横坐标y={}, 通用坐标Y={}".format(x3, y3, Y3))

    def ZS_6(self, a, e, ep):
        PI = 3.1415926
        L = re.compile(r"\d+").findall(self.lineEdit.text())
        L1 = self.RAD(float(L[0]), float(L[1]), float(L[2]))
        B = re.compile(r"\d+").findall(self.lineEdit_2.text())
        B1 = self.RAD(float(B[0]), float(B[1]), float(B[2]))
        At = float(1 + 3 * e / 4 + 45 * e * e / 64 + 175 * e * e * e / 256)
        Bt = float(3 * e / 4 + 15 * e * e / 16 + 525 * e * e * e / 512)
        Ct = float(15 * e * e / 64 + 105 * e * e * e / 256)
        Dt = float(35 * e * e * e / 512)
        X = float(
            a * (1 - e) * (At * B1 - Bt * math.sin(2 * B1) / 2 + Ct * math.sin(4 * B1) / 4 - Dt * math.sin(6 * B1) / 6))
        W = float(math.sqrt(1 - e * math.sin(B1) * math.sin(B1)))
        N = float(a / W)
        n = float(math.sqrt(ep) * math.cos(B1))
        t = float(math.tan(B1))
        DH6 = L1 / (6 * PI / 180) + 1
        L06 = DH6 * (6 * PI / 180) - (3 * PI / 180)
        l6 = L1 - L06
        m6 = math.cos(B1) * l6
        x6 = X + N * t * (m6 * m6 / 2 + (5 - t * t + 9 * n * n + 4 * n * n * n * n) * m6 * m6 * m6 * m6 / 24 + (61 - 58 * t * t + t * t * t * t) * m6 * m6 * m6 * m6 * m6 * m6 / 720)
        y6 = N * (m6 + (1 - t * t + n * n) * m6 * m6 * m6 / 6 + (5 - 18 * t * t + t * t * t * t + 14 * n * n - 58 * n * n * t * t) * m6 * m6 * m6 * m6 * m6 / 120)
        Y6 = DH6 * 1000000 + 500000 + y6
        self.label_9.setText("转换后结果为：纵坐标x={}, 横坐标y={}, 通用坐标Y={}".format(x6, y6, Y6))

    def FS_3(self, a, c, e, ep):
        PI = 3.1415926
        x = float(self.lineEdit.text())
        y = float(self.lineEdit_2.text())
        Y = float(self.lineEdit_3.text())
        At = float(1 + 3 * e / 4 + 45 * e * e / 64 + 175 * e * e * e / 256)
        Bt = float(3 * e / 4 + 15 * e * e / 16 + 525 * e * e * e / 512)
        Ct = float(15 * e * e / 64 + 105 * e * e * e / 256)
        Dt = float(35 * e * e * e / 512)
        B0 = x / (a * (1 - e) * At)
        B1 = (x - a * (1 - e) * (-Bt * math.sin(2 * B0) / 2 + Ct * math.sin(4 * B0) / 4 - Dt * math.sin(6 * B0) / 6)) / (a * (1 - e) * At)
        while math.fabs(B1 - B0) > 1 * pow(10, -8):
            B0 = B1
            B1 = (x - a * (1 - e) * (-Bt * math.sin(2 * B0) / 2 + Ct * math.sin(4 * B0) / 4 - Dt * math.sin(6 * B0) / 6)) / (a * (1 - e) * At)
        Bf = float(B1)
        nf = float(math.sqrt(ep) * math.cos(Bf))
        tf = float(math.tan(Bf))
        Vf = float(math.sqrt(1 + ep * math.cos(Bf) * math.cos(Bf)))
        Nf = float(c / Vf)
        B = float(Bf - Vf * Vf * tf / 2 * ((y / Nf) * (y / Nf) - (5 + 3 * tf * tf + nf * nf - 9 * nf * nf * tf * tf) * pow((y / Nf),4) / 12 + (61 + 90 * tf * tf + 45 * tf * tf) * pow((y / Nf), 6) / 360))
        L = float(((y / Nf) - (1 + 2 * tf * tf + nf * nf) * (y / Nf) * (y / Nf) * (y / Nf) / 6 + (5 + 28 * tf * tf + 24 * pow(tf, 4) + 6 * nf * nf + 8 * nf * nf * tf * tf) * pow((y / Nf),5) / 120) / math.cos(Bf))
        DH = float(Y) / 1000000
        L3 = 3 * PI / 180 * float(DH) + L
        self.label_9.setText("转换后结果为：大地维度B={}, 大地经度L={}".format(self.RBD(B), self.RBD(L3)))
    def FS_6(self, a, c, e, ep):
        PI = 3.1415926
        x = float(self.lineEdit.text())
        y = float(self.lineEdit_2.text())
        Y = float(self.lineEdit_3.text())
        At = float(1 + 3 * e / 4 + 45 * e * e / 64 + 175 * e * e * e / 256)
        Bt = float(3 * e / 4 + 15 * e * e / 16 + 525 * e * e * e / 512)
        Ct = float(15 * e * e / 64 + 105 * e * e * e / 256)
        Dt = float(35 * e * e * e / 512)
        B0 = x / (a * (1 - e) * At)
        B1 = (x - a * (1 - e) * (-Bt * math.sin(2 * B0) / 2 + Ct * math.sin(4 * B0) / 4 - Dt * math.sin(6 * B0) / 6)) / (a * (1 - e) * At)
        while math.fabs(B1 - B0) > 1 * pow(10, -8):
            B0 = B1
            B1 = (x - a * (1 - e) * (-Bt * math.sin(2 * B0) / 2 + Ct * math.sin(4 * B0) / 4 - Dt * math.sin(6 * B0) / 6)) / (a * (1 - e) * At)
        Bf = float(B1)
        nf = float(math.sqrt(ep) * math.cos(Bf))
        tf = float(math.tan(Bf))
        Vf = float(math.sqrt(1 + ep * math.cos(Bf) * math.cos(Bf)))
        Nf = float(c / Vf)
        B = float(Bf - Vf * Vf * tf / 2 * ((y / Nf) * (y / Nf) - (5 + 3 * tf * tf + nf * nf - 9 * nf * nf * tf * tf) * pow((y / Nf),4) / 12 + (61 + 90 * tf * tf + 45 * tf * tf) * pow((y / Nf), 6) / 360))
        L = float(((y / Nf) - (1 + 2 * tf * tf + nf * nf) * (y / Nf) * (y / Nf) * (y / Nf) / 6 + (5 + 28 * tf * tf + 24 * pow(tf, 4) + 6 * nf * nf + 8 * nf * nf * tf * tf) * pow((y / Nf),5) / 120) / math.cos(Bf))
        DH = float(Y) / 1000000
        L6 = 6 * PI / 180 * float(DH) - 3 * PI / 180 + L
        self.label_9.setText("转换后结果为：大地维度B={}, 大地经度L={}".format(self.RBD(B), self.RBD(L6)))

    def calculate(self):
        arr = self.choose_3()
        a = arr[0]
        c = arr[2]
        e = arr[3]
        ep = arr[4]
        text_1 = self.comboBox.currentText()
        text_3 = self.comboBox_3.currentText()
        if text_1 == "高斯投影正算":
            if text_3 == "3°":
                self.ZS_3(a, e, ep)
            elif text_3 == "6°":
                self.ZS_6(a, e, ep)
        elif text_1 == "高斯投影反算":
            if text_3 == "3°":
                self.FS_3(a, c, e, ep)
            elif text_3 == "6°":
                self.FS_6(a, c, e, ep)

