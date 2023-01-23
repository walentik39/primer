#!/usr/bin/env python3

memory = {(1, 0): 1, (0, 1): 1}

def func(x, y):
    if (x, y) not in memory:
        if x == 0:
            memory[(x, y)] = func(x, y-1)
        elif y == 0:
            memory[(x, y)] = func(x - 1, y)
        else:
            memory[(x, y)] = func(x - 1, y) + func(x, y-1)
    return memory[(x, y)]


print(func(2, 2))
print(func(20, 20))

c = 1
for i in range(20):
    c = c*(40-i)//(1+i)
print(c)    
