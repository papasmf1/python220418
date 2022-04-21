# DemoForm2.py 
# DemoForm2.ui(화면을 디자인) + DemoForm2.py(로직을 구현)
import sys
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#화면을 로딩(DemoForm2.ui)
form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]

#윈도우 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드(시그널을 처리)
    def firstClick(self):
        self.label.setText("첫번째 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 클릭을 클릭했습니다.")

#직접 모듈을 실행했는지 체크
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show()
app.exec_() 
