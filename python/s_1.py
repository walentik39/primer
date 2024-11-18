#!/usr/bin/env python3

import random
import subprocess

class S:
    def main(self):
        s = []
        a = []
        for i in range(random.randint(0,9)):
            s +=[i**i] 
            b = list(s)
            random.shuffle(b)
            a.append((b))
            with open('test.odt','w') as f:
                f.write(str(a))
            with open('test.odt','r') as file:
                result = file.read()
                print(result)


if __name__=='__main__':
    m = S()
    m.main()
