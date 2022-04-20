# try1.py (곽튜브 + IT잇섭)
#함수 정의
def divide(a,b):
    return a/b 

try:
    #함수 호출
    result = divide(5,2)
except TypeError:
    print("숫자여야 합니다.")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except:
    print("예상하지 못한 에러")
else:
    print("결과:{0}".format(result))
finally:
    print("한번 더 체크(무조건 실행)")

print("전체 코드 실행 종료")

