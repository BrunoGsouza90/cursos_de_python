'''
    Aqui estamos importando a biblioteca completa do Tkinter.
'''
from tkinter import *

'''
    Aqui estamos criando o nosso Aplicativo ou Programa.
'''
app = Tk()

'''
    Aqui estamos configurando o título do Aplicativo ou Programa.
'''
app.title("CFB Cursos")

'''
    Aqui estamos configurando o tamanho da janela do Aplicativo ou Programa.
'''
app.geometry('960x490')

'''
    Aqui estamos configurando a cor de fundo do nosso Aplicativo ou Programa.
'''
app.configure(background='lightblue')

'''
    Aqui estamos configurando um caixa de texto.
'''
txt1 = Label(app, text='Curso de Python', background='yellow', foreground='black')

'''
    Aqui definimos a posição da caixa de texto e o seu tamanho.
'''
txt1.place(x = 10, y = 10, width = 150, height = 30)

vtxt = 'Módulo Tkinter'
vgb = 'yellow'
vfg = 'black'
txt2 = Label(app, text = vtxt, background = vgb, foreground = vfg)

'''
    Forma de configurar conteiners.
    ipadx = Aqui é definido o "padding" horinzontal.
    ipady = Aqui é definido o "padding" vertical.
    padx = Aqui é definido a "margem" horizontal.
    pady = Aqui é definido a "margem" vertical.
    side = Define a posição do conteiner.
    fill = Determinará se o elemento será "X = Horizontal" ou "Y = Vertical".
    expand = Define se o container ficará centralizado ou não.
'''
txt2.pack(ipadx = 50, ipady = 50, padx = 5, pady = 5, side = 'right', fill = X, expand = True)

'''
    Aqui estamos executando o nosso Aplicativo ou Programa.
'''
app.mainloop()