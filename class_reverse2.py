#!/usr/bin/env python3

def Reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


def Main():
    rev = Reverse([i ** 2 for i in range(12)])
    for char in rev:
        print(char)
    data = [i ** 3 for i in range(10)]
    print(list(data[i] for i in range(len(data)-1, -1, -1)))

if __name__=='__main__':
    Main()
