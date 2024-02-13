#!/usr/bin/env python3

import random 
def fun():
    with open('text2.odt','r+') as f:
        res = list(f.read())
        random.shuffle(res)
        with open('text2.odt','w') as file:
            file.write(str(''.join(res)))
fun()
