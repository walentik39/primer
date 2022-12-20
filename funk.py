#!/usr/bin/env python3
import random
from math import *
class A:
    def main_func():
        a = []
        def inner_func():
            for i in range(12):
                a.append(random.randint(1,123))
                print(sorted(a, key=None, reverse=True))
                print(fsum(a))
                print(sorted(a))
        return inner_func()
    main_func()


if __name__=='__main__':
    A
