#!/usr/bin/env python3

import subprocess
class Process:
    '''I process . Dont is all.'''
    def __init__(self):
        self.result = []

    
    def pr(self):
        name = input("Введите название хоста: ")
        self.result = subprocess.run(['host',name],stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,encoding='utf-8')


    def get(self):
        print(self.result)

if __name__=='__main__':
    c = Process()
    c.pr()
    c.get()
