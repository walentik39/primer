#!/usr/bin/env python3

import os
import random
class D:
    def main():
        d = {}
        def main_2():
            a = {}
            i = 1
            while i < 6:
                print(d)
                a = {input()}
                for j in a:
                    if j in d:
                        d[j] += a
                    else:
                        d[j] = a
                i += 1
        return main_2()       
    main()
if __name__=='__main__':
    D
                     
