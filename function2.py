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

#기본값 지정
def times(a=10,b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출
print(connectURI("credu.com","80"))
print(connectURI(port="80",server="credu.com"))

#가변인자(가변적인 상황)
def union(*ar):
    #유니크한 글자를 담을 지역변수(List)
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#정의되지 않은 인자처리(**딕셔너리)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출
print(userURIBuilder("credu.com", "80", id="kim", passwd="1234"))
print(userURIBuilder("credu.com", "80", id="kim", passwd="1234", name="mike"))

#람다함수(이름이 없는 간결한 함수 정의):일회용품(함수의 인자로 함수명)
# x와y를 입력받아서 처리 
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
#보통은 정의하고 바로 호출
print((lambda x:x*x)(3))
print(globals())
