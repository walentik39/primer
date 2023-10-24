#!/usr/bin/env python3

import random
class I:
    def index():
        a = []
        def main():
            for j in range(12):
                a.append(random.randint(1,100))
            for i in range(12):    
                print(i,a[i])
                a[i] +=a[-1]
            print(a)    
        return main()
    index()

if __name__=='__main__':
    I
