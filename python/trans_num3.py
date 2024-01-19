#!/usr/bin/env python3

a = input()
n = int(input("Система исчисления: "))

power = 1
ans = 0
for i in a[::-1]:
    if i < 'a':
        ans += int(i)*power
    else:
        ans += (ord(i) - ord('a') + 10)*power
    power *= n
print(ans)
