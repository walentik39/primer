#!/usr/bin/env python3

import sys
import random 
from math import *

def main_func():
    a = []
    def inner_func():
        for i in range(10):
            a.append(random.randint(1,55))
            print(sorted(a))
            print(fsum(a), sys.stdout.write("сумма чисел ="))
            with open('wr.docs','w') as file:
                file.write(str(a))
    return inner_func()

def file_read(name):
    with open('wr.docs','r') as file:
        res = file.read()
        for i in res:
            print(i,end='')



if __name__=='__main__':
    result = file_read(main_func())
    print(result)
