#!/usr/bin/env python3

class My:
    def square(self):
        self.x = int(input())
        return self.x * self.x
if __name__=='__main__':
    m = My()
    nums = [i for i in range(15)]
    nums_squared = [num + m.square() for num in nums]
    for num in nums_squared:
        print(num)
