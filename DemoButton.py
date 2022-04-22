# DemoButton.py
#디자이너를 사용하지 않고 100% 맨땅에 헤딩하는 코드
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        #화면의 좌측상단(x, y)
        btn1.move(20, 20)
        #시그널과 슬롯메서드를 연결하는 코드 
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_() 