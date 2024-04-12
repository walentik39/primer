#!/usr/bin/env python3


import heapq
import random

def fun():
    nums = []
    strocka = fun.__dir__()
    for i in range(12):
        nums.append(random.randint(0,50))
        strocka1 = heapq.nlargest(3,nums)
        strocka2 = heapq.nsmallest(3, nums)
        with open('test.odt','w') as f:
            f.write(str(strocka1))
            f.write(str(strocka))
            f.write(str(strocka2))

if __name__=='__main__':
    fun()
    with open('test.odt','r') as file:
        res = file.read()
        print(res)

