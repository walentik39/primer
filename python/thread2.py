#!/usr/bin/env python3

import time
import threading as th
import random

def countdown(n):
    for i in range(n):
        print(n - i -1, "left")
        time.sleep(0.5)

if __name__=='__main__':
    t = th.Thread(target=countdown, args=(random.randint(1,20),))
    t.start()


class Thr1(th.Thread): # Создаём экземпляр потока Thread
    def __init__(self, var):
        th.Thread.__init__(self)
        self.daemon = True # Указываем, что этот поток - демон
        self.var = var # это интервал, передаваемый в качестве аргумента

    def run(self): # метод, который выполняется при запуске потока
        num = 1
        while True:
            y = num*num + num / (num - 10) # Вычисляем функцию
            num += 1
            print("При num =", num, " функция y =", y) # Печатаем результат
            time.sleep(self.var) # Ждём указанное количество секунд

if __name__=='__main__':
    x = Thr1(0.9)
    x.start()
    time.sleep(2)
