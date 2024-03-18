#!/usr/bin/env python3

import random
import subprocess

class S:
    def fun():
        def inner():
            b = []
            a = subprocess.run(['ls'],stdout=subprocess.PIPE,
                               shell=True)
            b +=[a]
            print(b)
            with open('test.odt','w') as f:
                f.write(str(b))
        return inner()

if __name__=='__main__':
    S.fun()

