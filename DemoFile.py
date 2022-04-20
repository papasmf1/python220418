# DemoFile.py 

url = "http://www.credu.com/?page=" + str(1) 
print(url)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---약간 변경---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---약간 변경---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(10))

#서식문자를 지정
print("{0:x}".format(10))    
print("{0:b}".format(10))    
print("{0:,}".format(15000000))    
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#파일을 생성하기(유니코드로 저장)
f = open("c:/work/demo.txt", "wt", encoding="utf-8")
f.write("하나\n두번째\n세번째\n")
f.close() 
