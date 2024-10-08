#!/usr/bin/env python3

class My:
    def fun(self):
        a = [i ** 2 for i in range(12) if i%3==0]
        i = 0
        while i < len(a):
            print(a[i])
            i += 1

if __name__=='__main__':
    m = My()
    m.fun()
