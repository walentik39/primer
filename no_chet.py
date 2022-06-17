#!/usr/bin/env python3
"""Вычислить сумму значений нечётных элементов массива...списка"""
a = [1, 3, 6, 9]
size = 4
index = 0
sum = 0
while(index < size):
    if(a[index]%2 > 0):
        sum = sum + a[index]
    index = index + 1
print(sum)

"""Вычислить сумму нечётных элементов массива"""

d = [1, 3, 6, 9]
size = 4
index = 0
sum = 0
while(index < size):
    if(index%2 > 0):
        sum = sum + d[index]
    index = index + 1
print(sum)    
