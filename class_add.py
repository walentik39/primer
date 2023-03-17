#!/usr/bin/env python3

class Addition:
    first = 0
    second = 0
    answer = 0

    #параметры конструктора
    def __init__(self, f, s):
        self.first = f
        self.second = s

    # выводим на печать
    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition two numbers = " + str(self.answer))

    # действие.
    def calculate(self):
        self.answer = self.first + self.second

if __name__=='__main__':
    # создаём обьект класса.
    obj = Addition(int(input()),int(input()))
    obj.calculate()
    obj.display()
