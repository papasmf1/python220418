#coding:utf-8

class Animal:
    def __init__(self):
        print("Animal __init__()")

class Tiger(Animal):
    def __init__(self):
        super().__init__()      #부모 클래스의 생성자 메서드 호출 
        print("Tiger __init__()")

class Lion(Animal):
    def __init__(self):
        super().__init__()      #부모 클래스의 생성자 메서드 호출 
        print("Lion __init__()")

class Liger(Tiger, Lion):
    def __init__(self):
        super().__init__()
        print("Liger __init__()")
        
        
