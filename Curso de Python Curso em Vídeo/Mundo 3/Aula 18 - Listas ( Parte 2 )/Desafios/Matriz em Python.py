lista = list()
lista1 = list()
p = 0
while p < 3:
    for c in range(0,3):
        num = int(input(f'\n\033[1:34mDigite um valor para \033[m\033[1:33m[{p},{c}]\033[m\033[1:34m: \033[m'))
        lista.append(num)
    lista1.append(lista[:])
    lista.clear()
    p += 1
print('')
for c in lista1:
    print(f'\033[1:31m[\033[m\033[1:33m{c[0]}\033[m\033[1:31m][\033[m\033[1:33m{c[1]}\033[m\033[1:31m][\033[m\033[1:33m{c[2]}\033[m\033[1:31m]\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')