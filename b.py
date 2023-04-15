#!/usr/bin/env python3

import builtins

#print(dir(builtins))

class A:
    def degree(x):
        y = int(input("введите число, которое надо возвести в степень: "))
        def degree_two():
            return y ** x
        return degree_two()
    print(degree(int(input("Введите степень числа: "))))


if __name__=='__main__':
    A



