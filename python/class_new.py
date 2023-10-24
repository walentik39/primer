#!/usr/bin/env python3

class Counter:
    '''I count . Dont is all.'''
    def __init__(self):
        self.value = [] 

    
    def increment(self):
        self.value = [value ** 2 for value in range(12,-1,-1) if value % 3 == 0]


    def get(self):
        print(self.value[::-1]) 


if __name__=='__main__':
    c = Counter()
    c.increment()
    c.get()
