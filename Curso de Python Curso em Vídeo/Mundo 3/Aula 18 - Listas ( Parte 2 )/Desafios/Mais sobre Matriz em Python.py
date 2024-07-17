lista= list()
dimensao = int(input('\n\033[1:34mDigite a dimensão: \033[m'))
soma = maior = soma_terceira = 0
for c in range(dimensao):
    lista.append([0] * dimensao)
for c in range(dimensao):
    for x in range(dimensao):
        num = int(input(f'\n\033[1:34mDigite o valor da posicao\033[m \033[1:33m[{c}:{x}]\033[m \033[1:34m: \033[m'))
        lista[c][x] = num
        if num % 2 == 0:
            soma += num
for lista_pequena in lista:
    print('')
    for numero in lista_pequena:
        print(f'\033[1:31m[\033[m\033[1:33m{numero:^5}\033[m\033[1:31m]\033[m',end='')
print('')
for lista_pequena in lista:
    soma_terceira += lista_pequena[2]
for c in lista[1]:
    if c > maior:
        maior = c
print('\n\033[1:31mO maior valor da segunda linha é o:\033[m \033[1:33m{}\033[m \033[1:31m!\033[m'.format(maior))
print('\033[1:31mA soma dos valores da terceira coluna é:\033[m \033[1:33m{}\033[m \033[1:31m!\033[m'.format(soma_terceira))
print(f'\033[1:31mA soma de todos os valores pares digitados é:\033[m \033[1:33m{soma}\033[m \033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')