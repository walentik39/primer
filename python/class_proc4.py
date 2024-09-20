#!/usr/bin/env python3

import subprocess
class Process:
    def __init__(self):
        self.result = []

    def pr(self):
        name = input("Введите название хоста: ")
        self.result = subprocess.run(['host',name],stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,encoding='utf-8')
        return self.result


    def get(self):
        print(self.result)

if __name__=='__main__':
    c = Process()
    with open('test.odt','w') as f:
        f.write(str(c.pr()))
