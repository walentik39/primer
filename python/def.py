#!/usr/bin/env python3
import random
numbers = []
size = 12
for i in range(12):
    numbers.append(random.randint(1,100))
    print(sorted(numbers, key=None, reverse=True))
current_index = 0
max_numer_index = 0
max = numbers[0]
while(current_index < size):
    if(numbers[current_index] > max):
        max = numbers[current_index]
        max_number_index = current_index
    current_index = current_index + 1
print(max)
for j in range(12):
    numbers.append(random.randint(1,100))
    print(sorted(numbers, key=None, reverse=False))
