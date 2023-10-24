#!/usr/bin/env python3

import random

class A:
    def main_func():
        a = [i ** 2 for i in range(12,35) if i%2!=0 ]
        i = 0
        size = len(a)
        sum1 = 0
        while i < size:
            print(random.choice(a))
            sum1 += a[i]
            i += 1
        average = sum1 / size
        print(average)
    main_func()


if __name__=='__main__':
    A
