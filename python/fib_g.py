#!/usr/bin/env python3

from typing import Generator

def fib_g(n: int) -> Generator[int, None, None]:
    yield 0 #специальный случай
    if n > 0: yield 1 # специальный случай
    last: int = 0 # начальное значение fib(0)
    next: int = 1 # начальное значение fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # главный этап генерации.

if __name__=='__main__':
    for i in fib_g(int(input())):
        print(i)

