#!/usr/bin/env python3

def fib(n: int):
    last: int = 0
    next: int = 1
    for i in range(1, n):
        last, next = next, last + next
        print(next)

fib(int(input('Введите число: ')))
