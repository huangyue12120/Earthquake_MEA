from MainMenu import *
from Transform import *
from newTQCS import *
from Gaussian import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Tra_Dialog()
        self.child.setupUi(self)
class child_childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = New_Dialog()
        self.child.setupUi(self)

class childWindow_2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Gau_Dialog()
        self.child.setupUi(self)
