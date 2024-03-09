#!/usr/bin/env python3

import random 
import subprocess
import os


def fun():
    result = subprocess.run(['ifconfig','re0'],capture_output=True)

    return result

def fun2():
    output = subprocess.run(['ifconfig','lo0'],capture_output=True)
    return output

if __name__=='__main__':
    res = [fun(),fun2()]
    out = random.choice(res)
    with open('test.odt','w') as f:
        f.write(str(out))
    os.system('cat test.odt')    
