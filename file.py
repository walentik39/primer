#!/usr/bin/env python3

import os
f = open('test.txt','a', encoding='UTF-8')
os.system('nslookup mail.ru > test.txt')
os.system('lsof -i > test.txt')
f.close()

f = open('test.txt', 'r', encoding='UTF-8')
for x in f:
    print(x)
f.close()    
