#계산기 프로그램
'''
여러 줄 주석
입니다.
'''

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))
result = a + b
print(a, '+', b, '=', result)
result = a - b
print(a, '-', b, '=', result)
result = a * b
print(a, '*', b, '=', result)
result = a / b
print(a, '/', b, '=', result)

data = '안녕' + \ # \ 붙이면 줄 바꿔도 한 줄로 인식#
       '하세요?' + \
       '파이썬!'
print(data)
