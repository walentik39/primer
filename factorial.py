#!/usr/bin/env python3

def factorial(n):
    res = 1
    i = 1
    while i < n+1:
        res *= i
        i += 1
    print(res)

factorial(int(input()))
