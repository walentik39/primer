#!/usr/bin/env python3

import sys

def fun():
    line = sys.stdin.readline().strip()
    if line == "h":
        print("Hello")
    else:
        print("World")

if __name__=='__main__':
    fun()
