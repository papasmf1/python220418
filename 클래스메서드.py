# 클래스메서드.py
class CoeffVar(object):
    coefficient = 1 
    @classmethod
    def mul(cls, fact):
        return cls.coefficient * fact 

#파생형식을 정의
class MulFive(CoeffVar):
    coefficient = 5 

x = MulFive.mul(4)
print(x)
