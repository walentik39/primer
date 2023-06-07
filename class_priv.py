#!/usr/bin/env python3

#pip install accessify
from accessify import private, protected

class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y


    #@private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1)
print(pt.set_coord(12, 15))
print(pt._Point__check_value(5))
print(pt)

