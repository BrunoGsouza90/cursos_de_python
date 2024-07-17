primeiro_termo = int(input('\n\033[1:34mDigite o primeiro termo:\033[m '))
razao = int(input('\033[1:34mDigite a razão:\033[m '))
termo = 0
print('')
while termo < 10:
    print('\033[1:32m{}\033[m'.format(primeiro_termo),end=' ')
    print('\033[1:31m→\033[m' if termo < 9 else '\033[1:31m!\033[m',end=' ')
    primeiro_termo += razao
    termo += 1
input('\n\n\033[1:34mDigite "sair" para sair: ')