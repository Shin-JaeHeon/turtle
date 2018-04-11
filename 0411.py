import turtle
import random
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.title("원그리기")

def create_circle(x1, y1, r1):
    t.hideturtle()
    t.penup()
    t.goto(x1, y1)
    t.goto(x1, y1 - r1)
    t.pendown()
    t.circle(r1)
    t.penup()
    t.goto(0, 0)
a=0
while a<100:
    create_circle(random.randint(-250,250),random.randint(-250,250),random.randint(10,250));
    a+=1
