import random
tupla = tuple(int(input('\n\033[1:34mDigite um número:\033[m '))for c in range(5))
print(f'\n\033[1:31mVocê digitou os valores:\033[m\033[1:33m {tupla}\033[m\033[1:31m!\033[m')
print(f'\033[1:31mO valor \033[1:33m"9"\033[1:31m apareceu\033[m \033[1:33m{tupla.count(9)}\033[m \033[1:31mvezes!\033[m')
if 3 in tupla:
    tres = tupla.index(3)
    print(f'\033[1:31mO primeiro valor\033[m \033[1:33m"3"\033[m \033[1:31mfoi digitado na\033[m \033[1:33m{tres}°\033[m \033[1:31mposição!\033[m')
else:
    print('\033[1:31mNão existe o valor\033[m \033[1:33m"3"\033[m \033[1:31mna tupla!\033[m')
    print('\033[1:31mOs números pares na tupla são:\033[m\033[1:33m ',end='')
for num in tupla:
    if num % 2 == 0:
        print(f'{num}',end=' ')
input('\033[m\033[1:31m!\033[m\n\033[1:34mDigite "sair" para sair: \033[m')