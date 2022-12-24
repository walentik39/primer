#!/usr/bin/env python3

sp = [5,7,8,12,9,15]
sp1 = []
for i in sp:
    sp1.append(i ** 2)
print(sp1)    
sp2 = [i **2 for i in sp]
print(sp2)
sp3 = [i **3 for i in sp]
print(sp3)


