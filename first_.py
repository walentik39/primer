#!/usr/bin/env python3

import os
import subprocess

def write_file(user):
    with open('first.odt','w') as file:
        file.write(str(user))


def sub():
    res = subprocess.run(['netstat','-ln'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8")
    output = res.stderr + res.stdout
    return output

def read_file():
    with open('first.odt','r') as f:
        for i in f:
            print(i)

if __name__=='__main__':
    result = sub()
    result2 = write_file(result)
    result3 = read_file()
    print(result3)
