import json
import ast
import time

lista = list()
pessoas = list()

def menu():
    print('-' * 50)
    print(f'{'MENU PRINCIPAL'.center(50)}')
    print('-' * 50)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('-' * 50)
    opcao = int(input('Sua Opção: '))
    return opcao

def cadastrar_pessoas():
    global lista
    print('-' * 50)
    print(f'{'NOVO CADASTRO'.center(50)}')
    print('-' * 50)
    nome = str(input('Digite o nome: ')).strip().capitalize()
    while True:
        try:
            idade = int(input('Digite a idade: '))
            break
        except ValueError:
            print('Erro: por favor, digite um número inteiro válido.')
    
    dicionario = {'Nome': nome, 'Idade': idade}
    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(json.dumps([dicionario]) + ',')
    print(f'Novo registro de {nome} adicionado.')
    print('-' * 50)

def ver_pessoas():
    print('-' * 50)
    print(f'{'PESSOAS CADASTRADAS'.center(50)}')
    print('-' * 50)

    with open('cadastro.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        linha.strip()
        dicionario = ast.literal_eval(linha)
        global pessoas
        pessoas.append(dicionario)

    for pessoa in pessoas:
        for dicionario in pessoa:
            for dado in dicionario:
                print(f'{dado['Nome']:<40} {dado['Idade']} anos')
    pessoas.clear()
    print('-' * 50)

while True:
    time.sleep(1)
    opcao = menu()
    if opcao == 1:
        time.sleep(1)
        ver_pessoas()
    elif opcao == 2:
        time.sleep(1)
        cadastrar_pessoas()
    elif opcao == 3:
        time.sleep(1)
        print('-' * 50)
        print(f'{'Volte Sempre!'.center(50)}')
        print('-' * 50)
        break
    else: 
        print('Opção Inválida!')



input('Digite "sair" para sair: ')