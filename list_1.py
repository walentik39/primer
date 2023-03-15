#!/usr/bin/env python3
import random
list1 = []
list2 = []
i = 1
for i in range(5):
    list1.append(random.randint(12,99))
    for i in range(4):
        list2.append(sorted(list1))
print(list2)

