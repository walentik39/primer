#!/usr/bin/env python3

from functools import lru_cache, wraps, update_wrapper
def fib(x):
    return fib(x-1) + fib(x-2) if x>1 else x

@lru_cache
class counter:
    cnt = 0

    def __init__(self,func):
        update_wrapper(self,wrapped=func)
        self.__func = func


    def __call__(self,*args, **kwargs):
        self.cnt += 1
        return self.__func(*args, **kwargs)


    def mydec(n):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs) * n
            return wrapper
        return decorator

print(fib(12))
