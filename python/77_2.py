#!/usr/bin/env python3

import subprocess

def fun():
    string = input("Введите номер телефона ")
    n = len(string)
    if string.isdigit() and n>=8:
        print("*"*(n-4)+string[n-4:])
    else:
        print("Ошибка")
    return string

def file_write(name):
    with open('test.md','w') as f:
        f.write(str(name))

def main():
    file_write(fun())

if __name__=='__main__':
    main()
