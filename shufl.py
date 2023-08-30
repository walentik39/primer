#!/usr/bin/env python3

import random

def read_file():
    with open('test.odt','r') as fi:
        result = fi.read()
        print(result)

def one():
    words = ['sky', 'storm', 'rock', 'falcon', 'forest']
    random.shuffle(words)
    val = ['1','2','3','4','5','6','7','8','9','0']
    random.shuffle(val)
    def main():
        i = 0
        while i < 6:
            words.append(random.choice(words))
            words.append(random.choice(val))
            print(words)
            with open('test.odt','w') as f:
                f.write(''.join(str(words * random.randint(0,9))))
            i += 1
    return main()




if __name__=='__main__':
    res = one()
    read_file()

