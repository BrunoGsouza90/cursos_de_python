import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho = 'Curso de Python CFB Cursos\\Banco de Dados\\agenda.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()


vsql = """
SELECT * FROM contatos;
"""

def consultarDados(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

resultados = consultarDados(vcon, vsql)

for resultado in resultados:
    print(resultado)