#!/usr/bin/env python3
from tkinter import *
import turtle
t=turtle.Turtle()
for c in ('#220033','red','yellow','blue','orange','green'):
        for x in ('#bbccfb','green','#440011','#661211','red','black'):
                t.color(c)
                t.forward(55)
                t.left(55)
                t.circle(22)
                t.forward(45)
                t.color(x)
                t.forward(55)
                t.left(55)
                t.circle(33)
	
