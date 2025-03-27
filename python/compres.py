#!/usr/bin/env python3

import random
import subprocess

class My:
    def func(self):
        res = subprocess.run(['lsof','-i'],stdout=subprocess.PIPE,
                             stderr=subprocess.DEVNULL,encoding='utf-8')
        return res
    def object(self):
        with open('test.md','w') as f:
            f.write(str(self.func()))

if __name__=='__main__':
    m = My()
    m.object()
    with open('test.md','r') as file:
        print(file.read())
