#!/usr/bin/env python3

import random
def rand_nums():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(0,100))
        print(sorted(numbers, key=None, reverse=True))
    print(sorted(numbers))        
rand_nums()
