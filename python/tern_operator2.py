#!/usr/bin/env python3

name = input('введите своё имя ')
age = input('ваш возраст ')
message = 'Проходите ' + name if int(age) >= 18 else 'вам пока рано .'
print(message)
