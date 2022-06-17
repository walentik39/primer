#!/usr/bin/env python3
a = [2, 4, 7, 1, 6]
count = 0
for i in range(5):
	for j in range(3):
		if a[j] > a[j + 1]:
			count += 1
			a[j],a[j+1] = a[j+1], a[j]
print(*a)
print(count)
