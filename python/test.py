#!/usr/bin/env python
from math import *
import sys
import random
import os
import functools
from tkinter import *
from tkinter.messagebox import showinfo
class My:
    def foo(self):
        a = float(input("Введите первое число:"))
        b = float(input("Введите второе число:"))
        print("Вычисление среднего значения чисел:",(a + b) /2,'\n' "И корня",sqrt(a+b))

if __name__=='__main__':
    m = My()
    m.foo()
    widget = Button(None, text='Всё готово!' , command=quit)
    widget.pack()
    widget.mainloop()
    sys.exit()
