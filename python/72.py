#!/usr/bin/env python3
# программа выводит первый и последний символы
string = input('Введите строку ')
i = len(string)
if i >= 2:
    print(string[0]+string[i-1])
else:
    print('Ошибка!')
