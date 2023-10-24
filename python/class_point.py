#!/usr/bin/env python3

#__init__ иницилизатор объекта
#__del__ финализатор объекта(удаляет self)
class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        print("Вызов __init__")
        self.x = x
        self.y = y

    
    def __del__(self):
        print("Удаление экземпляра: " + str(self))


    def set_coords(self, x, y):
        self.x = x
        self.y = y


    def get_coords(self):
        return self.x, self.y


pt = Point(1,[i ** 2 for i in range(12) if i%3 ==0])
print(pt.__dict__)
