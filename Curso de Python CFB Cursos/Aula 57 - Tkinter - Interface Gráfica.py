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
    Aqui estamos configurando o tamanho da janela do Aplicativo
        ou Programa.
'''
app.geometry('960x490')

'''
    Aqui estamos configurando a cor de fundo do nosso Aplicativo
        ou Programa.
'''
app.configure(background='#66ccff')

'''
    Aqui estamos configurando um caixa de texto.
'''
txt1 = Label(app, text='Curso de Python', background='#ff0', foreground='#000')

'''
    Aqui definimos a posição da caixa de texto e o seu tamanho.
'''
txt1.place(x = 10, y = 10, width = 150, height = 30)

vtxt = 'Módulo Tkinter'
vgb = '#ff0'
vfg = '#000'
txt2 = Label(app, text = vtxt, background = vgb, foreground = vfg)

'''
    Forma de configurar conteiners.
'''
txt2.pack(ipadx = 10, ipady = 20, padx = 5, pady = 5, side = 'top', fill = X, expand = True)

'''
    Aqui estamos executando o nosso Aplicativo ou Programa.
'''
app.mainloop()