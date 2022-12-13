#!/usr/bin/env python3

import random
class A:
    def main_func():
        for n in iter(lambda: random.randrange(10), 7):
            print(n)
    main_func()


    def ineer_func():
        a, *b, c = [i ** 2 + 3 + j for i in range(6) for j in range(7) if j%2!=0]
        print(a, sorted(b,key=None, reverse=True),c)


if __name__=='__main__':
    A.ineer_func()
