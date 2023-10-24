#!/usr/bin/env python3

import os
import datetime
x = datetime.datetime.now()
with open('test.txt','w') as myfile:
    myfile.write(str(x))
    myfile.write(str(os.system('uname -a >> test.txt')))

f = open('test.txt', 'r', encoding='UTF-8')
for x in f:
    print(x)
f.close()    
def fun(name):
    res = os.getcwd()
    return res

if __name__=='__main__':
    print(fun(f))
