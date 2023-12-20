#!/usr/bin/env python3

def Recursion(i):
    if i == 1:
        return i
    else:
        print(i)
        return Recursion(i - 1)
Recursion(int(input()))
