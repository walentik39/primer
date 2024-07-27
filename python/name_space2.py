#!/usr/bin/env python3

import random

def a():
    name = ['Марья', 'Юлиана', 'Светлана', 'Наталья']
    random.shuffle(name)
    print(locals())
    def b():
        name = ['Степан','Пятро','Прокоп','Семен','Василий']
        random.shuffle(name)
        print(locals())
    b()
a()
name = 'Иван'
print(f'{name}')

if __name__=='__main__':
    a()
