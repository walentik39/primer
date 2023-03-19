#!/usr/bin/env python3
from tkinter import *
import random
colors = ('red','yellow','blue','green','grey')
import time
def button_clicked():
    # изменяем текст кнопки
    button['text'] = time.strftime('%H:%M:%S')
root=Tk()
# создаём виджет
button = Button(root, bg=random.choice(colors))
# конфигурируем виджет после создания
button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)
# также можно использовать квадратные скобки:
# button['text'] = time.strftime('%H:%M:%S')
# button['command'] = button_clicked
button.pack()
root.mainloop()
