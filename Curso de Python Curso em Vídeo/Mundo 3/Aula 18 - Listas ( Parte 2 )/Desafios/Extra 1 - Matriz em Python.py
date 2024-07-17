lista = list()
dimensao = int(input('\n\033[1:34mDigite a dimensão que deseja: \033[m'))
for c in range(dimensao):
    lista.append([])
    for x in range(dimensao):
        lista[c].append(0)
for c in range(dimensao):
    for x in range(dimensao):
        num = int(input('\n\033[1:34mDigite o número que deseja: \033[m'))
        lista[c][x] = num
print(lista)
input('\n\033[1:34mDigite "sair" para sair: \033[m')