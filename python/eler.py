#!/usr/bin/env python3

result = 0
max_number = 0
for i in range(800001,1000000,2):
    count = 0
    checker = i
    while i > 1:
        if i%2 == 0:
            i = i / 2
        else:
            i = 3*i + 1
        count += 1
    if result < count:
        result = count
        max_number = checker
print(max_number,result)
