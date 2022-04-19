# ifelse.py 
#다중 라인 주석 처리: ctrl + / (cmd + / )
# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 80 <= score < 90:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

#반복구문
value = 5 
while value > 0:
    print(value)
    value -= 1 

print("전체 실행 종료")

lst = ["문자열", 100, 3.14]
for item in lst:
    print(item, type(item))

print(len(lst))

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue구문")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

#수열함수
print(list(range(10)))
print(list(range(1,11)))

#메뉴얼하게 루프를 도는 경우
for i in range(10):
    print(i)

#년도
print(list(range(2000,2023)))

#리스트 컴프리헨션(리트스 임베딩)
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])

