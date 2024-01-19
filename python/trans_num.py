#!/usr/bin/env python3

a = int(input("Введите число: "))
n = int(input("введите в какую систему: "))
s = ''
al = 'abcdef'

while a>0:
    c = a % n
    if c < 10:
        s=str(c) + s
    else:
        s = al[c-10] + s
    a //= n
print(s)
