#!/usr/bin/env python3

def fact(n):
    "Это функция находит факториал числа"
    if (n <= 1): return 1
    else: return n * fact(n - 1)

print(fact(int(input())))
print(fact.__doc__)

