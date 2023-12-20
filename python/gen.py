#!/usr/bin/env python3

import time
import random
from math import *

class A:
    def f1():
        a = []
        for i in range(12):
            a.append(random.randint(1,554))
            print(sorted(a))
            time.sleep(0.5)
            print(fsum(a))
    f1()


    def f2():
        b = []
        for x in range(12):
            b.append(random.randint(1,717))
            print(sorted(b))
            time.sleep(0.3)
            for y in b:
                print(chr(y))


if __name__=='__main__':
    A.f2()

