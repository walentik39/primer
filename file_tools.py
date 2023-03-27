#!/usr/bin/env python3
import os
import random

def f():
    with open('file_tool.md','r+') as mfile:        
        for j in mfile:
            print(j)
    with open('file_tool.md','a') as myfile:
        x = os.listdir('/usr/home/awp/')
        myfile.write(str(x))
f()         
