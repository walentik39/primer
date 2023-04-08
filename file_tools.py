#!/usr/bin/env python3
import os
import random

def f():
    with open('file_tool.md','a') as myfile:
        a = []
        for i in range(7):
            a.append(random.randint(1,222))
            myfile.write(str(sorted(a, key=None, reverse=True)))

    with open('file_tool.md','r+') as mfile:        
        for j in mfile:
            print(j)
f()         
