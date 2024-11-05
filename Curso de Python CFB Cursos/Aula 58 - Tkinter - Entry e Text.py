from tkinter import *

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background = 'lightblue')

'''
    "anchor" é usado apartir dos pontos cardeais.
    N = Norte.
    S = Sul.
    E = Leste.
    W = Oeste.
    NE = Noroeste.
    NO = Noroeste.
    SE = Sudeste.
    SO = Sudoeste.
'''
label_nome = Label(app, text="Nome :", background="lightblue", foreground="black", anchor=W).place(x=15, y=10, width=40, height=20)
entry_nome = Entry(app).place(x= 80, y=10, width=150, height=20)

label_telefone = Label(app, text="Telefone :", background="lightblue", foreground="black", anchor=W).place(x=10, y=35, width=60, height=20)
entry_telefone = Entry(app).place(x= 80, y=35, width=150, height=20)

label_sobrenome = Label(app, text="Sobrenome :", background="lightblue", foreground="black", anchor=W).place(x=250, y=10, width=80, height=20)
entry_sobrenome = Entry(app).place(x= 335, y=10, width=150, height=20)

label_email = Label(app, text="Email :", background="lightblue", foreground="black", anchor=W).place(x=270, y=35, width=60, height=20)
entry_email = Entry(app).place(x= 335, y=35, width=150, height=20)

label_observacao = Label(app, text="Obs. :", background="lightblue", foreground="black", anchor=W).place(x=20, y=85, width=60, height=20)
entry_observao = Text(app).place(x= 80, y=65, width=400, height=80)

app.mainloop()