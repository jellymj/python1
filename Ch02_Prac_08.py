import turtle
import random

## 함수 선언 부분 ##

def screenLeftClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    turtle.stamp()

## 변수 선언 부분 ##
pSize = random.random()

## 메인 코드 부분 ##

turtle.title('심화문제 8번')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)

turtle.done()
