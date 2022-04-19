class MyClass:
    def __init__(self, value):
        self.Value = value 
        print("Class is created! Value = ", value)
        
    def __del__(self):
        print("Class is deleted!")
        

c = MyClass(10)
c_copy = c
del c 
del c_copy
