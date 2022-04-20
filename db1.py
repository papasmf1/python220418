# db1.py 
import sqlite3

#연결객체를 만들기(먼저 메모리에서 연습)
con = sqlite3.connect(":memory:")
#구문을 수행할 커서 객체 
cur = con.cursor() 
#테이블 구조(테이블 스키마)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick','010');")
#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)


