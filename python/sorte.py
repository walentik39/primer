#!/usr/bin/env python3

import random 
import subprocess

def fun():
    res = subprocess.run(['lsof','-i'],stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,encoding='utf-8')
    return res.stdout

def file_write(name):
    with open('test.odt','w') as f:
        f.write(str(name))

if __name__=='__main__':
    file_write(fun())
    with open('test.odt','r') as file:
        fil = file.read()
        print(fil)
