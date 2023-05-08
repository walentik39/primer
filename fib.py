#!/usr/bin/env python3

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        a += 1
    print()
fib(int(input("Введите число: ")))
