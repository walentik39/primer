#!/usr/bin/env python3

def fib5(n: int) -> int:
    if n == 0: return n # специальный случай
    last: int = 0 # начальное значение fib(0)
    next: int = 1 # начальное значение fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__=='__main__':
    print(fib5(int(input())))
