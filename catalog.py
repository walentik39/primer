#!/usr/bin/env python3

def price():
    catalog = {}
    with open('catalog.txt','r+') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        for i in range(3):
            t = input("Введите товар ")
            k = int(input("Количество "))
            if t in catalog:
                catalog[t] += k
            else:
                catalog[t] = k
        for x in catalog:
            f.write("{}:{}\n".format(x, catalog[x]))

price()            
