#!/usr/bin/env python3

class B:
    def message(x):
        def print_message(y):
            return x * y
        return print_message
    print(message(int(input("введите число: ")))(int(input("второе число: "))))

if __name__=='__main__':
    B
