#!/usr/bin/env python3

class Logger:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __getattribute__(self, item):
        try:
            value = object.__getattribute__(self, item)
            print(f"Accessed attribute: {item}")
            return value
        except AttributeError:
            pass
        return object.__getattribute__(self, "wrapped").__getattribute__(item)

class MyClass:
    def __init__(self):
        self.x = 10

obj =Logger(MyClass())
print(obj.x)
