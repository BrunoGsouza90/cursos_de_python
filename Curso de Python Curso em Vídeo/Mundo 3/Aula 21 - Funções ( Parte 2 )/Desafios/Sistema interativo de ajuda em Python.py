dicionario_cor = (
    '\033[m',
    '\033[1:39:41m',
    '\033[1:39:42m',
    '\033[1:39:43m',
    '\033[1:39:44m',
    '\033[1:39:45m',
)

def ajuda():
    print(dicionario_cor[1] + '~' * 30)
    print(f'{'Sistema de Ajuda PyHelp'.center(30)}')
    print('~' * 30)
    print('\033[m')
    while True:
        comando = str(input('\n\033[1:34mDigite a Função ou Biblioteca: \033[m'))
        print(dicionario_cor[2])
        help(comando)
        print('\033[m')
        resposta = str(input('\n\033[1:34mQuer analisar mais algum comando? [S/N] \033[m')).strip().upper()[0]
        while resposta not in 'SN':
            print('\n\033[1:31mOpção Inválida!')
            resposta = str(input('\n\033[1:34mQuer analisar mais algum comando? [S/N] \033[m')).strip().upper()[0]
        if resposta == 'N':
            break
ajuda()

input('\n\033[1:34mDigite "sair" para sair: \033[m')