#!/usr/bin/env python
from math import *
import sys
import subprocess
import random
import os
import dis
def foo():
    a=float(input("Введите первое число: "))
    b=float(input("Введите второе число: "))
    res = print("Вычисление среднего значения чисел:",(a + b) /2,'\n' "а корень из чисел",sqrt(a+b))
    return res

def rand():
    with open('test.md','w') as f:
        f.write(str(dis.dis(foo)))
        

if __name__=='__main__':
    rand()
