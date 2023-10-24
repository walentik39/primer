#!/usr/bin/env python3

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    
    def __iter__(self):
        return self


    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def Main():
    rev = Reverse([i ** 2 for i in range(12)])
    for char in rev:
        print(char)

if __name__=='__main__':
    Main()
