#!/usr/bin/env python3

import random
import subprocess

class My:
    def __init__(self, funk, param):
        self.funk = funk
        self.param = param

    def fun(self):
        self.funk = subprocess.run(["inxi","-b"],stdout=subprocess.PIPE,
                                   stderr=subprocess.DEVNULL,encoding='utf-8')
        return self.funk


if __name__=='__main__':
    my = My("inxi","-y")
    res = my.fun()
    print(res)
