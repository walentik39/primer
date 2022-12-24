#!/usr/bin/env python3

import random 
for i in range(12):
	i = i * "XYZ"
	a = i.replace("X","x").split("Y")
	print(a)


x = 0
while x<(random.randint(2,22)):
    print(x)
    x += 1

print("Done")
