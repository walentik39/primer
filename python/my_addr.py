#!/usr/bin/env python3

import subprocess

def fun():
    res = subprocess.run(["curl","https://api.ipify.org"],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
    return res.stdout

def file_write(name):
    with open('test.odt','w') as f:
        f.write(str(name))

if __name__=='__main__':
    file_write(fun())
    with open('test.odt','r') as fil:
        result = fil.read()
        for i in result:
            print(i, end='')
