#!/usr/bin/env python3

import subprocess
class Fun:
    def get_speak_func(self):
        name = input("Введите название hosta: ")
        res = subprocess.run(["whois",name],stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,encoding="utf-8")
        return res

    def write_file(self):
        with open('test.odt','w') as f:
            f.write(str(self.get_speak_func()))

if __name__=='__main__':
    f = Fun()
    f.write_file()

