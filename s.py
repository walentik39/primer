#!/usr/bin/env python3

import random
class S:
    def main():
        s = set()
        a = set()
        for i in range(12):
            s.add(str(i))
            a.add(str(s))
            s.pop()
            print(''.join(a))
    
    main()


if __name__=='__main__':
    S
