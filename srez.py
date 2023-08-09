#!/usr/bin/env python3

import random

def fun():
    a = []
    i = 0
    while i < 6:
       print(a)
       a.append(random.randint(12,22))
       i += 1

def main_func(name):
    count = 0
    for i in range(int(input())+1):
        count += i
    return count    

if __name__=='__main__':
    result = main_func(fun())
    print(result)
    result2 = main_func(fun())
    print(result2)


