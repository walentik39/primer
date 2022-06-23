#!/usr/bin/env python3
from random import randint
num = []
size = len(num)
count = 0
for i in range(15):
    num.append(randint(0, 500))

for i in range(size-1):
    for j in range(size-i-1):
        if num[j] > num[j+1]:
            num[j],num[j+1] = num[j+1], num[j]
            count += 1

print(num)  

