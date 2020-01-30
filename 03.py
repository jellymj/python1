# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
'''
def q3(fruits, add, n):
    if add in fruits:
        fruits[add] += n
    else:
        fruits[add] = n
    return fruits
'''
def q3(fruits, add, n):
    if add in fruits:
        fruits[add] += n
    else:
        fruits[add] = n
    return fruits






# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q3({'apple': 1}, 'apple', 3))
    print(q3({'apple': 1}, 'banana', 1))
    print(q3({}, 'apple', 3))