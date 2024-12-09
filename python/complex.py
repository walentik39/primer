#!/usr/bin/env python3

import subprocess

class Geom():
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Line(Geom):
    def func(self):
        res = subprocess.run(['ping','-c2','rambler.ru'],stdout=subprocess.PIPE,
                             stderr=subprocess.DEVNULL,encoding='utf-8')
        return res


class Rect(Geom):
    def fun(self):
        result = subprocess.run(['whois','rambler.ru'],stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL,encoding='utf-8')
        return result


if __name__=='__main__':
    l = Line()
    r = Rect()
    l.set_coords(1,2,2,3)
    r.set_coords(9,8,8,8)
    print(l.__dict__) 
    print(r.__dict__)
