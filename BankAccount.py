# BankAccount.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #인스턴스 멤버 변수 초기화
        #내부에 숨김(이름변경)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    #원하는 결과 출력(ToString()메서드)
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#print(account1.__balance)
#외부에서 접근: _클래스명__balance
#백도어
#print(account1._BankAccount__balance)
print(account1)
