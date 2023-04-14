#!/usr/bin/env python3

def square(x):
    return x * x
nums = [i for i in range(15)]
nums_squared = [square(num) for num in nums]
for num in nums_squared:
    print(num)
