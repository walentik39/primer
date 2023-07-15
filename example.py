#!/usr/bin/env python3

class CM:
    def __init__(self, var):
        self.var = var
    def __enter__(self):
        print(">>>")
    def __exit__(self, *args):
        print("<<<",args)
        return self.var

if __name__=='__main__':
    with CM(True) as c:
        print("###", c)
    print("Done")    
    with CM(True) as c:
        print("$$$", c)
        raise IOError
    print("Done")
