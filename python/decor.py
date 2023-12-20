#!/usr/bin/env python3

def my_decor(func):
    def wrapper():
        print('Start')
        func()
        print('end')
    return wrapper

@my_decor
def my_func():
    print('Тут основная функция')

my_func()

def my_decor(func):
    def wrapper(n):
        print('Start')
        func(n)
        print('end')
    return wrapper

@my_decor
def my_func(number):
    print(number ** 2)

my_func(int(input()))
