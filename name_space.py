#!/usr/bin/env python3

name = 'utr'

def a(name):
    name = 'user'
    print(locals())
    def b():
        name = 'num'
        print(locals())
    b()
a(name)    
