#!/usr/bin/env python3
# программа выводит первые три и последние три символа
string = input('Введите строку ')
i = len(string)
if i >= 5:
    print(string[:3]+string[i-3:])
else:
    print('Ошибка!')
