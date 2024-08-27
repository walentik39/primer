#!/usr/bin/env python3

import subprocess
from sys import argv
def fun():
    ip_list = ['0.0.0.0','127.0.1.1','test.me','mail.ru','8.8.8.8']
    for ip in ip_list:
        result = subprocess.run(['ping','-c','3',ip],stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL,encoding='utf-8')
    #output = result.stderr + result.stdout
    #print(output)
        if result.returncode == 0:
            print(f"Адрес {ip} пингуется")
        else:
            print(f"адрес {ip} не пингуется")

if __name__=='__main__':
    fun()
