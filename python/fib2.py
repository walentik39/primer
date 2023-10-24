#!/usr/bin/env python3

def fib():
    a , b = 0,1
    n = int(input())
    x = []
    while a < n:
        x +=[a]
        print(a, end=' ')
        a += 1
        a , b = b, a + b
    print('\n',x)
fib()    


