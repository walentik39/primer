#!/usr/bin/env python3

a = int(input("Введите число: "))
n = int(input("введите в какую систему: "))
s = ''

while a>0:
    c = a % n
    if c < 10:
        s=str(c) + s
    else:
        s = chr(ord('a')+c-10) + s
    a //= n
print(s)
# функция "chr" перводит цифровую в символьную, а функция "ord" обратно.
