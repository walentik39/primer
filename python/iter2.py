#!/usr/bin/env python3

import random
def read_file():
    with open("w_f.odt","r") as file:
        for i in file:
            print(i)

def main_func():
    for n in iter(lambda: random.randrange(10), 7):
        print(n)
        print(sorted(iter(lambda: random.randrange(10), 7)))


def ineer_func():
    a, *b, c = [i ** 2 + 3 + j for i in range(6) for j in range(7) if j%2!=0]
    print(a, sorted(b,key=None, reverse=True),c)




if __name__=='__main__':
    read_file()
    main_func()
    ineer_func()
