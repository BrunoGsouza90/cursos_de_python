print('')
par = impar = 0
num = 1
while num != 0:
    num = int(input('\033[1:34mDigite um número:\033[m '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('\n\033[1:31mA quantidade de números impares é \033[m\033[1:33m{}\033[m \033[1:31me a quantidade de números pares é\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(impar, par))
input('\n\033[1:34mDigite "sair" para sair: \033[m')