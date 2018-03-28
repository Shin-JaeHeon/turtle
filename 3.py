import turtle

t = turtle.Turtle()
n = int(turtle.numinput("숫자를 입력하세요", "n각형 그리기", 10))
t.pendown()
def n_polygon(n):
    for i in range(n):
        t.right(360//n);
        t.forward(50)
for i in range(10):
    n_polygon(n)
    t.right(15)
