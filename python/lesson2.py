#!/usr/bin/env python3

import subprocess
from contextlib import contextmanager
def fun():
    result = subprocess.run(['ping','-c2','opennet.ru'],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

def fun2():
    result = subprocess.run(['ping6','-c2','linux.org.ru'],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

if __name__=='__main__':
    with managed_file('test2.md') as f:
        f.write(str(fun()))
        f.write('Пока!')
        f.write(str(fun2()))
        f.write('И снова ПОКА!')
    with open('test2.md','r') as file:
        res = file.read()
        print(res)

