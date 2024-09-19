#!/usr/bin/env python3

import random
import subprocess
class Myfunc:
    def fun(self):
        name = input('Введите имя хоста: ')
        res = subprocess.run(['whois',name],stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,encoding='utf-8')
        return res

    def main_func(self):
        n = input('Введите адрес : ')
        result = subprocess.run(['arp',n],stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,encoding='utf-8')
        return result


if __name__=='__main__':
    my = Myfunc()
    with open('test.odt','w') as f:
        f.write(str(my.fun()))
        f.write(str(my.main_func()))


