#!/usr/bin/env python3
import subprocess
import urllib.request

class My:
    def fun(self):
        name = input('Введите хост :')
        res = subprocess.run(['whois',name],stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,encoding='utf-8')

        file = urllib.request.urlopen(name)
        message = file.read().decode('utf-8')
        print(message)
        with open('primer.odt','w') as f:
            f.write(str(message))
            f.write(str(res))

if __name__=='__main__':
    c = My()
    c.fun()

