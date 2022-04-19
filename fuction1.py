# fuction1.py
#함수를 정의
def setValue(newValue):
    x = newValue
    print("함수내부:", x)


#호출
#디버깅할 때 중단점(Break Point)
retValue = setValue(5)
print(retValue)

#교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print(intersect("HAM","SPAM"))

