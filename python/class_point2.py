#!/usr/bin/env python3

class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __getattribute__(self, item):
        print("__getattribute__")
        if item == "x":
            raise ValueError("Доступ запрещён")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print("__setattr__")
        if key == "z":
            raise AttributeError("недопустимое имя атрибута ")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
    

    def __delattr__(self, item):
        print("__delattr__: " +item)
        object.__delattr__(self, item)


pt1 = Point(1,2)
pt2 = Point(10,20)
del pt1.x
print(pt1.__dict__)
print(pt1.MAX_COORD)
