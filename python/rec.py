#!/usr/bin/env python3
from threading import Thread
import random
import time

class My:
    def fun():
        s = [ i ** 2 for i in range(12) if i%2 !=0]
        y = []
        for x in s:
            time.sleep(1)
            print(x)
            y.append(x)
            print(sorted(y))


    def loop1():
        b = []
        for i in range(12):
            b.append(random.randint(22,66))
            time.sleep(1)
            print(sorted(b))


    def loop2():
        a = []
        for i in range(12):
            a.append(random.randint(1,555))
            time.sleep(1)
            print(sorted(a))


Thread(target=My.loop1())
Thread(target=My.fun())
Thread(target=My.loop2())

if __name__=='__main__':
    My

