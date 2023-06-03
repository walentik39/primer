#!/usr/bin/env python3
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



    
