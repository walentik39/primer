#!/usr/bin/env python3

import subprocess
import random

def fun():
    res = subprocess.run(["netstat","-rn"],stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,encoding='utf-8')
    result = (res.stdout,res.stderr)
    return random.choice(result)

def file_write(name):
    with open('test.odt','w') as f:
        f.write(str(name))

if __name__=='__main__':
    file_write(fun())
    with open('test.odt','r') as file:
        rs = file.read()
        print(rs)
