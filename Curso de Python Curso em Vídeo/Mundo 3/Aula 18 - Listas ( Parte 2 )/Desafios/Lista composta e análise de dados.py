lista = list()
lista1 = list()
peso_total = 0
cont = 1
while True:
    print('')
    print('\033[1:31:40m-=' * 15 + f'\033[1:32:40m{cont}° PESSOA\033[m' + '\033[1:31:40m-=\033[m' * 15)
    nome = str(input('\n\033[1:34mDigite o nome: \033[m'))
    peso = float(input('\033[1:34mDigite o peso: \033[m'))
    peso_total += peso
    lista.append(nome)
    lista.append(peso)
    lista1.append(lista[:])
    lista.clear()
    resposta = str(input('\n\033[1:34mQuer cadastrar uma mais um usário:\033[m \033[1:35m[S/N] \033[m')).strip().upper()[0]
    while resposta not in 'SN':
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        resposta = str(input('\n\033[1:34mQuer cadastrar uma mais um usário:\033[m \033[1:35m[S/N] \033[m')).strip().upper()[0]
    if resposta == 'N':
        break
    cont += 1
media = peso_total / cont
print(f'\n\033[1:32mAo total foram cadastradas\033[m \033[1:33m{cont}\033[m\033[1:32m pessoas!\033[m')
for c in lista1:
    if c[1] > media:
        print(f'\033[1:31mO(a)\033[m \033[1:33m{c[0]}\033[m\033[1:31m, é mais pesado e está com \033[m\033[1:33m{int(c[1])}\033[m \033[1:31mKg!\033[m')
for c in lista1:
    if c[1] <= media:
        print(f'\033[1:31mO(a)\033[m \033[1:33m{c[0]}\033[m\033[1:31m, é mais leve e está com\033[m \033[1:33m{int(c[1])}\033[m \033[1:31mKg!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')