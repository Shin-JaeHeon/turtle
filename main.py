import turtle
import tkinter.messagebox as msg
import math

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.title("원그리기 그래프")


def y_line(k):
    t.goto(10, k)
    t.penup()
    t.goto(0, k)
    t.write("  " + str(k))
    t.pendown()
    t.goto(-10, k)
    t.penup()
    t.goto(0, k)


def x_line(g):
    t.goto(g, -10)
    t.penup()
    t.goto(g, 0)
    t.write("  " + str(g))
    t.pendown()
    t.goto(g, 10)
    t.penup()
    t.goto(g, 0)


def create_circle(x1, y1, r1, text):
    t.hideturtle()
    t.penup()
    t.goto(x1, y1)
    t.write(text + "(" + str(x1) + ", " + str(y1) + ")")
    t.goto(x1, y1 - r1)
    t.pendown()
    t.circle(r1)
    t.penup()
    t.goto(0, 0)


def resets():
    reset(0, 0, -1, 0, 0, -1, False)


def lim():
    msg.showinfo("Lim 모드는", "x또는 y의 시작값부터 x또는 y의 종료값까지 원을 움직이며, r의 시작값부터 종료값까지 크기가 커집니다.")
    msg.showerror("경고! 사용자 및 관찰자의 건강을 해칠 수 있습니다!", "광 과민성 발작등이 발생하거나 어지럼증등이 발생할 수있습니다.\n반드시 밝은 곳에서 봐주시기 바랍니다.")
    allow = msg.askyesno("경고 사용자 및 관찰자의 건강을 해칠 수 있습니다!", "정말로 진행하시겠습니까?")
    if not allow:
        resets()
    x1 = turtle.numinput("숫자를 입력하세요", "큰원의 중심좌표 x의 시작값", 0)
    y1 = turtle.numinput("숫자를 입력하세요", "큰원의 중심좌표 y의 시작값", 0)
    r1 = turtle.numinput("숫자를 입력하세요", "큰원의 반지름 r의 시작값", 100)
    x2 = turtle.numinput("숫자를 입력하세요", "큰원의 중심좌표 x의 종료값", 100)
    y2 = turtle.numinput("숫자를 입력하세요", "큰원의 중심좌표 y의 종료값", 100)
    r2 = turtle.numinput("숫자를 입력하세요", "큰원의 반지름 r의 종료값", 100)
    X1 = turtle.numinput("숫자를 입력하세요", "작은 원의 중심좌표 X의 시작값", 0)
    Y1 = turtle.numinput("숫자를 입력하세요", "작은 원의 중심좌표 Y의 시작값", 0)
    R1 = turtle.numinput("숫자를 입력하세요", "작은 원의 반지름 R의 시작값", 300)
    X2 = turtle.numinput("숫자를 입력하세요", "작은 원의 중심좌표 X의 종료값", -100)
    Y2 = turtle.numinput("숫자를 입력하세요", "작은 원의 중심좌표 Y의 종료값", -100)
    R2 = turtle.numinput("숫자를 입력하세요", "작은 원의 반지름 R의 종료값", 300)
    V = turtle.numinput("표시 횟수", "표시 횟수를 입력하세요\n표시횟수가 높을 수록 좀 더 세세하게 변화합니다.", 100)
    t0 = x1
    t1 = y1
    t2 = r1
    t3 = X1
    t4 = Y1
    t5 = R1
    temp = 0
    v = int((x2 - x1) / V)
    v1 = int((y2 - y1) / V)
    v2 = int((r2 - r1) / V)
    v3 = int((X2 - X1) / V)
    v4 = int((Y2 - Y1) / V)
    v5 = int((R2 - R1) / V)
    while temp < V:
        t0 += v
        t1 += v1
        t2 += v2
        t3 += v3
        t4 += v4
        t5 += v5
        reset(t0, t1, t2, t3, t4, t5, True)
        temp += 1


def reset(x, y, r, X, Y, R, mode):
    t.reset()
    t.hideturtle()
    t.speed(0)
    if not mode:
        x = turtle.numinput("숫자를 입력하세요", "큰원의 중심좌표 x", 0)
        y = turtle.numinput("숫자를 입력하세요", "큰원의 중심좌표 y", 0)
        r = turtle.numinput("숫자를 입력하세요", "큰원의 반지름 r", 100)
        X = turtle.numinput("숫자를 입력하세요", "작은 원의 중심좌표 X", 0)
        Y = turtle.numinput("숫자를 입력하세요", "작은 원의 중심좌표 Y", 0)
        R = turtle.numinput("숫자를 입력하세요", "작은 원의 반지름 R", 300)
    text1 = "중심 좌표"
    if not mode:
        a = 1
        b = 1
        t.penup()
        while a < 10:
            x_line(a * 100)
            a = a + 1
        while b < 6:
            y_line(b * 100)
            b = b + 1
        a = 1
        b = 1
        while a < 10:
            x_line(a * -100)
            a = a + 1
        while b < 6:
            y_line(b * -100)
            b = b + 1
    if x == X and y == Y:
        text1 = "두 원의 중심 좌표"
    create_circle(x, y, r, text1)
    create_circle(X, Y, R, text1)
    if not mode:
        dis = math.sqrt((X - x) ** 2 + (Y - y) ** 2)
        if dis == r + R:
            msg.showinfo("알림", "두 원은 외부에서 접합니다.\nR키를 눌러 초기화 하세요.\nL키를 눌러 지정된 범위에서 원의 크기를 조정할 수 있습니다.")
        elif dis == abs(R - r):
            msg.showinfo("알림", "두 원은 내부에서 접합니다.\nR키를 눌러 초기화 하세요.\nL키를 눌러 지정된 범위에서 원의 크기를 조정할 수 있습니다.")
        elif abs(R - r) < dis < R + r:
            msg.showinfo("알림", "두 원은 겹칩니다\nR키를 눌러 초기화 하세요.\nL키를 눌러 지정된 범위에서 원의 크기를 조정할 수 있습니다.")
        elif x == X and y == Y:
            msg.showinfo("알림", "두 원은 동심원입니다.\nR키를 눌러 초기화 하세요.\nL키를 눌러 지정된 범위에서 원의 크기를 조정할 수 있습니다.")
        elif dis > r + R:
            msg.showinfo("알림", "두 원은 만나지 않습니다.\nR키를 눌러 초기화 하세요.\nL키를 눌러 지정된 범위에서 원의 크기를 조정할 수 있습니다.")
        elif dis < abs(R - r):
            msg.showinfo("알림", "한 원이 다른 원의 내부에 있습니다.\nR키를 눌러 초기화 하세요.\nL키를 눌러 지정된 범위에서 원의 크기를 조정할 수 있습니다.")
        turtle.onkey(lim, "l")
        turtle.onkey(lim, "L")
        turtle.onkey(resets, "r")
        turtle.onkey(resets, "R")
        turtle.listen()
        turtle.mainloop()


resets()
