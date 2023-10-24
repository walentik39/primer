#!/usr/bin/env python3

import random

def fun():
    a = []
    i = 0
    while i < 6:
       print(a)
       a.append(random.randint(12,22))
       i += 1
    return a

def main_func():
    count = 0
    for i in range(int(input())+1):
        count += i
    return count    

def write_file(name):
    with open('test.odt','w') as f:
        f.write(str(name))

def read_file():
    with open('test.odt','r') as fi:
        i = fi.read()
        print(i)

if __name__=='__main__':
    result = write_file(main_func())
    result1 = read_file()
    result2 = write_file(fun())
    result3 = read_file()


