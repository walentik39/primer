#!/usr/bin/env python3
import random
from math import *
import sys
import os
import pickle
import subprocess
from tkinter import *
def fd():
    subprocess.call(["tasklist","/m"])

def tk():
    root=Tk()
    root.title('Привет!')
    button=Button(None, text='Нажми!',width=8, height=1, bg='#566112', command=quit)
    canvas = Canvas(root, width=1020, height=620, bg='#600123')
    canvas.pack()
    button.pack()
    root.mainloop()
    
def main():
    fd()
    tk()
print(main())      
input()
