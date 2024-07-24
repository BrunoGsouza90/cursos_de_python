import ast
from lib import interface

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        interface.cabecalho('PESSOAS CADASTRADAS')
        linhas = a.readlines()
        lista = list()

        for linha in linhas:
            dicionario = ast.literal_eval(linha.strip())
            lista.append(dicionario)
            for linhas in lista:
                print(f'{linhas['Nome']:<30} {linhas['Idade']} anos')
    finally:
        a.close()

def cadastrar(nome_arquivo, nome = 'Desconhecido', idade = 0):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            dicionario = {'Nome': f'{nome}', 'Idade': f'{idade}'}
            a.write(f'{dicionario}' + '\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
