#!/usr/bin/env python3

import random
import time
class R:
    def main_func():
        a = []
        def inner_func():
            for i in range(5):
                a.append(random.randint(12,232))
                time.sleep(0.4)
                b = []
                for j in range(4): 
                    b.append(random.randint(1,12))
                    b.extend(a)
                    print(sorted(b, key=None, reverse=True))
                    time.sleep(0.4)
        return inner_func()
    main_func()

if __name__=='__main__':
    R
            

