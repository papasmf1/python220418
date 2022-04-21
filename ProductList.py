import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

#DB파일이 없으면 만들고 있다면 접속한다. 
if os.path.exists("c:\\work\\ProductList.db"):
    con = sqlite3.connect("c:\\work\\ProductList.db")
    cur = con.cursor()
else: 
    con = sqlite3.connect("c:\\work\\ProductList.db")
    cur = con.cursor()
    cur.execute(
        "create table Products (id integer primary key autoincrement, Name text, Price integer);")

#디자인 파일을 로딩
form_class = uic.loadUiType("c:\\work\\ProductList.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        #초기값 셋팅 
        self.id = 0 
        self.name = ""
        self.price = 0 
        self.setupUi(self)
        #QTableWidget의 컬럼폭 셋팅하기 
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        #QTableWidget의 헤더 셋팅하기
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        #QTableWidget의 컬럼 정렬하기 
        #self.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        #self.tableWidget.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)


    def addProduct(self):
        #입력 파라메터 처리 
        self.name = self.prodName.toPlainText()
        self.price = self.prodPrice.toPlainText()
        cur.execute("insert into Products (Name, Price) values(?,?);", 
            (self.name, self.price))
        #리프레시
        self.getProduct() 
        #입력,수정,삭제 작업후에는 커밋을 한다. 
        con.commit() 

    def updateProduct(self):
        #업데이트 작업시 파라메터 처리 
        self.id  = self.prodID.toPlainText()
        self.name = self.prodName.toPlainText()
        self.price = self.prodPrice.toPlainText()
        cur.execute("update Products set name=?, price=? where id=?;", 
            (self.name, self.price, self.id))
        #리프레시
        self.getProduct() 
        #입력,수정,삭제 작업후에는 커밋을 한다. 
        con.commit()  

    def removeProduct(self):
        #삭제 파라메터 처리 
        self.id  = self.prodID.toPlainText()
        strSQL = "delete from Products where id=" + str(self.id)
        cur.execute(strSQL)
        #리프레시
        self.getProduct() 
        #입력,수정,삭제 작업후에는 커밋을 한다. 
        con.commit()  

    def getProduct(self):
        #검색 결과를 보여주기전에 기존 컨텐트를 삭제(헤더는 제외)
        self.tableWidget.clearContents()

        cur.execute("select * from Products;") 
        #행숫자 카운트 
        row = 0 
        for item in cur: 
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])
            
            #각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력한다. 
            itemID = QTableWidgetItem(int_as_strID) 
            itemID.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 0, itemID)
            
            #제품명은 그대로 출력한다. 
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            
            #각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력한다. 
            itemPrice = QTableWidgetItem(int_as_strPrice) 
            itemPrice.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 2, itemPrice)
            
            row += 1
            print("row: ", row)  

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())


#인스턴스를 생성한다. 
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()



