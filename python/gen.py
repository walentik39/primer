#!/usr/bin/env python3

import random
import sys
from math import *

def func():
    for x in range(random.randint(0,22)):
        yield x ** 2

if __name__=='__main__':
    g = func()
    for z in g:
        if z%2 !=0:
            print(z)
        else:
            print(sqrt(z))
