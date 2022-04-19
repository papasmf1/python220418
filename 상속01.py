#부모 클래스 
class Person:
    #초기화 메서드(생성자)
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식클래스 
class Student(Person):
    #재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #재정의(덮어쓰기)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(self.subject, self.studentID))
#인스턴스(복사본)
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()

