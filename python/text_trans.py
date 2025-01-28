#!/usr/bin/env python3

import random
class N:
    def num(self):
        a = []
        b = []
        c = int(input("Введите число: "))
        i = 0
        while i < c:
            if i%2 == 0:
                a.append(chr(random.randint(0,100)))
            else:
                b.append(chr(random.randint(0,100)))
            i += 1
        with open('rand_simv.odt','w') as f:
            f.write(str(a))
        with open('rand2_simv.odt','w') as f2:
            f2.write(str(b))
if __name__=='__main__':
    n = N()
    n.num()
