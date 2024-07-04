lista = []
lista_pares = []
lista_impares = []
for c in range(1,8):
    num = int(input(f'\n\033[1:34mDigite o {c}° número:\033[m '))
    if num not in lista_pares and num not in lista_impares:
        if num % 2 == 0:
            lista_pares.append(num)
        else:
            lista_impares.append(num)
lista.append(sorted(lista_pares))
lista.append(sorted(lista_impares))
print(f'\n\033[1:31mA lista de números pares é:\033[m \033[1:33m{lista[0]}\033[m \033[1:31m!\033[m')
print(f'\033[1:31mA lista de números impares é:\033[m \033[1:33m{lista[1]}\033[m \033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')