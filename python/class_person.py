#!/usr/bin/env python3

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    
    def get_old(self):
        return self.__old



    def set_old(self, old):
        self.__old = old

    
    old = property(get_old, set_old)


p = Person("Иван", 33)
p.__dict__['old'] = 'old in object p'
p.set_old(4)
p.old = 55
print(p.old, p.__dict__)
