#!/usr/bin/env python3

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


if __name__=='__main__':
    bob = Person('Bob Switch', 45, 7890, 'hardware')
    sue = Person('Sue Jones', 43, 7676, 'software')
    print(bob.name, sue.pay)

    print(bob.lastName())
    sue.giveRaise(.12)
    print(sue.pay)

                      
