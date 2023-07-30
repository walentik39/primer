#!/usr/bin/env python3

import os
with open('test.odt','r+') as f1:
    for i in f1:
        print(i)
with open('test2.odt','a') as f2:
    f2.write(str(os.system('cal > test.odt')))
