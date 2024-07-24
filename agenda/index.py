from tkinter import *
from tkinter import messagebox
from tkinter import ttk




windowAgenda = Tk()
windowAgenda.title("Agenda")
windowAgenda.geometry("1200x800")
windowAgenda.resizable(width=False, height=False)
windowAgenda.iconbitmap(default="agenda/LogoIcon.ico")


logo = PhotoImage (file="agenda/logo.png")



leftframe = Frame(windowAgenda, width=350, height=800, bg="BLUE")
leftframe.pack(side=LEFT)

rightframe = Frame(windowAgenda, width=845, height=800, bg='#696969')
rightframe.pack(side=RIGHT)

logoLabel = Label(leftframe, image=logo, bg="BLUE")
logoLabel.place(x=120, y=700)

toAddButton = ttk.Button (leftframe, text="Adicionar um novo contato", width=40)
toAddButton.place (x=50, y=250)

ToEditButton = ttk.Button (leftframe, text="Editar um contato", width=40)
ToEditButton.place(x=50, y=400)

deleteButton = ttk.Button (leftframe, text="Excluir um contato", width=40)
deleteButton.place (x=50, y=550)

searchButton = Label(rightframe, text="Buscar", width=10)
searchButton.place(x=650, y=50)

searchEntry = Entry(rightframe, width=80)
searchEntry.place(x=150, y=50)




windowAgenda.mainloop()