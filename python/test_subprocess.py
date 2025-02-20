#!/usr/bin/env python3

import subprocess
import random

def func():
    res = subprocess.run(['netstat','-rn'],stdout=subprocess.PIPE,
                        stderr=subprocess.DEVNULL,encoding='utf-8')
    return res.stdout
    

if __name__=='__main__':
    with open('test.odt','w') as f:
        f.write(str(func()))
