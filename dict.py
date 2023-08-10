#!/usr/bin/env python3
import random
import subprocess
def f(name):
    dict = {}
    a = []
    i = 1
    while i < 6:
        a.append(random.randint(1,22))
        a = sorted(a, key=None, reverse=True)
        dict[i] = a
        i += 1
    return dict
def sub_():
    result = subprocess.run(['lsof','-i'],stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='utf-8')
    output = result.stdout + result.stderr
    print(output)
if __name__=='__main__':
    res = f(sub_())
    print(res)

