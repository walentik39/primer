#!/usr/bin/env python3

import random
class S:
    def main():
        s = []
        a = []
        for i in range(random.randint(0,9)):
            s +=[i] 
            b = random.shuffle(s)
            a.append((s))
            with open('test.odt','w') as f:
                f.write(str(a))
    
    def read_file():
        with open('test.odt','r') as file:
            result = file.read()
            print(result)


if __name__=='__main__':
    S.main()
    S.read_file()
