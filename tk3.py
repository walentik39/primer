#!/usr/bin/env python3
from tkinter import *
from tkinter import colorchooser
import time

root = Tk()

class But_print:
    def __init__(self):
        self.but = Button(root)
        self.but["text"] = "Печать"
        self.but.bind("<Button-1>",self.printer)
        self.but.pack()


    def printer(self, event):
        print ("Как всегда очередной 'Hello World'")

obj = But_print()
root.mainloop()

def f1():
    for i in('Text'):
        for x in range(4):
            print(str(i) * x)

def f2():
    for i in('Привет!'):
        for x in range(5):
            print(str(i) * x)

def main():
      f1()
      f2()

if __name__=="__main__":
     main()

