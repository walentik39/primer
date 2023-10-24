#!/usr/bin/env python3

import random
class S:
    def main():
        s = set()
        a = set()
        for i in range(random.randint(0,9)):
            s.add(str(i))
            a.add(str(s))
            with open('test.odt','w') as f:
                f.write(''.join(a))
    
    def read_file():
        with open('test.odt','r') as file:
            result = file.read()
            print(result)


if __name__=='__main__':
    S.read_file()
    S.main()
