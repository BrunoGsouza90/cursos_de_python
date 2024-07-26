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
('1', 'teste_nome','teste_telefone','teste_email');
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