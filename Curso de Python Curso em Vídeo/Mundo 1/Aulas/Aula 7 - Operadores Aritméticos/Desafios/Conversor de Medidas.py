valor=int(input('\nDigite um valor em metros: '))
print('O valor digitado em centímetros é \033[31m{}\033[m, e em milímitros é \033[31m{}\033[m!'.format(valor*100,valor*1000))
input('\n\033[1:34mDigite "sair" para sair: \033[m')