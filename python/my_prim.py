#!/usr/bin/env python3

import subprocess
import random

def func():
    res = subprocess.run(["curl","https://www.freebsd.org/docs/"],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
    return res.stdout

def fun():
    res = subprocess.run(["curl","https://distrowatch.com"],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
    return res.stdout

def file_write(name):
    with open("test.odt","w") as f:
        f.write(str(name))

def convert():
    result = subprocess.run(["convert","test.odt","test.pdf"],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

if __name__=='__main__':
    test = [func(),fun()]
    test2 = random.choice(test)
    file_write(test2)
    convert()
