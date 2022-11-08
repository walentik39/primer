#!/usr/bin/env python3

class A:
    def fun(self):
        return "A"


class B(A):
    def fun(self):
        return super().fun() + "B"


if __name__=='__main__':
    b = B()
    print(b.fun())
