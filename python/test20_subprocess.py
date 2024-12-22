#!/usr/bin/env python3

import subprocess
import random
class My:
    def fun(self):
        ip_list = ['8.8.4.4','127.0.1.1','test.me','linux.org','8.8.8.8']
        random.shuffle(ip_list)
        for ip in ip_list:
            result = subprocess.run(['ping','-c 1',ip],stderr=subprocess.DEVNULL,
                                        stdout=subprocess.PIPE,encoding='utf-8')
            return result.stdout

if __name__=='__main__':
    m = My()
    with open('text.odt','w') as f:
        f.write(str(m.fun()))
