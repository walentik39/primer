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
# Tab 1
label_id = ctk.CTkLabel(master=tab_1, text="1")
label_id.pack()

textbox_1 = ctk.CTkTextbox(master=tab_1, width=449, height=299, wrap="word", spacing3=10)
textbox_1.pack()

example = """Не завидуй тому, кто силен и богат,
за рассветом всегда наступает закат.
С этой жизнью короткою, равною вдоху,
Обращайся, как с данной тебе напрокат."""
textbox_1.insert("0.0", example)

app.mainloop()
