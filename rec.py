#!/usr/bin/env python3

class My:
    def fun():
        s = [ i ** 2 for i in [1, 2, 4, 5, 8] if i%2 ==0]
        y = []
        for x in s:
            print(x)
            y.append(x)
            print(y)
My.fun()    

