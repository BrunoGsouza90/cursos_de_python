lista = []
cont = 1
while True:
    num = int(input(f'\n\033[1:34mDigite o {cont}° valor: \033[m'))
    lista.append(num)
    resposta = str(input('\n\033[1:34mQuer continuar? [S/N] \033[m')).upper().strip()[0]
    while resposta not in 'SN':
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        resposta = str(input('\033[1:34mQuer continuar? [S/N] \033[m')).upper().strip()[0]
    if resposta == 'N':
        break
lista.sort(reverse=True)
if lista.count(5) == 0:
    print('\n\033[1:31mO número\033[m \033[1:33m"5"\033[m \033[1:31mnão apareceu na lista!\033[m')
else:
    print(f'\n\033[1:31mO número\033[m \033[1:33m"5"\033[1:31m apareceu\033[m \033[1:33m{lista.count(5)}\033[m \033[1:31mveze(s) na lista!\033[m')
print(f'\033[1:31mOs números que foram digitados em ordem descrecente são:\033[m \033[1:33m{lista}\033[m \033[1:31m!\033[m')
print(f'\033[1:33m{len(lista)}\033[m \033[1:31mnúmeros foram digitados!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')


