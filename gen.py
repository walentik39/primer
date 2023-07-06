#!/usr/bin/env python3

import random
import sys

def fun():
    for i in range(12):
        yield i ** 2


gen = fun()
for j in gen:
    if j%2 !=0:
        print(j)
    else:
        print(random.randint(0,j))
