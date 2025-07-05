#!/usr/bin/env python3

import random

class My:
    def fun(self):
        a = []
        i = 0
        while i < 6:
            print(a)
            a.append(random.randint(12,22))
            i += 1
            return a

    def main_func(self):
        count = 0
        for i in range(int(input())+1):
            count += i
            return count    


if __name__=='__main__':
    m = My()
    with open('test.odt','w') as f:
        f.write(str(m.fun()))
        f.write(str(m.main_func()))
    with open('test.odt','r') as file:
        result = file.read()
        print(result)

