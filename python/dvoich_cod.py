#!/usr/bin/env python3
# Программа переводит десятичные числа в двоичные
a = int(input("Введите целое число: "))
binary = ''
while a>0:
    tmp = a%2
    binary = str(tmp) + binary
    a = a//2
print(binary)
