#!/usr/bin/env python3

from random import *
for i in range(12):
	i = i * "XYZ"
	a = i.replace("X","x").split("Y")
	print(a)
