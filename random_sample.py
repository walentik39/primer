#!/usr/bin/env python3

import random
number = random.randint(0,10)
for i in range(3):
    num = int(input("Введите ваше число от 0 до 10 "))
    if num == number:
        print("Вы выиграли")
        break
    elif num < number:
        print("Загаданное число больше")
    elif num > number:
        print("Загаданное число меньше")
else:
    print("Вы проиграли")
