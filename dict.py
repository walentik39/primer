#!/usr/bin/env python3
import random
import subprocess
def f():
    dict1 = {}
    a = []
    for i in range(12):
        a.append(random.randint(1,22))
        dict1[i] = a
        with open('test2.odt','a') as f:
            f.write(str(dict1))

def sub_():
    result = subprocess.run(['lsof','-o'],stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='utf-8')
    output = result.stdout + result.stderr
    return output

def file_write(file):
    with open('test2.odt','w') as f:
        f.write(str(file))

def read_file():
    with open('test2.odt','r') as fil:
        for i in fil:
            print(i)

if __name__=='__main__':
    file_write(str(sub_()))
    print(read_file())

