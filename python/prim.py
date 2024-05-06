#!/usr/bin/env python3

import subprocess
import os

def fun():
    result = subprocess.run(["nmap","-A","test.me"],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout
def fun2():
    result = subprocess.run(["ping","-c2","test.me"],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

def func(*args):
    return args


if __name__=='__main__':
    res = func(fun(),fun2())
    with open("file.md","w") as f:
        f.write(str(res))
    with open("file.md","r") as file:
        r=file.read()
        print(r)
