#!/usr/bin/env python3

def my_decor(func):
    def wrapper():
        print('start')
        func()
        print('stop')
    return wrapper

def my_func():
    print('Тут основная функция')

my = my_decor(my_func)
my()

def my_dec(func):
    def wrapper():
        print('start')
        func()
        print('stop')
    return wrapper

def my_func():
    print('Тут основная функция')

@my_dec
def my_func():
    print('Повтор')

my_func()
