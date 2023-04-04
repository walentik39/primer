#!/usr/bin/env python3

import os
import datetime
x = datetime.datetime.now()
with open('test.txt','a') as myfile:
    myfile.write(str(x))
f = open('test.txt', 'r', encoding='UTF-8')
for x in f:
    print(x)
f.close()    
