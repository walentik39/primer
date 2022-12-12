#!/usr/bin/env python3
import random

class R:
    def main_func():
        a = []
        def inner_func():
            for i in range(12):
                a.append(random.randint(12,232))
                for j in enumerate(a):
                    print(j, sorted(a))
        return inner_func()
    main_func()


if __name__=='__main__':
    R
