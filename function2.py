# function2.py
#전역변수와 지역변수(LGB)
x = 1 
def func(a):
    return a+x 

#호출
print(func(1))

def func2(a):
    x = 2 
    return a+x 

#호출
print(func2(1))

