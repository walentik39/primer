#!/usr/bin/env python3
import random

class Addition:
    first = []
    second = []
    answer = 0

    #параметры конструктора
    def __init__(self):
        self.first = [i * 2 for i in range(12) if i%2 ==0]
        self.second = [j ** 2 for j in range(12) if j%3 !=0]

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
    obj = Addition()
    obj.calculate()
    obj.display()
