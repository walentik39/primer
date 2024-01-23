#!/usr/bin/env python3

import random
import subprocess
import time
import sys

def funcs():
    result = subprocess.run(['top','-n'],stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    with open('test.odt','w') as f:
        f.write(str(result))
    time.sleep(2)
    sys.exit()

def file_read():
    with open('test.odt','r') as file:
        res = file.read()
        print(res)

if __name__=='__main__':
    file_read()
    funcs()
