# DemoForm.py 
# DemoForm.ui(화면을 디자인) + DemoForm.py(로직을 구현)
import sys
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#화면을 로딩
form_class = uic.loadUiType("c:\\work\\DemoForm.ui")[0]

#윈도우 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")

#직접 모듈을 실행했는지 체크
# if __name__ == "__main__":
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show()
app.exec_() 
