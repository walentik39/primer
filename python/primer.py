#!/usr/bin/env python3

import random
import subprocess
from collections import deque

class My:
    def search(self,lines, pattern, history=5):
        previuos_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line, previuos_lines
            previuos_lines.append(line)    

if __name__=='__main__':
    m = My()
    with open('test.odt','r') as f:
        for line, prevlines in m.search(f, 'falcon', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

