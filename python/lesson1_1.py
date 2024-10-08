#!/usr/bin/env python3

import subprocess
from contextlib import contextmanager
class Sub:
    def fun(self):
        n = input("Введите хост :")
        result = subprocess.run(['ping','-c2',n],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
        return result.stdout

    def fun2(self):
        n2 = input("Введите второй хост :")
        result = subprocess.run(['ping6','-c2',n2],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
        return result.stdout

    @contextmanager
    def managed_file(self,name):
        try:
            f = open(name, 'w')
            yield f
        finally:
            f.close()

if __name__=='__main__':
    s = Sub()
    with s.managed_file('test.odt') as f:
        f.write(str(s.fun()))
        f.write('Пока!')
        f.write(str(s.fun2()))
        f.write('И снова ПОКА!')
    with open('test.odt','r') as file:
        res = file.read()
        print(res)

