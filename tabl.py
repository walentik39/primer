#!/usr/bin/env python3

import random
class T:
    def main():
        with open('test.odt','w') as myfile:
            def two_main():
                a = []
                for i in range(3):
                    for j in range(4):
                        a.append(random.randint(12,66))
                        myfile.write(str(set(a)))
            return two_main()
    main()

    def read():
        with open('test.odt','r') as myfile:
            for i in myfile:
                print(i, end=' ')
            print()    
    read()            

if __name__=='__main__':
    T
