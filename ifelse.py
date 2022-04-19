# ifelse.py 
score = int(input("점수를 입력:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 80 <= score < 90:
    grade = "C"
else:
    grade = "D"

print("등급은 ", grade)


