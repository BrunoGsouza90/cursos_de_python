lista = list()
lista1 = list()
mais_pesados = list()
mais_leves = list()
cont = 1
while True:
    print('')
    print('\033[1:31:40m-=' * 15 + f'\033[1:32:40m{cont}° PESSOA\033[m' + '\033[1:31:40m-=\033[m' * 15)
    nome = str(input('\n\033[1:34mDigite o nome: \033[m'))
    peso = float(input('\033[1:34mDigite o peso: \033[m'))
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
pesado = leve = lista1[0][1]
for c in lista1:
    if c[1] > pesado:
        pesado = c[1]
    if c[1] < leve:
        leve = c[1]
for c in lista1:
    if c[1] == pesado:
        mais_pesados.append(c[0])
    if c[1] == leve:
        mais_leves.append(c[0])
print(f'\n\033[1:32mAo total foram cadastradas\033[m \033[1:33m{cont}\033[m\033[1:32m pessoas!\033[m')
print(f'\033[1:31mO maior peso é\033[m \033[1:33m{pesado}\033[m \033[1:31me os usuários com esse peso são:\033[m \033[1:33m{mais_pesados}\033[m\033[1:31m!\033[m')
print(f'\033[1:31mO menor peso é \033[m\033[1:33m{leve}\033[m \033[1:31me os usuários com esse peso são:\033[m \033[1:33m{mais_leves}\033[m\033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')
