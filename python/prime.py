#!/usr/bin/env python3
import sys
a=float(input('Введите число:\n'))
b=float(input('Введите второе:\n'))
if a<b:
    while a<1000:
        print(a)
        a,b=b,a+b
else:
    while a<1000:
        print(a)
        a,b=b, a-b
if a>1000 or a == 1000:
    exit(0)




    
