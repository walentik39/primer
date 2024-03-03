#!/usr/bin/env python3

import random
a = []
for j in range(random.randint(0,20)):
    a.append(j)
    random.shuffle(a)
    for i in a:
        print(a)

print(sorted(a, key=None, reverse=False))
