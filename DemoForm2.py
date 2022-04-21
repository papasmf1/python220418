# DemoForm2.py 
# DemoForm2.ui(화면을 디자인) + DemoForm2.py(로직을 구현)
import sys
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버와 통신
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup


#화면을 로딩(DemoForm2.ui)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드(시그널을 처리)
    def firstClick(self):
        #파일에 저장
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
        #페이지 번호를 생성
        for i in range(1,6): 
            #웹서버에 요청
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print(url)
            data = urllib.request.urlopen(url)
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")

            for item in cartoons:
                title = item.find("a").text 
                print(title.strip())
                f.write(title + "\n")
        f.close() 
        self.label.setText("네이버 웹툰 크롤링 종료~~")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 클릭을 클릭했습니다.")

#직접 모듈을 실행했는지 체크
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show()
app.exec_() 
