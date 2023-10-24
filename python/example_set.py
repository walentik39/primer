#!/usr/bin/env python3

import random
class S:
    def main():
        a = []
        def two_main():
            i = 0
            while i < 12:
                a.append(random.randint(1,55))
                print(set(a))
                i += 1
        return two_main()
    main()

if __name__=='__main__':
    S
