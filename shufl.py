#!/usr/bin/env python3

import random

def one():
    words = ['sky', 'storm', 'rock', 'falcon', 'forest']
    random.shuffle(words)
    def main():
        i = 0
        while i < 6:
            words.append(random.choice(words))
            print(words)
            i += 1
    return main()

if __name__=='__main__':
    one()

