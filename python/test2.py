#!/usr/bin/env python
from math import *
import sys
import subprocess
import random
import os
class Exp:
    def foo(self):
        a=float(input("Введите первое число: "))
        b=float(input("Введите второе число: "))
        res = ("Вычисление среднего значения чисел:",(a + b) /2, "а корень из чисел",sqrt(a+b))
        return res

    def rand(self):
        with open('test.odt','w') as f:
            f.write(str(self.foo()))

    def convert(self):
        a = input('Какой файл выбрали: ')
        b = input('в какой превратить: ')
        result = subprocess.run(['convert',a,b],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
        return result.stdout

if __name__=='__main__':
    e = Exp()
    e.rand()
    e.convert()
