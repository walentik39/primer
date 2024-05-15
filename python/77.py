#!/usr/bin/env python3

string = input("Введите номер телефона ")
n = len(string)
if string.isdigit() and n>=8:
    print("*"*(n-4)+string[n-4:])
else:
    print("Ошибка")
