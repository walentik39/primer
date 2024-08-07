#!/usr/bin/env python3

import math as m
import os
import subprocess
import sys
import random
from tkinter import *
from tkinter import colorchooser
import turtle
w1=turtle.Turtle()
for c in ['green','red','blue','black']:
    w1.color(c)
    w1.forward(75)
    w1.left(90)
    
w1 = Tk()
w1.title("Надо попробовать!")
w1.geometry("300x300")
w1.config(bg='#773119')

w2=turtle.Turtle()
for c in ['yellow','black','green','blue']:
    w2.color(c)
    w2.forward(35)
    w2.left(30)
    w2.forward(30)
    w2.left(30)
    w2.forward(30)
    w2.left(30)

w2 =Tk()
w2.title('Привет')
w2.geometry('100x100')
w2.config(bg='#229988')
w1.mainloop()
w2.mainloop()


