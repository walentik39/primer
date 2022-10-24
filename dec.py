#!/usr/bin/env python3

from functools import lru_cache, wraps, update_wrapper


@lru_cache
def fib(x):
    return fib(x-1) + fib(x-2) if x>1 else x


print(fib(int(input())))
