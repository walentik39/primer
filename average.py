#!/usr/bin/env python3

import random

class A:
    def main_func():
        a = []
        for x in range(12):
            a.append(random.randint(12, 565))
            print(sorted(a, key=None, reverse=True))
            def inner_func():
                sum1 = 0
                i = 0
                n = len(a)
                for i in a:
                    sum1 += i
                    i += 1
                    average = sum1/n
                    print(average)
            return inner_func()
    main_func()


if __name__=='__main__':
    A
