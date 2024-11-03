#!/usr/bin/env python3

from threading import Thread
import random
import time

class A:
    def main_func(self):
        a = []
        for i in range(6):
            a.append(random.randint(12,233))
            time.sleep(0.5)
            def inner_func(self):
                b = []
                for j in range(5):
                    b.append(random.randint(1,56))
                    print(sorted(b,key=None, reverse=True))
                    time.sleep(0.3)
                    b.extend(a)
            return inner_func(self)

    def func(self):
        c = []
        d = {}
        i = 1
        while i < 6:
            c.append(random.randint(1,99))
            d[i] = c
            print(d)  
            time.sleep(0.2)
            i += 1



if __name__=='__main__':
    my = A()
    Thread(target=my.main_func())
    Thread(target=my.func())


