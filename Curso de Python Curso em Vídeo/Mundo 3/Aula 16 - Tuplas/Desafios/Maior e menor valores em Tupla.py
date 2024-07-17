import random
#tupla = tuple(random.sample(range(0,10),5))
#print(tupla)

tupla = tuple(random.randint(0,9)for _ in range(5))
maior = menor = tupla[0]
for num in tupla:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'\033[1:31mO maior valor da tupla é o\033[m \033[1:33m{maior}\033[m \033[1:31me o menor valor é o\033[m \033[1:33m{menor}\033[m\033[1:31m!\033[m')

tupla = (random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))
print(f'\033[1:31mO maior valor da tupla é o\033[m \033[1:33m{max(tupla)}\033[m \033[1:31me o menor valor é o\033[m \033[1:33m{min(tupla)}\033[m\033[1:31m!\033[m')

input('\n\033[1:34mDigite "sair" para sair: \033[m')