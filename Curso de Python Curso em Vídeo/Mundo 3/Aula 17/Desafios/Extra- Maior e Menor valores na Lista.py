lista = []
lista_maior = []
lista_menor = []
for c in range(1,6):
    num = int(input(f'Digite o {c}° valor: '))
    lista.append(num)
maior = max(lista)
menor = min(lista)
for p in lista:
    if p == maior:
        lista_maior.append(str(p))
    if p == menor:
        lista_menor.append(str(p))
print(', '.join(lista_maior) + '.')
print(', '.join(lista_menor) + '.')

input('\n\033[1:34m''Digite "sair" para sair: \033[m')