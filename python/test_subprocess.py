#!/usr/bin/env python3

import subprocess
import random

class My:
    def rand(self):
        ip = ['openbsd.org','freebsd.org','rambler.ru','linux.org.ru','linux.net']
        i = random.choice([x for x in ip])
        return i

    def func(self):
        res = subprocess.run(['nmap',self.rand()],stdout=subprocess.PIPE,
                        stderr=subprocess.DEVNULL,encoding='utf-8')
        return res.stdout

    def funcs(self):
        result = subprocess.run(['ping','-c1',self.rand()],stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,encoding='utf-8')
        return result.stdout + result.stderr

if __name__=='__main__':
    m = My()
    with open('test.odt','w') as f:
        f.write(str(m.func()))
        f.write(str(m.funcs()))
