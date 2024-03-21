#!/usr/bin/env python
from math import *
import sys
import subprocess
import random
import os
from tkinter import *
from tkinter.messagebox import showinfo
def foo():
    a=float(input("Введите первое число:"))
    b=float(input("Введите второе число:"))
    res = print("Вычисление среднего значения чисел:",(a + b) /2,'\n' "а корень из чисел",sqrt(a+b))
foo()
def quit():
    sys.exit()
widget = Button(None, text='Всё готово!' , command=quit)
widget.pack()
widget.mainloop()
