# class1.py 
#클래스 정의
class Person:
    #초기화 메서드(생성자)
    def __init__(self):
        #초기화 루틴
        self.name = "default name"
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person() 
p1.name = "전우치"
p1.print()
p2.print()

#런타임(실행시간)에 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

#인스턴스에 추가
p1.age = 30 
print(p1.age)
#print(p2.age)



    
