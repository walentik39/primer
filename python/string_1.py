#!/usr/bin/env python3

string = input()
n = len(string)
if len(string) >= 2:
    print(string[0],string[n-1])
else:
    print("Ошибка")
