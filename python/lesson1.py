#!/usr/bin/env python3

import subprocess
from contextlib import contextmanager
def fun():
    result = subprocess.run(['ping','-c2','localhost'],stdout=subprocess.PIPE,
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
    with managed_file('test.md') as f:
        f.write(str(fun()))
        f.write('Пока!')
    with open('test.md','r') as file:
        res = file.read()
        print(res)

