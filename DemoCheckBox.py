# DemoCheckBox.py
import sys
from PyQt5.QtWidgets import *

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.checkBox1 = QCheckBox("아이폰", self)
        self.checkBox1.move(10, 20)
        self.checkBox1.resize(150, 30)
        self.checkBox1.stateChanged.connect(self.checkBoxState)

        self.checkBox2 = QCheckBox("안드로이드폰", self)
        self.checkBox2.move(10, 50)
        self.checkBox2.resize(150, 30)
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        self.checkBox3 = QCheckBox("윈도우폰", self)
        self.checkBox3.move(10, 80)
        self.checkBox3.resize(150, 30)
        self.checkBox3.stateChanged.connect(self.checkBoxState)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self):
        msg = ""
        if self.checkBox1.isChecked() == True:
            msg += "아이폰 "
        if self.checkBox2.isChecked() == True:
            msg += "안드로이드폰 "
        if self.checkBox3.isChecked() == True:
            msg += "윈도우폰 "
        self.statusBar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_()