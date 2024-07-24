from tkinter import *
from tkinter import messagebox
from tkinter import ttk




windowAgenda = Tk()
windowAgenda.title("Agenda")
windowAgenda.geometry("1200x800")
windowAgenda.resizable(width=False, height=False)
windowAgenda.iconbitmap(default="agenda/LogoIcon.ico")


logo = PhotoImage (file="agenda/logo.png")



leftframe = Frame(windowAgenda, width=350, height=800, bg="#A9A9A9")
leftframe.pack(side=LEFT)

rightframe = Frame(windowAgenda, width=845, height=800, bg='#E0FFFF')
rightframe.pack(side=RIGHT)
welcomeLabel = Label (leftframe, text="Seja Bem-vindo usuario!")
welcomeLabel.place (x=30, y=40)


logoLabel = Label(leftframe, image=logo, bg="#A9A9A9")
logoLabel.place(x=120, y=700)

toAddButton = ttk.Button (leftframe, text="Adicionar um novo contato", width=40)
toAddButton.place (x=50, y=250)

ToEditButton = ttk.Button (leftframe, text="Editar um contato", width=40)
ToEditButton.place(x=50, y=400)

deleteButton = ttk.Button (leftframe, text="Excluir um contato", width=40)
deleteButton.place (x=50, y=550)

searchLabel = Label(rightframe, text="Informe o nome para buscar:", bg='#E0FFFF')
searchLabel.place(x=90, y=50)

searchButton = Button(rightframe, text="Buscar", width=10)
searchButton.place(x=650, y=47)

searchEntry = Entry(rightframe, width=60)
searchEntry.place(x=250, y=50)

assLabel = Label (rightframe, text="Desenvolvido por: Kauan Luiz", fg="black", bg="#A9A9A9")
assLabel.place(x=685, y=780)

agendaFrame = Frame(rightframe, width=800, height=500, bg="white")
agendaFrame.place(x=23, y=200)




windowAgenda.mainloop()