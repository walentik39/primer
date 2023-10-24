#!/usr/bin/env python3

from turtle import *
from random import *

finish = 200

t1= Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(-200,20)
t1.pendown()
t1.speed(3)

t2= Turtle()
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(-200,-20)
t2.pendown()
t2.speed(3)

def razmetka():
    t=Turtle()
    t.speed(0)
    for i in range(1,21):
        t.penup()
        t.goto(-200+i*20, 50)
        t.pendown()
        t.goto(-200+i*20, -100)
    t.hideturtle()

razmetka()    


def catch1(x,y):     # это обработчик сщбытия нажатия
    t1.write('Ouch!', font=('Arial', 14, 'normal')) #пишем на экране Ауч
    t1.fb(randint(10,15)) #черепашка делает случайный шаг от 10 до 15

t1.onclick(catch1)

def catch2(x,y):
    t2.write('Ouch!', font=('Arial', 14, 'normal')) #пишем на экране Ауч
    t2.fb(randint(10,15)) #черепашка делает случайный шаг от 10 до 15

t2.onclick(catch2)

while t1.xcor()<finish or t2.xcor()<finish:
    t1.forward(randint(2,7))
    t2.forward(randint(2,7))
