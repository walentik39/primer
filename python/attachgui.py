#!/usr/bin/env python3

from tkinter import *
from tkinter102 import MyGui

#Главное окно приложения
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# Окно диалога
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
