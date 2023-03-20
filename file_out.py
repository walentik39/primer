#!/usr/bin/env python3

f1 = open('test.odt','r')
for i in f1:
    print(i)
f2 = open('test2.odt','w')
for line in f1:
    f2.write(line.upper())
f1.close()
f2.close()
