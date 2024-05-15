#!/usr/bin/env python3

string = input('Введите строку ')
string = string.replace(' ', '').lower()
if string == string[::-1]:
    print("Да ")
else:
    print("Нет ")
