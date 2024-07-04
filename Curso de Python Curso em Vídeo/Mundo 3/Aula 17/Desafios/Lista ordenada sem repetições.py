lista = []
for cont in range(1,6):
    num = int(input(f'Digite o {cont}° valor: '))
    if cont == 1 or num > lista[-1]:
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao,num)
                break
            else:
                lista.insert(posicao + 1,num)
                break
            posicao += 1
print(lista)
input('\n\033[1:34mDigite "sair" para sair: \033[m')