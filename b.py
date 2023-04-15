#!/usr/bin/env python3
# Замыкание
def degeer(x): # функция
    def print_degeer(y): # вложенная функция.
        return x ** y
    return print_degeer
print(degeer(int(input("Введите число , которое надо возвести в степень: ")))(int(input("введите степень: "))))
