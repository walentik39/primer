#!/usr/bin/env python3

from functools import reduce
def f(a):
    if a%2 == 0:
        return a

a = filter(f, [i for i in range(20)])
print(list(a))
b = filter(lambda x:  (x%2 == 0),[i for i in range(33)])
print(list(b))
print(reduce(lambda a, b: a * b,[i for i in range(1,6)]))
y = [ i for i in range(12)]
x = "abcdefghjlki"
result = zip(x, y)
print(list(result))

