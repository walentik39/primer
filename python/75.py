#!/usr/bin/env python3
# В этом примере мы не указываем начало и конец среза и берём каждый второй символ исходной строки целиком. Если же указать меньше пяти , то в обратном порядке.
string = input('Введите строку ')
i = len(string)
if i >= 5:
    print(string[1::2])
else:
    print(string[::-1])