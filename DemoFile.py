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

    
