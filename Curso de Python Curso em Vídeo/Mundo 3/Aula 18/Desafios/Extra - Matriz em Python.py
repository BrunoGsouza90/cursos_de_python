lista = list()
for c in range(3):
    lista.append([0] * 3)
for c in range(0,3):
    for x in range(0,3):
        lista[c][x] = int(input(f'\n\033[1:34mDigite o valor \033[m\033[1:33m[{c}:{x}]\033[m\033[1:34m: \033[m'))
print('')
for c in lista:
    print(f'[{c[0]}][{c[1]}][{c[2]}]')
input('\n\033[1:34mDigite "sair" para sair: \033[m')