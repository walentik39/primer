#!/usr/bin/env python3

import customtkinter as ctk
import sqlite3

def update_poem():
    print('Test')

def insert_poem():
    print("INSERT")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


app = ctk.CTk()
app.title("Рубаи Омар Хайям")
app.geometry("600x500+1000+300")
app.resizable(False, False)

# Таб

tabview = ctk.CTkTabview(master=app)
tabview.pack(pady=20, padx=50, fill="both", expand=True)
tab_1 = tabview.add("Случайное")
tab_2 = tabview.add("добавить")

# Таб 1

label_id = ctk.CTkLabel(master=tab_1, text="1")
label_id.pack()

textbox_1 = ctk.CTkTextbox(master=tab_1, width=440, height=289, wrap="word", spacing3=10)
textbox_1.pack()
example = """ Чтоб мудро жизнь прожить, знать надобно немало,
Два важных правила запомни для начала:
Ты лучше голодай, чем что попало есть,
И лучше будь один, чем вместе с кем попало. """
textbox_1.insert("0.0", example)

button_1 = ctk.CTkButton(master=tab_1, text="Обновить", command=update_poem)
button_1.pack(pady=20)

# Таб 2

textbox_2 = ctk.CTkTextbox(master=tab_2, width=430, height=279, wrap="word", spacing3=10)
textbox_2.pack(pady=20)

button_2 = ctk.CTkButton(master=tab_2, text="Сохранить", command=insert_poem)
button_2.pack()


app.mainloop()
