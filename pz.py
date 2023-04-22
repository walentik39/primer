#!/usr/bin/env python3
import random 

class Num:
    def main():
        num = []
        def two_main():
            i = 0
            while i < 7:
                with open('test.md','a') as myfile:
                    num.append(random.randint(1,500))
                    myfile.write(str(num))
                i += 1
        return two_main()
    main()

if __name__=='__main__':
    Num

