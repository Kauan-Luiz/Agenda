from tkinter import *
from tkinter import messagebox
from tkinter import ttk



windowAgenda = Tk()
windowAgenda.title("Agenda")
windowAgenda.geometry("1200x800")
windowAgenda.resizable(width=False, height=False)
windowAgenda.iconbitmap(default="logoicon.ico")

leftframe = Frame(windowAgenda, width=350, height=800, bg="BLUE")
leftframe.pack(side=LEFT)

rightframe = Frame(windowAgenda, width=845, height=800, bg='#696969')
rightframe.pack(side=RIGHT)


windowAgenda.mainloop()