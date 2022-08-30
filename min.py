#!/usr/bin/env python3

import random
import time

a = 1
b = 2
c = 3
d = 4
min = a
if b< min:
    min = b
if c < min:
    min = c
if d< min:
    min = d
print(min)

x = []
for i in range(12):
	x.append(random.randint(1,500))
	time.sleep(0.5)
	print(sorted(x))
