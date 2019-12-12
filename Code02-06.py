import turtle

## 함수 선언 부분 ##

## 변수 선언 부분 ##
myT = None

## 메인 코드 부분 ##
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0, 4) :
    myT.forward(200)
    myT.right(90)
myT.done()

pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

def screenLeftClick(x, y) :  ##마우스 왼쪽 버튼 누르면 클릭한 지점까지 거북이가 임의의 색상으로 선을 그리면서 따라옴##
    global r, g, b ##전역변수 선언 : 다른 함수에서도 사용할 수 있는데 필요##
    turtle.pencolor((r, g, b))
    turtle.pendown() ##거북이가 펜을 바닥에 대고 선을 그림##
    turtle.goto(x, y)

def screenRightClick(x, y): ##마우스 오른쪽 누르면 거북이가 이동##
    turtle.penup()  ##거북이가 펜을 들고 이동하므로 선이 그려지지 않고 이동만##
    turtle.goto(x, y)

def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrage(1,10)
    turtle.shapesize(tSize)
    r = random.random()  ##random.random() : 0~0.99999 중 임의의 실수를 뽑는다##
    g = random.random()
    b = random.random()
