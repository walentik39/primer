#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import math as m
from tkinter import *
from tkinter import colorchooser
import random
import subprocess
a=float(input('Введите число:\n'))
b=float(input('Введите второе:\n'))
if a<b:
    while a<1000:
        print(a)
        a,b=b,a+b
else:
    while a<1000:
        print(a)
        a,b=b, a-b
input()



    
