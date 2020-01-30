# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
'''
def q4(word):
    
    ssafy = 'safy'
    for char in word:
        if char in ssafy:
            return True
    return False
'''


def q4(word):
    saffy= 'safy'
    for i in word:

        if i in saffy:
            return True
        
    return False
            


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q4('fish'))
    print(q4('united'))
    print(q4('galaxy'))