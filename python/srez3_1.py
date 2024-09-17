#!/usr/bin/env python3

import random
import subprocess
class Myfunc:
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

    def read_file(self):
        with open('test.odt','r') as fi:
            i = fi.read()
            return i

    def convert(self):
        res = subprocess.run(['convert','test.odt','test.jpg'],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
        return res.stdout

if __name__=='__main__':
    my = Myfunc()
    with open('test.odt','w') as f:
        f.write(str(my.fun()))
        f.write(str(my.main_func()))
    my.read_file()
    my.convert()


