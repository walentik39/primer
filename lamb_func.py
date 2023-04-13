#!/usr/bin/env python3

def rectangle_area():
    print((lambda a, b: a * b)(float(input()),float(input())))
    print((lambda a, b: a if a > b else b)(input(),input()))

rectangle_area()
