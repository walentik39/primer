#!/usr/bin/env python3
import math as m

from tkinter import *

root = Tk()
root.title("Построение графика функции x=sin(y)")
root.geometry("1020x620")
canvas = Canvas(root, width=1020, height=620, bg='#002')
button = Button(None, text='Выход!', bg='#711337', command=quit)
button.pack()
for y in range(21):
    k = 50 * y
    canvas.create_line(10+k, 610, 10+k, 10, width=1, fill='#191938')

for x in range(23):
    k = 50 * x
    canvas.create_line(10, 10+k, 1010, 10 +k, width=1, fill='#191938')

# линии координат x и y

canvas.create_line(10, 10, 10, 610, width=1, arrow=FIRST, fill='white')
canvas.create_line(0, 310, 1010, 310, width=1, arrow=LAST, fill='white')

w = 0.0209    # циклическая частота
phi = 20      # смещение графика по X
A = 100       # амплитуда
dy = 210      # смещение графика по y

xy = []
for x in range(1000):
    y = m.sin(x * w)
    xy.append(x + phi)
    xy.append(y * A + dy)

sin_line = canvas.create_line(xy, fill='blue')
canvas.pack()

root.mainloop()
