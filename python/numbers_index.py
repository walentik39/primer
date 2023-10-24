#!/usr/bin/env python3

import random

numbers = []
for i in range(12):
    numbers.append(random.randint(12,222))
    print(numbers)
    size = len(numbers)
    current_index = 0
    max_number_index = 0
    max = numbers[0]
    while (current_index < size):
        if(numbers[current_index] > max):
            max = numbers[current_index]
            max_number_index = current_index
        current_index = current_index + 1
        print(max)
        print(current_index)
