lista = []
for cont in range(1,6):
    num = int(input(f'Digite o {cont}° valor: '))
    if (cont == 1):
        lista.append(num)
    elif num > lista[-1]:
        lista.append(num)
    elif num < lista[0]:
        lista.insert(0,num)
    else:
        for x in lista:
            if x > num:
                lista.insert(lista.index(x),num)
                break
print(lista)
input('\n\033[1:34mDigite "sair" para sair: \033[m')