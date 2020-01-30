# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.

'''
def q2(number):
    result = 1
    
    num = list(str(number))
    for i in range(0, len(num)):
        result *= int(num[i])

    return result
'''
lst = []

def q2(number):
    result = 1
    lst = list(str(number))
    for i in range(0, len(lst)):
        result *= int(lst[i])
    return result




# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q2(123))
    print(q2(2020))
    print(q2(123456789))