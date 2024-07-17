def escreva(texto):
    print('\n' + '\033[1:31m~\033[m' * int(len(texto) + 4))
    print(f'\033[1:33m{texto.center(len(texto) + 4)}\033[m')
    print('\033[1:31m~\033[m' * int(len(texto) + 4))

texto = str(input('\n\033[1:35mDigite o texto: \033[m'))
escreva(texto)

input('\n\033[1:34mDigite "sair" para sair: \033[m')