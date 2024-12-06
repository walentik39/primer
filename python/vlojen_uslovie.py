#!/usr/bin/env python3

import random
import subprocess

class R:
    def fun(self):
        #a = int(input('Введите число '))
        a = random.randint(0,20)
        with open('num.md','w') as f:
            f.write(str(a))
        if a > 10:
            if a < 20:
                print('Это число больше 10 , но меньше 20 ')
        else :
            print('число равно 10 или меньше 10 ')
        #print(a)

if __name__=='__main__':
    r = R()
    r.fun()
