#!/usr/bin/env python3

import random
import subprocess
class My:
    def rand(self):
        ip_list = ['12.0.0.0','127.0.1.1','test.me','mail.ru','8.4.4.8']
        ip = random.choice(ip_list)
        return ip

    def fun(self):
        result = subprocess.run(['ping','-c3',self.rand()],stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL,encoding='utf-8')
    #output = result.stderr + result.stdout
    #print(output)
        if result.returncode == 0:
            print(f"Адрес пингуется")
        else:
            print(f"адрес не пингуется")

if __name__=='__main__':
    m = My()
    m.fun()
