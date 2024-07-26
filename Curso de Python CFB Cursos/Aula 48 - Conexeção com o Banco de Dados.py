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
CREATE TABLE IF NOT EXISTS contatos(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
nome VARCHAR(30),
telefone VARCHAR(14),
email VARCHAR(30)
);
"""

def CriarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada!')
    except Error as ex:
        print(ex)

CriarTabela(vcon, vsql)
vcon.close()