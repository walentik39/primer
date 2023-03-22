#!/usr/bin/env python3

import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Рубаи Амар Хаям")
app.geometry("600x500+1000+300")
app.resizable(False, False)

tabview = ctk.CTkTabview(master=app)
tabview.pack(pady=20, padx=50, fill='both', expand=True)
tab_1 = tabview.add("Случайное")
tab_2 = tabview.add("Добавить")

app.mainloop()
