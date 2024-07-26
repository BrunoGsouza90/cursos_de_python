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
INSERT INTO contatos
VALUES
('2', 'Bruno','35991754424','bruno.gsouza199@gmail.com');
"""
def inserirDados(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido com sucesso!')
    except Error as ex:
        print(ex)

inserirDados(vcon, vsql)

vsql = """
UPDATE contatos
SET nome = 'Diego'
WHERE id = 2;
"""

def atualizarDados(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Dado(s) atualizado(s) com sucesso!')
    except Error as ex:
        print(ex)

atualizarDados(vcon, vsql)