# demoOS.py
from os.path import * 

print(abspath("python.exe"))
print(basename("c:\\python39\\python.exe"))
print(getsize("c:\\python39\\python.exe"))
print(exists("c:\\python39\\python.exe"))
print(isfile("c:\\python39\\python.exe"))

#운영체제정보
from os import *
print("운영체제이름:", name)
#다른 실행파일 실행
#system("notepad.exe")

#파일 리스트 
import glob 
print(glob.glob("c:\\work\\*.py"))



