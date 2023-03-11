#!/usr/bin/env python3
import time
import turtle
turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('yellow')

for step in range(6):
    turtle.begin_fill()
    for t in range(3):
        turtle.forward(30)
        turtle.left(120)
        turtle.pensize(3)
    time.sleep(0.4)
    turtle.forward(50)
    turtle.right(60)
    turtle.end_fill()    

#turtle.hide_turtle()
