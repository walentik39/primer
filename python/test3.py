#!/usr/bin/env python3

from threading import Thread
import random
import time

class A:
    def main_func():
        a = []
        for i in range(6):
            a.append(random.randint(12,233))
            time.sleep(0.5)
            def inner_func():
                b = []
                for j in range(5):
                    b.append(random.randint(1,56))
                    print(sorted(b,key=None, reverse=True))
                    time.sleep(0.3)
                    b.extend(a)
            return inner_func()

    def func():
        c = []
        d = {}
        i = 1
        while i < 6:
            c.append(random.randint(1,99))
            d[i] = c
            print(d)  
            time.sleep(0.2)
            i += 1


Thread(target=A.main_func())
Thread(target=A.func())

if __name__=='__main__':
    A

