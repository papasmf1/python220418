# DemoTupleDict.py 
# Tuple 
tp = (1,2,3)
print(type(tp))
print(tp)
print(len(tp))
print(tp[0])

#주로 데이터를 담아서 전달
#함수를 정의(리턴을 튜플에 담아서 여러개)
def calc(a,b):
    return a+b, a*b 

#호출
result = calc(3,4)
print(result)

#한방에 입력
args = (5,6)
#*는 튜플에 담아서 입력 
print(calc(*args))

#세트는 집합연산
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))

#다른 형식으로 변환:tuple ==> list로(타입캐스팅)
a = {1,2,3}
b = list(a)
print(b)
print(type(b))
b.append(4)
print(b)
        
#딕셔너리
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device)
print(type(device))
print(len(device))
print(device["아이폰"])
#입력
device["갤럭시폴더"] = 15 
device["아이폰"] = 6 
print(device)
#삭제
del device["아이폰"]
print(device)
#print(device[0])

#반복문
for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)


