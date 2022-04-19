# 메모리구조.py
class SuperClass:
    def __init__(self):
        self.x = 10 
    def printX(self):
        print(self.x)

class SubClass(SuperClass):
    def __init__(self):
        self.y = 20
    def printY(self):
        print(self.y)

s = SubClass()
s.a = 30 
print("SuperClass:", SuperClass.__dict__)
print("SubClass:", SubClass.__dict__)
print("s:", s.__dict__)
