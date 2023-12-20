#!/usr/bin/env python3

import os
import fnmatch

class F:
    def fname():
        for fname in os.listdir('.'):
            if fnmatch.fnmatch(fname, '*.py'):
                print(fname, end=' ')
    fname()


    def main():
        for root, dirs, files in os.walk('/home'):
            for name in files:
                fullname = os.path.join(root,name)
                print(fullname)
                if('pass' in fullname):
                    print('Бинго!!!')
    main()

if __name__=='__main__':
    F
