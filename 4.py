import turtle # 터틀 그래픽 모듈을 포함한다.
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color('green', 'green')
def square(length):
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()

def drawit(x, y): 
    t.penup()
    t.goto(x,y)
    square(50)

s = turtle.Screen() # 그림이 그려지는 화면을 얻는다.
s.onscreenclick(drawit) # 마우스 클릭 이벤트 처리 함수를 등록한다.
