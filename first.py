#!/usr/bin/env python3

numbers = [2, 3, 5, 7, 12] #Синтаксичечкая ошибка: Не создан массив!#
first = numbers[0]
second = numbers[0]
if(numbers[1] > first):
    first = numbers[1]
else:
    second = numbers[1]
if(numbers[3] > first):
    second = first
    first = numbers[3]
else:
    if(numbers[3] > second):
        second = numbers[3]
#Логическая ошибка: не понятно что должно получиться?#
