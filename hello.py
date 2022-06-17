#!/usr/bin/env python3

a = int(input("Введите число:"))
k = 0
delit = []
for i in range(1, a+1):
    if a % i == 0:
        k += 1
        delit.append(i)
if k == 2:
    print("Число простое")
else:
    print("число непростое")
    print(delit)
