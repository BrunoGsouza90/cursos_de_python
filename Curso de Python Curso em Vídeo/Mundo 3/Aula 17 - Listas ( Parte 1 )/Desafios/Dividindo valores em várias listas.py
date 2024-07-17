lista = list()
lista_pares = list()
lista_impares = list()
cont = 1
while True:
    num = int(input(f'\n\033[1:34mDigite o {cont}° valor: \033[m'))
    cont += 1
    if num % 2 == 0:
        lista_pares.append(num)
        lista.append(num)
    else:
        lista_impares.append(num)
        lista.append(num)
    resposta = str(input('\n\033[1:34mVocê quer continuar? [S/N] \033[m')).upper().strip()[0]
    while resposta not in 'SN':
        print('\n\033[1:31mOpção Inválida!\033[m')
        resposta = str(input('\n\033[1:34mVocê quer continuar? [S/N] \033[m')).upper().strip()[0]
    if resposta == 'N':
        break

print(f'\n\033[1:31mLista digitada completa:\033[m \033[1:33m{sorted(lista)}\033[m \033[1:31m!\033[m')
print(f'\033[1:31mLista dos números pares:\033[m \033[1:33m{sorted(lista_pares)}\033[m \033[1:31m!\033[m')
print(f'\033[1:31mLista dos números impares:\033[m \033[1:33m{sorted(lista_impares)}\033[m \033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')