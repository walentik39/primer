#!/usr/bin/env python3
import random
def f():
    dict = {}
    a = []
    i = 1
    while i < 6:
        a.append(random.randint(1,22))
        a = sorted(a, key=None, reverse=True)
        dict[i] = a
        i += 1
    return dict

print(f())
