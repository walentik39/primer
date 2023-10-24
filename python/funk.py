#!/usr/bin/env python3
import random
from math import *
class A:
    def main_func():
        a = []
        def inner_func():
            d = {}
            for i in range(5):
                a.append(random.randint(1,123))
                d = list(d)
                d.append(sorted(a, key=None, reverse=False))
                d = tuple(d)
                print(d)
        return inner_func()
    main_func()


if __name__=='__main__':
    A
