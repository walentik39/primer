#!/usr/bin/env python
from math import *
import sys
import random
import os
import functools
from tkinter import *
from tkinter.messagebox import showinfo
def foo():
    a=float(input("Введите первое число:"))
    b=float(input("Введите второе число:"))
    print("Вычисление среднего значения чисел:",(a + b) /2,'\n' "И корня",sqrt(a+b))
foo()
def quit():
    sys.exit()
widget = Button(None, text='Всё готово!' , command=quit)
widget.pack()
widget.mainloop()
