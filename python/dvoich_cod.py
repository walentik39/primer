#!/usr/bin/env python3
#Десятичное число переводится в двоичное
a = int(input("Введите целое число: "))
k = ''
while a>0:
    tmp = a%2
    k = str(tmp) + k
    a = a//2
print(k)
