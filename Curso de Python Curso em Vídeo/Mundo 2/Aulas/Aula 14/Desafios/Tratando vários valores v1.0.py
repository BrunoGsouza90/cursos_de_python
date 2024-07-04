parar = int(input('\033[1:34mDigite um número:\033[m '))
soma = contador = 0
while parar != 999:
    soma += parar
    contador += 1
    parar = int(input('\033[1:34mDigite um número:\033[m '))
print('\n\033[1:31mA soma dos valores é\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(soma))
print('\033[1:31mForam digitados\033[m \033[1:33m{}\033[m \033[1:31mnúmeros!\033[m'.format(contador))
input('\n\033[1:34mDigite "sair" para sair: \033[m')