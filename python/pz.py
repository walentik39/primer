#!/usr/bin/env python3
import random 

class Num:
    def main():
        num = []
        def two_main():
            i = 0
            while i < 7:
                if (i % 2 == 0):
                    with open('test1.md','w') as myfile:
                        num.append(random.randint(1,500))
                        myfile.write(str(sorted(num, key=None,reverse=False)))
                else:
                    with open('test2.md','w') as file:
                        num.append(random.randint(1,100))
                        file.write(str(sorted(num, key=None,reverse=True)))
                i += 1
        return two_main()
    main()

if __name__=='__main__':
    Num

