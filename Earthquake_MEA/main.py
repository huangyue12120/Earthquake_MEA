import P_C
import sys
import os

if __name__=='__main__':
    app = P_C.QApplication(sys.argv)
    window = P_C.parentWindow()
    child = P_C.childWindow()
    child_2 = P_C.childWindow_2()
    child_child = P_C.child_childWindow()
    btn1 = window.main_ui.pushButton
    btn2 = window.main_ui.pushButton_2
    btn3 = window.main_ui.pushButton_3
    child_btn1 = child.child.pushButton_2
    child_btn2 = child_2.child.pushButton_2
    child_btn1.clicked.connect(child_child.show)
    child_btn2.clicked.connect(child_child.show)
    btn1.clicked.connect(child.show)
    btn2.clicked.connect(child_2.show)
    btn3.clicked.connect(window.close)
    window.show()
    sys.exit(app.exec_())
