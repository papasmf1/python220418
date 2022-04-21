import sys
from PyQt5.QtWidgets import *
import urllib.request
from bs4 import BeautifulSoup
import webbrowser   #브라우저로 넘기는 경우 
import re 

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #창의 시작위치와 폭, 높이(x,y,width,height) 
        self.setGeometry(200, 200, 800, 800)
        
        #입력 텍스트 
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(20, 20)

        #버튼
        self.btn = QPushButton("검색", self)
        self.btn.move(120, 20)
        self.btn.clicked.connect(self.setTableWidgetData)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(20, 70)
        self.tableWidget.resize(800, 600)
        self.tableWidget.setRowCount(50)  #행의 갯수 
        self.tableWidget.setColumnCount(2)  #컬럼의 갯수 
        #컬럼의 폭을 지정한다. 0번 1번 
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 300)
        
        #self.setTableWidgetData()
        self.tableWidget.doubleClicked.connect(self.doubleClicked)

    def setTableWidgetData(self):
        row = 0
        #User-Agent를 조작하는 경우 
        hdr = {'User-agent':'Mozila/5.0 (compatible; MSIE 5.5; Windows NT)'}
        for n in range(0,5):
            #클리앙의 중고장터 주소 
            data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
            req = urllib.request.Request(data, 
                headers = hdr)
            data = urllib.request.urlopen(req).read()
            page = data.decode('utf-8', 'ignore')
            soup = BeautifulSoup(page, 'html.parser')
            list = soup.find_all('a', attrs={'class':'list_subject'})

            f = open("clien.txt", "a+", encoding="utf-8")
            for item in list:
                try:
                    span = item.contents[3]
                    title = item.text.strip()
                    #라인에디터에 입력된 문자열 받아서 검색
                    if (re.search(self.lineEdit.text(), title)):
                        title = title.replace("\t", "")
                        title = title.replace("\n", "")
                        print(title)
                        link = 'https://www.clien.net'  + item['href'] 
                        print(link.strip())
                        f.write(title+"\n")
                        f.write(link + "\n")
                        #행데이터로 출력 
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(title))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(link))
                        row += 1
                        print("row: ", row) 
                except:
                    pass
             
            f.close()

    def doubleClicked(self):
        url = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        webbrowser.open(url) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Form()
    mywindow.show()
    app.exec_()



