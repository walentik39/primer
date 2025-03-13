#!/usr/bin/env python3

import subprocess
import random
import socket

def fun():
    result = subprocess.run(['arp','rambler.ru'],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout 

class ManagedFile:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

if __name__=='__main__':
    with ManagedFile('test.odt') as f:
        f.write(str(fun()))
        f.write('а теперь, пока!')
