#!/usr/bin/env python3

import subprocess
import os
def fun():
    result = subprocess.run(["curl","wttr.in/shklov"],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

def fin():
    result = subprocess.run(["cat","test.odt"],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

def fun2():
    with open("test.md","w") as f:
        f.write(str(fin()))
        f.write(str(fun()))

def fun3(*args):
    return args

if __name__=='__main__':
    fun3(fun2())
    with open("test.md","r") as file:
        res = file.read()
        print(res)
