#!/usr/bin/env python3

import sys
import random 
from math import *

def main_func():
    a = []
    def inner_func():
        for i in range(10):
            a.append(random.randint(1,55))
            print(sorted(a))
            print(fsum(a))
    return inner_func()

main_func()


