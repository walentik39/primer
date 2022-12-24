#!/usr/bin/env python3
import random
class A:
    def func(arg=[]):
        arg.append(1)
        for i in range(12):
            arg.append(random.randint(1,232))
            print(sorted(arg))
    func()        


if __name__=='__main__':
    A
