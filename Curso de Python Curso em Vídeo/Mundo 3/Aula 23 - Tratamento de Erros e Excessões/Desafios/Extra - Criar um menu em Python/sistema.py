from lib import interface
from lib import arquivo
from time import sleep

nome_arquivo = 'cursoemvideo.txt'
if not arquivo.arquivoExiste(nome_arquivo):
    arquivo.criarArquivo(nome_arquivo)
    print('Arquivo encontrado com sucesso!')


while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Progama'])
    if resposta == 1:
        arquivo.lerArquivo(nome_arquivo)
    elif resposta == 2:
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(nome_arquivo,nome,idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!')
