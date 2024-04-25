#!/usr/bin/env python3

a = input('Введите первое число ' )
b = input('второе число ')
if a.isdigit() and b.isdigit():
    result = int(a)+int(b)
    print('Сумма =', str(result))
else:
    print('Ошибка')
