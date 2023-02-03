#!/usr/bin/env python3

def fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return fibonacci(idx - 1) + fibonacci(idx - 2)
print(fibonacci(int(input())))
