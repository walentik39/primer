#!/usr/bin/env python3

def fib(n):
    last: int = 0
    next: int = 1
    for i in range(1, n):
        last, next = next, last + next
        print(i)

fib(int(input('Введите число:')))
